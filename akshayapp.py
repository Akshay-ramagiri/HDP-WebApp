import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model1.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("akshtml.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    
    features = [np.array(float_features)]
    prediction = model.predict(features)
    if prediction==1:
         return render_template("akshtml.html", prediction_text = "You likely to have heart disease")  
    
    else :
        return render_template("akshtml.html", prediction_text = "You likely to have heart disease") 
    
    

if __name__ == "__main__":
    app.run(debug=True)
