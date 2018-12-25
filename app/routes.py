from flask import render_template,request,url_for
from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

from app import app



def train():
	df = pd.read_csv("./dataset/spam.csv", encoding='latin-1')
	df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1, inplace=True)
	df.rename(columns={'v1':'label','v2':'text'},inplace=True)
	df["label_as_num"] = df.label.map({"ham":0, "spam":1})
	x = df['text']
	cv.fit_transform(x)
	return

@app.route("/")
@app.route("/index")
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
	NB_spam_model = open('./pretrainedModel/NB_spam_model.pkl','rb')
	clf = joblib.load(NB_spam_model)
	
	message = request.form['message']
	data = [message]
	vect = cv.transform(data).toarray()
	my_prediction = clf.predict(vect)
	return render_template('result.html',prediction = my_prediction)

cv = CountVectorizer()
train()