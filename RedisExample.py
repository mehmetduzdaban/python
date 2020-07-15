#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis

class MyClass(object):
    def __init__(self, server, port=6379):
        try:
            self.db = redis.StrictRedis(server, port, 0)
            self.db.get('anything')
        except:
            print("Error : Could not connect to redis server")
    
    def GenerateKey(self):
        return self.db.incr("id")

    def AddData(self, key, value):
        self.db.set(key, value)
    
    def DelData(self, key):
        if self.CheckKey(key):
            self.db.delete(key)
        else:
            print("Error : Key does not exists!")
    
    def CheckKey(self, key):
        return self.db.exists(key)

    def DeleteAll(self):
        self.db.flushdb()

    def GetData(self, key):
        print(self.db.get(key))

if __name__ == "__main__":
    obj = MyClass("localhost")
    obj.AddData("author", "ahmet")
    obj.GetData("author")
    obj.DelData("author")
    obj.GenerateKey()
