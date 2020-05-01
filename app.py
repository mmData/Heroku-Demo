# based on https://www.youtube.com/watch?v=mrExsjcvF4o&list=PLZoTAELRMXVOAvUbePX1lTdxQR8EY35Z1&index=2
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) # __name__ will be the name of the current file
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    # By default we render the index.html page
    return render_template('index.html')

# /predict mean that this function will run when we tourch the prediction button in the webpage
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # request.form.values() takes input from all the forms
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    # render again index.html but put also the prediction_text
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)