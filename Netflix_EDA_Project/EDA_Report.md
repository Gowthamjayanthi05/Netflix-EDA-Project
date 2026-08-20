# Exploratory Data Analysis (EDA)
## Netflix Movies and TV Shows Dataset

---

## 1. Introduction

Exploratory Data Analysis (EDA) is the process of analyzing a dataset to understand its structure, identify patterns, discover trends, and find relationships between variables.

This project performs EDA on a Netflix Movies and TV Shows dataset containing information about Netflix titles such as content type, title, country, release year, rating, duration, and genre.

The analysis uses Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn.

---

## 2. Objectives

The main objectives of this project are:

- Analyze the Netflix dataset.
- Understand the structure and characteristics of the data.
- Identify missing values.
- Perform statistical analysis.
- Compare Movies and TV Shows.
- Analyze Netflix content by release year.
- Identify the top content-producing countries.
- Identify popular genres.
- Analyze content ratings.
- Study relationships between numerical variables.
- Present findings using visualizations.

---

## 3. Dataset Description

The dataset contains information about movies and TV shows available on Netflix.

### Dataset Size

- Total records: 8,807
- Number of features: 12

### Important Columns

| Column | Description |
|---|---|
| show_id | Unique ID of the title |
| type | Movie or TV Show |
| title | Name of the title |
| director | Director of the title |
| cast | Actors and actresses |
| country | Country where the title was produced |
| date_added | Date added to Netflix |
| release_year | Original release year |
| rating | Content rating |
| duration | Movie duration or number of seasons |
| listed_in | Genre/category |
| description | Description of the title |

---

## 4. Tools and Technologies

The following technologies were used:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code

---

## 5. Data Loading

The dataset was loaded using the Pandas library.

```python
df = pd.read_csv("dataset/netflix_titles.csv")
