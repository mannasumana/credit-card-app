from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = None
    if request.method == "POST":
        limit_bal = float(request.form["limit_bal"])
        age = float(request.form["age"])
        bill_amt1 = float(request.form["bill_amt1"])

        X = np.array([[limit_bal, age, bill_amt1]])
        X_scaled = scaler.transform(X)

        prediction = model.predict(X_scaled)
        prediction_text = "Default" if prediction[0] == 1 else "No Default"

    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)