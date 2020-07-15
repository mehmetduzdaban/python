#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=10, connectTimeoutMS=15000)
    db = client.mongotest
except ConnectionFailure:
    print("Error : MongoDb Server Connection Failure")

class MyClass(object):
    def __init__(self, author, description):
        self.Date = str(datetime.datetime.now())
        self.Author = author
        self.Description = description
    
    def Add(self):
        log = db.test.insert_one(self.__dict__)
        print(f"ID : { log.inserted_id } - Record Added.")    
    
    def Delete(self):
        log = db.test.delete_many({})
        print(f"{ log.deleted_count} Record Deleted.")

    def List(self):
        print(self.__dict__)

if __name__ == "__main__":
    obj = MyClass("author name", "description")
    #obj.Delete() # Delete Records
    obj.Add() # Add One Record
    obj.List() # List Records
