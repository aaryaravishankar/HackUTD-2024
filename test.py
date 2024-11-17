import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

# df = pd.read_csv(r'HackUTD-2024\data\Bold_744H-10_31-11_07.csv')
# df['Inj Gas Valve Percent Open'].fillna(method='ffill', inplace=True)

# df2 = pd.read_csv(r'HackUTD-2024\data\Courageous_729H-09_25-09_28.csv')
# df2['Inj Gas Valve Percent Open'].fillna(method='ffill', inplace=True)

# df3 = pd.read_csv(r'HackUTD-2024\data\Fearless_709H-10_31-11_07.csv')
# df3['Inj Gas Valve Percent Open'].fillna(method='ffill', inplace=True)


# # df 1 - bold
# plt.figure(figsize=(10, 6))
# plt.plot(df['Time'], df['Inj Gas Meter Volume Instantaneous'],
#          label='Inj Gas Meter Volume Instantaneous')
# plt.plot(df['Time'], df['Inj Gas Meter Volume Setpoint'],
#          label='Inj Gas Meter Volume Setpoint')
# plt.plot(df['Time'], df['Inj Gas Valve Percent Open'],
#          label='Inj Gas Valve Percent Open')
# plt.xlabel('Time')
# plt.ylabel('Values')
# plt.legend()
# plt.title('Time Series of Gas Meter Volume and Valve Percent Open')
# plt.xticks(rotation=45)
# plt.tight_layout()


# # df - 2 courageous
# plt.figure(figsize=(10, 6))
# plt.plot(df2['Time'], df2['Inj Gas Meter Volume Instantaneous'],
#          label='Inj Gas Meter Volume Instantaneous')
# plt.plot(df2['Time'], df2['Inj Gas Meter Volume Setpoint'],
#          label='Inj Gas Meter Volume Setpoint')
# plt.plot(df2['Time'], df2['Inj Gas Valve Percent Open'],
#          label='Inj Gas Valve Percent Open')
# plt.xlabel('Time')
# plt.ylabel('Values')
# plt.legend()
# plt.title('Time Series of Gas Meter Volume and Valve Percent Open')
# plt.xticks(rotation=45)
# plt.tight_layout()


# # df 3 - fearless
# plt.figure(figsize=(10, 6))
# plt.plot(df3['Time'], df3['Inj Gas Meter Volume Instantaneous'],
#          label='Inj Gas Meter Volume Instantaneous')
# plt.plot(df3['Time'], df3['Inj Gas Meter Volume Setpoint'],
#          label='Inj Gas Meter Volume Setpoint')
# plt.plot(df3['Time'], df3['Inj Gas Valve Percent Open'],
#          label='Inj Gas Valve Percent Open')
# plt.xlabel('Time')
# plt.ylabel('Values')
# plt.legend()
# plt.title('Time Series of Gas Meter Volume and Valve Percent Open')
# plt.xticks(rotation=45)
# plt.tight_layout()



# List of CSV filenames 
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

# Number of files to plot
num_files = len(csv_files)

# Create subplots: Arrange 3 rows and 3 columns (you can adjust this as needed)
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))

# Flatten the axes array to easily iterate through subplots
axes = axes.flatten()

# Loop through each file and plot its data in a separate subplot
for i, file_name in enumerate(csv_files):
    # Read the CSV file
    df = pd.read_csv(file_name)
    df['Inj Gas Valve Percent Open'].fillna(method='ffill', inplace=True)

    # Plot the data on the corresponding subplot (axes[i])
    axes[i].plot(df['Time'], df['Inj Gas Meter Volume Instantaneous'],
                 label='Volume Instantaneous', linestyle='-', alpha=0.7)
    
    axes[i].plot(df['Time'], df['Inj Gas Valve Percent Open'],
                 label='Valve Percent Open', linestyle=':', alpha=0.7)

    # Set titles and labels for each subplot
    axes[i].set_title(f'{file_name}')
    axes[i].set_xlabel('Time')
    axes[i].set_ylabel('Values')
    axes[i].legend()

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()
