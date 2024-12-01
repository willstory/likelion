import pandas as pd
from pandas import Series, DataFrame

df_csv = pd.read_csv('example.csv')

print("CSV 파일 읽기")
print(df_csv)
print("---------------------")

df_excel = pd.read_excel('example.xlsx')

print("\\엑셀 파일 데이터")
print(df_excel)
print("---------------------")


data = [
    ['Alice', 85],
    ['Bob', 90],
    ['Charlie', 88]
]

df = pd.DataFrame(data, columns=['name', 'score'])
print(df)