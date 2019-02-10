import redis as rd
import sys
sys.path.insert(0, 'C:/Users/Alan Sanchez/Desktop/Actividad3/data-structures')
from StringStruct import *
from List import *
from Set import *
from Hash import *

def create(struct):
    struct.create()

def read(struct):
    struct.read()

def update(struct):
    struct.update()

def delete(struct):
    struct.delete()

def main():
    while 1:
        print("Transactions\n1.- Create \n2.- Read \n3.- Update \n4.- Delete \n0.- Exit program")
        option = input('Choose A Transaction: ')
        if option == 0:
                print("Closing the application")
                exit()       

        switcher = {
                1: create,
                2: read,
                3: update,
                4: delete
        }
        CRUDOperation = switcher.get(option, lambda: "Invalid Operation")
        while 1:
                print("Choose a Structure\n1.- String\n2.- List\n3.- Set\n4.- Hash\n0.- Return\n")
                structOpt = input("Enter the struct option: ")
                if structOpt == 0:
                        break
                switcher2 = {
                        1: StringStruct,
                        2: List,
                        3: Set,
                        4: Hash
                }
                struct = switcher2.get(structOpt, lambda: "Invalid Estructure")
                CRUDOperation(struct)
                

main()