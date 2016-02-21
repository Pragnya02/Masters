import pandas as pd
import difflib
from multiprocessing import Process
import time
import matplotlib.pyplot as plt


#Initializing Global Variable, to be used in many functions
disease = "DISEASE"

def clean_data(df,columnName):
    #Change the column names with respect to whats needed.
    if columnName=='DEATHS':
        df.rename(columns={columnName:'Count'},inplace=True)

    elif columnName=='YEAR':
        df.rename(columns={columnName:'Year'},inplace=True)
    else:
        df.rename(columns={columnName:disease},inplace=True)
    #Change the disease column to upper case (to match all df's)
    df[disease] = map(lambda x: x.upper(), df[disease])

    return df



def count_per_disease(df,name):

    death_count_per_disease = df.groupby(disease)['Count'].sum()
    print " "
    print "DEATH DUE TO DISEASES IN ",name
    print "------------"
    print (death_count_per_disease.reset_index()).sort_values(by='Count',ascending=False)

    if name=='USA':

        #Death due to disease in Al States

        death_count_per_disease.plot(kind='bar',x=disease,y='Count')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)


def death_per_year(df):
    year = df['Year'].unique()
    indexx={}
    #Using dict to store {year, last index for year} pair
    for i in year:
        indexx[i] = (df['Year']==i+1).argmax() - 1

    '''
    {1999: 883, 2000: 1767, 2001: 2651, 2002: 3535, 2003: 4419, 2004: 5303, 2005: 6187, 2006: 7071, 2007: 7955, 2008: 8839, 2009: 9723, 2010: 10607, 2011: 11491, 2012: 12375, 2013: -1}

    '''
    #Removing All causes disease from the df
    df=df[df[disease] != 'ALL CAUSES']
    #print (df.loc[df['Year']==2011]).loc[df[disease]=='DISEASES OF HEART']
    #put 1999-2002 together, 2003-2006 , 2007-2010, 2011-2013 according to index.

    #Creating DataFrames that stores all value for particular set of years (without using loc)
    df9902 = df[0:indexx[2002]]
    df0306 = df[indexx[2002]+1:indexx[2006]]
    df0710 = df[indexx[2006]+1:indexx[2010]]
    df1113 = df[indexx[2010]+1:indexx[2013]]
    #print df9902[0;3]

    df_Year9902 = ((df9902.pivot_table('Count',[disease,'STATE'],'Year')).reset_index())
    #print df_Year9902.groupby(['STATE'])[1999,2000,2001,2002].sum().reset_index()
    (df_Year9902.groupby(['STATE'])[1999,2000,2001,2002].sum().reset_index()).plot(kind='bar',x='STATE',subplots=True)
    plt.subplots_adjust(hspace=.5)
    #plt.show()

    df_Year0306 = ((df0306.pivot_table('Count',[disease,'STATE'],'Year')).reset_index())
    #print df_Year0306.groupby(['STATE'])[2003,2004,2005,2006].sum().reset_index()
    (df_Year0306.groupby(['STATE'])[2003,2004,2005,2006].sum().reset_index()).plot(kind='bar',x='STATE',subplots=True)
    plt.subplots_adjust(hspace=.5)
    #plt.show()

    df_Year0710 = ((df0710.pivot_table('Count',[disease,'STATE'],'Year')).reset_index())
    #print df_Year0710.groupby(['STATE'])[2007,2008,2009,2010].sum().reset_index()
    (df_Year0710.groupby(['STATE'])[2007,2008,2009,2010].sum().reset_index()).plot(kind='bar',x='STATE',subplots=True)
    plt.subplots_adjust(hspace=.5)
    #plt.show()

    df_Year1113 = ((df1113.pivot_table('Count',[disease,'STATE'],'Year')).reset_index())
    #print df_Year1113.groupby(['STATE'])[2011,2012,2013].sum().reset_index()
    (df_Year1113.groupby(['STATE'])[2011,2012,2013].sum().reset_index()).plot(kind='bar',x='STATE',subplots=True)
    plt.subplots_adjust(hspace=.5)
    plt.show()

    #All these plot show a similar trend in death count in each state in the years

