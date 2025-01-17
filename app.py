#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from flask import Flask,render_template,request
import pickle


app = Flask(__name__)
model = pickle.load(open('lr_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lead_scoring',methods=['POST'])
def predict_expenses():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Predicted Hot/Cold Lead $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

