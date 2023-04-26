import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Load the cleaned data into a pandas DataFrame
cleaned_data_path = r"C:\Users\deonl\Desktop\cleaned_data.csv"
data = pd.read_csv(cleaned_data_path, encoding='ISO-8859-1')

# Select the features and target
feature_columns = ["ratings", "rate", "comments"]
X = data[feature_columns]
y = data["views"]

# Standardize the features
scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=feature_columns)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNeighborsRegressor using the training data
k = 5  # Choose the number of neighbors
model = KNeighborsRegressor(n_neighbors=k)
model.fit(X_train, y_train)

# Predict the views on the test set and evaluate the model
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print("R-squared score:", r2)
print("Mean Squared Error:", mse)