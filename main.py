import pandas as pd

# --- File path ---
file_path = "dataset/healthcare_dataset.csv"

# --- Load dataset ---
df = pd.read_csv(file_path)

# 01. --- Remove duplicates based on specific columns ---
# df = df.drop_duplicates()
df = df.drop_duplicates(subset=['Name', 'Doctor', 'Hospital'], keep='first')

drop_duplicate_file_path = "dataset/cleaned_duplicate_healthcare_dataset.csv"
df.to_csv(drop_duplicate_file_path, index=False)
print("✅ Cleaned dataset saved successfully after removing duplicates")


# 02. --- Remove missing (NaN) values ---
# df = df.dropna()
df = df.dropna(subset=['Name', 'Doctor', 'Hospital'])

drop_missing_value_file_path = "dataset/cleaned_missing_value_healthcare_dataset.csv"
df.to_csv(drop_missing_value_file_path, index=False)
print("✅ Cleaned dataset saved successfully after missing values.")