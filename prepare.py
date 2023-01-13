import numpy as np
import pandas as pd
from scipy import stats
import sklearn.preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import QuantileTransformer


def scale_data(t, v, te):
    ss_scaler = sklearn.preprocessing.StandardScaler()
    ss_scaler.fit(t)
    
    st=train_scaled = ss_scaler.transform(t)
    sv=validate_scaled = ss_scaler.transform(v)
    ste=test_scaled = ss_scaler.transform(te)

    return st, sv, ste


def remove_outliers(df, k=1.5):
    a=[]
    b=[]
    fences=[a, b]
    features= []
    col_list = []
    i=0
    for col in df:
        new_df=np.where(df[col].nunique()>8, True, False)
        if new_df==True:
            if df[col].dtype == 'float' or df[col].dtype == 'int':
                '''
                for each feature find the first and third quartile
                '''
                q1, q3 = df[col].quantile([.25, .75])
                '''
                calculate inter quartile range
                '''
                iqr = q3 - q1
                '''
                calculate the upper and lower fence
                '''
                upper_fence = q3 + (k * iqr)
                lower_fence = q1 - (k * iqr)
                '''                        appending the upper and lower fences to lists
                '''
                a.append(upper_fence)
                b.append(lower_fence)
                '''
                appending the feature names to a list
                '''
                features.append(col)
                '''
                assigning the fences and feature names to a dataframe
                '''
                var_fences= pd.DataFrame(fences, columns=features, index=['upper_fence', 'lower_fence'])
                col_list.append(col)
            else:
                print(col)
                print('column is not a float or int')
        else:
            print(f'{col} column ignored')
                                    
    for col in col_list:
        df = df[(df[col]<= a[i]) & (df[col]>= b[i])]
        i+=1
    return df, var_fences