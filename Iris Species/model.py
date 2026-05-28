import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv(r'D:\Coding journey\Kaggle competitions\Iris Species\Iris.csv')

X = df.drop(columns=['Species'])
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

knn = KNeighborsClassifier(n_neighbors=3)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(knn, X_train, y_train, cv=skf)

print("Cross validation score: ",scores)
print("Average CV accuracy: ",scores.mean())

knn.fit(X_train,y_train)

print("Test accuracy: ",knn.score(X_test,y_test))
