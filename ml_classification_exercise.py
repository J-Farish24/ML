# The Iris dataset is referred to as a “toy dataset” because it has only 150 samples and four features. 
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris 
# virginica. Each sample’s features are the sepal length, sepal width, petal 
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower 
# that protect the smaller inside petals before the flower buds bloom.

#EXERCISE
# load the iris dataset and use classification
# to see if the expected and predicted species
# match up
from sklearn.datasets import load_iris
iris = load_iris()

# display the shape of the data, target and target_names
print(iris.data.shape)
print(iris.target.shape)
print(iris.target_names.shape)

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)
from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(
    iris.data, iris.target, random_state = 11)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X=data_train, y= target_train)

predicted = knn.predict(X = data_test)
expected = target_test

predicted_flower = [iris.target_names[p] for p in predicted]
expected_flower = [iris.target_names[e] for e in expected]
print('Predicted:\n',predicted_flower[:10])
print('Expected:\n', expected_flower[:10])

# display the values that the model got wrong
wrong = [(p,e) for (p,e) in zip(predicted_flower, expected_flower) if p != e]
print('Wrong values:', wrong)

# visualize the data using the confusion matrix
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected_flower, y_pred=predicted_flower)
confusion_df = pd.DataFrame(confusion, index = iris.target_names, columns = iris.target_names)

figure = plt.figure()
axes = sns.heatmap(confusion_df, annot = True,cmap = plt.cm.nipy_spectral_r)

plt.xlabel("Expected")
plt.ylabel("Predicted")
plt.show()
