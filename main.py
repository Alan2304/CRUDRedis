import redis as rd
from DataStructures import *

def create(data):
    data.create()

def read(data):
    data.read()

def update(data):
    data.update()

def delete(data):
    data.delete()

def isValidTransaction(value):
    try:
        if 0 <= int(value) <= 4:
            return True
        else:
            return False
    except:
        return False

def isValidStructure(value):
    try:
        if 0 <= int(value) <= 5:
            return True
        else:
            return False
    except:
        return False

def main():
    while 1:

        print("Transactions\n1.- Create registry\n2.- Read value\n3.- Update registry\n4.- Delete registry\n0.- Exit program")
        selected = input('Choose an operation: ')
        if isValidTransaction(selected):
            if selected == '0':
                print('Closing program.')
                print('------------------------------------------------------------')
                break

            while 1:
                print("Data structures\n1.- String\n2.- List\n3.- Set\n4.- Hash\n5.- Sorted set\n0.- Cancel transaction")
                index = input('Chose data structure: ')
                if isValidStructure(index):
                    if index == '0':
                        print('------------------------------------------------------------')
                        break
                    structures = {'1': String, '2': List, '3': Set, '4': Hash, '5': Sset}
                    data = structures[index]()

                    transactions = { '1': create, '2': read, '3': update, '4': delete}
                    transactions[selected](data)
                    break
                else:
                    print('Choose a valid data structure.')
                    print('------------------------------------------------------------')
        else:
            print('Pick a valid transaction.')
            print('------------------------------------------------------------')

main()
