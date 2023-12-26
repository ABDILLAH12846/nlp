from flask import Flask, request
import joblib
import sklearn
import numpy as np

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return "Hello World!"

@app.route("/", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

    # Load the vectorizer
    test_vect = joblib.load('vect.pkl')
    test_model = joblib.load('model.pkl')


    sample_text = test_vect.transform(
        np.array([text], dtype=object)
    )

    result = test_model.predict(sample_text)

    sentimen = ''

    if result == 1 or result == 0:
      sentimen = 'Positive'
    else:
      sentimen = 'Negative'

    return {"prediction": sentimen}

if __name__ == "__main__":
    app.run(app.run(host='0.0.0.0', port=5000))

