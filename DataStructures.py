import redis as rd

HOSTNAME = 'localhost'
PORT = 6379
DB = 0

def connect():
    try:
        r = rd.StrictRedis(host=HOSTNAME, port=PORT, db=DB)
        return r, r.ping()
    except:
        return r, False

#----------------------------------------------Clase String()
class String():
    def create(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if not r.exists(key):
                value = input("Value: ")
                r.set(key, value)
                print('Added successfully.')
            else:
                print('That key is already set.')
        else:
            print('Could not connect to server.')

    def read(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if r.exists(key):
                print('The value for the key: ', key, ', is: ', r.get(key))
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    def update(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if r.exists(key):
                newValue = input("New value: ")

                r.set(key, newValue)
                print('Updated successfully.')
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    def delete(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")
            if r.exists(key):
                r.delete(key)
                print('Key ', key, ' was deleted.')
            else:
                print('Key does not exist in database.')
        else:
            print('Could not connect to server.')

#--------------------------------------------------Clase List()
class List():
    def create(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if not r.exists(key):
                value = input("Value: ")
                r.rpush(key, value)
                print('Added successfully.')
            else:
                print('That key is already set.')
        else:
            print('Could not connect to server.')

    def read(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if r.exists(key):
                print('The value for the key: ', key, ', is: ', r.lrange(key, 0, -1))
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    def update(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if r.exists(key):
                newValue = input("Add new value: ")

                r.rpushx(key, newValue)
                print('Updated successfully.')
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    def delete(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")
            if r.exists(key):

                print('Value ', r.lpop(key),'of the Key ', key, ' was deleted.')
            else:
                print('Key does not exist in database.')
        else:
            print('Could not connect to server.')

#----------------------------------------------Clase Set()
class Set():
    def create(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if not r.exists(key):
                while 1:
                    value = input("Value: ")
                    r.sadd(key, value)
                    if(input("Add another value to the set? y/n") == n):
                        break

                print('Set added successfully.')
            else:
                print('That key is already set.')
        else:
            print('Could not connect to server.')

    def read(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if r.exists(key):
                print('The elements of the set: ', key, ' are: ', r.members(key))
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    def update(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")

            if r.exists(key):
                while 1:
                    value = input("Value: ")
                    r.sadd(key, value)
                    if(input("Add another value to the set? y/n") == n):
                        break

                print('Values added successfully to set: ', key)
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    def delete(self):
        r, isConnected = connect()

        if isConnected:
            key = input("Key: ")
            if r.exists(key):

                print('The element:', r.spop(key), ' was removed from set: ', key)
            else:
                print('Key does not exist in database.')
        else:
            print('Could not connect to server.')

#-----------------------------------------------------Clase Hash()
class Hash():
    def create(self):
        r, isConnected = connect()
        if isConnected:
            key = input('Hash-key: ')
            if not r.exists(key):
                sub_key = input('Sub-key: ')
                value = input('Value: ')
                r.hset(key, sub_key, value)
                print('Added successfully')
            else:
            	print('That key is already set.')
        else:
            print('Could not connect to the server')

    def read(self):
        r, isConnected = connect()

        if isConnected:
            key = input('Hash-key: ')
            sub_key= input('Sub-key: ')

            if r.hexists(key,sub_key):
                
                print (' The key value: ', key, ' is: ', r.hget(key, sub_key)) 
            else:
            	print('Key does not exist in database.')
        else: 
            print('Could not connect to the server')

    def update(self):
        r, isConnected = connect()

        if isConnected:
            key = input('Hash-key: ')
            sub_key = input('Sub-key: ')

            if r.hexists(key, sub_key):
                newValue = input('New value: ')
                r.hset(key, sub_key, newValue)
                print('Updated successfully')
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to the server')

    def delete(self):
        r, isConnected= connect()

        if isConnected:
            key= input('Hash-key: ')
            sub_key= input ('Sub-key: ')

            if r.hexists(key, sub_key): 
                if r.hdel(key, sub_key) == 1:
                    print('Deleted succesfully')
                else:
                    print('Something went wrong')
            else:
                print('Key does not exist in database. ')
        else:
            print('Could not connect to server')

#----------------------------------------------------Clase Sortedsets()
class Sset():
    def create(self):
        r, isConnected = connect()

        if isConnected:
            key= input("zSet-key: ")

            if not r.exists(key):
                while 1:
                    score= input('Score: ')
                    value= input('Value: ')
                    r.zadd(key, score, value)
                    if (input ("Add another value to the set? y/n") == 'n'):
                        break
                print('Sorted set added successfully')
            else:
                print('That key is already set.')
        else:
            print('Could not connect to server.')

    def read(self):
        r, isConnected = connect()

        if isConnected:
            key = input('Key: ')

            if r.exists(key):
                print('The elements of the set', key, 'are', r.zrange(key, '0', '-1', withscores=True))
            else: 
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    def update(self):
        r, isConnected = connect()

        if isConnected:
            key= input("zSet-key: ")

            if r.exists(key):
                while 1:
                    score= input('Score: ')
                    newValue= input(' New Value: ')
                    r.zadd(key, score, newValue)
                    if (input ("Add another value to the set? y/n") == 'n'):
                        break
                print('Sorted set updated successfully')
            else:
                print('That key does not exist.')
        else:
            print('Could not connect to server.')

    def delete(self):
        r, isConnected= connect()

        if isConnected:
            key= input("Key: ")
            value= input("Value:  ")

            if r.exists(key):
                if r.zrem(key, value) == 1:
                    print('Deleted successfully')
                else:
                	print('Something went wrong')
            else:
                 print('Key does not exist in database. ')
        else:
            print('Could not connect to server.')





