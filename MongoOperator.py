from pymongo import mongo_client
import pandas as pd


def get_connection(username,password,db,host,port):
    print("inside connection method")
    if username and password :
        connection_string="%s,%s,%s,%s,%s",host,port,db,username,password
        connection=mongo_client(connection_string)
    else:
        connection=mongo_client(host,port)
    return connection

def read_mongo(connection,db,collection,query):
    cursor=connection[db][collection].find(query)




