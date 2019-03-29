
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#get_ipython().run_line_magic('matplotlib', 'inline')

titanic_df=pd.read_csv("titanic_data.csv")
titanic_df.head()
titanic_df.info()
titanic_df.describe()


"""
#########   Homework_1(a)  ################
(a) Plot a histogram detailing the age distribution of the dataset. What do you conclude from this
histogram? 
"""

#age = titanic_df.iloc[:, 3].values
age = titanic_df.loc[:, 'Age'].values

plt.hist(age, bins = 20)

plt.title("Histogram - Titanic Passsengers' Age Distribution")
plt.xlabel("Age (year)")
plt.ylabel("Number of Passenger")

plt.show()


"""
#########   Homework_1(b)  ################
(b) Show a violin plot detailing the age distribution, separated by survivors and deceased. What do you
conclude from this plot?
"""

sns.factorplot(data=titanic_df,x='Survived',y='Age',kind="violin",size=5,aspect=3)
plt.yticks([0,1], ['Decceased (0)' ,'Survived (1)'])


"""
#########   Homework_1(c)  ################
(c) Show a box plot summarizing the fare distribution, separated by survivors and deceased. What do you
conclude from this plot?
"""

ax = sns.boxplot(x="Survived", y="Fare", 
                data=titanic_df)
ax = sns.stripplot(x="Survived", y="Fare",
                   data=titanic_df, jitter=True,
                   edgecolor="gray")
#sns.title("Box Plot - Titanic Passsengers' Fare Distribution in terms of Servival",fontsize=12);



"""
#########   Homework_1(d)  ################
(d) Show a scatter plot of gender vs. survival. What do you conclude from this plot?
"""

plt.scatter(titanic_df.Survived, titanic_df.Sex, alpha=0.1)   ## here the plot has to be transparent so we need to pic low alpha value
plt.title("Scatter Plot - Titanic Passsengers' Gender vs. Survival")
plt.xlabel("Gender : Female (0)  ----   Male(1)")
plt.ylabel("Survival: Decceased (0) ----  Survived (1)")
plt.show()



"""
#########   Homework_1(e)  ################
(e) Plot a histogram showing the distribution of survivors as a function of gender. What do you conclude
from this histogram?
"""

age_sex_hist = sns.FacetGrid(titanic_df, col='Sex', hue='Sex')
age_sex_hist.map(plt.hist, 'Survived', bins=20)



"""
#########   Homework_1(f)  ################
(f) Plot a histogram showing the distribution of gender as a function of survival. What do you conclude
from this histogram?
"""

age_sex_hist = sns.FacetGrid(titanic_df, col='Survived', hue='Survived')
age_sex_hist.map(plt.hist, 'Sex', bins=20)


