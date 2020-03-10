import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('Final_Cleaned_Data (1).csv', encoding='UTF-8')

df = df.dropna(how='any',axis=0)

print(df.head(50))

categories = {'0':"No Toxicity", '1':"toxic", '2':"obscene", '3':"severe_toxic", '4':"threat", '5':"insult", '6':"identity_hate", '7':"Many Kind of Toxicity"}

X_train, X_test, y_train, y_test = train_test_split(df['comment_text'], df['is_toxic'], shuffle=True, test_size=0.33, random_state=42)

count_vect = CountVectorizer(ngram_range=(1,2))
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# clf = DecisionTreeClassifier(random_state=0).fit(X_train_tfidf, y_train)
clf = MultinomialNB().fit(X_train_tfidf, y_train)

X_test_counts = count_vect.transform(X_test)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

predictions_NB = clf.predict(X_test_tfidf)

print(accuracy_score(predictions_NB, y_test)*100)

# pickle.dump(clf, open('DT.sav', 'wb'))
pickle.dump(clf, open('Naive_Bayes.sav', 'wb'))
pickle.dump(count_vect, open('CountVect.sav', 'wb'))
pickle.dump(tfidf_transformer, open('TfIdf.sav', 'wb'))



temp = clf.predict(count_vect.transform(["you are fuck"]))
temp = temp.tostring()
print(categories[str(np.frombuffer(temp,dtype=int)[0])])