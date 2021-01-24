from flask import Flask, render_template, url_for, session
import os
from flask import flash, request, redirect
from werkzeug.utils import secure_filename
from pdf_writer_module import Pdf_writer
from multipleLR import multiple_linear_regression
from polynomial_R_module import Polynomial_regression
from random_forest_regression_module import Random_forest_regression
from support_vector_regression_module import Support_vector_regression
from flask import send_file

SESSION_TYPE = 'filesystem'
app = Flask(__name__)

posts = [

    {
        'author': 'ASSABBANE Mehdi',
        'title': 'Linear Regression',
        'content': 'In statistics, linear regression is a linear approach to modelling the relationship between a scalar response and one or more explanatory variables. The case of one explanatory variable is called simple linear regression; for more than one, the process is called multiple linear regression',
        'date_posted': 'December 21, 2020',
        'url': '/linear_regression'
    },
    {
        'author': 'ASSABBANE Mehdi',
        'title': 'Polynomial regression',
        'content': 'In statistics, polynomial regression is a form of regression analysis in which the relationship between the independent variable x and the dependent variable y is modelled as an nth degree polynomial in x. Polynomial regression fits a nonlinear relationship between the value of x and the corresponding conditional mean of y.',
        'date_posted': 'December 21, 2020',
        'url': '/polynomial_regression'
    },
    {
        'author': 'ASSABBANE Mehdi',
        'title': 'Random forest regression',
        'content': 'Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operate by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes(classification) or mean/average prediction(regression) of the individual trees. Random decision forests correct for decision trees habit of overfitting to their training set.',
        'date_posted': 'December 21, 2020',
        'url': '/random_forest_regression'
    },
    {
        'author': 'ASSABBANE Mehdi',
        'title': 'Support vector regression',
        'content': 'In machine learning, support-vector machines are supervised learning models with associated learning algorithms that analyze data for classification and regression analysis',
        'date_posted': 'December 21, 2020',
        'url': '/support_vector_regression'
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


@app.route('/polynomial_regression')
def polynomial_regression():
    session['reg'] = "polynomial_regression"
    print("session ===> " + str(session['reg']))
    return render_template('upload.html')


@app.route('/random_forest_regression')
def random_forest_regression():
    session['reg'] = "random_forest_regression"
    print("session ===> " + str(session['reg']))
    return render_template('upload.html')


@app.route('/support_vector_regression')
def support_vector_regression():
    session['reg'] = "support_vector_regression"
    print("session ===> " + str(session['reg']))
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
    if(session['reg'] == "linear_regression"):
        return ml_regression(f.filename)
    elif(session['reg'] == "polynomial_regression"):
        return poly_regression(f.filename)
    elif(session['reg'] == "random_forest_regression"):
        return random_forest(f.filename)
    elif(session['reg'] == "support_vector_regression"):
        return support_vector(f.filename)


def ml_regression(file_name):
    reg = multiple_linear_regression(file_name)
    reg.algo()
    print(reg.get_result_file())
    return render_template('success_upload.html', msg='file uploaded successfully, chozen regression : ' + session['reg'], download='/download/' + str(reg.get_result_file()))


def poly_regression(file_name):
    reg = Polynomial_regression(file_name)
    reg.algo()
    print(reg.get_result_file())
    return render_template('success_upload.html', msg='file uploaded successfully, chozen regression : ' + session['reg'], download='/download/' + str(reg.get_result_file()))


def random_forest(file_name):
    reg = Random_forest_regression(file_name)
    reg.algo()
    print(reg.get_result_file())
    return render_template('success_upload.html', msg='file uploaded successfully, chozen regression : ' + session['reg'], download='/download/' + str(reg.get_result_file()))


def support_vector(file_name):
    reg = Support_vector_regression(file_name)
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
