import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd 
import numpy as np
# import pymongo
from pymongo import MongoClient

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    # function to read Phissing data and convert into json
    def csv_to_json_converter(self,file_path):
        try:
            # Reading data from csv
            data=pd.read_csv(file_path)
            # Drop default indexing in csv file
            data.reset_index(drop=True, inplace=True)
            # Converting csv in the list of json records
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    # Function to load data into mongo
    # def insert_data_mongodb(self,records,database,collection):
    #     try:
    #         self.database=database
    #         self.collection=collection
    #         self.records=records

    #         self.mongo_client=pymongo.mongo_client(MONGO_DB_URL)
    #         self.database = self.mongo_client[self.database]

    #         self.collection = self.database[self.collection]
    #         self.collection.insert_many(self.records)
    #         return(len(self.records))
    #     except Exception as e:
    #         raise NetworkSecurityException(e,sys)
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.records = records

            self.mongo_client = MongoClient(
                MONGO_DB_URL,
                tlsCAFile=certifi.where()
            )

            self.database = self.mongo_client[database]
            self.collection = self.database[collection]

            self.collection.insert_many(self.records)
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

        

if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="ANKITAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)