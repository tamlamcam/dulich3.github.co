from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cars")
def cars():
    return render_template("cars.html")

@app.route("/price")
def price():
    return render_template("price.html")

@app.route("/contact", methods=["GET","POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]
        car = request.form["car"]
        date = request.form["date"]

        data = {
            "Tên":[name],
            "SĐT":[phone],
            "Xe":[car],
            "Ngày":[date],
            "Thời gian":[datetime.now()]
        }

        df = pd.DataFrame(data)

        file = "don_dat_xe.xlsx"

        if os.path.exists(file):

            old = pd.read_excel(file)
            df = pd.concat([old,df])

        df.to_excel(file,index=False)

        return redirect("/")

    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)