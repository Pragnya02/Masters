import pandas as pd
import difflib
from multiprocessing import Process
import time

disease = "DISEASE"


def clean_data(df,columnName):
    #Change the column names with respect to whats needed.
    if columnName=='DEATHS':
        df.rename(columns={columnName:'Count'},inplace=True)

    else:
        df.rename(columns={columnName:disease},inplace=True)
    #Change the disease column to upper case (to match all df's)
    df[disease] = map(lambda x: x.upper(), df[disease])

    return df

def count_per_disease(df,name):
    death_count_per_disease = df.groupby(disease)['Count'].sum()
    print "IN ",name
    print death_count_per_disease

def find_same_disease(df_NYC,dfcali_death,dfUSA_death):
    #Find diseases that are common in the three dfs
    dfs=[df_NYC,dfUSA_death,dfcali_death]
    print reduce(lambda x,y: (pd.merge(x,y, how='inner')),dfs)[disease].unique()

def change_disease(df,name):
    if name=='dfcali_death':
        df[disease] = (df[disease].replace({'HIV':'HUMAN IMMUNODEFICIENCY VIRUS DISEASE','HTD':'DISEASES OF HEART','OTH':'All Other Causes','LIV':'CHRONIC LIVER DISEASE AND CIRRHOSIS','HOM':'ASSAULT (HOMICIDE)','PNF':'INFLUENZA AND PNEUMONIA','INJ':'Unintentional Injuries','CLD':'CHRONIC LOWER RESPIRATORY DISEASES','STK':'CEREBROVASCULAR DISEASE','CAN':'MALIGNANT NEOPLASMS','HYP':'Essential Hypertension and Hypertensive Renal Disease','SUI':'INTENTIONAL SELF-HARM (SUICIDE)','AID':'AIDS','ALZ':'ALZHEIMERS DISEASE','DIA':'Diabetes Mellitus'},regex=True))
    elif name == 'dfUSA_death':
        df[disease] = (df[disease].replace({'Alzheimer\'s disease':'ALZHEIMERS DISEASE','Homicide':'ASSAULT (HOMICIDE)','Stroke':'Cerebrovascular Disease','CLRD':'Chronic Lower Respiratory Diseases','Diabetes':'DIABETES MELLITUS','Diseases of Heart':'DISEASES OF HEART','Essential hypertension and hypertensive renal disease':'Essential hypertension and renal disease','Suicide':'INTENTIONAL SELF-HARM (SUICIDE)','Cancer':'MALIGNANT NEOPLASMS','Parkinson\'s disease':'PARKINSONS DISEASE','Unintentional Injuries':'ACCIDENTS EXCEPT DRUG POISONING','All Causes':'all other Causes'},regex=True))

        print ""

    '''
    elif name=='df_cali':
        df[disease] = (df[disease].replace({'Alzheimer\'s disease','ALZHEIMERS DISEASE'},regex=True))
        print "CALI DIseases"
        print df[disease].unique()
        print " ***************************************"
    '''

    df[disease]= df[disease].str.upper()

    return df



def load_files():
    df_NYC = pd.read_csv("/home/paggu/Masters/Python/Pandas_Project/NYC_Health/New_York_City_Leading_Causes_of_Death.csv")

    df_NYC = clean_data(df_NYC,"Cause of Death")
    #print df_NYC[disease].unique()

    '''
    df_cali = pd.read_csv("/home/paggu/Masters/Python/Pandas_Project/Cali_disease/Infectious_Disease_Cases_by_County__Year__and_Sex__2001-2014.csv")
    df_cali = clean_data(df_cali,"Disease")
    df_cali = change_disease(df_cali,"df_cali")
    #print df_cali[disease].unique()
    '''

    dfcali_death = pd.read_csv("/home/paggu/Masters/Python/Pandas_Project/Cali_death/Leading_Causes_of_Death_by_ZIP_Code__1999-2013.csv")
    dfcali_death = clean_data(dfcali_death,"Causes of Death")
    dfcali_death = change_disease(dfcali_death,"dfcali_death")

    #print dfcali_death[disease].unique()

    dfUSA_death = pd.read_csv("/home/paggu/Masters/Python/Pandas_Project/death_US/Leading-causes-State-Year.csv")
    dfUSA_death = dfUSA_death.convert_objects(convert_numeric=True) #DEATHS column was in string dtype,converted that to numeric

    dfUSA_death = clean_data(dfUSA_death,"CAUSE_NAME")
    dfUSA_death = clean_data(dfUSA_death,"DEATHS")
    dfUSA_death = change_disease(dfUSA_death,"dfUSA_death")
    #print dfUSA_death[disease].unique()

    #Using multiprocessingto support parallel call of function - reduces execution time
    p1 = Process(target=count_per_disease(df_NYC,"New York"))
    p1.start()
    p2 = Process(target=count_per_disease(dfcali_death,"California"))
    p2.start()
    p3 = Process(target=count_per_disease(dfUSA_death,"USA"))
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    #play_with_df(df_NYC)
    '''
    count_per_disease(df_NYC,"New York")
    print "******************"
    count_per_disease(dfcali_death,"California")
    print "******************"
    count_per_disease(dfUSA_death,"USA")
    '''
    #find_same_disease(df_NYC,dfcali_death,dfUSA_death)

if __name__ == '__main__':

    start_time = time.time()
    load_files()
    print (time.time() - start_time)
