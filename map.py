import pandas as pd 
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt

import folium
from folium.plugins import MarkerCluster

from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree


from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler 
from sklearn import metrics
import sqlite3
from collections import Counter

#connection
def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except sqlite3.Error as e:
        print(e)

    return conn

#sql_statement
def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows




# def convert_dtype(x):
#     if not x:
#         return ''
#     try:
#         return str(x)   
#     except:        
#         return ''

conn = create_connection('normalized.db', False)
sql_statement = "SELECT Latitude, Longitude, IncidentType, Date FROM Crime WHERE Latitude != ''"
df=pd.read_sql(sql_statement, conn)
# print(type(df["Latitude"].iloc[0]))
#df=pd.read_csv('Crime_Incidents.csv',converters={'Full_address': convert_dtype})
# c_na=df['Longitude'].isna().sum()
# print(c_na)
# df = df[df['Location'].notna()]

df = df[["Latitude", "Longitude","IncidentType", "Date"]]

m = folium.Map(location=df[["Latitude", "Longitude"]].mean().to_list(), zoom_start=13)

# if the points are too close to each other, cluster them, create a cluster overlay with MarkerCluster, add to m
marker_cluster = MarkerCluster().add_to(m)
counter = 0
for i,r in df.iterrows():
    location = (r["Latitude"], r["Longitude"])
    folium.Marker(location=location,
                      popup = r['Date'],
                      tooltip=r['IncidentType'])\
    .add_to(marker_cluster)
    counter+=1
# save the map
m.save("buffalo_crime_map_db.html")


