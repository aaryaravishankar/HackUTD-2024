import pandas as pd

df = pd.read_csv(r'combinedDataset.csv')
df['Time'] = pd.to_datetime(df['Time'], format='%m/%d/%Y %I:%M:%S %p')

df['Time Difference (minutes)'] = df['Time'].diff().dt.total_seconds() / 60  # Time difference in minutes

# Calculate rate of change for 'Inj Gas Meter Volume Instantaneous' per minute
df['Rate of Change Volume (per minute)'] = df['Inj Gas Meter Volume Instantaneous'].diff() / df['Time Difference (minutes)']
df.to_csv(r'combinedDataset.csv', index=False)
print(df.head)