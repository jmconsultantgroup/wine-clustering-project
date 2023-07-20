
    
def plot_variable_pairs(df):
    df = df.sample(n=10000)
    cols = ['fixed acidity','volatile acidity', 'citric acid','residual sugar','chlorides'   
    'free sulfur dioxide' ,'total sulfur dioxide','density','pH','sulphates','proof']
    target = 'quality'
    
    for col in cols:
        sns.lmplot(data=df, x=col, y=target, hue='proof')

    
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

    


def plot_categorical_and_continuous_vars(df, cat_var_col, con_var_col):
    '''This function graphs a swarmplot, lmplot, stripplot, and violinplot to visualize the relationship between categorical and continuous variables.'''
    
    # sample the data to make the graph readable
    df = df.sample(n=1000)
    
    plt.figure(figsize=(18, 8)) 

    # Swarm Plot
    plt.subplot(1, 4, 1)
    sns.swarmplot(x=cat_var_col, y=con_var_col, data=df)
    plt.title('Swarm Plot')

    # lmplot
    plt.subplot(1, 4, 2)
    sns.lmplot(x=cat_var_col, y=con_var_col, data=df)
    plt.title('lmplot')

    # Strip Plot
    plt.subplot(1, 4, 3)
    sns.stripplot(x=cat_var_col, y=con_var_col, data=df)
    plt.title('Strip Plot')


    plt.tight_layout()
    plt.show()
