
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import re
from nltk.stem import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

nltk.download('stopwords')
nltk.download('punkt')

happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
])
sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
])
emoticons = happy.union(sad)
emojiptn = re.compile("["
                      u"\U0001F600-\U0001F64F"
                      u"\U0001F300-\U0001F5FF"
                      u"\U0001F680-\U0001F6FF"
                      u"\U0001F1E0-\U0001F1FF"
                      u"\U00002702-\U000027B0"
                      u"\U000024C2-\U0001F251"
                      "]+", flags=re.UNICODE)

def clean_typed_data(text):

    text = re.sub(r':', '', text)
    text = re.sub(r'‚Ä¶', '',  text)
    text = re.sub(r'[^\x00-\x7F]+', ' ',  text)
    text = emojiptn.sub(r'',  text)
    text = re.sub(r'http\S+', '', text)
    for k in text.split("\n"):
        text =re.sub(r"[^a-zA-Z]+", ' ', k)
    # print(text)
    words = word_tokenize(text.lower())
    print(words)
    editedwords = []
    ps = PorterStemmer()

    stopWords = set(stopwords.words('english'))  # a set of English
    for w in words:
        if w not in stopWords:
            w = ps.stem(w)
            editedwords.append(w)

    # print(editedwords)
    stringconverted = ' '.join(editedwords)
    listadd = []
    listadd.append(stringconverted)
    print(listadd)
    count_vect = TfidfVectorizer(max_features=3000, min_df=1, decode_error='ignore', stop_words='english')
    Train_X_tf = count_vect.fit_transform(listadd)
    print(Train_X_tf.shape)


text = ":) 😁😁😁😁😁😁 @@@@  999 This is a the punarva gaming gamer. It is a book  "
clean_typed_data(text)