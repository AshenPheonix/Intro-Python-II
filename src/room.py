# Implement a class to hold room information. This should have name and
# description attributes.
from pprint import pprint

class Room(object):
    def __init__(self, name, desc,inv=None):
        self.name=name
        self.desc=desc
        self.n_to=None
        self.s_to=None
        self.e_to=None
        self.w_to=None
        if inv:
            self.inv=inv
        else:
            self.inv=[]
    
    def __str__(self):
        return f"ROOM: {self.name},{self.desc}"

    def addToInv(self, *items):
        if len(items)>0:
            for item in items:
                self.inv.append(item)
        

    def removeFromInv(self, *items):
        if len(items)>0:
            for item in items:
                if self.inv.index(item):
                    self.inv.remove(item)
    
    def printInv(self):
        ret=''
        for item in self.inv:
            ret+=f"{item.name} is here\n"
        return ret