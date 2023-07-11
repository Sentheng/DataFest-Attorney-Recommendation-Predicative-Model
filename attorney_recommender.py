# -*- coding: utf-8 -*-
"""Attorney_Recommender.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zEFe082Td5uxjPbzFsDkeQl9RjfKgh4b
"""

!pip install kneed

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from nltk import sent_tokenize
import nltk
nltk.download('punkt')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from kneed import KneeLocator

qbank = pd.read_csv("/content/drive/Shareddrives/Data Fest 2023/data/answered_merged_questions.csv")
attorney_cat_count = pd.read_csv("/content/drive/Shareddrives/Data Fest 2023/data/attorney_cat_count.csv")
unanswered_q = pd.read_csv("/content/drive/Shareddrives/Data Fest 2023/data/nan_MergedQuestions.csv")
qbank = qbank[['QuestionUno', 'PostText', "TakenByAttorneyUno"]]
qbank

unanswered_q['PostText'][6512]

def find_cat_attorney(target, compare_database):
  target = target["Category"]
  subset_data = compare_database[compare_database['Category'] == target]
  sorted_subset_data = subset_data.sort_values(by = ['count'], ascending = False)
  return sorted_subset_data.head()

attorney_cat_count

attorney_cat = find_cat_attorney(unanswered_q.iloc[6512], attorney_cat_count)
attorney_cat

# target = unanswered_q['PostText'][6512]
# compare_database = list(qbank["PostText"])

def find_attorney(target, compare_database):
  target = target['PostText']
  vectorizer = TfidfVectorizer()

  # To make uniformed vectors, both documents need to be combined first.
  compare_database.insert(0, target)
  embeddings = vectorizer.fit_transform(compare_database)

  cosine_similarities = cosine_similarity(embeddings[0:1], embeddings[1:]).flatten()
  qbank1 = qbank
  qbank1["scores"] = cosine_similarities
  qbank1 = qbank1.sort_values(by = ['scores'], ascending = False)

  return qbank1

results = find_attorney(unanswered_q.iloc[6512], list(qbank["PostText"]))
attorney_most_sim = results.head()
attorney_most_sim

plt.scatter(range(106606), y = results["scores"])
k1 = KneeLocator(range(106606), results["scores"], curve = 'convex', direction = 'decreasing')

threshold = results.iloc[k1.elbow]['scores']
results_top = results[results["scores"]>threshold]
attorney_most_xp = results_top.groupby("TakenByAttorneyUno").count().sort_values(by = ['scores'], ascending = False).head()
pd.DataFrame(attorney_most_xp["QuestionUno"])

recs = pd.DataFrame()
df1 = pd.DataFrame(list(attorney_most_xp.index))
df2 = pd.DataFrame(list(attorney_most_sim["TakenByAttorneyUno"]))
df3 = pd.DataFrame(list(attorney_cat["AttorneyUno"]))
recs["AttorneyUno"] = pd.concat([df1,df2,df3])
recs.groupby(["AttorneyUno"])
recs = recs.reset_index().drop(columns = "index")
recs = pd.DataFrame(recs.groupby('AttorneyUno').size())
recs.sort_values(by = 0, ascending = False)
