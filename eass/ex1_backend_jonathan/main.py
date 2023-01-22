from fastapi import FastAPI
#import datetime as dt
#import pandas_datareader as web
import json
#import DB 
#import os, sys
#import module 
#import numpy as np
#import matplotlib.pyplot as plt
import requests
import pandas as pd
import yfinance 

#from sklearn.preprocessing import MinMaxScaler

#TODO --->>> real time data ---- פתאום הפסיק לעבוד, מקווה שאצליח למצוא פתרון

async def getData(num):
    dataDict = {
        1 : "META",
        2 : "BTC-USD",
        3 : "TSLA",
        4 : "KO",
        5 : "GC=F"
    }
    

    base = r"./DBs/"
    df = pd.DataFrame(pd.read_csv(base + dataDict[num]+".csv"))
    print("data of "+ dataDict[num])
    print(type(df))
    print(df)
    return df



app = FastAPI()


@app.get("/")
async def home():

    return "Welcome Home, Select Your Choice To Make a Prediction:"
#---------------------------------------------------------------
#---------------------------------------------------------------


 #-----------------------------------------------CocaCola function:----------------------
@app.get("/CocaCola") 
async def getCocaColaData():
    #df = getData(4)
# TODO sending the DataFrame To ML microservice to process the data
#    x = DataToML(df,4)
    start = pd.to_datetime('2018-01-01')
    end = pd.datetime.now()
    df = yfinance.download('KO',start,end) #['Adj Close']
    df_To_UI = df['Adj Close']
    return df.to_json()   


# TODO Updating the csv file in new real time data ----> לא כלכך עובד עכשיו 
    return "Updating new CocaCola's data to DB"



#-----------------------------------------------TESLA function:--------------------

#select silver data
@app.get("/TESLA") 
async def getTeslaData():
    #df = yfinance.download(dropdown,start,end)['Adj Close']

    #df = getData(3)
    start = pd.to_datetime('2018-01-01')
    end = pd.datetime.now()
    df = yfinance.download('TSLA',start,end) #['Adj Close']
    df_To_UI = df['Adj Close']
# TODO sending the DataFrame To ML microservice to process the data
#    x = DataToML(df,3)

    return df.to_json()  

# TODO Updating the csv file in new real time data ----> לא כלכך עובד עכשיו 
    return "Updating new TESLA's data to DB"

#------------------------------------------------------------------------------------

#-----------------------------------------------BitCoin function----------------
#select bitcoin data
@app.get("/BitCoin") 
async def getBitCoinData():
    
    #df = getData(2)
# TODO sending the DataFrame To ML microservice to process the data
#    x = DataToML(df,2)
    start = pd.to_datetime('2018-01-01')
    end = pd.datetime.now()
    df = yfinance.download('BTC-USD',start,end) #['Adj Close']
    df_To_UI = df['Adj Close']

    return df.to_json() 



# TODO Updating the csv file in new real time data ----> לא כלכך עובד עכשיו     
    return "Updating BitCoins' data to DB"

#-------------------------------------------------------------------------------


#-----------------------------------------------Meta function-------------------
@app.get("/Meta") 
async def GetMetaData():
    #df = getData(1)
    start = pd.to_datetime('2018-01-01')
    end = pd.datetime.now()
    df = yfinance.download('META',start,end) #['Adj Close']
    df_To_UI = df['Adj Close']
    print(df)
    
# TODO sending the DataFrame To ML microservice to process the data
#    x = DataToML(df,1)

    return df.to_json()




#--------------------------------------------------------------------------------
@app.get("/Gold") 
async def getGoldData():
    #df = getData(5)
    start = pd.to_datetime('2018-01-01')
    end = pd.datetime.now()
    df = yfinance.download('GC=F',start,end) #['Adj Close']
    #df_To_UI = df['Adj Close']
    print(df)
# TODO sending the DataFrame To ML microservice to process the data
#    x = DataToML(df,1)

    return df.to_json()


        #df = getData(1)


#--------------------------------------------------------------------------------

###(conector with UI)
###funcUI_Selector  -> getting the chice of dropbox and fit the right backend func

@app.get("/selector/{choice_id}") 
async def funcUI_Selector(choice_id):
    #something i get from DropBox of UI
    #TODO finish the function...
    dataDict = {
    "1" : GetMetaData(),
    "2" : getBitCoinData(),
    "3" : getTeslaData(),
    "4" : getCocaColaData(),
    "5" : getGoldData()
}

@app.get("/MultiGraph") 
async def getMultigraphData(stocks,start,end):
    #df = getData(5)
    #start = pd.to_datetime('2018-01-01')
    #end = pd.datetime.now()
    #start = pd.to_datetime(lst[1])
    #end = pd.to_datetime(lst[2])
    #df = yfinance.download(stocks,start,end) #['Adj Close']
    df = yfinance.download(stocks[0],start,end)
    #df_To_UI = df['Adj Close']
    print(df)
# TODO sending the DataFrame To ML microservice to process the data
#    x = DataToML(df,1)

    return df.to_json()


        #df = getData(1)





