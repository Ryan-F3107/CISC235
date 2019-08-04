'''
Name: Ryan Fernandes
CISC 235, Assignment 1.1
'''
import random
class bag:
    def __init__(self):
        self.base=[]
    def add(self,item): #adds items into the abstract bag
        return self.base.append(item)

    def remove(self):
        num=random.randint(0,len(self.base)-1)  #random number generator
        print("item to be removed: ", self.base[num])
        del self.base[num]  #removes an item randomly
        return self.base

    def contains(self, item):
        if item in self.base:   #checks if the item is in the bag
            print(" The item",item,"is in the bag")
            return True
        else:
            print(" The item", item, "is not in the bag")
            return False

    def numItems(self): #counts the number of items in the bag.
        print("The number of items in the bag:",len(self.base))
        return len(self.base)

    def grab(self): #grabs an item at random from the bag, but does not remove it.
        if len(self.base) == 0:
            print("bag is empty")
        else:
            num=random.randint(0,len(self.base)-1)
            print("item grabbed at random is :",self.base[num])

    def __str__(self):  #prints the items in ADT Bag
        return str(self.base)

def main():
    #Test to see if the program works properly
    b=bag() #created a new ADT bag
    print(b.__str__())
    b.add("cat")
    b.add(14)
    b.add(12.3)
    b.add(182)
    b.add("mosquito")
    print(b.__str__())
    b.numItems()
    b.remove()
    b.numItems()
    print(b.__str__())
    b.contains(14)
    b.contains('c')
    b.contains("cat")
    print(b.__str__())
    b.grab()
main()
