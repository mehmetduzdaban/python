#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis

class MyClass(object):
    def __init__(self, server, port, db):
        self.r = redis.StrictRedis(server, port, db)

    def AddData(self, key, value):
        self.r.set(key, value)
    
    def DelData(self, key):
        self.r.delete(key)

    def GetData(self, key):
        print(self.r.get(key))

if __name__ == "__main__":
    obj = MyClass("localhost", 6379, 0)
    obj.AddData("author", "ahmet")
    obj.GetData("author")
    obj.DelData("author")
