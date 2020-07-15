import numpy as np
from tqdm import tqdm_notebook, tnrange
from sklearn.preprocessing import MinMaxScaler
import skimage

def get_df(df, dataset_num=5):
    df = df.copy()
    df.index = df.Dist.astype(float).values*(10**(-5))
    colums_inspectr = list(np.array([[ str(i) +'.'+ str(j)  for j in range(1,5) ] for i in range(1,17)]).ravel())
    df = df[colums_inspectr]
    if dataset_num==5:
        df = df.iloc[10000:-5000]
        df.index-=10.215
    return df
 
def crop_squares_with_defects(df, defects, centering=True, scaling='local'):

    pictures_with_defects = []
    for NUMBER in tnrange(len(defects)):

        loc = defects.iloc[[NUMBER]]['Distance, m'].iloc[0]
        if centering:
            a = loc - 0.2
            b = a + 0.4
            # searching min value for distance and sensors
            # select working sensors
            working_sensors = df[(df.index >= a) & (df.index <= b)].mean()
            working_sensors = working_sensors[working_sensors>2800].dropna().index
            # find indices with min values for both axis
            loc = df[working_sensors][(df.index >= a) & (df.index <= b)].min(axis=1).idxmin()
        else:
            loc = df.index[df.index <= loc][-1]
        index_dist = np.where(df.index == loc)[0][0]

        picture = df.iloc[index_dist - 32:index_dist + 32].T
        if scaling:
            picture = np.nan_to_num(MinMaxScaler().fit_transform(picture[picture>2000]) / 2 + 0.5)
            picture = picture / picture.max()
        else:
            picture = np.nan_to_num(picture[picture>2000])
        pictures_with_defects.append(picture)
    return pictures_with_defects
    

def crop_squares_with_welds(df, journal, defects, centering=True, scaling = True):
    
    defected_welds = defects[defects['Defect location'] == 'Сварной шов']['Distance, m']
    
    pictures_with_defected_welds = []
    pictures_with_healthy_welds = []
    for NUMBER in tnrange(len(journal)):

        loc = journal.iloc[[NUMBER]]['Location of the section beginning, m'].iloc[0]
        if centering:
            a = loc - 0.2
            b = a + 0.4
            # searching min value for distance and sensors
            # select working sensors
            working_sensors = df[(df.index >= a) & (df.index <= b)].mean()
            working_sensors = working_sensors[working_sensors>2800].dropna().index
            # find indices with min values for both axis
            loc = df[working_sensors][(df.index >= a) & (df.index <= b)].min(axis=1).idxmin()
        else:
            loc = df.index[df.index <= loc][-1]
        index_dist = np.where(df.index == loc)[0][0]
        
#        welds_dict[NUMBER] = df.iloc[index_dist - 32:index_dist + 32]
        is_defected = [1 if (i>loc-0.5) and (i<=loc+0.5) else 0 for i in defected_welds]
        if 1 in is_defected:
            picture = df.iloc[index_dist - 32:index_dist + 32].T
            if scaling:
                picture = np.nan_to_num(MinMaxScaler().fit_transform(picture[picture>2000]) / 2 + 0.5)
                picture = picture / picture.max()
            else:
                picture = np.nan_to_num(picture[picture>2000])
            pictures_with_defected_welds.append(picture)
        else:
            picture = df.iloc[index_dist - 32:index_dist + 32].T
            if scaling:
                picture = np.nan_to_num(MinMaxScaler().fit_transform(picture[picture>2000]) / 2 + 0.5)
                picture = picture / picture.max()
            else:
                picture = np.nan_to_num(picture[picture>2000])
            pictures_with_healthy_welds.append(picture)
    return pictures_with_healthy_welds, pictures_with_defected_welds
    
def crop_squares_with_healthy(df, journal, defects, scaling = True):
    
    # we select sections without defects
    sections_without_defects = list(set(journal['№ of the section']) - set(defects['№ of the section']))
    healthy_journal = journal[journal['№ of the section'].isin(sections_without_defects)]

    healthy_pictures = []
    for NUMBER in tnrange(len(sections_without_defects)-1):

        start = healthy_journal.iloc[[NUMBER]]['Location of the section beginning, m'].iloc[0] + 0.2
        end = start + healthy_journal.iloc[[NUMBER]]['Section length, m'].iloc[0] - 0.2
        a = start
        i = 0
        while (i < 10):
            index_dist = np.where(df.index > a)[0][0]
            
            picture = df.iloc[index_dist - 32:index_dist + 32].T
            if scaling:
                picture = np.nan_to_num(MinMaxScaler().fit_transform(picture[picture>2000]) / 2 + 0.5)
                picture = picture / picture.max()
            else:
                picture = np.nan_to_num(picture[picture>2000])
            healthy_pictures.append(picture)
            
            a = df.index[index_dist + 65]
            i += 1
    return healthy_pictures
    
def train_test_saving(pictures, kind='healthy'):
    '''kind: str
    healthy, defect, healthy_weld, defected_weld '''
    classes = {'healthy':'class_001/',
              'defect':'class_002/',
              'healthy_weld':'class_003/',
              'defected_weld':'class_004/',}
    name_train = '../../data/train/'+classes[kind]
    name_test = '../../data/test/'+classes[kind]
    [io.imsave(name_train+str(i)+'.png', skimage.img_as_ubyte(x)) for i, x in enumerate(pictures, start=1) if i % 10 != 0]
    [io.imsave(name_test+str(i)+'.png', skimage.img_as_ubyte(x)) for i, x in enumerate(pictures, start=1) if i % 10 == 0]