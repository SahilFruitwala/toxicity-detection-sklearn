import nltk
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re

nltk.download('all') # download all courpus and other data

df = pd.read_csv("train.csv")
df.head()

del df['id']

print(df.head())


def cleaning(df):
	"""
		Takes a dataframe as argument and return cleaned dataframe
		Removes url, emojies, new lines, tabs and other characters except alphanumeric data in english.
	"""
    df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii')) # remove emojies https://stackoverflow.com/questions/57514169/how-can-i-remove-emojis-from-a-dataframe
    df['comment_text'] = df['comment_text'].apply(lambda x: re.split('http(s)?:\/\/.*', str(x))[0])  # removing urls from text # ref: https://stackoverflow.com/questions/51994254/removing-url-from-a-column-in-pandas-dataframe
    df['comment_text'] = df['comment_text'].str.replace(r'[\t\n]', ' ')
    df['comment_text'] = df['comment_text'].str.replace(r'[^a-zA-Z0-9 \']', '') # removed all characters except alphanumeric data and whitespace
    df['comment_text'] = df['comment_text'].str.strip()
    return(df)

def all_in_one_toxcity_column(df):
	"""
		Takes df as input and return dataframe with new column names is_toxic.
		Put all categories in one column in numeric form.
		0 for no toxicity,
		1 for toxic,
		2 for obscene,
		3 for severe_toxic,
		4 for threat,
		5 for insult,
		6 for identity_hate,
		7 for more than one toxicity,
	"""
    df['is_toxic'] = -1
    for i in range(len(df)):
        if (df.toxic[i] + df.obscene[i] + df.severe_toxic[i] + df.threat[i] + df.insult[i] + df.identity_hate[i]) > 1:
            df['is_toxic'][i] = 7    
        elif df.toxic[i] == 1:
            df['is_toxic'][i] = 1
        elif df.obscene[i] == 1:
            df['is_toxic'][i] = 2
        elif df.severe_toxic[i] == 1:
            df['is_toxic'][i] = 3
        elif df.threat[i] == 1:
            df['is_toxic'][i] = 4
        elif df.insult[i] == 1:
            df['is_toxic'][i] = 5
        elif df.identity_hate[i] == 1:
            df['is_toxic'][i] = 6
        else:
            df['is_toxic'][i] = 0
    df.drop(df.iloc[:, 1:7], inplace=True, axis=1)
    return(df)

def remove_contractions(df):
	"""
		Takes df as input and return dataframe with all data lowercase and removed contractions.
	"""
    contractions = { 
		    "ain't": "am not",
		    "aren't": "are not",
		    "can't": "can not",
		    "can't've": "can not have",
		    "'cause": "because",
		    "could've": "could have",
		    "couldn't": "could not",
		    "couldn't've": "could not have",
		    "didn't": "did not",
		    "doesn't": "does not",
		    "don't": "do not",
		    "hadn't": "had not",
		    "hadn't've": "had not have",
		    "hasn't": "has not",
		    "haven't": "have not",
		    "he'd": "he had",
		    "he'd've": "he would have",
		    "he'll": "he will",
		    "he'll've": "he will have",
		    "he's": "he has",
		    "how'd": "how did",
		    "how'd'y": "how do you",
		    "how'll": "how will",
		    "how's": "how has",
		    "i'd": "I had",
		    "i'd've": "I would have",
		    "i'll": "I shall",
		    "i'll've": "I shall have",
		    "i'm": "I am",
		    "i've": "I have",
		    "isn't": "is not",
		    "it'd": "it had",
		    "it'd've": "it would have",
		    "it'll": "it shall",
		    "it'll've": "it shall have",
		    "it's": "it has",
		    "let's": "let us",
		    "ma'am": "madam",
		    "mayn't": "may not",
		    "might've": "might have",
		    "mightn't": "might not",
		    "mightn't've": "might not have",
		    "must've": "must have",
		    "mustn't": "must not",
		    "mustn't've": "must not have",
		    "needn't": "need not",
		    "needn't've": "need not have",
		    "o'clock": "of the clock",
		    "oughtn't": "ought not",
		    "oughtn't've": "ought not have",
		    "shan't": "shall not",
		    "sha'n't": "shall not",
		    "shan't've": "shall not have",
		    "she'd": "she had",
		    "she'd've": "she would have",
		    "she'll": "she shall",
		    "she'll've": "she shall have",
		    "she's": "she has",
		    "should've": "should have",
		    "shouldn't": "should not",
		    "shouldn't've": "should not have",
		    "so've": "so have",
		    "so's": "so as",
		    "that'd": "that would",
		    "that'd've": "that would have",
		    "that's": "that has",
		    "there'd": "there had",
		    "there'd've": "there would have",
		    "there's": "there has",
		    "they'd": "they had",
		    "they'd've": "they would have",
		    "they'll": "they shall",
		    "they'll've": "they shall have",
		    "they're": "they are",
		    "they've": "they have",
		    "to've": "to have",
		    "wasn't": "was not",
		    "we'd": "we had",
		    "we'd've": "we would have",
		    "we'll": "we will",
		    "we'll've": "we will have",
		    "we're": "we are",
		    "we've": "we have",
		    "weren't": "were not",
		    "what'll": "what shall",
		    "what'll've": "what shall have",
		    "what're": "what are",
		    "what's": "what has",
		    "what've": "what have",
		    "when's": "when has",
		    "when've": "when have",
		    "where'd": "where did",
		    "where's": "where has",
		    "where've": "where have",
		    "who'll": "who shall",
		    "who'll've": "who shall have",
		    "who's": "who has",
		    "who've": "who have",
		    "why's": "why has",
		    "why've": "why have",
		    "will've": "will have",
		    "won't": "will not",
		    "won't've": "will not have",
		    "would've": "would have",
		    "wouldn't": "would not",
		    "wouldn't've": "would not have",
		    "y'all": "you all",
		    "y'all'd": "you all would",
		    "y'all'd've": "you all would have",
		    "y'all're": "you all are",
		    "y'all've": "you all have",
		    "you'd": "you had",
		    "you'd've": "you would have",
		    "you'll": "you shall",
		    "you'll've": "you shall have",
		    "you're": "you are",
		    "you've": "you have"
    }

    df['comment_text'] = df['comment_text'].str.lower()
    df['comment_text'] = df['comment_text'].replace(contractions)

    return(df)

# https://gist.github.com/sebleier/554280
# we are removing the words from the stop words list: 'no', 'nor', 'not'

# import time
# from tqdm import tqdm_notebook as tqdm

def lemmatization_remove_stopwords(df):
	"""
		Takes df as input and return dataframe with removed stopwords and lemmatized data.
		Used custom stopwords and nltk library's WordNetLemmatizer for lemmatizing.
	"""
	stopwords= ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"]
    word_Lemmatized = WordNetLemmatizer()
    for index, comment in enumerate(df['comment_text']):
        temp_data = []
        for word in str(comment).split():
            if word not in stopwords and word.isalpha():
                temp_word = word_Lemmatized.lemmatize(word)
                temp_data.append(temp_word)
        df.loc[index,'comment_text'] = ' '.join(temp_data)
    return df

train = cleaning(df)
train.head()
print('Checking Null')
print(df.isnull().any())

train1 = all_in_one_toxcity_column(train)
train1.head()
print(train1.head())

train1 = remove_contractions(train)
# train1.to_csv('new_train_data.csv',index=False)
print(train1.head())

df = lemmatization_remove_stopwords(df)
print(df['comment_text'].head())
df.to_csv('Final_Cleaned_Data.csv', index=False)