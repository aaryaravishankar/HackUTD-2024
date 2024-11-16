import os
import pandas as pd


# Valiant dataframe 
dfValiant = pd.read_csv(r'HackUTD-2024\data\Valiant_505H-09_22-09_30.csv')
dfValiant['Inj Gas Meter Volume Setpoint'].fillna(910.5, inplace=True)
dfValiant.to_csv(r'HackUTD-2024\data\Valiant_505H-09_22-09_30.csv', index=False)
print(dfValiant)

#SteadFast
dfSteadfast = pd.read_csv(r'HackUTD-2024\data\Steadfast_505H-10_30-11_07.csv')
dfSteadfast['Inj Gas Meter Volume Setpoint'].fillna(1800.0, inplace=True)
dfSteadfast.to_csv(r'HackUTD-2024\data\Steadfast_505H-10_30-11_07.csv', index=False)
print(dfSteadfast)

#Ruthless
dfRuthless = pd.read_csv(r'HackUTD-2024\data\Ruthless_745H-10_01-10_08.csv')
dfRuthless['Inj Gas Meter Volume Setpoint'].fillna(1350.0, inplace=True)
dfRuthless.to_csv(r'HackUTD-2024\data\Ruthless_745H-10_01-10_08.csv', index=False)
print(dfRuthless)


# Check current working directory
print("Current Working Directory:", os.getcwd())

# List of CSV filenames in the 'data' folder
csv_files = [
    r'HackUTD-2024\data\Bold_744H-10_31-11_07.csv',
    r'HackUTD-2024\data\Courageous_729H-09_25-09_28.csv',
    r'HackUTD-2024\data\Fearless_709H-10_31-11_07.csv',
    r'HackUTD-2024\data\Gallant_102H-10_04-10_11.csv',
    r'HackUTD-2024\data\Noble_4H-10_24-10_29.csv',
    r'HackUTD-2024\data\Resolute_728H-10_14-10_21.csv',
    r'HackUTD-2024\data\Ruthless_745H-10_01-10_08.csv',
    r'HackUTD-2024\data\Steadfast_505H-10_30-11_07.csv',
    r'HackUTD-2024\data\Valiant_505H-09_22-09_30.csv'
]


# Read each CSV file into a dataframe
dataframes = [pd.read_csv(file) for file in csv_files]

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Display the combined DataFrame
print(combined_df)

# making a new csv file for the data 
combined_df.to_csv(r'combinedDataset.csv', index=False)
