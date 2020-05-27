import numpy as np
def get_df(df,dataset_num=5):
    df = df.copy()
    df.index = df.Dist.astype(float).values*(10**(-5))
    colums_inspectr = list(np.array([[ str(i) +'.'+ str(j)  for j in range(1,5) ] for i in range(1,17)]).ravel())
    df = df[colums_inspectr]
    if dataset_num==5:
        df = df.iloc[10000:-5000]
        df.index-=10.215
        return df