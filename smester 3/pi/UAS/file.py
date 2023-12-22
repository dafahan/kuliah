import pandas as pd
import unittest
#Data
data = {
 'Courses': ['Spark', 'Hadoop', 'Pandas', 'Java', 'Pyspark'],
 'Categories': ['DS', 'DS', 'PI', 'PI', 'DS'],
 'Fee': [20000, 25000, 30000, 22000, 26000],
 'Duration': ['30days', '40days', '35days', '60days', '50days'],
 'Percentage Discount': ['5%', '10%', '5%', '5%', '5%']
}
#Membuat DataFrame dari data
df = pd.DataFrame(data)
#Menampilkan DataFrame
print(df)
data_tambahan = {
 'Courses': ['Python', 'SQL', 'JavaScript', 'PHP', 'C++'],
 'Categories': ['DS', 'PI', 'Web', 'Web', 'C++'],
 'Fee': [28000, 23000, 15000, 18000, 20000],
 'Duration': ['45days', '50days', '45days', '50days', '50days'],
 'Percentage Discount': ['8%', '5%', '5%', '7%', '6%']
}
#Menggabungkan data yang sudah ada dengan data tambahan
data_combined = {key: data[key] + data_tambahan[key] for key in
data}
#Membuat DataFrame dari data yang sudah digabungkan
df = pd.DataFrame(data_combined)
print(df)
#Mengonversi Duration ke bentuk numerik (menghapus 'days')
df['Duration'] = df['Duration'].str.replace('days', '').astype(int)
#Mengubah Percentage Discount dari string ke bentuk pecahan
df['Percentage Discount'] = df['Percentage
Discount'].str.rstrip('%').astype(float) / 100
#Fungsi untuk menghitung total berdasarkan kategori
def calculate_total(row):
 if row['Categories'] == 'PI':
 total_discount_2_percent = row['Fee'] * row['Duration'] *
0.02
 return (row['Fee'] * row['Duration']) - (row['Fee'] *
row['Duration'] * row['Percentage Discount']) -
total_discount_2_percent
 else:
 return (row['Fee'] * row['Duration']) - (row['Fee'] *
row['Duration'] * row['Percentage Discount'])
#Menambahkan kolom "Total" ke DataFrame
df['Total'] = df.apply(calculate_total, axis=1)
#Menampilkan DataFrame dengan kolom baru "Total"
print(df)
class StatCalculator:
 def __init__(self, data_frame):
 self.data_frame = data_frame
 def calculate_mean(self, column_name):
 return self.data_frame[column_name].sum() /
len(self.data_frame[column_name])
 def calculate_median(self, column_name):
 sorted_column = sorted(self.data_frame[column_name])
 length = len(sorted_column)
 if length % 2 == 0:
 return (sorted_column[length // 2 - 1] +
sorted_column[length // 2]) / 2
 else:
 return sorted_column[length // 2]
 def calculate_mode(self, column_name):
 return self.data_frame[column_name].mode()[0]
#Data yang sudah diproses sebelumnya
data_combined = {
 'Courses': ['Spark', 'Hadoop', 'Pandas', 'Java', 'Pyspark',
'Python', 'SQL', 'JavaScript', 'PHP', 'C++'],
 'Categories': ['DS', 'DS', 'PI', 'PI', 'DS', 'DS', 'PI', 'Web',
'Web', 'C++'],
 'Fee': [20000, 25000, 30000, 22000, 26000, 28000, 23000, 15000,
18000, 20000],
 'Duration': [30, 40, 35, 60, 50, 45, 50, 45, 50, 50],
 'Percentage Discount': [0.05, 0.1, 0.05, 0.05, 0.05, 0.08, 0.05,
0.05, 0.07, 0.06],
 'Total': [560000, 900000, 945000, 1320000, 1300000, 1260000,
1150000, 675000, 1260000, 1200000]
}
#Membuat DataFrame dari data yang sudah digabungkan
df = pd.DataFrame(data_combined)
#Menghitung mean, median, dan mode untuk kolom 'Fee'
calculator_fee = StatCalculator(df)
df['Fee_Mean'] = calculator_fee.calculate_mean('Fee')
df['Fee_Median'] = calculator_fee.calculate_median('Fee')
df['Fee_Mode'] = calculator_fee.calculate_mode('Fee')
#Menghitung mean, median, dan mode untuk kolom 'Total'
calculator_total = StatCalculator(df)
df['Total_Mean'] = calculator_total.calculate_mean('Total')
df['Total_Median'] = calculator_total.calculate_median('Total')
df['Total_Mode'] = calculator_total.calculate_mode('Total')
#Menampilkan DataFrame dengan kolom baru yang berisi mean, median,
dan mode
print(df)
class StatCalculator:
 def __init__(self, data_frame):
 self.data_frame = data_frame
 def calculate_mean(self, column_name):
 try:
 return self.data_frame[column_name].sum() /
len(self.data_frame[column_name])
 except ZeroDivisionError:
 return None
 def calculate_median(self, column_name):
 try:
 sorted_column = sorted(self.data_frame[column_name])
 length = len(sorted_column)
 if length % 2 == 0:
 return (sorted_column[length // 2 - 1] +
sorted_column[length // 2]) / 2
 else:
 return sorted_column[length // 2]
 except IndexError:
 return None
 def calculate_mode(self, column_name):
 try:
 return self.data_frame[column_name].mode()[0]
 except IndexError:
 return None
class TestStatCalculator(unittest.TestCase):
 def setUp(self):
 # Persiapan DataFrame untuk pengujian
 self.test_data = {
 'Courses': ['Python', 'SQL', 'JavaScript', 'PHP',
'C++'],
 'Categories': ['DS', 'PI', 'Web', 'Web', 'C++'],
 'Fee': [28000, 23000, 15000, 18000, 20000],
 'Duration': [45, 50, 45, 50, 50],
 'Percentage Discount': [0.08, 0.05, 0.05, 0.07, 0.06],
 'Total': [1260000, 1150000, 675000, 1260000, 1200000]
 }
 self.test_df = pd.DataFrame(self.test_data)
 self.calculator = StatCalculator(self.test_df)
 def test_calculate_mean(self):

self.assertAlmostEqual(self.calculator.calculate_mean('Fee'), 20360,
delta=1)
 def test_calculate_median(self):

self.assertEqual(self.calculator.calculate_median('Duration'), 50)
 def test_calculate_mode(self):

self.assertEqual(self.calculator.calculate_mode('Categories'),
'C++')
if __name__ == '__main__':
 #Menjalankan pengujian unit
 unittest.main(argv=[''], exit=False)