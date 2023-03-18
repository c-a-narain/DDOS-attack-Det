import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics as metrics

dataset = pd.read_csv('Iot Bot dataset final.csv')
dataset=dataset.dropna(how="any")
print(dataset)

print(dataset.info())


#histogram of attack
plt.figure(figsize=(10,8))
plt.title("Histogram of attack")
plt.hist(dataset['attack'],rwidth=0.9)
plt.show()

#
m = dataset['attack']
n = dataset['N_IN_Conn_P_SrcIP']
plt.figure(figsize=(4,4))
plt.title("Bar plot graph",fontsize=20)
plt.xlabel("attack",fontsize=15)
plt.ylabel("N_IN_Conn_P_SrcIP",fontsize=15)
plt.bar(m,n,label="bar plot",color=["orange"],width=0.5)
plt.legend(loc='best')
plt.show()

X = dataset.iloc[:,6:16].values
y = dataset.iloc[:, 16].values

print(X)
print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state =121)


print(X_train)
print(" ")


print(y_train)

print("Training Started");
print("Processing");
# Fitting KNN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
history = classifier.fit(X_train, y_train)
import pickle
knnPickle = open('knnpickle_file', 'wb')
pickle.dump(classifier, knnPickle)                      
print("Training Completed")
# load the model from disk


ypred=classifier.predict(X_test)
ypred = ypred.round()
print(ypred)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,ypred)
print("Confussion Matrix")
print(cm)
from sklearn.metrics import plot_confusion_matrix
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
plot_confusion_matrix(classifier, X_test, y_test)  
plt.show()
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,ypred))

