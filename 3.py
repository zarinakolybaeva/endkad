import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data.csv"
df = pd.read_csv(file_path)

df['size'] = pd.to_numeric(df['size'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['offer_price'] = pd.to_numeric(df['offer_price'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=30, kde=True)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='brand', y='offer_price', data=df, estimator='mean', ci=None)
plt.title('Average Offer Price by Brand')
plt.xticks(rotation=90)
plt.xlabel('Brand')
plt.ylabel('Average Offer Price')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='price', y='offer_price', data=df, hue='brand', alpha=0.7)
plt.title('Price vs Offer Price')
plt.xlabel('Price')
plt.ylabel('Offer Price')
plt.show()

plt.figure(figsize=(10, 6))
df['color'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Most Common Colors')
plt.xlabel('Color')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x='size', y='price', data=df, estimator='mean', ci=None)
plt.title('Average Price by Size')
plt.xlabel('Size')
plt.ylabel('Average Price')
plt.show()

df['discount_percent'] = ((df['price'] - df['offer_price']) / df['price']) * 100
plt.figure(figsize=(10, 6))
sns.histplot(df['discount_percent'], bins=30, kde=True)
plt.title('Discount Percentage Distribution')
plt.xlabel('Discount Percentage')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
df['brand'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Brands by Frequency')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df[['price', 'offer_price', 'size', 'discount_percent']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='brand', y='discount_percent', data=df, estimator='mean', ci=None)
plt.title('Average Discount Percentage by Brand')
plt.xticks(rotation=90)
plt.xlabel('Brand')
plt.ylabel('Average Discount Percentage')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='color', y='offer_price', data=df)
plt.title('Offer Price Distribution by Color')
plt.xticks(rotation=90)
plt.xlabel('Color')
plt.ylabel('Offer Price')
plt.show()

top_brands = df['brand'].value_counts().head(5).index
filtered_df = df[df['brand'].isin(top_brands)]
plt.figure(figsize=(10, 6))
sns.countplot(x='brand', hue='color', data=filtered_df)
plt.title('Top Colors for Top 5 Brands')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.legend(title='Color')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='brand', y='size', data=df, estimator='mean', ci=None)
plt.title('Average Size by Brand')
plt.xticks(rotation=90)
plt.xlabel('Brand')
plt.ylabel('Average Size')
plt.show()

top_discounted = df.sort_values(by='discount_percent', ascending=False).head(10)
print("Top 10 Discounted Products:")
print(top_discounted[['brand', 'color', 'price', 'offer_price', 'discount_percent']])

plt.figure(figsize=(10, 6))
df['size'].value_counts().sort_index().plot(kind='bar')
plt.title('Frequency of Sizes')
plt.xlabel('Size')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
df.groupby('size')[['price', 'offer_price']].mean().plot(kind='bar')
plt.title('Price and Offer Price by Size')
plt.xlabel('Size')
plt.ylabel('Average Price')
plt.legend(title='Price Type')
plt.show()
