import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import AdaBoostRegressor
import pickle
import sqlite3
import psycopg2

app = Flask(__name__)
reg1 = pickle.load(open('x_cord', 'rb'))
reg2 = pickle.load(open('y_cord', 'rb'))
DB_HOST = "ec2-3-223-72-172.compute-1.amazonaws.com"
DB_NAME = "d5habih2mgsfqu"
DB_USER = "ojwlqolbgopaus"
DB_PASS = "70d25ffa67f05b1532833e77fa53198f92bde5c67bdf9cbf6fb5815c2faa7487"



@app.route('/')
def home():
    return "hi"


@app.route('/database')
def database():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    #cur.execute("CREATE TABLE coordinates (id SERIAL PRIMARY KEY, coord1 DECIMAL, coord2 DECIMAL);")
    #cur.execute("INSERT INTO coordinates (coord1,coord2) VALUES(2,2)")
    cur.execute("SELECT * FROM coordinates;")
    row1 = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return "{}".format(row1)


@app.route('/count')
def count():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM student;")
    row2 = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return "{}".format(row2)


@app.route('/predict', methods=['GET'])
def predict():
    rssi = [i.split(',') for i in request.args.values()]

    float_features = []
    for x in rssi:
        for ele in x:
            float_features.append(float(ele))
    x1 = reg1.predict([float_features])
    y1 = reg2.predict([float_features])
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute("INSERT INTO coordinates(coord1,coord2) VALUES(%s,%s)", ("{}".format(x1[0]), "{}".format(y1[0])))
    conn.commit()
    cur.close()
    conn.close()

    return "status:200"


"""@app.route('/results', methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    e = np.array([])
    for item in prediction:
        for x in item:
            e = np.append(e, round(x, 1))

    return jsonify(e)"""

if __name__ == "__main__":
    app.run(host="192.168.0.105", port=8090, debug=True)
