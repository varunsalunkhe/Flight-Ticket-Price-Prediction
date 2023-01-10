import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


data = pd.read_excel("FlightFare_Dataset.xlsx")
data.head()



# Handling Date_of_Journey Column

data["journey_date"]=pd.to_datetime(data["Date_of_Journey"], format= "%d/%m/%Y").dt.day
data["journey_Month"]=pd.to_datetime(data["Date_of_Journey"], format= "%d/%m/%Y").dt.month
data.drop(["Date_of_Journey"],axis=1, inplace=True)
data.head()



# Handling Dep_Time Column

data["Dep_hour"]=pd.to_datetime(data["Dep_Time"]).dt.hour
data["Dep_minute"]=pd.to_datetime(data["Dep_Time"]).dt.minute
data.drop(["Dep_Time"], axis=1,inplace=True)
data.head()



#Handling Arrival_time column

data["Arrival_hour"]= pd.to_datetime(data.Arrival_Time).dt.hour
data["Arrival_minute"]= pd.to_datetime(data.Arrival_Time).dt.minute
data.drop(["Arrival_Time"], axis=1, inplace=True)

data.head()


data.Additional_Info.value_counts()



#Handling Duration column

dur= list(data.Duration)

for i in range(len(dur)):
    if len(dur[i].split()) != 2:
        if "h" in dur[i]:
            dur[i] = dur[i].strip() + " 0m"   
        else:
            dur[i] = "0h " + dur[i] 
            

Duration_hour=[]
Duration_minute=[]

for i in dur:
    
    a,b =i.split(sep="h")
    Duration_hour.append(int(a))
    m=b.strip()
    Duration_minute.append(int(m[0:len(m)-1]))

data["Duration_hour"]=Duration_hour
data["Duration_minute"]=Duration_minute
data.drop("Duration", axis=1, inplace=True)
data.head()


data["Airline"].value_counts()


air_count=data["Airline"].value_counts()
check=list(air_count.index[0:8])
type(check)


#Handling Airline Column

airline=data["Airline"]
new_airline=[]


for i in range(airline.shape[0]):
    if airline[i] in check:
        new_airline.append(airline[i])
    else:
        new_airline.append("Other")
data["Airline"]=new_airline
data["Airline"].value_counts()



airplane_dummy = pd.get_dummies(data.Airline)
print(airplane_dummy.shape)
airplane_dummy.head()



#Handling Source Column

data.Source.value_counts()

source = pd.get_dummies(data.Source)
source.head()


#Handling Destination Column

data.Destination.value_counts()


destination =pd.get_dummies(data.Destination)
destination.head()


# Additional_Info contains almost 80% no_info
# Route and Total_Stops are related to each other
data.drop(["Route", "Additional_Info"], axis = 1, inplace = True)


Total_Stops = pd.get_dummies(data.Total_Stops)
Total_Stops.head()



data.drop(["Airline","Source","Destination","Total_Stops"],  axis=1, inplace=True)
data.head()


data=pd.concat([airplane_dummy, source,destination,Total_Stops,data],axis=1)
data.head()


x=data.loc[:,data.columns!="Price"]
y=data["Price"]


from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(x, y)

data_c = pd.read_excel("FlightFare_Dataset.xlsx")
data_c.iloc[937:938,:]


import joblib
joblib.dump(model, 'model.pkl')

first_half_columns= data_c.columns[:4]
joblib.dump(first_half_columns, 'first_half_columns.pkl')

sec_half_columns=x.columns[-8:]
joblib.dump(sec_half_columns, 'sec_half_columns.pkl')

all_cols=x.columns[:25]
joblib.dump(all_cols, 'all_cols.pkl')


