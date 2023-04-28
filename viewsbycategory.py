from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Youtube Data Analysis") \
    .getOrCreate()

# Load the data
cleaned_data_path = "C:/Users/deonl/Desktop/cleaned_data.csv"
data = spark.read.csv(cleaned_data_path, header=True, inferSchema=True)

# Drop the "category_UNA" column if it exists
if "category_UNA" in data.columns:
    data = data.drop("category_UNA")

# List of categories
categories = [
    "Autos & Vehicles", "Comedy",
    "Entertainment", "Film & Animation",
    "Gadgets & Games", "Howto & DIY", "Music",
    "News & Politics", "People & Blogs",
    "Pets & Animals", "Sports", "Travel & Places"
]

# Aggregate the views by category
views_by_category = {}
for category in categories:
    category_column = f"category_{category}"
    views_by_category[category] = data.filter(data[category_column] == 1).groupBy().sum("views").collect()[0][0]

# Find the most viewed category and its views
most_viewed_category = max(views_by_category, key=views_by_category.get)
max_views = views_by_category[most_viewed_category]

# Print the most viewed category and its views
print(f"The most viewed category is {most_viewed_category} with {max_views} views.")

# Create a bar chart
plt.bar(views_by_category.keys(), views_by_category.values())

# Add a title and labels to the plot
plt.title("Number of Views by Category")
plt.xlabel("Category")
plt.ylabel("Number of Views")

# Customize x-axis labels
plt.xticks(range(len(categories)), categories, rotation=90)

# Show the plot
plt.show()

# Stop the Spark session
spark.stop()