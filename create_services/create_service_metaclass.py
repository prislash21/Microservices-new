import pymongo
import json
from flask import Flask
from flask import Response, request
from bson.objectid import ObjectId
# from flask_jwt_extended import JWTManager
# from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'THISismyshundorebongoshadharonANDmonorom2ektiSEcretkeyANDeijinishonkBishalditehoy'
# jwt = JWTManager(app)
# database config

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.namelist
    mongo.server_info()
except:
    print("cannot connect to DB")


class SingleInstanceMetaClass(type):
    def __init__(self, name, bases, dic):
        self.__single_instance = None
        super().__init__(name, bases, dic)

    def __call__(cls, *args, **kwargs):
        if cls.__single_instance:
            return cls.__single_instance
        single_obj = cls.__new__(cls)
        single_obj.__init__(*args, **kwargs)
        cls.__single_instance = single_obj
        return single_obj


class Setting(metaclass=SingleInstanceMetaClass):
    def __init__(self):
        self.db = db
        self.port = 27017


@app.route('/', methods=['POST'])
def createName():
    try:
        usernamedetails = request.get_json()
        dbResponse = createName(usernamedetails)

        return Response(
            response=json.dumps(
                {"message": "user created Successfully",
                 "userId": f"{dbResponse.inserted_id}"
                 }
            ),
            status=201,
            mimetype='application/json'
        )
    except Exception as ex:
        print('*********************')

        print(ex)
        print('********************')


@app.route('/ping', methods=['GET'])
def demo():
    # p("heloo")

    return Response(
        response=json.dumps(
            {"message": "working"

             }
        ),
        status=201,
        mimetype='application/json'
    )

# Create Service
def createName(object):
    try:
        dbResponse = db.namelist.insert_one(object)
        return dbResponse

    except Exception as ex:
        print("88888")
        print(ex)





if __name__ == "__main__":
    bar1 = Setting()
    bar2 = Setting()

    if id(bar1) == id(bar2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    print(bar1.db, bar1.port)
    bar1.db = db
    print(bar2.db, bar2.port)
    app.run(host='0.0.0.0', port=5000 ,debug=True)
