# -*- coding: utf-8 -*-
"""Student_result _analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BC0AWIJtj4p5kR1CYItaJrClGkQ4hz1Q
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as

df = pd.read_csv("/content/Expanded_data_with_more_features.csv")
print(df.head())

df.describe()

df.info()

df.isnull().sum()

#drop unnamed column
df = df.drop("Unnamed: 0", axis=1)
print(df.head())

#drop unnamed column
df = df.drop("Unnamed: 0", axis=1)
print(df.head())

"""# **Gender distribution**"""

plt.figure(figsize=(6,6))
ax = sns.countplot(x="Gender", data=df, hue="Gender", palette=["#3498db", "#e74c3c"])

# Adding values on top of each bar for both genders
for container in ax.containers:
    ax.bar_label(container)

plt.title("Gender Distribution")
plt.show()

#from th above chart we have analysed that the no.of females in the data is more than the no.of males

gb= df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)

plt.figure(figsize=(4,4))
sns.heatmap(gb, annot=True)
plt.title("Relation ship between student's score and parent's Education")
plt.show

"""**From the above chart we have conclude that the education of the parent have a good impact on their student score.**"""

gb1= df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb1)

plt.figure(figsize=(4,4))
sns.heatmap(gb1, annot=True)
plt.title("Relation ship between student's score and parent marital status")
plt.show

"""**From the above chart we have conclude that the parent Marital status have no impact on their student score.**"""

sns.boxplot(data=df)
plt.show()

print(df["EthnicGroup"].unique())

"""# **Distribution of ethinic group**"""

#distribution of ethinic group
groupA = df.loc[(df["EthnicGroup"] == 'group A')]
print(groupA.head())

import matplotlib.pyplot as plt
import seaborn as sns

groupA = df.loc[(df["EthnicGroup"] == 'group A')].count()
groupB = df.loc[(df["EthnicGroup"] == 'group B')].count()
groupC = df.loc[(df["EthnicGroup"] == 'group C')].count()
groupD = df.loc[(df["EthnicGroup"] == 'group D')].count()
groupE = df.loc[(df["EthnicGroup"] == 'group E')].count()
l = ["group A", "group B","group C","group D","group E"] # Labels for the pie chart
mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]] # Values for the pie chart
# Use a lambda function to format the percentage with a '%' sign
plt.pie(mlist, labels=l, autopct=lambda p: '{:.1f}%'.format(p))
plt.title("Distribution of Ethnic Group")
plt.show()

plt.figure(figsize=(6,6))
ax = sns.countplot(x="EthnicGroup", data=df)
for container in ax.containers:
    ax.bar_label(container)

plt.show()