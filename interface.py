from flask import Flask, render_template,jsonify,request
from utils import HealthInsurance
import config
app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Health insurance Price Prediction")
    return render_template("home.html")


@app.route("/insurance",methods=["GET","POST"])
def health_insurance():
    if request.method == "POST":
        data = request.form
        print("data :",data)

        age = int(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']
        # make = request.form["make"]

        price = HealthInsurance(data)
        predicted_amount = price.pred_health()
        return jsonify({"Predicted amount :":predicted_amount})
        # return render_template("home.html", prediction = predicted_amount)

    else:
        data = request.form
        print("data :",data)

        age = int(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']
        # make = request.form["make"]

        price = HealthInsurance(data)
        predicted_amount = price.pred_health()
        return jsonify({"Predicted amount :":predicted_amount})
        # return render_template("home.html", prediction = predicted_amount)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port= config.PORT)
