#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pyodbc
import collections
from pymongo import MongoClient

class DataTransfer(object):
    def __init__(self):
        self.MongoConnection = None
        self.MsSQLConnection = None

    def MongoDbConnect(self, server, port, dbname, collection):
        try:
            self.MongoConnection = MongoClient(server, port, serverSelectionTimeoutMS=10, connectTimeoutMS=15000)
            db = self.MongoConnection[dbname]
            return db[collection]
        except:
            print("HATA : MongoDb Veriler Alınamadı")

    def MsSQLConnect(self, Server, DataBase, UserName, Password, TableName):
        #try:
            self.MsSQLConnection = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server="+Server+";Database="+DataBase+";uid="+UserName+";pwd="+Password)
            sqlCur = self.MsSQLConnection.cursor()
            sqlCur.execute("select * from " + TableName)
            return sqlCur.fetchall()
        #except:
        #    print("HATA : MsSQL Veriler Alınamadı")

    def TabloAktar(self, data, MongoTable):
        odbcArray = []
        for tuple in data:
            doc = collections.OrderedDict()
            id = 0
            for item in data[0].cursor_description:
                doc[item[0]] = tuple[id]
                id += 1
            odbcArray.append(doc)

        MongoTable.insert_many(odbcArray)

    def TabloSil(self, MongoTable):
        MongoTable.delete_many({})

    def Disconnect(self):
        self.MongoConnection.close()
        self.MsSQLConnection.close()

MyObj = DataTransfer()

MsSQL = MyObj.MsSQLConnect( "192.168.1.2","msdatabase","username","password","mstable")
Mongo = MyObj.MongoDbConnect("localhost", 27017, "mongotest","test")

#MyObj.TabloSil(Mongo)   # MongoDB Tablosunu boşaltır
MyObj.TabloAktar(MsSQL, Mongo) # MSSQL'deki verileri MongoDB'ye aktarır 

MyObj.Disconnect()
