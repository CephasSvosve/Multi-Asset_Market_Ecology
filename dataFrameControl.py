import numpy as np
import pandas as pd

class dfControl:
    
    def appendNextRow(dataFrame,newRow):
        try:
            dataFrame.loc[len(dataFrame)]  = newRow  
        except:
            print('newRow does not match dataFrame columns')   
        

    def replaceRowAt(dataFrame,newRow,index):
        try:
            dataFrame.loc[index]  = newRow  
        except:
            print('newRow does not match dataFrame columns')  
        

    def addFirstRow(dataFrame,newRow):
        try:
            dataFrame.loc[0]  = newRow
        except:
            print('newRow does not match dataFrame columns')
        

    def getLastRow(dataFrame):
        return dataFrame.iloc[-1]

        
    def getRow(index,dataFrame):
        return dataFrame.iloc[index]
        

    def getPenultimateRow(dataframe):
        if len(dataframe)>1:
            return dataframe.iloc[-2]
        else:
            return np.zeros(len(dataframe.columns))


    def getColumn(columnName, dataframe, lastValueOnly):
        if lastValueOnly == False:
            return dataframe[columnName]
        if lastValueOnly == True:
            return dataframe[columnName].values[-1]

    
    
        