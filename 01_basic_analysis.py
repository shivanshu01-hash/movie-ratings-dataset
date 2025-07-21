import pandas as pd

tags = pd.read_csv(r"C:\Users\dell\OneDrive\Desktop\FSDSAI\python\MIDb project\tag.csv")
movies = pd.read_csv(
    r"C:\Users\dell\OneDrive\Desktop\FSDSAI\python\MIDb project\movie.csv"
)
ratings = pd.read_csv(
    r"C:\Users\dell\OneDrive\Desktop\FSDSAI\python\MIDb project\rating.csv"
)

# View the full output of a DataFrame(optional)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# Delet non-numeric columns
del ratings["timestamp"]
del tags["timestamp"]

# Dataframe
# 'Tags' DataFrame
print("\nOverview of the data:\n", tags.head())
print("\nRow indices (labels):\n", tags.index)
print("\nColumn names:\n", tags.columns)
print("\nRows at positions 0, 11, and 500:\n", tags.iloc[[0, 11, 500]])

# 'Movies' DataFrame
print("\nOverview of the data:\n", movies.head())
print("\nRow indices (labels):\n", movies.index)
print("\nColumn names:\n", movies.columns)
print("\nRows at positions 0, 11, and 500:\n", movies.iloc[[0, 11, 500]])

# Descriptive statical
# 'Tags' DataFrame
print("\nOverview of the ratings (describe):\n", ratings["rating"].describe())
print("\nMean of the ratings:\n", ratings["rating"].mean())
print("\nMaximum rating:\n", ratings["rating"].max())
print("\nMinimum rating:\n", ratings["rating"].min())
print("\nStandard deviation of ratings:\n", ratings["rating"].std())
print("\nMost common rating (mode):\n", ratings["rating"].mode())
print("\nCorrelation matrix of the DataFrame:\n", ratings.corr())

# Filter
print("\nRatings greater than 10:\n", ratings["rating"] > 10)
print("\nRatings greater than 0:\n", ratings["rating"] > 0)

filter_positive = ratings["rating"] > 0
print("\nIs there any rating greater than 0?:\n", filter_positive.any())
print("\nAre all ratings greater than 0?:\n", filter_positive.all())

filter_positive = ratings["rating"] > 10
print("\nIs there any rating greater than 10?:\n", filter_positive.any())
print("\nAre all ratings greater than 10?:\n", filter_positive.all())

# Data cleaning : Handling Missing Data
print(ratings.shape)
print(ratings.isnull().any().any())

print(tags.shape)
print(tags.isnull().any().any())

print(movies.shape)
print(movies.isnull().any().any())

# Data Visualisation
import matplotlib.pyplot as plt

ratings.hist(column="rating", figsize=(10, 5))
plt.show()

ratings.boxplot(column="rating", figsize=(10, 5))
plt.show()

# #Slicing out columns
print(tags["tag"].head())
print(movies[["title", "genres"]].head())
tag_count = tags["tag"].value_counts()
print(tag_count[-10:])
tag_count[:10].plot(kind="bar", figsize=(10, 5))
plt.show()

is_highly_rated = ratings["rating"] >= 5.0
ratings[is_highly_rated][30:50]
is_actions = movies["genres"].str.contains("Action")
movies[is_actions][5:15]
movies[is_actions].head(5)

# Group by aggregate
rating_count = ratings[["movieId", "rating"]].groupby("rating").count()
print(rating_count)

average_rating = ratings[["movieId", "rating"]].groupby("movieId").mean()
print(average_rating)

movie_count = ratings[["movieId", "rating"]].groupby("movieId").count()
print(movie_count.tail())

# Merge Dataframe
print(tags.head())
print(movies.head())
t = movies.merge(tags, on="movieId", how="inner")
print(t.head())

avg_ratings = ratings.groupby("movieId", as_index=False).mean()
# del avg_ratings('userId')
print(avg_ratings.head())

box_office = movies.merge(avg_ratings, on="movieId", how="inner")
print(box_office.tail())

is_highly_rated = box_office["rating"] >= 4.0
print(box_office[is_highly_rated][-5:])

is_adventure = box_office["genres"].str.contains("adventure")
print(box_office[is_adventure][:5])
print(box_office[is_adventure & is_highly_rated][:-5])

# Vectorized string operation
# Split 'genres' into multiple columns
movies_genres = movies["genres"].str.split("|", expand=True)
print(movies_genres[:10])

# Add a new columns for comedy genres

movies_genres["is comedy"] = movies["genres"].str.contains("comedy")
print(movies_genres[:10])

# Extract Year from title eg (2007)
movies["year"] = movies["title"].str.extract(r".*\((.*)\).*", expand=True)
print(movies.tail())

tags["parsed_time"] = pd.to_datetime(tags["timestamp"], unit="s")
print(tags["parsed_time"].dtype())

greater_than_t = tags["parsed_time"] > "2015-02-01"
selected_rows = tags[greater_than_t]
print(tags.shape, selected_rows.shape)

tags.sort_values(by="parsed_time", ascending=True)[:10]

average_rating = (
    ratings[["movieId", "rating"]].groupby("movieId", as_index=False).mean()
)
print(average_rating.tail())

joined = movies.merge(average_rating, on="movieId", how="inner")
print(joined.head())
print(joined.corr())
