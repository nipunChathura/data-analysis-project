import pandas as pd

file_path = "dataset/healthcare_dataset.csv"
df = pd.read_csv(file_path)
header = df.columns.tolist()

df = df.drop_duplicates(subset=['Name', 'Doctor', 'Hospital'])

df = df.reset_index(drop=True)

new_file_path = "dataset/cleaned_healthcare_dataset.csv"
df.to_csv(new_file_path, index=False)
