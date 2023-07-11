# -*- coding: utf-8 -*-
"""attorney_experience.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QN_na6NdTHII0gtk__knjG3ziJwTExVI
"""

import pandas as pd
import numpy as np

attorney_cases = pd.read_csv("/content/drive/Shareddrives/Data Fest 2023/data/attorney_cases.csv")

categories = pd.read_csv("/content/drive/Shareddrives/Data Fest 2023/data/categories.csv")

pd.unique(categories["Category"])

pd.unique(attorney_cases['AttorneyUno'])

pd.unique(attorney_cases['AttorneyUno'])

zoo.groupby('animal').count()

#unique_categories = pd.unique(categories["Category"])
dictionary = {
 'AttorneyUno' : [],
 'Consumer Financial Questions' : [],
 'Education' : [],
 'Work, Employment and Unemployment' : [],
 'Family and Children' : [],
 'Health and Disability' : [],
 'Juvenile' : [],
 'Housing and Homelessness' : [],
 'Income Maintenance' : [],
 'Individual Rights' : [],
 'Other' : []
 }
df = pd.DataFrame(dictionary,
                         columns = ['AttorneyUno', 'Consumer Financial Questions', 'Education',
                                    'Work, Employment and Unemployment', 'Family and Children',
                                    'Health and Disability', 'Juvenile', 'Housing and Homelessness',
                                    'Income Maintenance', 'Individual Rights', 'Other'])
for i in pd.unique(attorney_cases['AttorneyUno']):
  worked_cat = list(attorney_cases[(attorney_cases['AttorneyUno']==i)].groupby('Category').count().index)
  worked_cat_count = list(attorney_cases[(attorney_cases['AttorneyUno']==i)].groupby('Category').count()['Id_x'])
  tuples = [(key, value)
          for i, (key, value) in enumerate(zip(worked_cat, worked_cat_count))]
  df2 = dict(tuples)
  df2 = df2.update({"AttorneyUno": i})
  df = df.append(df2, ignore_index = True)

df

# initializing lists
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# create a list of tuples using enumerate()
tuples = [(key, value)
          for i, (key, value) in enumerate(zip(test_keys, test_values))]

# convert list of tuples to dictionary using dict()
res = dict(tuples)

print(res)

rslt_df = dataframe[(dataframe['Age'] == 22) &
          dataframe['Stream'].isin(options)]

list(attorney_cases[(attorney_cases['AttorneyUno']=='7A2C12BE-9F37-4C9D-A6ED-41B916820CE0')].groupby('Category').count().index)

list(attorney_cases[(attorney_cases['AttorneyUno']=='7A2C12BE-9F37-4C9D-A6ED-41B916820CE0')].groupby('Category').count()['Id_x'])

attorney_cases.groupby('AttorneyUno','Category')

attorney_cases.iloc['AttorneyUno'=="2BD64F66-B14E-4119-9B2F-6B22D6BB98AC"]

categories = pd.unique(categories["Category"])

dictionary = {
 'AttorneyUno' : [],
 'Consumer Financial Questions' : [],
 'Education' : [],
 'Work, Employment and Unemployment' : [],
 'Family and Children' : [],
 'Health and Disability' : [],
 'Juvenile' : [],
 'Housing and Homelessness' : [],
 'Income Maintenance' : [],
 'Individual Rights' : [],
 'Other' : []
 }
 dataframe = pd.DataFrame(dictionary,
                         columns = ['AttorneyUno', 'Consumer Financial Questions', 'Education',
                                    'Work, Employment and Unemployment', 'Family and Children',
                                    'Health and Disability', 'Juvenile', 'Housing and Homelessness',
                                    'Income Maintenance', 'Individual Rights', 'Other'])

dataframe = pd.DataFrame(dictionary,
                         columns = ['AttorneyUno', 'Consumer Financial Questions', 'Education',
                                    'Work, Employment and Unemployment', 'Family and Children',
                                    'Health and Disability', 'Juvenile', 'Housing and Homelessness',
                                    'Income Maintenance', 'Individual Rights', 'Other'])

dataframe

