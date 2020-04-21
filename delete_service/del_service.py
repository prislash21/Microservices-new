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

@app.route('/deleteUser/<id>', methods=['DELETE'])
def deleteName(id):
     try :
        dbResponse = deleteName(id)
        if dbResponse.deleted_count == 1:
         return Response(
             response=json.dumps(
                 {"message": " username Deleted Successfully ! ", "id": f"{id}"}
             ),
             status=200,
             mimetype='application/json'
         )
        else:
         return Response(
             response=json.dumps(
                 {"message": " OOpsS!! user not found anymore! ", "id": f"{id}"}
             ),
             status=404,
             mimetype='application/json'
         )
     except Exception as ex:
         print("**********")
         print(ex)
         print("***********")
         return Response(
             response=json.dumps(
                 {"message": "Sorry ! :( can not delete "}
             ),
             status=500,
             mimetype='application/json'
         )

def deleteName(id):
    try:
        dbResponse = db.namelist.delete_one({"_id": ObjectId(id)})
        return dbResponse
    except Exception as ex:
        print("####")
        print(ex)
        print("#######")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000 ,debug=True)