import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
import pandas as pd
from pydataset import data
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# -----------------------------acquire--------------------------------


def wine_merge_data():
     
    df_red = pd.read_csv('https://query.data.world/s/hak4rebpd7f6xonzxkpsg5cvc7xnuf?dws=00000')
    df_red['strain'] = 'red'
    
    df_white = pd.read_csv('https://query.data.world/s/5d3mv3aqzasknnepvoc7boia7pyftu?dws=00000')
    df_white['strain'] = 'white'
    
    df = pd.concat([df_red, df_white], ignore_index=True)
    

    return df



# -----------------------------outliers--------------------------------

def detect_outliers_iqr(df, columns, threshold=1.5):
    if isinstance(columns, str):
        columns = [columns]
    
    outliers = pd.DataFrame()
    
    for col in columns:
        # Calculate the IQR
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        
        # Determine the outlier thresholds
        lower_threshold = q1 - threshold * iqr
        upper_threshold = q3 + threshold * iqr
        
        # Identify outliers
        outliers_col = df[(df[col] < lower_threshold) | (df[col] > upper_threshold)]
        outliers = pd.concat([outliers, outliers_col], ignore_index=True)
    
    return outliers
# -----------------------------prep--------------------------------
def prep_wine_data(df):
    # Rename the 'alcohol' column to 'proof'

    quality_median = df['quality'].median()
    df['quality_bin'] = df['quality'].apply(lambda x: 1 if x > quality_median else 0)
    
    # Perform one-hot encoding on the 'strain' column
    encoded_cols = pd.get_dummies(df['strain'], prefix='strain')
    df = pd.concat([df, encoded_cols], axis=1)
    df = df.rename(columns={'alcohol': 'proof'})
    df = df.drop_duplicates()
    
    # Assuming 'split_wine_data' is a custom function to split the data into train, validate, and test sets
    train, validate, test = split_wine_data(df)
    
    return train, validate, test
# -----------------------------split--------------------------------



def split_wine_data(df):
    
  
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123) 
                                       

    
    return train, validate, test
    
# -----------------------------scale--------------------------------
    
def scale_data(train, validate, test):
    
    
    numeric_cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'proof']
    
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    scaler = MinMaxScaler()
    scaler.fit(train[numeric_cols])
    
    train_scaled[numeric_cols] = scaler.transform(train[numeric_cols])
    validate_scaled[numeric_cols] = scaler.transform(validate[numeric_cols])
    test_scaled[numeric_cols] = scaler.transform(test[numeric_cols])
    
    return train_scaled, validate_scaled, test_scaled


def wrangle_wine():
  
    df = wine_merge_data()
    train, validate, test = prep_wine_data(df)
    return train, validate, test


