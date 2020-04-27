import pymongo
import json
from flask import Flask
from flask import Response, request
import prometheus_client as prom
import random
import time

app = Flask(__name__)
req_summary = prom.Summary('python_my_req_example', 'Time spent processing a request')

try:
    mongo = pymongo.MongoClient(
        host="172.25.0.4",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.namelist
    mongo.server_info()
except:
    print("cannot connect to DB")


@req_summary.time()
def process_request(t):
   time.sleep(t)

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


    counter = prom.Counter('python_my_counter', 'This is my counter')
    gauge = prom.Gauge('python_my_gauge', 'This is my gauge')
    histogram = prom.Histogram('python_my_histogram', 'This is my histogram')
    summary = prom.Summary('python_my_summary', 'This is my summary')
    prom.start_http_server(8080)

    while True:
        counter.inc(random.random())
        gauge.set(random.random() * 15 - 5)
        histogram.observe(random.random() * 10)
        summary.observe(random.random() * 10)
        process_request(random.random() * 5)

        time.sleep(1)
