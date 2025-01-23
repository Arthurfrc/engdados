import pandas as pd

file_path = '../data/wine_data.csv'

df = pd.read_csv(file_path)

column_means = df.mean()
print("Média das colunas:")
print(column_means)

df.to_csv('../data/processed_file.csv', index=False)