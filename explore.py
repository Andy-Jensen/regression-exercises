import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_variable_pairs(df):
    df2=df.sample(5000)
    for col in df2:
        for f in df2:
            sns.lmplot(data=df2, 
                       x=col, 
                       y= f, 
                       palette= 'Blues', 
                       line_kws={'color': 'red'},
                       markers='.')
            plt.title(f'{col} and {f} relationship')
            plt.show()




def plot_categorical_and_continuous_vars(df, tar, cat):
    sns.swarmplot(x=cat.sample(5000), y=tar.sample(5000), data=df)
    plt.show()
    sns.barplot(x=cat.sample(5000), y=tar.sample(5000), data=df)
    plt.show()
    sns.boxplot(x=cat.sample(5000), y=tar.sample(5000), data=df)
    plt.show()