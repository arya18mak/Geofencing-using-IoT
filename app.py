import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import AdaBoostRegressor
import pickle

app = Flask(__name__)
reg1 = pickle.load(open('x_cord', 'rb'))
reg2 = pickle.load(open('y_cord', 'rb'))

@app.route('/')
def home():
    return "hi"


@app.route('/predict', methods=['GET'])
def predict():
    rssi = [i.split(',') for i in request.args.values()]

    float_features = []
    for x in rssi:
        for ele in x:
            float_features.append(float(ele))
    print(float_features)
    x1 = reg1.predict([float_features])
    y1 = reg2.predict([float_features])

    return "X: {}, Y: {}".format(x1, y1)


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
