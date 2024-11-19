import pandas as pd
import numpy as np

# adding a new column 
df = pd.read_csv(r'HackUTD-2024\combinedDataset.csv')
print(df.head)
df['Deviation'] = (df['Inj Gas Meter Volume Setpoint'] -
                   df['Inj Gas Meter Volume Instantaneous']) / df['Inj Gas Meter Volume Setpoint']
print(df)

df.to_csv(r'HackUTD-2024\combinedDataset.csv', index=False)
