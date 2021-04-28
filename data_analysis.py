import pandas as pd

data = pd.read_csv('st.csv')

print(data.head())
print(data['user'].value_counts())
print(data['Trans'].value_counts())