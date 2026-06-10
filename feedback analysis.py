# CUSTOMER FEEDBACK ANALYSIS PROJECT
# Dataset: flipkart_product.csv

# Install required libraries:
# pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: LOAD CSV FILE
# -----------------------------

# Load dataset
df = pd.read_csv("flipkart_product.csv", encoding="latin1")

# Show first 5 rows
print("First 5 Rows of Dataset:")
print(df.head())

# Show column names
print("\nColumn Names:")
print(df.columns)

# -----------------------------
# STEP 2: DATA CLEANING
# -----------------------------

# Remove missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nDataset Shape After Cleaning:")
print(df.shape)

# -----------------------------
# STEP 3: PRODUCT RATING ANALYSIS
# -----------------------------

plt.figure(figsize=(8,5))
plt.plot(df['Rate'])
plt.title("Customer Product Ratings")
plt.xlabel("Customers")
plt.ylabel("Rating")
plt.grid(True)
plt.show()

# -----------------------------
# STEP 4: RATING DISTRIBUTION
# -----------------------------

plt.figure(figsize=(8,5))
df['Rate'].value_counts().sort_index().plot(kind='bar')
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.grid(True)
plt.show()

# -----------------------------
# STEP 5: PRODUCT-WISE REVIEW COUNT
# -----------------------------

plt.figure(figsize=(10,5))
df['ProductName'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Product Review Count")
plt.xlabel("Product Name")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# -----------------------------
# STEP 6: TOTAL REVIEWS BAR GRAPH
# -----------------------------

total_reviews = len(df)

plt.figure(figsize=(5,5))
plt.bar(['Total Reviews'], [total_reviews])
plt.title("Total Customer Reviews")
plt.ylabel("Count")
plt.show()

# -----------------------------
# STEP 7: AVERAGE PRODUCT RATING BAR
# -----------------------------

average_rating = df['Rate'].mean()

plt.figure(figsize=(5,5))
plt.bar(['Average Rating'], [average_rating])
plt.title("Average Product Rating")
plt.ylabel("Rating")
plt.show()

# -----------------------------
# STEP 8: BASIC OUTPUT
# -----------------------------

print("\nAverage Rating:")
print(df['Rate'].mean())

print("\nMaximum Rating:")
print(df['Rate'].max())

print("\nMinimum Rating:")
print(df['Rate'].min())

print("\nTotal Reviews:")
print(total_reviews)