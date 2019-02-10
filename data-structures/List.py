from RedisConfig import *

class List():
    @staticmethod
    def create():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Enter the List Key: ")

            if not r.exists(key):
                while 1:
                    value = raw_input("Enter the Value: ")
                    r.rpush(key, value)
                    print('Added successfully.')
                    if(raw_input("Add another value to the List? y/n: ") == 'n'):
                        break
            else:
                print('That List already exist.')
        else:
            print('Could not connect to server.')

    @staticmethod
    def read():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Enter The Key: ")

            if r.exists(key):
                print('The value for the key: ', key, ', is: ', r.lrange(key, 0, -1))
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    @staticmethod
    def update():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Key: ")

            if r.exists(key):
                newValue = raw_input("Add new value: ")

                r.rpushx(key, newValue)
                print('Updated successfully.')
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    @staticmethod
    def delete():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Key: ")
            if r.exists(key):

                print('Value ', r.lpop(key),'of the Key ', key, ' was deleted.')
            else:
                print('Key does not exist in database.')
        else:
            print('Could not connect to server.')