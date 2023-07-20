import wrangle_wine as w
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import ttest_ind
from scipy.stats import pearsonr

import warnings
warnings.filterwarnings('ignore')
    

def plot_variable_pairs(df):
    cols = ['fixed acidity','volatile acidity', 'citric acid','residual sugar','chlorides',   
    'free sulfur dioxide' ,'total sulfur dioxide','density','pH','sulphates','proof']
    target = 'quality'
    
    for col in cols:
        sns.lmplot(data=df, y=col, x=target)
        
        

    
# def plot_categorical_and_continuous_vars(df, cat_var_col, con_var_col):
#     '''This function graphs a swarmplot that shows the density of home values within each county.'''
    
    
#     # sample the data to make the graph readable
#     df = df.sample(n=1000)
    
#     plt.figure(figsize=(12, 6)) 

#     fig, axs = plt.subplots(1, 3, figsize=(18, 8))
    
#     sns.stripplot(ax=axs[0], x=cat_var_col, y=con_var_col, data=df)
#     axs[0].set_title('Strip Plot')
    

#     sns.violinplot(x=cat_var_col, y=con_var_col, data=df, s=1)
#     axs[2].set_title('Violin Plot')

#     plt.title('Features Vs Wine Quality')
#     plt.show()

    
    

def plot_continuous_vs_categorical(df, cat_var_col, con_var_col):

    for con_var in con_var_col:
        plt.figure(figsize=(12, 4))
        
        
        # Long-form DataFrame
        data_long = df.melt(id_vars=[cat_var_col], value_vars=[con_var], var_name='Variable', value_name='Value')
        
        # Swarm Plot
        plt.subplot(1, 3, 1)
        sns.swarmplot(x=cat_var_col, y='Value', data=data_long)
        plt.title(f'{con_var} vs {cat_var_col}')
        
        # Histogram
        plt.subplot(1, 3, 2)
        sns.histplot(data=data_long, x='Value', hue=cat_var_col, kde=True)
        plt.title(f'{con_var} Histogram')
        
        # Bar Plot
        plt.subplot(1, 3, 3)
        mean_values = df.groupby(cat_var_col)[con_var].mean().reset_index()
        sns.barplot(x=cat_var_col, y=con_var, data=mean_values, ci=None)
        plt.title(f'Mean {con_var} Bar Plot')
        
        plt.tight_layout()
        plt.show()