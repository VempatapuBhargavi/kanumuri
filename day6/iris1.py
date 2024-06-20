
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
iris = sns.load_dataset('iris')
# 1. Data Collection
print("First few rows of the dataset:")
print(iris.head())
# 2. Data Cleaning
# Check for missing values
print("\nMissing values:")
print(iris.isnull().sum())
# 3. Data Transformation
# Encode categorical data if necessary (not needed for iris dataset)
# 4. Data Visualization
# Pairplot to visualize relationships between variables
sns.pairplot(iris, hue='species')
plt.suptitle('Pairplot of Iris Dataset')
plt.show()
# 5. Descriptive Statistics
print("\nDescriptive statistics:")
print(iris.describe())
# 6. Correlation Analysis
numeric_iris = iris.drop(columns=['species'])
correlation_matrix = numeric_iris.corr()
print("\nCorrelation matrix:")
print(correlation_matrix)
# Heatmap of the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()
# 7. Hypothesis Testing
# Example: Test if the mean sepal length is different for different species
from scipy.stats import f_oneway

setosa = iris[iris['species'] == 'setosa']['sepal_length']
versicolor = iris[iris['species'] == 'versicolor']['sepal_length']
virginica = iris[iris['species'] == 'virginica']['sepal_length']
f_stat, p_value = f_oneway(setosa, versicolor, virginica)
print("\nANOVA test for sepal length across species:")
print(f"F-statistic: {f_stat}, P-value: {p_value}")
# 8. Feature Engineering
# Example: Create a new feature 'sepal_area'
iris['sepal_area'] = iris['sepal_length'] * iris['sepal_width']
print("\nFirst few rows with the new feature 'sepal_area':")
print(iris.head())
# Visualize the new feature
sns.boxplot(x='species', y='sepal_area', data=iris)
plt.title('Boxplot of Sepal Area by Species')
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
iris = sns.load_dataset('iris')
# 4.2.1 Descriptive Statistics
mean_sepal_length = iris['sepal_length'].mean()
median_sepal_length = iris['sepal_length'].median()
mode_sepal_length = iris['sepal_length'].mode()[0]
print(f"Mean Sepal Length: {mean_sepal_length}")
print(f"Median Sepal Length: {median_sepal_length}")
print(f"Mode Sepal Length: {mode_sepal_length}")
# 4.2.2 Dispersion Statistics
variance_sepal_length = iris['sepal_length'].var()
std_dev_sepal_length = iris['sepal_length'].std()
print(f"Variance of Sepal Length: {variance_sepal_length}")
print(f"Standard Deviation of Sepal Length: {std_dev_sepal_length}")
# 4.2.3 Correlation Analysis
import seaborn as sns

iris = sns.load_dataset('iris')
# Drop the non-numeric 'species' column
numeric_iris = iris.drop(columns=['species'])
# Calculate the correlation matrix
correlation_matrix = numeric_iris.corr()
print("Correlation matrix:")
print(correlation_matrix)
# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()


