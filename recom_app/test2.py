import sys
import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv')
data = df[['Option','Description','Company']]
cos_sim_data=pd.read_excel('cosine.xlsx')

if (sys.argv[1]=='runserver'):
    nameC="vermeg"

else:
    nameC = "%s" % (sys.argv[1])

INDEX=data[data['Company'] == nameC ].index[0]

index_recomm =cos_sim_data.loc[INDEX].sort_values(ascending=False).index.tolist()[1:6]
movies_recomm =  data['Company'].loc[index_recomm].values


resultat='The companies are : '
for company in movies_recomm:
    resultat=resultat + company + ' , '
print(resultat)
print()


resultat2=' '
for q in range(len(movies_recomm)):
    resultat2 = resultat2 + data['Description'].loc[index_recomm[q]] + ' \n '

print(resultat2)


