'''
Refrences:

http://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas
http://stackoverflow.com/questions/26724378/pandas-settingwithcopywarning
'''

import pandas as pd
import numpy as np

def read_data(fname):
    # read in the data from filename fname
        
    data = pd.read_csv(fname, low_memory=False, skiprows=2)    #read_csv() is used to read the contents from the csv file
    
    #print data
    # return a single object
    return data

def num_countries(data):
    # return the total number of unique countries
       
    value = data['Country / territory of asylum/residence'].drop_duplicates()   #drop_duplicates : shows only the unduplicated value in the column
    
    return len(value)

def origins(data, country):
    # given a country name, return the countries that the persons of concern originated from
    val= (data['Origin'].loc[data['Country / territory of asylum/residence']==country]).unique()
    
    #print val
    return val       


def max_people(data, country):
    # given a country name, return the year that the maximum number of persons of a concern were in that country and how many were there
    
    #Converting all '*' values to 4
    if data['Total Population'].all()=='*':
        data['Total Population']=4
    
    value= data.loc[data['Country / territory of asylum/residence']==country]
    
    #Store in a separate Dataframe values of Year and Total Population Column
    df=pd.DataFrame(zip(value['Year'],value['Total Population']), columns=['Year','Total Population'])
    
    for i in df['Year'].unique():
        # converting the column to numeric type
        df['Total Population'] = df['Total Population'].astype(str).convert_objects(convert_numeric=True)
           
        #Groupby year and find the sum of each year
        summ = pd.DataFrame((df.groupby('Year')['Total Population'].sum()))
        
        #idxmax returns the index of the maximum Total Population (index here is the year)
        total_population = summ['Total Population'].loc[summ['Total Population'].idxmax()]
        year=summ['Total Population'].idxmax()
        
    #print total_population.type()
    
    #Converting the Total Population from float to int
    total_population=int(total_population)
    
    return (year,total_population)

def calc_2014range(data, country):
    # given a country name, return the possible minimum and maximum of the number of persons of concern in that country in 2014
    year=2014
    value1= data.loc[data['Year']==year]
    
    df=pd.DataFrame(zip(value1['Total Population'],value1['Country / territory of asylum/residence']), columns=['Total Population','Country / territory of asylum/residence'])
    
    row_index= df['Total Population']=='*'
    
    #Find Maximum
    df.loc[row_index,'Total Population'] = 4
    df['Total Population']=df['Total Population'].apply(int)
    maximum=(df.loc[df['Country / territory of asylum/residence']==country,'Total Population']).sum()
    
    #Find Minimum
    df.loc[row_index,'Total Population'] = 1
    df['Total Population']=df['Total Population'].apply(int)    
    minimum = (df.loc[df['Country / territory of asylum/residence']==country,'Total Population']).sum()
    #print minimum
   
    return (minimum,maximum)
    

def run(fname):
    data = read_data(fname)
    
    print "Number of unique countries/territories:", num_countries(data)
    
    for country in ["Turks and Caicos Islands","Qatar"]:
        result = origins(data, country)
        print "Origin of refugees in {}:".format(country),', '.join(sorted(result))
        
    for country in ["Greece", "United States of America"]:    
        country_max = max_people(data, country)
        print "{} | Year of Maximum: {}, Number: {}".format(country,
                                                             country_max[0],
                                                             country_max[1])
    for country in ["France", "Australia"]:
        r = calc_2014range(data, country)
        print "2014 Range for {}: {}-{}".format(country, r[0], r[1])
    
def convert_to_numeric(data,value):
    data[value] = data[value].astype(str).convert_objects(convert_numeric=True)
    
             
if __name__ == '__main__':
    run("unhcr_popstats_export_persons_of_concern_all_data.csv")

