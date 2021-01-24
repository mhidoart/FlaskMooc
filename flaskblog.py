from flask import Flask, render_template, url_for, session
import os
from flask import flash, request, redirect
from werkzeug.utils import secure_filename
from pdf_writer_module import Pdf_writer
from multipleLR import multiple_linear_regression
from flask import send_file

SESSION_TYPE = 'filesystem'
app = Flask(__name__)

posts = [
    {
        'author': 'ASSABBANE Mehdi',
        'title': 'Data pre-processing',
        'content': '''is an important step in the data mining process. The phrase "garbage in, garbage out" is particularly applicable to data mining and machine learning projects''',
        'date_posted': 'December 21, 2020',
        'url': '/pre_processing'

    },
    {
        'author': 'ASSABBANE Mehdi',
        'title': 'Linear Regression',
        'content': 'In statistics, linear regression is a linear approach to modelling the relationship between a scalar response and one or more explanatory variables. The case of one explanatory variable is called simple linear regression; for more than one, the process is called multiple linear regression',
        'date_posted': 'December 21, 2020',
        'url': '/linear_regression'
    }
]


UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config["SESSION_PERMANENT"] = False


@app.route("/")
@app.route("/home")
def home():
    session['reg'] = ""
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/linear_regression')
def linear_regression():
    current_operation = "linear_regression"
    session['reg'] = "linear_regression"
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
    return ml_regression('Data.csv')


def ml_regression(file_name):
    reg = multiple_linear_regression(file_name)
    reg.algo()
    print(reg.get_result_file())
    return render_template('success_upload.html', msg='file uploaded successfully, chozen regression : ' + session['reg'], download='/download/' + str(reg.get_result_file()))


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def downloadFile(filename):
    # For windows you need to use drive name [ex: F:/Example.pdf]
    path = os.path.join('.', filename)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)
