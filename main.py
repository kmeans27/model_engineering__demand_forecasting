import pandas as pd

# List of files
files = ['data\data-apr14.csv', 'data\data-may14.csv', 'data\data-jun14.csv', 'data\data-jul14.csv', 'data\data-aug14.csv', 'data\data-sep14.csv']

# Combine all files into a single dataframe
#df = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)
#df.to_csv('combined_data.csv', index=False)


df = pd.read_csv('data/combined_data.csv')
print(df.head())

# bring data into correct structure
# Convert 'Date/Time' column to datetime format
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Extract components
df['Day'] = df['Date/Time'].dt.day
df['Weekday'] = df['Date/Time'].dt.day_name()
df['Month'] = df['Date/Time'].dt.month_name()
df['Year'] = df['Date/Time'].dt.year
df['Time'] = df['Date/Time'].dt.time

# Convert the 'Time' column to a datetime format
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time

# Extract hour from the Time column
df['Hour'] = df['Time'].apply(lambda x: x.hour)

# Extract minute from the Time column
df['Minute'] = df['Time'].apply(lambda x: x.minute)

# Reorder columns
df = df[['Date/Time', 'Day', 'Weekday', 'Month', 'Year', 'Time','Hour', 'Minute', 'Lat', 'Lon', 'Base']]
print(df.head())
df.to_csv('data/structured_data.csv', index=False)



