import pandas as pd

# Membaca dataset
data = pd.read_csv('package_tourism.csv')

# 1. Menghapus duplikasi
data.drop_duplicates(inplace=True)

# 2. Menghapus kolom yang tidak relevan (misal kolom kosong)
data.dropna(axis=1, how='all', inplace=True)

# 3. Mengatasi missing values
# Mengisi missing values dengan metode yang relevan (misal, dengan nilai sebelumnya)
data.fillna(method='ffill', inplace=True)

# Atau jika ingin menghapus baris yang memiliki missing values
# data.dropna(inplace=True)

# Menyimpan dataset yang sudah diproses
data.to_csv('prepocessing_output.csv', index=False)

print("Preprocessing selesai. Dataset telah dibersihkan dan disimpan.")