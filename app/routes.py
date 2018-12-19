from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    # df = pd.read_csv("spam.csv", encoding="latin-1")
    # df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    # # Features and Labels
    # df['label'] = df['class'].map({'ham': 0, 'spam': 1})
    # X = df['message']
    # y = df['label']
    return "in progress"
