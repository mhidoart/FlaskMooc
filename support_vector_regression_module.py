# Support Vector Regression (SVR)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from pdf_writer_module import Pdf_writer


class Support_vector_regression:

    def __init__(self, file):
        # Importing the self.dataset
        # dataset = pd.read_csv('ENTER_THE_NAME_OF_YOUR_DATASET_HERE.csv')
        self.dataset = pd.read_csv(os.path.join('./uploads', file))
        self.writer = Pdf_writer('support_vector_reg')

    def get_result_file(self):
        return str(self.writer.get_target())

    def algo(self):
        self.writer.add_page()
        X = self.dataset.iloc[:, :-1].values
        y = self.dataset.iloc[:, -1].values
        y = y.reshape(len(y), 1)

        # Splitting the dataset into the Training set and Test set
        from sklearn.model_selection import train_test_split
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
        # Feature Scaling
        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        sc_y = StandardScaler()
        X_train = sc_X.fit_transform(X_train)
        y_train = sc_y.fit_transform(y_train)

        # Training the SVR model on the Training set
        from sklearn.svm import SVR
        regressor = SVR(kernel='rbf')
        regressor.fit(X_train, y_train)

        # Predicting the Test set results
        y_pred = sc_y.inverse_transform(
            regressor.predict(sc_X.transform(X_test)))
        # writ to pdf
        self.writer.write_line('')
        self.writer.write_line("predicted values :")
        self.writer.write_line(str(y_pred))

        np.set_printoptions(precision=2)
        print(np.concatenate((y_pred.reshape(len(y_pred), 1),
                              y_test.reshape(len(y_test), 1)), 1))

        # Evaluating the Model Performance
        from sklearn.metrics import r2_score
        r2_score(y_test, y_pred)
        self.writer.write_line('')
        self.writer.write_line('score of the Model: ')
        self.writer.write_line(str(r2_score(y_test, y_pred)))
        self.writer.save()
