import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('exercises/titanic.csv').dropna()

# Select the following three features : Sex, Age and Fare
X = _____

# Get the target column 'Survived'
Y = ____

# Replace values for the Sex features from female/male to 1/0
X = X.replace(____)

# Split your data to your train/test sets with a proportion of 70%/30% for train/test and a random state value to 100
X_train, X_test, y_train, y_test = ____

# Define your Decision Tree classifier with a max depth of 3
clf = ____

# Fit the classifier with the training data
clf.____

# Predict on the test data
y_pred = ____

# Compute the accuracy score and round 
accuracy = int(____ * 100)
print("Accuracy: ", accuracy)
