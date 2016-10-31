from flask import Flask, render_template
from flask import send_file


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prostitution/")
def image1():
    return render_template("image1.html")

@app.route("/car_prowl/")
def car_prowl():
    return render_template("image2.html")


if __name__ == '__main__':
    app.run(port=33507)
