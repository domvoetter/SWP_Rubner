from copy import copy
from ListElementEinfach import *

class EinfachVerketteteListe:

    def __init__(self):
        self.startElem = ListElementEinfach(None)


    # append
    def addLast(self, o):
        if self.startElem.getObj == None:
            self.startElem = ListElementEinfach(o)
        else:
            newElem = ListElementEinfach(o)
            lastElem = self.getLastElem()
            lastElem.setNextElem(newElem)


    # insert
    def insertAfter(self, prevItem, newItem):
        nextElem = ListElementEinfach(None)
        pointerElem = self.startElem.getNextElem()
        while pointerElem != None and pointerElem.getObj() != prevItem:
            pointerElem = pointerElem.getNextElem()
        newElem = ListElementEinfach(newItem)
        nextElem = pointerElem.getNextElem()
        pointerElem.setNextElem(newElem)
        newElem.setNextElem(nextElem)


    # remove
    def delete(self, o):
        le = self.startElem
        while le.getNextElem() != None and le.getObj() != o:
            if le.getNextElem().getObj() == o:
                if le.getNextElem().getNextElem() != None:
                    le.setNextElem(le.getNextElem().getNextElem())
                else:
                    le.setNextElem(None)
                    break
            le = le.getNextElem()
        return o

    # index
    def index(self, o):
        le = self.startElem
        cnt = 0
        while le != None:
            cnt += 1
            if le.getObj() == o:
                return cnt-1
            le = le.nextElem
        return None


    def find(self, o):
        le = self.startElem
        while le != None:
            if le.getObj() == o:
                return True
            le = le.nextElem
        return False

    
    def getFirstElem(self):
        return self.startElem

    
    def getLastElem(self):
        le = self.startElem
        while le.getNextElem() != None:
            le = le.getNextElem()
        return le


    def writeList(self):
        le = self.startElem
        while le != None:
            print(str(le.getObj()) + "  ")
            le = le.getNextElem()

    
    # count
    def printLength(self):
        le = self.startElem
        cnt = 0
        while le != None:
            cnt += 1
            le = le.nextElem
        return cnt


    # clear (ganze Liste löschen)
    def clear(self):
        le = self.startElem
        zw = le
        for i in range(self.printLength()):
            if zw.getNextElem() is not None:
                le = zw.getNextElem()
                zw = copy(le)
                self.delete(le.getObj())
            else:
                self.delete(self.getFirstElem().getObj())
                self.delete(self.getLastElem().getObj())


    # copy
    def copyList(self):
        copied = EinfachVerketteteListe()
        le = self.startElem
        while le is not None:
            if le.getNextElem() is not None:
                le = le.getNextElem()
                copied.addLast(le.getObj())
            else:
                return copied


    # extend (hinzufügen aller Elemente einer anderen Liste)
    def extend(self, secondList):
        le = secondList.startElem.getNextElem()
        while le is not None:
            self.addLast(le.getObj())
            le = le.getNextElem()

    # pop ( löscht den Eintrag aus der Liste des übergebenen Index und liefert dessen Inhalt als Rückgabewert )
    def pop(self, index):
        le = self.startElem
        for c in range(index):
            le = le.getNextElem()
        self.delete(le.getObj())
        return le.getObj()


    # sort
    def sortalt(self):
        minimum = None
        le = self.startElem
        while le != None:
            minimum = le.getNextElem()
            while minimum != None:
                print(minimum.getObj())
                if(le.getObj() > minimum.getObj()):
                    a = le.getNextElem()
                    le.setObj(minimum)
                    self.addLast(a)
                minimum = minimum.getNextElem()
            le = le.getNextElem()

    def sort(self):
        if not self.startElem:
            return
    
        swapped = True
        while swapped:
            swapped = False
            current = self.startElem
            while current.nextElem:
                runner = current.nextElem
                if current.obj is not None and runner.obj is not None: # Vergleichsbedingung hinzufügen
                    if current.obj > runner.obj:
                        current.obj, runner.obj = runner.obj, current.obj
                        swapped = True
                current = current.nextElem

    def reverse(self):
        previousElem = None
        currentElem = self.startElem
        while currentElem:
            nextElem = currentElem.getNextElem()
            currentElem.nextElem = previousElem
            previousElem = currentElem
            currentElem = nextElem
        self.startElem = previousElem