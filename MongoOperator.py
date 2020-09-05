from pymongo import mongo_client
import pandas as pd

'''function to get the connection'''


def get_connection(username, password, db, host, port):
    print("inside connection method")
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        connection = mongo_client(mongo_uri)
    else:
        connection = mongo_client(host, port)
    return connection


'''function to read the data from mongodb'''


def read_mongo(connection, db, collection, query):
    cursor = connection[db][collection].find(query)
    input_df = pd.DataFrame(list(cursor))
    if '_id' in input_df:
        del input_df['_id']
    return input_df


'''function to save data into mongo db'''


def save_data(connection,dbname,collection,df):
    connection[dbname][collection].insert_many(df.to_dict('records'))


