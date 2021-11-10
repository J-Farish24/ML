''' Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line '''

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split


#how many sameples and How many features?
diabetes = datasets.load_diabetes()
print(diabetes.data.shape)
print(diabetes.target.shape)

# What does feature s6 represent?
print('s6 represents the blood sugar level of the patient')

X_train, X_test, y_train, y_test = train_test_split(diabetes.data, 
    diabetes.target, random_state=11
)

#print out the coefficient

#Set up model
lr = LinearRegression()
#Use fit to train the model
lr.fit(X = X_train, y = y_train)


coefficient = lr.coef_
intercept = lr.intercept_

print()
print(coefficient)

expected = y_test
#Use preidct to test yiur model predictions
predicted = lr.predict(X_test)


#print out the intercept
print()
print(intercept)

# create a scatterplot with regression line
plt.plot(expected, predicted, ".")

plt.xlabel('Expected')
plt.ylabel('Predicted')

x = np.linspace(0,330,100)
y = x

plt.plot(x,y)

plt.show()

