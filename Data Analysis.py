import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset 
df = pd.read_csv('Iris.csv')

# showing the first few rows
print(df.head())

# Checking for missing values
print(df.isnull().sum())

# Summary statistics for numerical columns
print(df.describe())

# Group by 'species' and calculate the mean of each group
print(df.groupby('species').mean())

# creating a Line Chart for Trend over index.
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['sepal_length'], label='Sepal Length')
plt.title('Sepal Length Trend')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# creating a Bar Chart of Average Sepal Length per Species.
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='sepal_length', data=df)
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.show()

# creating a Histogram for Distribution of Sepal Width.
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_width'], kde=True, bins=20)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

#  creating a Scatter Plot for Sepal Length vs Sepal Width.
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df)
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(title='Species')
plt.show()
