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
X = pd.DataFrame(scaler.fit_transform(X), columns=feature_columns)

# Train the KNeighborsRegressor using the entire data
k = 5  # Choose the number of neighbors
model = KNeighborsRegressor(n_neighbors=k)
model.fit(X, y)

def predict_views():
    try:
        ratings = int(ratings_entry.get())
        rate = float(rate_entry.get())
        comments = int(comments_entry.get())
        # length = int(length_entry.get())  # Add an input for length
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for ratings, comments, and length, and a valid float for rate.")
        return

    new_data = pd.DataFrame({"ratings": [ratings], "rate": [rate], "comments": [comments]})
    new_data = scaler.transform(new_data)
    new_data = pd.DataFrame(new_data, columns=feature_columns)

    predicted_views = model.predict(new_data)
    messagebox.showinfo("Predicted Views", f"Predicted views for new data point: {predicted_views[0]:.2f}")

# Create a basic tkinter window
root = tk.Tk()
root.title("Miss Cleos YouTube Predictor")
root.geometry("400x500")
root.minsize(400, 500)
root.configure(bg="#F0F2F5")

# Add the "Call me now!" label at the top
top_label = tk.Label(root, text="Call me now!", bg="#F0F2F5", font=("Segoe UI", 16, "bold"))
top_label.grid(row=0, column=0, pady=(10, 20), sticky=tk.NSEW)

# Load and display the image
response = requests.get("https://fox59.com/wp-content/uploads/sites/21/2016/07/miss-cleo-3.jpg")
img_data = response.content
img = Image.open(BytesIO(img_data))
img = img.resize((360, 240), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

image_label = tk.Label(root, image=img, bg="#F0F2F5")
image_label.grid(row=1, column=0, pady=(20, 30))

# Create labels and entry widgets for input
ratings_label = tk.Label(root, text="Ratings:", bg="#F0F2F5", font=("Segoe UI", 12))
ratings_entry = tk.Entry(root, font=("Segoe UI", 12), bg="#E9EBEE")
rate_label = tk.Label(root, text="Rate:", bg="#F0F2F5", font=("Segoe UI", 12))
rate_entry = tk.Entry(root, font=("Segoe UI", 12), bg="#E9EBEE")
comments_label = tk.Label(root, text="Comments:", bg="#F0F2F5", font=("Segoe UI", 12))
comments_entry = tk.Entry(root, font=("Segoe UI", 12), bg="#E9EBEE")
# length_label = tk.Label(root, text="Length:", bg="#F0F2F5", font=("Segoe UI", 12))  # Add a label for length
# length_entry = tk.Entry(root, font=("Segoe UI", 12), bg="#E9EBEE")  # Add an entry for length

predict_button = tk.Button(root, text="Predict Views", command=predict_views, bg="#6200EE", fg="white", font=("Segoe UI", 14), padx=10, pady=5)

image_label.grid(row=1, column=0, pady=(20, 30))

# Set the grid weights
for i in range(10):
    root.rowconfigure(i, weight=1)
root.columnconfigure(0, weight=1)

# Change the layout to use the grid geometry manager
ratings_label.grid(row=2, column=0, pady=3, sticky=tk.W)
ratings_entry.grid(row=3, column=0, pady=3, padx=3, ipady=5, sticky=tk.EW)
rate_label.grid(row=4, column=0, pady=3, sticky=tk.W)
rate_entry.grid(row=5, column=0, pady=3, padx=3, ipady=5, sticky=tk.EW)
comments_label.grid(row=6, column=0, pady=3, sticky=tk.W)
comments_entry.grid(row=7, column=0, pady=3, padx=3, ipady=5, sticky=tk.EW)
# length_label.grid(row=8, column=0, pady=3, sticky=tk.W) # Add length label to the window
# length_entry.grid(row=9, column=0, pady=3, padx=3, ipady=5, sticky=tk.EW) # Add length entry to the window
predict_button.grid(row=10, column=0, pady=(20, 1), sticky=tk.EW)

root.mainloop()