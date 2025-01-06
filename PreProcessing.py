import pandas as pd
#import numpy as np

data = pd.read_csv("movies.csv")

#print(data.sample(random_state=3))

#print(data.info())

print(data.isnull().sum())


#case1: deleting the row which has all null values
#data_1=data.dropna(axis=0,how="all")
#print(len(data))
#print(len(data_1))

#case2: deleting row if any data is null
data_1=data.dropna(axis=0,how="any")
#print(len(data))
#print(len(data_1))
#print(data_1.isnull().sum())
print(data_1.info())

#case3: deleting only those rows where a particular attribute is null
data_1=data.dropna(axis=0, how="all", subset=["GENRE"])
#print(data_1.isnull().sum())

#delete a column
print(data.info())
data=data.drop(["Gross"],axis=1)
#print(data.isnull().sum())

data["VOTES"]=data['VOTES'].fillna("0")
#print(data["VOTES"])

