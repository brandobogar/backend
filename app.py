import os
import glob
import cv2 as cv
from flask import Flask, request, redirect, url_for, abort, jsonify, render_template
import base64
from werkzeug.utils import secure_filename
import numpy as np
import sys
import tensorflow as tf
# from datates import data_tes
# from prediction import prediction
# from create_dataset import create_datates


app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = '../src/Assets/images/uploads'


@app.route("/")
def index():
    return jsonify("Hello world")

@app.route('/hello', methods=['GET'])
def hello():
    
    tes_data={
        "name": "Brando",
        "age": 20,
    }

    return jsonify(tes_data)


if __name__ == '__main__':
    app.run(debug=True)
