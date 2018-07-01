#!/usr/bin/env python3
class Worker():
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def printMe(self):
        print("My name is %s\nMy occupation is %s" % (self.name, self.occupation))
