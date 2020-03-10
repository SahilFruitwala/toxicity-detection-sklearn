import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


categories = {'0':"No Toxicity", '1':"toxic", '2':"obscene", '3':"severe_toxic", '4':"threat", '5':"insult", '6':"identity_hate", '7':"Many Kind of Toxicity"}

clf = pickle.load(open('Naive_Bayes.sav', 'rb'))
count_vect = pickle.load(open('CountVect.sav', 'rb'))
tfidfTransformer = pickle.load(open('TfIdf.sav', 'rb'))

temp = clf.predict(tfidfTransformer.transform(count_vect.transform(["bin laden socalled hijacker patsy"])))
# for i in temp[0]:
#     print(i*100)

temp = temp.tostring()
print(categories[str(np.frombuffer(temp,dtype=int)[0])])