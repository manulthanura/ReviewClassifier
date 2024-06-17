from flask import Flask, render_template, request, redirect
from handler import preprocessing, vectorizer, get_prediction
from datetime import datetime
from logger import logging

app = Flask(__name__)

logging.info("Flask server is started")

data = dict()
reviews = []
positive = 0
negative = 0

@app.route("/")
def index():
    data["reviews"] = reviews
    data["positive"] = positive
    data["negative"] = negative

    logging.info("Opening the home page")

    return render_template("index.html", data=data, now=datetime.utcnow())

@app.route("/", methods=["POST"])
def my_post():
    text = request.form["text"]
    logging.info(f'Text : {text}')

    preprocessed_text = preprocessing(text)
    logging.info(f'Preprocessed text : {preprocessed_text}')

    vectorized_text = vectorizer(preprocessed_text)
    logging.info(f'Vectorized text : {vectorized_text}')

    prediction = get_prediction(vectorized_text)
    logging.info(f'Prediction : {prediction}')

    if prediction == "Negative":
        global negative
        negative += 1
    else:
        global positive
        positive += 1

    reviews.insert(0, text)
    return redirect(request.url)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()