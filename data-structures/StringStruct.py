from RedisConfig import *

class StringStruct():
    @staticmethod
    def create():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Enter The Key: ")

            if not r.exists(key):
                value = raw_input("Enter the Value: ")
                r.set(key, value)
                print('Added successfully.')
            else:
                print('That key is already set.')
        else:
            print('Could not connect to server.')

    @staticmethod
    def read():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Enter the Key: ")

            if r.exists(key):
                print('The value for the key: ', key, ', is: ', r.get(key))
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    @staticmethod
    def update():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Enter the Key: ")

            if r.exists(key):
                newValue = raw_input("Enter the new value: ")

                r.set(key, newValue)
                print('Updated successfully.')
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    @staticmethod
    def delete():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Enter the Key to delete: ")
            if r.exists(key):
                r.delete(key)
                print('The Key ', key, ' was deleted Succesfully')
            else:
                print('The Key does not exist, please try again')
        else:
            print('Could not connect to server.')
