import pandas as pd
from flask import render_template, request
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

from app import app

cv = CountVectorizer()


@app.route("/train")
def train():
    df = pd.read_csv("./dataset/spam.csv", encoding='latin-1')
    df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    df.rename(columns={'v1': 'label', 'v2': 'text'}, inplace=True)
    df['label_as_num'] = df.label.map({"ham": 0, "spam": 1})
    y = df['label_as_num']
    x = df['text']

    x = cv.fit_transform(x)
    joblib.dump(cv.vocabulary_, './pretrainedModel/vocab.pkl')

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    # Naive Bayes Classifier
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))
    mse = mean_squared_error(y_test, y_pred)

    joblib.dump(clf, './pretrainedModel/NB_spam_model.pkl')

    return "mse = " + str(mse) + "\ntraining completed."


@app.route("/")
@app.route("/index")
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    ngram_size = 1
    nb_spam_model = open("./pretrainedModel/NB_spam_model.pkl", 'rb')
    clf = joblib.load(nb_spam_model)

    dictionary_filepath = open("./pretrainedModel/vocab.pkl", 'rb')
    vocabulary_to_load = joblib.load(dictionary_filepath)
    loaded_vectorizer = CountVectorizer(ngram_range=(ngram_size, ngram_size), min_df=1, vocabulary=vocabulary_to_load)
    loaded_vectorizer._validate_vocabulary()

    message = request.form['message']
    data = [message]
    vect = loaded_vectorizer.transform(data).toarray()
    my_prediction = clf.predict(vect)
    return render_template('result.html', prediction=my_prediction)

# train()
