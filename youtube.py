import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
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
X = scaler.fit_transform(X)

# Train the KNeighborsRegressor using the entire data
k = 1000  # Choose the number of neighbors
model = KNeighborsRegressor(n_neighbors=k)
model.fit(X, y)

def predict_views():
    try:
        ratings = int(ratings_entry.get())
        rate = float(rate_entry.get())
        comments = int(comments_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for ratings, a valid float for rate, and a valid integer for comments.")
        return

    new_data = pd.DataFrame({"ratings": [ratings], "rate": [rate], "comments": [comments]})
    new_data = new_data.to_numpy()
    new_data = scaler.transform(new_data)

    predicted_views = model.predict(new_data)
    messagebox.showinfo("Predicted Views", f"Predicted views for new data point: {predicted_views[0]:.2f}")

# Create a basic tkinter window
root = tk.Tk()
root.title("Miss Cleos YouTube Predictor")
root.geometry("300x350")
root.configure(bg="#E8E8E8")

# Load and display the image
response = requests.get("https://fox59.com/wp-content/uploads/sites/21/2016/07/miss-cleo-3.jpg")
img_data = response.content
img = Image.open(BytesIO(img_data))
img = img.resize((280, 120), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

image_label = tk.Label(root, image=img)
image_label.pack(pady=(10, 20))

# Create labels and entry widgets for input
ratings_label = tk.Label(root, text="Ratings:", bg="#E8E8E8")
ratings_entry = tk.Entry(root)
rate_label = tk.Label(root, text="Rate:", bg="#E8E8E8")
rate_entry = tk.Entry(root)
comments_label = tk.Label(root, text="Comments:", bg="#E8E8E8")
comments_entry = tk.Entry(root)

# Create a button for prediction
predict_button = tk.Button(root, text="Predict Views", command=predict_views, bg="#4F8A8B", fg="white")

# Add widgets to the window
ratings_label.pack()
ratings_entry.pack()
rate_label.pack()
rate_entry.pack()
comments_label.pack()
comments_entry.pack()
predict_button.pack(pady=(20, 10))

# Run the tkinter main loop
root.mainloop()