from flask import Flask
import cv2

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"
