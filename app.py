
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    min_price = float(request.form['min'])
    max_price = float(request.form['max'])
    modal_price = float(request.form['modal'])

    if modal_price > (min_price + max_price)/2 * 1.3:
        result = "Abnormal Spike Detected"
    else:
        result = "Normal Price"

    return render_template('index.html', prediction=result)

app = app

if __name__ == "__main__":
    app.run(debug=True)
