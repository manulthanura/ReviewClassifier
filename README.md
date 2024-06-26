# ReviewClassifier

ReviewClassifier is a web application that classifies reviews into positive and negative categories. The application uses a machine learning model to classify the reviews. The model is trained using a dataset of reviews that are labeled as positive and negative. The model is then used to predict the sentiment of new reviews. The application is built using Flask, a Python web framework, and deployed on Azure, a cloud platform as a service. The application is designed to be simple and easy to use. Users can enter a review in a text box and click a button to classify the review. The application will then display the predicted sentiment of the review.

<!-- add img -->
![ReviewClassifier](./static/images/reviewclassifier.jpg)


![Static Badge](https://img.shields.io/badge/Repo-ReviewClassifier-purple) ![GitHub](https://img.shields.io/github/license/manulthanura/ReviewClassifier) ![GitHub Repo stars](https://img.shields.io/github/stars/manulthanura/ReviewClassifier?color=yellow) ![GitHub last commit](https://img.shields.io/github/last-commit/manulthanura/ReviewClassifier)

## Problem statement

The aim of this project is to build a end-to-end machine learning project that can predict a input product review positive or negative.

## Installation

Create a virtual environment and install the required packages using the following command:

- Create a virtual environment: `python -m venv env`
- Activate the virtual environment: `source env/bin/activate`
- Install the required packages: `pip install -r requirements.txt`

## Download dataset

View data - https://www.kaggle.com/datasets/dineshpiyasamara/sentiment-analysis-dataset

Command to download data:

`dineshpiyasamara/sentiment-analysis-dataset` or `kaggle datasets download -d dineshpiyasamara/sentiment-analysis-dataset`

## Data Preprocessing

To preprocess the data we can use several techniques like removing stopwords, punctuation, and lemmatization.
in this project I use the following techniques:

- Remove stopwords
- Remove punctuation
- Stemming
- Remove special characters
- Remove numbers
- Remove links
- Convert to lowercase

## Vocabulary Building

In this step we will build a vocabulary from the dataset and vectorize the text data.

## Model Building

For build the model first we need to check the data is balanced or not. If the data is not balanced we need to balance the data using `imbalanced-learn` library.

Since this is a binary classification problem we can use several algorithms like:
- Logistic Regression
- Random Forest
- Decision Tree
- Support Vector Machine
- Naive Bayes

### Model Evaluation

To evaluate the model we can use several metrics like:
- Accuracy
- Precision
- Recall
- F1 Score

### Model Deployment

I use all the above algorithms and compare the accuracy of each model. To go ahead I choose logistic regression because it gives the best accuracy.

### Prediction Pipeline

After building the model we need to create a prediction pipeline that can predict the input review is positive or negative.

## Build Website

To build a website we can use Flask or Django. In this project, I use Flask to build a website. Also, use bootstrap for the styling of the website.

## Deployment

Before deploying project make sure to remove following libraries from requirements.txt file:
`pywin32==306` and `pywinpty==2.0.13`

Generally, these libraries are used for windows and not required for deployment. Mos of the cloud platforms like Heroku, Azure, AWS, etc. are Linux based. For the deployment, I use Azure.

## Usefull Commands

- To install libraries: `pip install -r requirements.txt`
- View installed libraries: `pip list`
- Open jupyter notebook: `jupyter notebook` or `python -m notebook`
- To create a requirements file: `pip freeze > requirements.txt`
- To run the flask app: `python app.py`
- Check python version: `python --version`

## File Structure

- `app.py`: Main file to run the flask app
- `handler.py`: File to handle the prediction
- `logger.py`: File to log the information
- `templates/`: Folder contains the html files
- `static/`: Folder contains the css and js files
- `notebooks/`: Folder contains the jupyter notebooks
- `artifacts/`: Folder contains the dataset

## Conclusion

This is end-to-end machine learning project that can predict the input review is positive or negative. The project is deployed on Azure and can be accessed using the following link: https://reviewclassifier.azurewebsites.net/

### Give a star if you like the project. Follow me for more updates!