from RedisConfig import *

class Set():
    @staticmethod
    def create():
        redis, isConnected = connect()

        if isConnected:
            key = raw_input("Enter the Key to the new set: ")

            if not redis.exists(key):
                while 1:
                    value = raw_input("Enter a Value: ")
                    redis.sadd(key, value)
                    if(raw_input("Add another value to the set? y/n: ") == 'n'):
                        break

                print('Set created successfully.')
            else:
                print('That key is already exists')
        else:
            print "Couldn't connect to server"

    @staticmethod
    def read():
        redis, isConnected = connect()

        if isConnected:
            key = raw_input("Enter the set Key: ")

            if redis.exists(key):
                print 'The elements of the set: ' + key + ' are: ', redis.smembers(key)
            else:
                print 'That key does not exist.'
        else:
            print "Couldn't connect to server"

    @staticmethod
    def update():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Enter the Key: ")

            if r.exists(key):
                while 1:
                    value = raw_input("Enter th Value: ")
                    r.sadd(key, value)
                    if(raw_input("Add another value to the set? y/n: ") == 'n'):
                        break

                print 'Values added successfully to set: ' + key
            else:
                print('That key does not exist.')
        else:
            print "Couldn't connect to server"

    @staticmethod
    def delete():
        r, isConnected = connect()

        if isConnected:
            key = raw_input("Enter the set Key: ")
            if r.exists(key):
                while 1:
                    value = raw_input("Enter The value to remove: ")
                    r.srem(key, value)
                    print 'The element: ' + value + ' was removed from set: ' + key
                    if(raw_input("Remove another value to the set? y/n: ") == 'n'):
                        break
            else:
                print 'Key does not exist in the database'
        else:
            print "Couldn't connect to server"