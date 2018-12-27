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

**To start python notebook from within python virtual environment follow below commands:**
1. `ipython kernel install --user --name=spamclassifier`
2. `jupyter notebook`
3. open `DataModelling&NaiveBayesModel.ipynb` from browser.

**NOTE**: if you are running multiple kernels in jupyter notebook, switch to `spamclassifier` kernel from `kernel->change kernel->spamclassifier` from browser.

### web app routes:
1. `localhost:5000\train`  will load dataset and create vocabulary, train Naive Bayes model using it.
2. `localhost:5000\` or `localhost:5000\index` is the main page of the web app.
3. `localhost:5000\predict` will predict the class of text passed. This api will load trained model which were created from 1st url and use it for prediction.

### References:
1. https://anbasile.github.io/programming/2017/06/25/jupyter-venv/

