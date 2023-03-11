import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/api/predict',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(np.array(data['instances']),columns=['frequency', 'total time', 'reading speed','Browse All','Particular Section', 'Static_loc', 'On-the-go'])
    prediction = model.predict(df)
    return jsonify(status='ok', predictions=prediction.tolist())

@app.route("/")
def home_view():
        return "<h1>Welcome to User Modeling Server</h1>"
        
@app.route("/get")
def get_view():
        return jsonify(status='ok')


if __name__ == '__main__':
    app.run(port=5000)