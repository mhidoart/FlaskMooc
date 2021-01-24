# Random Forest Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from pdf_writer_module import Pdf_writer


class Random_forest_regression:

    def __init__(self, file):
        # Importing the self.dataset
        # dataset = pd.read_csv('ENTER_THE_NAME_OF_YOUR_DATASET_HERE.csv')
        self.dataset = pd.read_csv(os.path.join('./uploads', file))
        self.writer = Pdf_writer('Random_forest')

    def get_result_file(self):
        return str(self.writer.get_target())

    def algo(self):
        self.writer.add_page()
        X = self.dataset.iloc[:, :-1].values
        y = self.dataset.iloc[:, -1].values

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
        # Training the Random Forest Regression model on the whole dataset
        from sklearn.ensemble import RandomForestRegressor
        regressor = RandomForestRegressor(n_estimators=10, random_state=0)
        regressor.fit(X_train, y_train)

        # Predicting the Test set results
        y_pred = regressor.predict(X_test)
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
