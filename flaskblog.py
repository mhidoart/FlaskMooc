from flask import Flask, render_template, url_for
import os
from flask import  flash, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

posts = [
    {
        'author': 'ASSABBANE Mehdi',
        'title': 'Data pre-processing',
        'content': '''is an important step in the data mining process. The phrase "garbage in, garbage out" is particularly applicable to data mining and machine learning projects''',
        'date_posted': 'December 21, 2020',
        'url':'/pre_processing'

    },
    {
        'author': 'ASSABBANE Mehdi',
        'title': 'Linear Regression',
        'content': 'In statistics, linear regression is a linear approach to modelling the relationship between a scalar response and one or more explanatory variables. The case of one explanatory variable is called simple linear regression; for more than one, the process is called multiple linear regression',
        'date_posted': 'December 21, 2020',
        'url':'/linear_regression'
    }
]




UPLOAD_FOLDER = 'uploads'
CURRENT_OPERATION =""

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route('/linear_regression')
def linear_regression():
   current_operation ="linear_regression"
   print(CURRENT_OPERATION)
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(UPLOAD_FOLDER,secure_filename(f.filename)))
      print(CURRENT_OPERATION)
      return render_template('success_upload.html', msg='file uploaded successfully, waiting for Operation : ' + CURRENT_OPERATION)

if __name__ == '__main__':
   app.run(debug = True)