from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import re
from nltk.stem import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle
import numpy as np
from sklearn.linear_model import SGDClassifier
import sklearn.linear_model

nltk.download('stopwords')
nltk.download('punkt')

happy_emojis = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
])
sad_emojis = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
])
emoticons = happy_emojis.union(sad_emojis)
emojipattern = re.compile("["
                          u"\U0001F600-\U0001F64F"
                          u"\U0001F300-\U0001F5FF"
                          u"\U0001F680-\U0001F6FF"
                          u"\U0001F1E0-\U0001F1FF"
                          u"\U00002702-\U000027B0"
                          u"\U000024C2-\U0001F251"
                          "]+", flags=re.UNICODE)


def clean_typed_data(text):
    text = re.sub(r'‚Ä¶', '', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = re.sub(r':', '', text)
    text = emojipattern.sub(r'', text)
    text = re.sub(r'http\S+', '', text)
    for k in text.split("\n"):
        text = re.sub(r"[^a-zA-Z]+", ' ', k)
    # print(text)
    words = word_tokenize(text.lower())
    # print(words)
    editedwords = []
    ps = PorterStemmer()
    stopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", \
                 "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
                 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', \
                 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
                 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
                 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
                 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
                 'after', \
                 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
                 'further', \
                 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
                 'more', \
                 'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
                 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o',
                 're', \
                 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', \
                 "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', \
                 "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren',
                 "weren't", \
                 'won', "won't", 'wouldn', "wouldn't"]

    for word in words:
        if word not in stopWords:
            word = ps.stem(word)
            editedwords.append(word)

    # print(editedwords)
    stringconverted = ' '.join(editedwords)
    listadd = []
    listadd.append(stringconverted)
    # print(listadd)
    sigmoid_clf = pickle.load(open("./prediction/sig_clf.p", "rb"))
    # print(sigmoid_clf)
    tfidf_fit_data = pickle.load(open("./prediction/tfidf_fit_data.p", "rb"))

    Train_X1_tf = tfidf_fit_data.transform(listadd)
    # print(Train_X1_tf.shape)

    # count_vect = TfidfVectorizer(max_features=3000, min_df=10, decode_error='ignore', stop_words='english')
    # Train_X_tf = count_vect.fit_transform(listadd)
    # print(Train_X_tf.shape)

    predict_y = sigmoid_clf.predict_proba(Train_X1_tf)

    predicted_y = np.argmax(predict_y, axis=1)
    # print("Total number of data points :", len(predicted_y))
    # print(predicted_y)
    if 1 in predicted_y:
        return ["The given text ",text," is toxic."]
    else:
        return ["The given text ",text," is not toxic."]
