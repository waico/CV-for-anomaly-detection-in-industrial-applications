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
 
def crop_squares_with_defects(df, defects):

    pictures_with_defects = []
    for NUMBER in tnrange(len(defects)):

        a = defects.iloc[[NUMBER]]['Distance, m'].iloc[0] - 0.2
        b = a + 0.4

        # searching min value for distance and sensors
        # select working sensors
        working_sensors = df[(df.index >= a) & (df.index <= b)].mean()
        working_sensors = working_sensors[working_sensors>2800].dropna().index
        # find indices with min values for both axis
        dist = df[working_sensors][(df.index >= a) & (df.index <= b)].min(axis=1).idxmin()
        index_dist = np.where(df.index == dist)[0][0]

        picture = df.iloc[index_dist - 32:index_dist + 32].T
        picture = np.nan_to_num(MinMaxScaler().fit_transform(picture[picture>2000]) / 2 + 0.5)
        pictures_with_defects.append(picture / picture.max())
    return pictures_with_defects
    
def crop_squares_with_welds(df, journal, defects):
    
    defected_welds = defects[defects['Defect location'] == 'Сварной шов']['Distance, m']
    
    pictures_with_defected_welds = []
    pictures_with_normal_welds = []
    for NUMBER in tnrange(len(journal)):

        a = journal.iloc[[NUMBER]]['Location of the section beginning, m'].iloc[0] - 0.2
        b = a + 0.4

        # searching min value for distance and sensors
        # select working sensors
        working_sensors = df[(df.index >= a) & (df.index <= b)].mean()
        working_sensors = working_sensors[working_sensors>2800].dropna().index
        # find indices with min values for both axis
        dist = df[working_sensors][(df.index >= a) & (df.index <= b)].min(axis=1).idxmin()
        index_dist = np.where(df.index == dist)[0][0]
        
#        welds_dict[NUMBER] = df.iloc[index_dist - 32:index_dist + 32]
        is_defected = [1 if (i>dist-0.5) and (i<=dist+0.5) else 0 for i in defected_welds]
        if 1 in is_defected:
            picture = df.iloc[index_dist - 32:index_dist + 32].T
            picture = np.nan_to_num(MinMaxScaler().fit_transform(picture[picture>2000]) / 2 + 0.5)
            pictures_with_defected_welds.append(picture / picture.max())
        else:
            picture = df.iloc[index_dist - 32:index_dist + 32].T
            picture = np.nan_to_num(MinMaxScaler().fit_transform(picture[picture>2000]) / 2 + 0.5)
            pictures_with_normal_welds.append(picture / picture.max())
    return pictures_with_normal_welds, pictures_with_defected_welds
    
def crop_squares_with_normal(df, journal, defects):
    
    # we select sections without defects
    sections_without_defects = list(set(journal['№ of the section']) - set(defects['№ of the section']))
    normal_journal = journal[journal['№ of the section'].isin(sections_without_defects)]

    normal_pictures = []
    for NUMBER in tnrange(len(sections_without_defects)-1):

        start = normal_journal.iloc[[NUMBER]]['Location of the section beginning, m'].iloc[0] + 0.2
        end = start + normal_journal.iloc[[NUMBER]]['Section length, m'].iloc[0] - 0.2
        a = start
        i = 0
        while (i < 10):
            index_dist = np.where(df.index > a)[0][0]
            
            picture = df.iloc[index_dist - 32:index_dist + 32].T
            picture = np.nan_to_num(MinMaxScaler().fit_transform(picture[picture>2000]) / 2 + 0.5)
            normal_pictures.append(picture / picture.max())
            
            a = df.index[index_dist + 65]
            i += 1
    return normal_pictures
    
def train_test_saving(pictures, kind='normal'):
    '''kind: str
    normal, defect, normal_weld, defected_weld '''
    classes = {'normal':'class_001/',
              'defect':'class_002/',
              'normal_weld':'class_003/',
              'defected_weld':'class_004/',}
    name_train = '../../data/train/'+classes[kind]
    name_test = '../../data/test/'+classes[kind]
    [io.imsave(name_train+str(i)+'.png', skimage.img_as_ubyte(x)) for i, x in enumerate(pictures, start=1) if i % 10 != 0]
    [io.imsave(name_test+str(i)+'.png', skimage.img_as_ubyte(x)) for i, x in enumerate(pictures, start=1) if i % 10 == 0]