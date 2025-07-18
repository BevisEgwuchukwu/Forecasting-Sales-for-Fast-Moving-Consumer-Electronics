import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)

df = pd.read_csv(
    '/Users/macintosh/Desktop/Forecasting-Sales-for-Fast-Moving-Consumer-Electronics/DataCleaning/ElectroTech Forecasting Data.csv'
    )

df.head(5)

df['Category'].value_counts()

print(f"{df.isnull().sum()}\n")
print(f"{df.duplicated().sum()}\n")
print(f"{df.dtypes}\n")

df['Date'] = df['Date'].astype('datetime64[ns]')

outlier_columns = df.select_dtypes(exclude=['object', 'datetime']).iloc[0:, 1:].columns.to_list()

for columns in outlier_columns: 
    plt.boxplot(df[columns])
    plt.title(columns)
    plt.show()
outlier_columns = df.select_dtypes(exclude=['object', 'datetime']).iloc[0:, 1:].columns.to_list()

for columns in outlier_columns: 
    q1 = df[columns].quantile(0.25)
    q3 = df[columns].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df[columns]=np.where(df[columns]< lower_bound, lower_bound, df[columns])
    df[columns]=np.where(df[columns]> upper_bound, upper_bound, df[columns])