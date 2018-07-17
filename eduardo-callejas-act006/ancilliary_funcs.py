import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# importamos scipy.stats que ayudará a generar distribuciones
import scipy.stats as statsp

def fetch_descriptive(dataframe):
    for key, value in dataframe.iteritems():
        print(value.describe())

def fetch_perdidas(dataframe, var, print_list=False):
    print('Columna:', var)
    print(dataframe[var].isna().value_counts())
    print(dataframe[var].isna().value_counts(True))
    print('\n')
    if print_list==True:
        
        print('Lista de observaciones:')
        print(dataframe['cname'][dataframe[var].isnull()])
        print('\n')

def plot_hist(dataframe, var, sample_mean = False, true_mean = False):
    dataframe_dropna = dataframe[var].dropna()
    plt.hist(dataframe_dropna, color='grey', alpha=.4)
    plt.title("Distribución empírica del índice de la variable "+var)
    if sample_mean == True:
        plt.axvline(dataframe_dropna.mean(), color='dodgerblue', linestyle='--', lw=2)
    if true_mean ==  True: 
        plt.axvline(df[var].dropna().mean(), color='red', linestyle='-', lw=2)

def get_dotplot(dataframe, plot_var, plot_by, global_stat= False, statistic = 'mean'):
    plt.title('Dot plot agrupado por '+ plot_by+ ' de la variable '+ plot_var )
    group_mean = round(dataframe.groupby(plot_by)[plot_var].mean(),2)
    plt.plot(group_mean.values, group_mean.index, 'o', color ='grey')
    
    if global_stat == True:
        if statistic == 'mean':
            plt.axvline(df[plot_var].mean(), color = 'tomato', linestyle = '--'); # 
        elif statistic == 'median':
            plt.axvline(df[plot_var].median(), color = 'tomato', linestyle = '--')