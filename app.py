from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnn_classifier.utils.common import decodeImage
from src.cnn_classifier.pipeline.prediction import PredictionPipeline
import numpy as np


os.putenv('LANG','es_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train",methods=['GET','POST'])
@cross_origin()
def trainRoute():
    # os.system("python main.py")
    os.system("dvc repro")
    return "Training Done Successfully"

@app.route("/predict",methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']                  
    decodeImage(image,clApp.filename)
    result = clApp.classifier.predict()
    # result = convert_numpy_to_python(result)
    return jsonify(result)


def convert_numpy_to_python(obj):
    """
    Recursively converts int64 numpy arrays to regular Python lists or integers.
    """
    if isinstance(obj, np.ndarray):
        if obj.dtype == 'int64':
            return obj.tolist()  # Convert int64 numpy array to Python list
        else:
            return obj.tolist()  # Convert other numpy arrays to Python lists
    elif isinstance(obj, (list, tuple)):
        return [convert_numpy_to_python(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_numpy_to_python(value) for key, value in obj.items()}
    else:
        return obj  # Return unchanged for other types


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)