def onlyNYC(df):
    #print df[0:10]
    #Detail of people who died in year/Ethnicity/Cause and number of deaths
    df['DiseaseInitials'] = df[disease].str[:3]

    df['Ethnicity']=df['Ethnicity'].replace('NON-HISPANIC 0BLACK','NON-HISPANIC BLACK')

    #Disease death in each year with their Initials
    dfy= df.groupby(['Year',disease,'DiseaseInitials'])['Count'].sum().reset_index()
    year=[]
    for i in dfy['Year'].unique():
        year.append(i)
    color=['red','green','pink','orange','blue']

    fig = plt.figure(figsize=(70, 70))
    a=321
    ax=[]
    for i in year:
        fig.subplots_adjust(hspace=.5)
        ax.append(fig.add_subplot(a+year.index(i)))
        (dfy.loc[dfy['Year'] == i]).plot(kind='bar',x='DiseaseInitials',y='Count',ax=ax[year.index(i)],color=color[year.index(i)])
        plt.legend([i],loc='upper left')
    plt.show()

    #Disease with respect to Gender
    dfGender=df.groupby(['Sex',disease,'DiseaseInitials'])['Count'].sum().reset_index()
    #Plot the comparison between deaths in Women vs Men
    fig = plt.figure(figsize=(70, 70))
    fig.subplots_adjust(hspace=.5)
    ax=fig.add_subplot(121)
    (dfGender.loc[dfGender['Sex']=='FEMALE']).plot(kind='bar',x='DiseaseInitials',y='Count',ax=ax)
    plt.title("Deaths due to disease in Women")

    ax=fig.add_subplot(122)
    (dfGender.loc[dfGender['Sex']=='MALE']).plot(kind='bar',x='DiseaseInitials',y='Count',ax=ax)
    plt.title("Deaths due to disease in Men")
    plt.show()

    #Disease death in each Ethnicity with the Initials
    dfe = df.groupby(['Ethnicity',disease,'DiseaseInitials'])['Count'].sum().reset_index()
    fig = plt.figure(figsize=(70, 70))
    a=221
    ax=[]
    eth=[]

    for j in dfe['Ethnicity'].unique():
        eth.append(j)
    ethN=['ASIAN & PACIFIC','HISPANIC ORIGIN','AFRICAN ORIGIN','EUROPEAN ORIGIN']

    for j in range(0,len(eth)):
        fig.subplots_adjust(hspace=.5)
        ax.append(fig.add_subplot(a+j))
        (dfe.loc[dfe['Ethnicity'] == eth[j]]).plot(kind='bar',x='DiseaseInitials',y='Count',ax=ax[j],color=color[j])
        plt.legend([ethN[j]],loc='upper left')
    plt.show()

    #Death in each Ethnicity in NYC
    print "TOTAL DEATHS IN EACH ETHNICITY "
    print df.groupby(['Ethnicity'])['Count'].sum().reset_index()

    print " These analysis show that Heart Disease is the leading cause of deaths in New York. To check for the Year of Maximum deaths:"
    print " "
    print ((df.loc[df[disease]=='DISEASES OF HEART']).groupby(['Year'])['Count'].sum()).reset_index().sort_values(by='Count',ascending=False)


