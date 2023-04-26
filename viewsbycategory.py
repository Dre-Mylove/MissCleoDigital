import matplotlib.pyplot as plt
import pandas as pd

# Load the data
cleaned_data_path = r"C:\Users\deonl\Desktop\cleaned_data.csv"
data = pd.read_csv(cleaned_data_path, encoding='ISO-8859-1')

# List of categories
categories = [
    "category_Autos & Vehicles", "category_Comedy",
    "category_Entertainment", "category_Film & Animation",
    "category_Gadgets & Games", "category_Howto & DIY", "category_Music",
    "category_News & Politics", "category_People & Blogs",
    "category_Pets & Animals", "category_Sports", "category_Travel & Places"
]

# Aggregate the views by category
views_by_category = [data[category].sum() for category in categories]

# Create a bar chart
plt.bar(categories, views_by_category)

# Add a title and labels to the plot
plt.title("Number of Views by Category")
plt.xlabel("Category")
plt.ylabel("Number of Views")

# Customize x-axis labels
category_labels = [
    "Autos & Vehicles", "Comedy", "Entertainment",
    "Film & Animation", "Gadgets & Games", "Howto & DIY",
    "Music", "News & Politics", "People & Blogs",
    "Pets & Animals", "Sports", "Travel & Places"
]
plt.xticks(range(len(category_labels)), category_labels, rotation=90)

# Show the plot
plt.show()