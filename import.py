#This file imports csv file from local space to mongodb

from pymongo import MongoClient
import pandas as pd
client = MongoClient()
db=client.elections
candetails = db.candetails
file=input('enter the file name')
def insert(file):
	data = pd.read_csv("C://Users//win//Desktop//"+file+".csv") #csv file which you want to import
	records_ = data.to_dict(orient = 'records')
	result = db.candetails.insert_many(records_ )
	return 0
insert(file)