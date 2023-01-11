#import libraries and the 'get_connection' function from env
import pandas as pd
import numpy as np
import env
import os
from env import get_connection

def wrangle_zillow():
    '''
    looking for an already existing zillow csv on the local machine
    '''
    if os.path.isfile('zillow.csv'):
        return pd.read_csv('zillow.csv')
    else:
        '''
        if there is no existing csv, then connect to the SQL server and get the information from 
        telco_churn db
        '''
        url = get_connection('zillow')
        '''
        use the query to rename columns too
        '''
        query = '''
                SELECT bedroomcnt as bedroom_count, bathroomcnt as bathroom_count, 
                calculatedfinishedsquarefeet as calc_finished_square_ft, 
                taxvaluedollarcnt as tax_value_dollar_count, yearbuilt as year_built, 
                taxamount as tax_amount, fips as fips_code 
                FROM properties_2017 
                JOIN propertylandusetype USING(propertylandusetypeid)
                WHERE propertylandusedesc = 'Single Family Residential'
                '''
        
        df = pd.read_sql(query, url)
        '''
        drop null values
        '''
        df=df.dropna()
        '''
        saving the newly queried SQL table to a csv so it
        can be used instead of connecting to the SQL server
        every time I want this info
        '''
        df.to_csv('zillow.csv', index=False)
        return df