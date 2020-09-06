from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from MongoOperator import get_connection, read_mongo, save_data
from configparser import ConfigParser

config = ConfigParser.read('config.ini')
mongo_config = config['MONGODB']
username = mongo_config['username']
password = mongo_config['password']
db_name = mongo_config['db']
host = mongo_config['host']
port = int(mongo_config['port'])

app = Flask(__name__)
api = Api(app)

'''post function will get the input data details via API which are stored in mongodb
 required transformation will be applied and saved into mongo db
 '''


class RemoveDuplicates(Resource):
    print("inside remove duplicate method")

    def get(self):
        return jsonify({"message": "please use post request"})

    def post(self):
        db_name = request.json('db')
        collection = request.json('collection')
        cols = request.json('cols')
        version = request.json('version')
        new_version = version + 1
        connection = get_connection(username, password, db_name, host, port)
        input_df = read_mongo(db_name, collection)
        input_df.drop_duplicates(subset=cols, inplace=True)
        input_df[version] = new_version
        save_data(connection, db_name, collection, input_df)
        return jsonify({"message": "success"})

class RemoveColumns(Resource):
    print("inside remove duplicate method")

    def get(self):
        return jsonify({"message": "please use post request"})

    def post(self):
        db_name = request.json('db')
        collection = request.json('collection')
        cols = request.json('cols')
        version = request.json('version')
        new_version = version + 1
        connection = get_connection(username, password, db_name, host, port)
        input_df = read_mongo(db_name, collection)
        input_df.drop(columns=cols, inplace=True)
        input_df[version] = new_version
        save_data(connection, db_name, collection, input_df)
        return jsonify({"message": "success"})




api.add_resource(RemoveDuplicates, "/removeduplicates")

api.add_resource(RemoveColumns,"/removecolumns")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
