import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.feature_selection import f_regression

def plot_residuals(df):
    sns.scatterplot(x='tax_value_dollar_count', y='residual', data=df, marker='.')
    sns.scatterplot(x='tax_value_dollar_count', y='residual_baseline', data=df, marker='.')
    plt.title('Residual of Tax Value Dollar Count and Predictions')
    plt.legend(['Residual','Residual Baseline'], shadow=True)
    plt.xlabel('Tax Value Dollar Count')
    plt.ylabel('Residual')

def regression_errors(df):
    sse=mean_squared_error(df['tax_value_dollar_count'], df['yhat'])*len(df)
    ess=sum((df['yhat']-df['tax_value_dollar_count'].mean())**2)
    tss=ess+sse
    mse=mean_squared_error(df['tax_value_dollar_count'], df['yhat_baseline'])
    rmse=mean_squared_error(df['tax_value_dollar_count'], df['yhat'], squared=False)
    return print(f'SSE = {sse}\nESS = {ess}\nTSS = {tss}\nMSE = {mse}\nRMSE = {rmse}')

def baseline_mean_errors(df):
    sse_baseline=mean_squared_error(df['tax_value_dollar_count'], df['yhat_baseline'])*len(df)
    mse_baseline=mean_squared_error(df['tax_value_dollar_count'], df['yhat_baseline'])
    rmse_baseline=mean_squared_error(df['tax_value_dollar_count'], df['yhat_baseline'], squared=False)
    return print(f'SSE baseline = {sse_baseline}\nMSE baseline = {mse_baseline}\nRMSE baseline = {rmse_baseline}')

def better_than_baseline(df):
    rmse=mean_squared_error(df['tax_value_dollar_count'], df['yhat'], squared=False)
    rmse_baseline=mean_squared_error(df['tax_value_dollar_count'], df['yhat_baseline'], squared=False)
    if rmse < rmse_baseline:
        print('The model performes better than the baseline!')
    else:
        print('The model does not perform better than the baseline.')