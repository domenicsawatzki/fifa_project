import pandas as pd

# show shape, df overview, and dtypes for dataframe 
def firstLook(df):
    
    # Input validation
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'raw_data' is not a valid DataFrame.")
    
    print(df.shape)
    display(df)
    print(df.dtypes)

# shows and count unique values
def showUnique(df):
     # Input validation
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'raw_data' is not a valid DataFrame.")
    
    for col in df:
        print('values of column:',col)
        l = 0
        print(df[col].unique())
        l = len(df[col].unique())
        print('number of unique values:', l, '\n')
        

def cleaningGender(x):
    if x in ['M', 'MALE']:
        return 'Male'
    elif x.startswith('F'):
        return 'Female'
    else:
        return x
        
def cleaningState(x):
    if x in ['WA']:
        return 'Washington'
    elif x in ['Cali']:
        return 'California'
    elif x in ['AZ']:
        return 'Arizona'
    else: 
        return x
 

    
# transform to snake_case, lower column names and strip
def clean_column_names(df):
    # Input validation
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'raw_data' is not a valid DataFrame.")
    
    # create copy
    clean_df = df.copy()
    
    #cleaning
    clean_df.columns= [col.strip() for col in clean_df.columns]
    clean_df.columns= [col.lower() for col in clean_df.columns]
    clean_df.columns= [col.replace(' ', '_') for col in clean_df.columns]
    
    return clean_df
    
def nullTable(dataset):
    round(dataset.isna().sum()/len(dataset),4)*100  # shows the percentage of null values in a column
    nulls_df = pd.DataFrame(round(dataset.isna().sum()/len(dataset),4)*100)
    nulls_df
    nulls_df = nulls_df.reset_index()
    nulls_df
    nulls_df.columns = ['header_name', 'percent_nulls']
    display(nulls_df)
    display(dataset.isna().sum())
    
    
def clean(dataframe):
    dataframe = columnCleaning(dataframe)
    dataframe
    dataframe = cleaningValues(dataframe)
    
    return dataframe
        
        
