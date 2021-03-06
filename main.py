from engine.engine import Engine
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
# import subprocess
# import json

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def show_page():
    return render_template("index.html")


@app.route('/scan',methods=['GET'])
def scan():
    engine=Engine()
    return engine.execute()


if __name__ == "__main__":
    app.run(debug=True)
