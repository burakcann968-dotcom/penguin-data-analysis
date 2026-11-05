# %%
import pandas as pd

df = pd.read_csv("penguins.csv")

print(df.head())
# %%
print(df.shape)
# Finding: Dataset has 344 rows and 7 columns
# Each row represents a penguin observation

# %%
print(df.info())
# Finding: The dataset contains 4 numerical and 3 categorical columns.
# All columns contain some missing values.
# The sex column has the most missing values (33).

# %%
# # Finding: All columns contain missing values.
# The sex column has the highest number of missing values (33).
# Species and island have the fewest missing values (18 each).


print(df.isnull().sum())

# %%
# Finding: The dataset contains no duplicate rows.


print(df.duplicated().sum())
# %%
# Finding: The average penguin body mass is approximately 4216 grams.
# The median body mass is 4050 grams.
# The body mass ranges from 2700 to 6300 grams.
# The mean is higher than the median, suggesting a possible right-skewed distribution.

print(df.describe())
# %%
# Finding: Adelie is the most common species with 145 penguins.
# Gentoo is the second most common species with 118 penguins.
# Chinstrap is the least common species with 63 penguins.
# There are also 18 missing species values.


print(df['species'].value_counts())
# %%

# Finding: Gentoo penguins have the highest average body mass (5106 g).
# Adelie and Chinstrap penguins have similar average body masses.
# Gentoo penguins are approximately 1.4 kg heavier on average than Adelie penguins.


print(df.groupby('species')['body_mass_g'].mean())
# %%
# Finding: Gentoo penguins have the highest average body mass.
# Adelie and Chinstrap penguins have similar average body masses.
# The bar chart clearly shows the differences between species.

import matplotlib.pyplot as plt

average_body_mass = df.groupby('species')['body_mass_g'].mean()
average_body_mass.plot(kind='bar', )

plt.title('Average Body Mass of Penguins by Species')
plt.xlabel('Species')
plt.ylabel('Average Body Mass (g)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# %%
