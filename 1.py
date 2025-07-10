import pandas as pd

# Define input and output paths
input_file = "input_1.xlsx"
output_file = "outputofrawdata.csv"

# Columns to keep in the new dataset
columns_to_keep = [
    "Fight ID", "Event Title", "Event Date", "Event Location", "Weight Class",
    "Fighter First Name", "Fighter Last Name", "Height Feet", "Height Inches",
    "Weight Pounds", "Reach Inches", "Stance", "Date of Birth", "odds"
]

try:
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Filter only the required columns and remove duplicate rows
    filtered_df = df[columns_to_keep].drop_duplicates()

    # Save the filtered DataFrame to CSV
    filtered_df.to_csv(output_file, index=False)
    print(f"Successfully processed and saved: {output_file}")

except Exception as e:
    print(f"Error processing file: {e}")
