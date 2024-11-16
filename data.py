import pandas as pd

df = pd.read_csv(r'data\Resolute_728H-10_14-10_21.csv')
df['Inj Gas Meter Volume Setpoint'] = 1455.0
print(df.head)
print(df['Inj Gas Meter Volume Setpoint'].nunique())
df.to_csv(r'data\Resolute_728H-10_14-10_21.csv', index=False)