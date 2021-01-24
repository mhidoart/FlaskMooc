# Polynomial Regression

# Importing the libraries
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from pdf_writer_module import Pdf_writer


class Polynomial_regression:
    def __init__(self, file):
        # Importing the self.dataset
        # dataset = pd.read_csv('ENTER_THE_NAME_OF_YOUR_DATASET_HERE.csv')
        self.dataset = pd.read_csv(os.path.join('./uploads', file))
        self.writer = Pdf_writer('poly_reg')

    def get_result_file(self):
        return str(self.writer.get_target())

    def algo(self):
        self.writer.add_page()
        X = self.dataset.iloc[:, :-1].values
        y = self.dataset.iloc[:, -1].values

        # Splitting the dataset into the Training set and Test set
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=0)

        # writing data to pdf
        self.writer.write_line("training set :")
        self.writer.write_line("\n\n")

        self.writer.write_line("X Matrix (X_train) :")
        self.writer.write_line(str(X_train))
        self.writer.write_line('')
        self.writer.write_line("Y Vector (y_train) :")
        self.writer.write_line(str(y_train))

        self.writer.write_line("")
        self.writer.write_line("test set ")
        self.writer.write_line("")

        self.writer.write_line("X Matrix (X_test) :")
        self.writer.write_line(str(X_test))
        self.writer.write_line('')
        self.writer.write_line("Y Vector (y_test) :")
        self.writer.write_line(str(y_test))
        # Training the Polynomial Regression model on the Training set
        poly_reg = PolynomialFeatures(degree=4)
        X_poly = poly_reg.fit_transform(X_train)
        regressor = LinearRegression()
        regressor.fit(X_poly, y_train)

        # Predicting the Test set results
        y_pred = regressor.predict(poly_reg.transform(X_test))
        self.writer.write_line('')
        self.writer.write_line("predicted values :")
        self.writer.write_line(str(y_pred))

        np.set_printoptions(precision=2)
        print(np.concatenate((y_pred.reshape(len(y_pred), 1),
                              y_test.reshape(len(y_test), 1)), 1))
        self.writer.write_line('')
        self.writer.write_line('score of the Model: ')
        self.writer.write_line(str(r2_score(y_test, y_pred)))
        # Evaluating the Model Performance
        print(str(r2_score(y_test, y_pred)))

        self.writer.save()
