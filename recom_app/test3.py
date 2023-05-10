import sys
import pandas as pd
import numpy as np


import seaborn as sns
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

stop_wordsFR  = set(stopwords.words('french'))
stop_wordsAN  = set(stopwords.words('english'))

df = pd.read_csv('exportdf.csv')

if (sys.argv[1]=='runserver'):
    nameC="ERP-BI"

else:
    nameC = "%s" % (sys.argv[1])


final_stopwords_list = stop_wordsAN | stop_wordsFR
tfidf = TfidfVectorizer(stop_words=final_stopwords_list)
df['Skills'] = df['Skills'].fillna('')
tfidf_matrix = tfidf.fit_transform(df['Skills'])

cosine_sim = linear_kernel(tfidf_matrix , tfidf_matrix)
indicies = pd.Series(df.index, index = df['Specialité'])




def get_recommendation(specialite, cosine_sim=cosine_sim):
    idx = indicies[specialite]
    sim_scores = enumerate(cosine_sim[idx[0]])
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    sim_index = [i[0] for i in sim_scores]
    return df['Skills'].iloc[sim_index].values


res=get_recommendation(nameC)
x=res[0]
y=res[1]
print(x + y)


