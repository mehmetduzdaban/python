#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=10, connectTimeoutMS=15000)
    db = client.mongotest
except ConnectionFailure:
    print("MongoDb Sunucusuna Bağlanılamadı")

class MyClass(object):
    def __init__(self, olusturan, aciklama):
        self.Tarih = str(datetime.datetime.now())
        self.Olusturan = olusturan
        self.Aciklama = aciklama
    
    def Ekle(self):
        log = db.test.insert_one(self.__dict__)
        print(log.inserted_id, " ID Numaralı kayıt eklendi.")    
    
    def Sil(self):
        log = db.test.delete_many({})
        print(log.deleted_count, " Adet kayıt silindi.")

    def Listele(self):
        print(self.__dict__)

if __name__ == "__main__":
    obj = MyClass("aerdogan", "deneme")
    obj.Sil() # Kayıtları sil
    obj.Ekle() # Kayıt ekle
    obj.Listele() # Kayıtları Listele
