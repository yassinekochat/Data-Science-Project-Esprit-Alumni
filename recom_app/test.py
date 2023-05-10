import sys
import pandas as pd
import numpy as np
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
stop_wordsFR  = set(stopwords.words('french'))
stop_wordsAN  = set(stopwords.words('english'))
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



df = pd.read_csv("export_df_2.csv")
vectorizer = TfidfVectorizer(stop_words=stop_wordsFR)
X = vectorizer.fit_transform(df["EntrepriseSpec"])
true_k = 6
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=200, n_init=10)
model.fit(X)
labels = model.labels_
wiki_cl = pd.DataFrame(list(zip(df['Specialité'], labels)), columns=['option', 'cluster'])
result = {'cluster': labels, 'wiki': df["EntrepriseSpec"]}
result = pd.DataFrame(result)

for k in range(0, true_k):
    text = " ".join(review for review in df["EntrepriseSpec"].astype(str))
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    print('Cluster: {}'.format(k))
    titles = wiki_cl[wiki_cl.cluster == k]['option']
    plt.figure(figsize=[7, 7])
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

    # store to file
    # plt.savefig("C:/Users/Karoui Houaida/Desktop/Alumni_Project/image/fig"+str(k)+".png", format="png")
    plt.savefig("C:/Users/admin/PycharmProjects/djangoProject1/img/cluster/fig" + str(k) + ".png",format="png")
    plt.show()