"""
Purpose: This programe covert CSV data to JSON format and display it.
Author:  Umesh Tiwari
Date:    24/10/2021
Language:Python
Version: 3.7 onwards
prerequisite :

1)data.csv file should be present in same path as this script
2)Python 3.7 + version should be installled in Linux Environment
3)Python Pandas Library should be installed.
"""

import sys
import os

#Validating if required library are installed in environment or not

try:
    import pandas as pd
except Exception as e:
    print("Missing Library ,Please install pandas library to run the programe")
    sys.exit(1)


#Python function to Create Json output
    
def to_flare_json(df):


    d = {"Output":"CSVTOJSON", "children": []} #create list of dictinory to store json output
    for index, row in df.iterrows():
        parent = row[3] #considering parent key as fourth coulmn of csv
        key_list = []   #Make a list of keys which holds unique parent name
        for item in d['children']:
            key_list.append(item['name'])

        #if 'parent' is NOT a key in list then append it to dictionary
        if not parent in key_list:
            d['children'].append({"name": parent, "children":[{"label": row[6], "id": row[7], "link": row[8],"children":[]}]})
        #if parent IS a key in list add a new child to it
        else:
            d['children'][key_list.index(parent)]['children'].append({"label": row[6], "id": row[7], "link": row[8],"children":[]})

    #Writing json format output
    with open('output.txt', 'w') as the_file:
        the_file.write("%s"%d)
        


#Checking if file is present or not .If Present it will read data from CSV to dataframe




try:
    df = pd.read_csv("data.csv")
except Exception as e:
    print("Missing File ,Please Check if file:data.csv is present in path:%s"%os.getcwd())
    sys.exit(1)

df=df.dropna(how='any')                     #removing rows from dataframe which contains null columns or incomplete row
df.drop(df.columns[0], axis=1,inplace=True) #removing first column from dataframe as it do not required
to_flare_json(df)                           #passing dataframe to function to convert into json
