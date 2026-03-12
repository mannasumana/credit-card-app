from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    limit_bal = float(data["limit_bal"])
    age = float(data["age"])
    bill_amt1 = float(data["bill_amt1"])

    # simple demo prediction
    if bill_amt1 > 4000:
        prediction = "High Default Risk"
    else:
        prediction = "Low Default Risk"

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)