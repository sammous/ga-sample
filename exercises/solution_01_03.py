import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

df = pd.read_csv('exercises/titanic-train.csv').dropna()

# Select the following three features : Sex, Age and Fare
X = df[['Sex', 'Age', 'Fare']]

# Get the target column 'Survived'
Y = df['Survived']

# Replace values for the Sex features from female/male to 1/0
X = X.replace({'Sex':{'female': 1, 'male': 0}})

# Split your data to your train/test sets with a proportion of 70%/30% for train/test and a random state value to 100
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

# Define your Decision Tree classifier with a max depth of 3
clf = DecisionTreeClassifier(max_depth=3)

# Fit the classifier with the training data
clf.fit(X_train, y_train)

# Predict on the test data
y_pred = clf.predict(X_test)

# Compute the accuracy score and round
accuracy = int(accuracy_score(y_test, y_pred) * 100)
print("Accuracy: ", accuracy)
