from engine
from flask import Flask, request, redirect, url_for, render_template, send_from_directory


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def show_page():
    return render_template("index.html")


@app.route('/scan',methods=['GET'])
def scan():
    print "hi"
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)
