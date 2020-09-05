from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)


class RemoveDuplicates:
    print("inside remove duplicate method")
    def get(self):
        return jsonify({"message":"please use post request"})
    def post(self):
        return jsonify({"message" : "success"})

api.resource(RemoveDuplicates,"/removeduplicates")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)