from RedisConfig import *

class Hash():
    @staticmethod
    def create():
        redis, isConnected = connect()
        if isConnected:
            key = raw_input('Enter the Hash-key: ')
            if not redis.exists(key):
                while 1:
                    sub_key = raw_input('Enter the Sub-key: ')
                    value = raw_input('Enter the Value: ')
                    redis.hset(key, sub_key, value)
                    print 'Hash Added successfully'
                    if(raw_input("Add another value to the Hash? y/n: ") == 'n'):
                        break
            else:
            	print('That hash key is already set.')
        else:
            print('Could not connect to the server')

    @staticmethod
    def read():
        redis, isConnected = connect()

        if isConnected:
            key = raw_input('Enter Hash-key: ')
            while 1:
                sub_key= raw_input('Enter the Sub-key: ')
                if redis.hexists(key,sub_key):
                    print ' The key value: ' + key + ' is:', redis.hget(key, sub_key)
                    if(raw_input("Get another value of the Hash? y/n: ") == 'n'):
                        break
            else:
            	print 'Key does not exist in database.'
        else: 
            print 'Could not connect to the server'

    @staticmethod
    def update():
        redis, isConnected = connect()

        if isConnected:
            key = raw_input('Hash-key: ')
            sub_key = raw_input('Sub-key: ')

            if redis.hexists(key, sub_key):
                newValue = raw_input('New value: ')
                redis.hset(key, sub_key, newValue)
                print('Updated successfully')
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to the server')

    @staticmethod            
    def delete():
        redis, isConnected= connect()

        if isConnected:
            key= raw_input('Hash-key: ')
            sub_key= raw_input ('Sub-key: ')

            if redis.hexists(key, sub_key): 
                if redis.hdel(key, sub_key) == 1:
                    print('Deleted succesfully')
                else:
                    print('Something went wrong')
            else:
                print('Key does not exist in database. ')
        else:
            print('Could not connect to server')