def load_files():
    df_NYC = pd.read_csv("New_York_City_Leading_Causes_of_Death.csv")
    df_NYC = clean_data(df_NYC,"Cause of Death")
    #print df_NYC[disease].unique()

    dfcali_death = pd.read_csv("Leading_Causes_of_Death_by_ZIP_Code__1999-2013.csv")
    dfcali_death = clean_data(dfcali_death,"Causes of Death")

    dfUSA_death = pd.read_csv("Leading-causes-State-Year.csv")
    #dfUSA_death = dfUSA_death.convert_objects(convert_numeric=True) #DEATHS column was in string dtype,converted that to numeric

    dfUSA_death = clean_data(dfUSA_death,"CAUSE_NAME")
    dfUSA_death = clean_data(dfUSA_death,"DEATHS")
    dfUSA_death = clean_data(dfUSA_death,"YEAR")
    #dfUSA_death = change_disease(dfUSA_death,"dfUSA_death")
    dfUSA_death['Count'] = pd.to_numeric(dfUSA_death['Count'],errors='coerce')
    dfUSA_death=dfUSA_death[dfUSA_death['DISEASE'] != 'ALL CAUSES']
    dfUSA_death=dfUSA_death[dfUSA_death['STATE'] != 'United States']

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

    #Show count per disease in all States in USA - line 42
    plt.title('Deaths due to each disease in All States in USA')
    #plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.4)
    plt.show()

    #According to the previous plot result - death rate of Disease of Heart in all states
    print " "
    print "DEATHS IN ALL STATES due to DISEASES of HEART"
    print " "
    dfDIS = pd.DataFrame((dfUSA_death.loc[dfUSA_death[disease]=='DISEASES OF HEART']).groupby(['STATE'])['Count'].sum().reset_index())
    print dfDIS.sort_values(by='Count',ascending=False)
    dfDIS.plot(kind='bar',x='STATE',y='Count')
    plt.title("Death count due to DISEASES OF HEART")
    plt.show()

    print " "
    print "PERCENT OF DEATHS DUE TO DISEASES OF HEART : "
    print (dfDIS['Count'].sum())/(dfUSA_death['Count'].sum())*100

    #Show death in each state

    print " "
    print " DEATH COUNT IN EACH STATE IN USA"
    print ((dfUSA_death.groupby('STATE')['Count'].sum()).reset_index()).sort_values(by='Count',ascending=False)
    ((dfUSA_death.groupby('STATE')['Count'].sum()).reset_index()).plot(kind='barh',x='STATE', y='Count',stacked=True)

    plt.title('Death count in Each State in USA')
    plt.show()

    #Increasing/Decreasing total deaths wrt year, in all states in US
    ((dfUSA_death.groupby('Year')['Count'].sum()).reset_index()).plot(x='Year',y='Count',stacked=True)
    plt.title('Death count in All States in USA per year')
    plt.show()

    #Compare the deaths in 2002,2004 and 2011-2013

    dfYear = ((dfUSA_death.groupby(['Year',disease])['Count'].sum()).reset_index())

    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
    fig.subplots_adjust(hspace=.5)
    #ax.append(fig.add_subplot(a+i)
    dfYear.loc[dfYear['Year']==2002].plot(kind='bar',x=disease,y='Count',ax=ax1)
    ax1.set_title("2002")
    dfYear.loc[dfYear['Year']==2004].plot(kind='bar',x=disease,y='Count',ax=ax2)
    ax2.set_title("2004")
    dfYear.loc[dfYear['Year']==2013].plot(kind='bar',x=disease,y='Count',ax=ax3)
    ax3.set_title("2013")
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
    plt.show()

    #Load Dataframes with respect to year, and plot the Death count in each wrt year
    grpbyUSA = ((dfUSA_death.groupby(['Year',disease,'STATE'])['Count'].sum()).reset_index())

    df_Year = ((grpbyUSA.pivot_table('Count',[disease,'STATE'],'Year')).reset_index())
    death_per_year(grpbyUSA)
    plt.show()

    conti='Y'

    while conti=='Y':
        state = raw_input("Enter the country: (Make sure the spelling is right!) ").title()
        dfUSA_death1 = dfUSA_death
        #Create a column called D_Ini which stores the disease Initials (First 3 letters)
        dfUSA_death1['D_Ini'] = dfUSA_death1[disease].str[:3]
        dfUSA_death1 =  dfUSA_death1.loc[dfUSA_death1['STATE']==state] #
        dfUSA_death1 = (dfUSA_death1.groupby(['D_Ini','Year'])['Count'].sum().reset_index())
        dfUSA_death1=dfUSA_death1[dfUSA_death1['D_Ini']!='ALL']

        #Divide the years into sets to plot Disease Initials,Year
        dfUSA_death1.loc[dfUSA_death1['Year'] <= 2002].plot(kind='bar',x=['D_Ini','Year'],y='Count')#,subplots=True)
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
        plt.legend(["DEATH/DISEASE/YEAR"])
        plt.title(state)

        (dfUSA_death1.loc[(dfUSA_death1['Year'] > 2002) & (dfUSA_death1['Year'] <= 2006)]).plot(kind='bar',x=['D_Ini','Year'],y='Count')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
        plt.legend(["DEATH/DISEASE/YEAR"])
        plt.title(state)

        (dfUSA_death1.loc[(dfUSA_death1['Year'] >2006) & (dfUSA_death1['Year'] <= 2011)]).plot(kind='bar',x=['D_Ini','Year'],y='Count')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
        plt.legend(["DEATH/DISEASE/YEAR"])
        plt.title(state)
        plt.show()
        conti = raw_input("Do you want to Continue? (Y/N) ")

    #About NYC - call function to plot
    onlyNYC(df_NYC)

    #Check if disease of heart is common for many states in year 2007

    dfDIS = pd.DataFrame((dfUSA_death.loc[dfUSA_death[disease]=='DISEASES OF HEART']).groupby(['STATE','Year'])['Count'].sum().reset_index())
    (dfDIS.loc[dfDIS['Year']==2007]).plot(kind = 'bar',x='STATE',y='Count')
    plt.title("DEATH IN ALL STATES IN 2007, CAUSE: DISEASE OF HEART")
    plt.show()

