# spam-classifier-webserver
A Flask based webserver which accepts text from user through webservice,
and generates prediction whether the text is spam or ham.

The data is a collection of SMS messages tagged as spam or ham that can be found [here](https://www.kaggle.com/uciml/sms-spam-collection-dataset). 
First, we will use this dataset to build a prediction model that will accurately classify which texts are spam.

Naive Bayes classifiers are a popular statistical technique of e-mail filtering. 
They typically use bag of words features to identify spam e-mail. 
Therefore, We’ll build a simple message classifier using Naive Bayes theorem.

# Installation
Run the following command on the root dorectory of this project.

**Optional commands to create virual environment to install dependency**:
1. `Create virtual environment: 'python -m venv spamclassifier'`
2. `Activate virual environment: 'spamclassifier\Scripts\activate'`

**Command to start server**:
1. `install dependency: 'pip install -r requirements.txt'`
2. `flask run`
This will start flask based spam classifier server in **production mode**.

To access home page browse to `http://localhost:5000`
