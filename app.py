from flask import Flask,request,jsonify, render_template
import joblib
import pandas as pd

# creating flask app
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

# Connect to POST API Predict() function

@app.route('/predict', methods=['POST'])
def predict():
    
    TV = request.form['TV']
    radio = request.form['radio']
    newspaper = request.form['newspaper']
    
    prediction = model.predict([[TV, radio, newspaper]])
    
    return render_template("index.html", prediction_text='If you spend ${}K  on TV, ${}K on Radio and ${}K on newspapaer advertisment, then your sales will be {}'.format(TV, radio, newspaper,'$'+str({round(prediction[0],2)})+'K'))

# Load the model and columns names

if __name__ == '__main__':
                           
    model = joblib.load('final_model.pkl')
    col_names = joblib.load('column_names.pkl')
    
    app.run(debug=True)