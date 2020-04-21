import pymongo
import json
from flask import Flask
from flask import Response, request
from bson.objectid import ObjectId

app = Flask(__name__)
# database config
try:
    mongo = pymongo.MongoClient(
        host='172.17.0.3',
        port=27017,
        serverSelectionTimeoutMS=40000
    )
    db = mongo.microservice
    mongo.server_info()
except Exception as ex:
    print(ex)


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
    app.run(debug=True)
