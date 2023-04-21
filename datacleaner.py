import os
import pandas as pd
import tempfile

# Function to clean the input file
def clean_file(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            decoded_line = line.decode('utf-8', errors='replace')  # Replace non-UTF-8 characters with the replacement character
            cleaned_line = decoded_line.replace('\ufffd', '')  # Remove the replacement character from the line (optional)
            outfile.write(cleaned_line)

# Set the directory path
dir_path = r"C:\Users\deonl\Desktop\CS 431 Project\0318\0318"

# Define the column names
column_names = [
    "video_id", "uploader", "age", "category", "length",
    "views", "rate", "ratings", "comments"
]

# Add "related_id_X" to the column names for each of the 20 related IDs
for i in range(1, 21):
    column_names.append(f"related_id_{i}")

# Open the output file in append mode
output_path = r"C:\Users\deonl\Desktop\cleaned_data.csv"
with open(output_path, mode="a", newline="") as file:
    # Loop through all the .txt files in the directory
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".txt") and file_name != "log.txt":
            # Create the full file path
            file_path = os.path.join(dir_path, file_name)

            # Create a temporary file to store the cleaned data
            with tempfile.NamedTemporaryFile(delete=False, mode='w+t') as temp_file:
                # Clean the input file and save it to the temporary file
                clean_file(file_path, temp_file.name)

                # Load the cleaned file into a pandas DataFrame with the specified column names
                df = pd.read_csv(temp_file.name, sep="\t", names=column_names)

                # Handle missing values (e.g., fill missing values with mean or median)
                df.fillna(df.mean(), inplace=True)  # You can also use df.dropna() to remove rows with missing values
                # One-hot encoding for the 'category' column (categorical variable)
                df = pd.get_dummies(df, columns=['category'])
                # Drop all related ID columns
                df = df.drop([f"related_id_{i}" for i in range(1, 21)], axis=1)
                # Append the cleaned data to the output file
                df.to_csv(file, index=False, header=not file.tell())

            # Remove the temporary file
            os.remove(temp_file.name)

print(f"Cleaned data saved to: {output_path}")

