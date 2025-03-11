import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Display the first few rows
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df.dropna(subset=['director', 'cast'], inplace=True)
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
content_type_counts = df['type'].value_counts()
print(content_type_counts)
country_counts = df['country'].value_counts().head(10)
print(country_counts)
director_counts = df['director'].value_counts().head(10)
print(director_counts)
genres = df['listed_in'].str.split(',').explode()
genre_counts = genres.value_counts().head(10)
print(genre_counts) 



sns.set(style='darkgrid')

# Plot the distribution of content types
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='type', palette='viridis')
plt.title('Distribution of Content Types')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Plot the top 10 countries producing content
plt.figure(figsize=(12, 8))
sns.barplot(x=country_counts.values, y=country_counts.index, palette='viridis')
plt.title('Top 10 Countries Producing Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()

# Plot the top 10 directors with most titles
plt.figure(figsize=(12, 8))
sns.barplot(x=director_counts.values, y=director_counts.index, palette='viridis')
plt.title('Top 10 Directors with Most Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()

# Plot the most common genres
plt.figure(figsize=(12, 8))
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='viridis')
plt.title('Most Common Genres')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()