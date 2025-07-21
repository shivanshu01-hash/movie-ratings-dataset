import pandas as pd

tags = pd.read_csv(r"C:\Users\dell\OneDrive\Desktop\FSDSAI\python\MIDb project\tag.csv")
movies = pd.read_csv(
    r"C:\Users\dell\OneDrive\Desktop\FSDSAI\python\MIDb project\movie.csv"
)
ratings = pd.read_csv(
    r"C:\Users\dell\OneDrive\Desktop\FSDSAI\python\MIDb project\rating.csv"
)


print(tags.head())
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
