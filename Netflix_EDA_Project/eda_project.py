import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("dataset/netflix_titles.csv")

print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

# -----------------------------
# 2. Basic Dataset Information
# -----------------------------
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

# -----------------------------
# 3. Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# 4. Statistical Summary
# -----------------------------
print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# 5. Content Type Analysis
# -----------------------------
print("\nMovies vs TV Shows:")
print(df["type"].value_counts())

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="type")
plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("images/content_type.png")
plt.show()

# -----------------------------
# 6. Release Year Analysis
# -----------------------------
year_counts = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.plot(year_counts.index, year_counts.values)
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("images/releases_by_year.png")
plt.show()

# -----------------------------
# 7. Top Countries
# -----------------------------
country_counts = df["country"].dropna().str.split(", ").explode().value_counts().head(10)

plt.figure(figsize=(10, 6))
country_counts.sort_values().plot(kind="barh")
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("images/top_countries.png")
plt.show()

# -----------------------------
# 8. Top Genres
# -----------------------------
genre_counts = df["listed_in"].dropna().str.split(", ").explode().value_counts().head(10)

plt.figure(figsize=(10, 6))
genre_counts.sort_values().plot(kind="barh")
plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("images/top_genres.png")
plt.show()

# -----------------------------
# 9. Ratings Analysis
# -----------------------------
print("\nContent Ratings:")
print(df["rating"].value_counts().head(10))

plt.figure(figsize=(10, 5))
df["rating"].value_counts().head(10).plot(kind="bar")
plt.title("Top Content Ratings on Netflix")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/ratings.png")
plt.show()

# -----------------------------
# 10. Correlation Analysis
# -----------------------------
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/correlation.png")
plt.show()

# -----------------------------
# 11. Important Insights
# -----------------------------
print("\n========== KEY INSIGHTS ==========")

print("1. Total number of titles:", len(df))
print("2. Most common content type:", df["type"].mode()[0])
print("3. Most common rating:", df["rating"].mode()[0])
print("4. Most common release year:", df["release_year"].mode()[0])

print("\nEDA PROJECT COMPLETED!")