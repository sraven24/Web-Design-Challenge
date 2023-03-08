import pandas as pd

df1 = pd.read_csv('cities.csv')
df1.to_html("data.html")
print("CSV file saved into html file.")