#Function to analyze wordwide country Data
def analyze(df1,country):
    df = df1.drop(df1.columns[[0,1,4,6,8]], axis=1) #0,3,4,6,8,10,11,12,13,14])

    df['Mean'] = (df['mean']+df['mean'].shift(-1))[::2]
    df= df.dropna()
    df['sex_name']=df['sex_name'].replace('Male','Both')
    df['sex_name']=df['sex_name'].replace('Female','Both')

    #Taking values only for All Ages field
    df=(df.loc[df['age_group_name']=='All Ages']).groupby(['location_name','year','cause_name','unit'])['Mean'].sum().reset_index()
    df=(df.loc[df['unit']=='number']) #'rate per 100,000'])#
    df['Mean'] = df['Mean']*100000
    df=  df.groupby(['year','cause_name'])['Mean'].sum().reset_index()
    fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
    (df.loc[df['cause_name']=='Cardiovascular diseases']).plot(x='year',ax=ax1)#,ax=ax[0])
    ax1.legend(['Diseases of Heart'],loc='upper left')
    plt.title(country)
    df = df.loc[df['cause_name'].str.contains("cancer",case=False)]
    df = df.groupby(['year'])['Mean'].sum().reset_index()
    df.plot(x='year',y='Mean',ax=ax2)#,ax=ax[1])
    ax2.legend(['Cancer'],loc='upper left')
    plt.show()


def hispanic():
    df_Cuba= pd.read_csv("hispanic/IHME_GBD_2013_CUB_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Arg= pd.read_csv("hispanic/IHME_GBD_2013_ARG_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Chl= pd.read_csv("hispanic/IHME_GBD_2013_CHL_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Cri= pd.read_csv("hispanic/IHME_GBD_2013_CRI_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Col= pd.read_csv("hispanic/IHME_GBD_2013_COL_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Bol= pd.read_csv("hispanic/IHME_GBD_2013_BOL_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Mex= pd.read_csv("hispanic/IHME_GBD_2013_MEX_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")

    analyze(df_Cuba,"CUBA")
    analyze(df_Arg,"ARGENTINA")
    analyze(df_Chl,"CHILE")
    analyze(df_Cri,"COSTA RICA")
    analyze(df_Col,"COLUMBIA")
    analyze(df_Bol,"BOLIVIA")
    analyze(df_Mex,"MEXICO")


def nonhispwhite():

    df_Nor = pd.read_csv("white/IHME_GBD_2013_NOR_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Swe = pd.read_csv("white/IHME_GBD_2013_SWE_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Bel = pd.read_csv("white/IHME_GBD_2013_BEL_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Irl = pd.read_csv("white/IHME_GBD_2013_IRL_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Nld = pd.read_csv("white/IHME_GBD_2013_NLD_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")

    analyze(df_Nor,"NORWAY")
    analyze(df_Bel,"BELGIUM")
    analyze(df_Swe,"SWEDEN")
    analyze(df_Irl,"IRELAND")
    analyze(df_Nld,"NETHERLAND")

def nonhispblack():
    df_Egy = pd.read_csv("black/IHME_GBD_2013_EGY_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Eth = pd.read_csv("black/IHME_GBD_2013_ETH_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Gha = pd.read_csv("black/IHME_GBD_2013_GHA_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Sud = pd.read_csv("black/IHME_GBD_2013_SDN_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Zwe = pd.read_csv("black/IHME_GBD_2013_ZWE_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")

    analyze(df_Egy,"EGYPT")
    analyze(df_Eth,"ETHIOPIA")
    analyze(df_Gha,"GHANA")
    analyze(df_Sud,"SUDAN")
    analyze(df_Zwe,"ZIMBABWE")

def asian():
    df_Aus = pd.read_csv("asian/IHME_GBD_2013_AUS_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Malay = pd.read_csv("asian/IHME_GBD_2013_MYS_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Pak = pd.read_csv("asian/IHME_GBD_2013_PAK_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Ind = pd.read_csv("asian/IHME_GBD_2013_IND_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")
    df_Chn = pd.read_csv("asian/IHME_GBD_2013_CHN_DEATHS_BY_CAUSE_1990_2013_Y2014M12D17.csv")

    analyze(df_Aus,"AUSTRALIA")
    analyze(df_Malay,"MALAYSIA")
    analyze(df_Pak,"PAKISTAN")
    analyze(df_Ind,"INDIA")
    analyze(df_Chn,"CHINA")

if __name__ == '__main__':
    start_time = time.time()
    load_files()
    
    #Worldwide Data
    option = raw_input(" Do you want to see Analysis of different Origin? Y/N ")
    while option=='Y':
        origin = raw_input("Choose one of these: asian/hispanic/european/african ")
        if origin=='asian':
            asian()
        elif origin=='hispanic':
            hispanic()
        elif origin=='european':
            nonhispwhite()
        elif origin=='african':
            nonhispblack()
        else:
            print "You entered the Origin which is not in our list!! "

        option = raw_input(" Do you want to see Analysis of different Origin? Y/N ")

    print "With these analysis,we can conclude that Origin might not be a reason for deaths due to Diseases of Heart, but Cancer could be genetic"

    #Print total execution time- used to find difference between using multiprocessor, and wihtout that.
    print "Execution Time: ",(time.time() - start_time)
