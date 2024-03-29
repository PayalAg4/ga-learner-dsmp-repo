# --------------
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Code starts here

df = pd.read_csv(path)
print(df.head())

X = df.iloc[:,:-1]  # independent variable
y = df.iloc[:,-1]   # dependent variable

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=6)
print(X_train.head())
print(X_test.head())
print(y_train.head())
print(y_test.head())


# Code ends here


# --------------
import matplotlib.pyplot as plt


# Code starts here

plt.boxplot(X_train['bmi'])
q_value = X_train['bmi'].quantile(q=0.95)
q_value
# Code ends here


# --------------
# Code starts here

relation = X_train.corr()
print(relation)

sns.pairplot(X_train)

# Code ends here


# --------------
import seaborn as sns
import matplotlib.pyplot as plt

# Code starts here

cols = ['children','sex','region','smoker']
fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize=(20,20))
for i in range(0,2):
    for j in range(0,2):
        col = cols[i*2+j]
        sns.countplot(X_train[col],hue= y_train, ax=axes[i,j])
       
# Code ends here


# --------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}

# Code starts here

lr = LogisticRegression(random_state=9)
grid = GridSearchCV(estimator=lr, param_grid=parameters)
grid.fit(X_train,y_train)
y_pred = grid.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print("The Accuracy for Grid : " , accuracy)

# Code ends here


# --------------
from sklearn.metrics import roc_auc_score
from sklearn import metrics

# Code starts here

score = roc_auc_score(y_test,y_pred)
print("ROC AUC Score : " , score)

y_pred_proba = grid.predict_proba(X_test)[:,1]
y_pred_proba

fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_proba)

roc_auc = roc_auc_score(y_test,y_pred_proba)
print("ROC AUC Score (probability) : ", roc_auc)

plt.plot(fpr, tpr, label="Logistic model, auc="+str(roc_auc))

# Code ends here


