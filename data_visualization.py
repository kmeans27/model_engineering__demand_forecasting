import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.plugins import HeatMap


df = pd.read_csv('data/structured_data.csv')


""" #plot distribution of latitude and longitude
plt.figure(figsize=(10, 8))
plt.scatter(df['Lon'], df['Lat'], s=0.5, alpha=0.5)
plt.title('Distribution of Latitude and Longitude Points')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
 """

""" # plotting the hourly distribution of taxi rides
df['Hour'].value_counts(sort=False).plot(kind='bar', figsize=(12, 6))
plt.title('Hourly Distribution of Taxi Rides')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Rides')
plt.show() """

""" # plotting the weekly distribution of taxi rides
df['Weekday'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).plot(kind='bar', figsize=(12, 6))
plt.title('Weekly Distribution of Taxi Rides')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Rides')
plt.show() """

""" # plotting the monthly distribution of taxi rides
df['Month'].value_counts().reindex(['April', 'May', 'June', 'July', 'August', 'September']).plot(kind='bar', figsize=(12, 6))
plt.title('Monthly Distribution of Taxi Rides')
plt.xlabel('Month of the Year')
plt.ylabel('Number of Rides')
plt.show() """

""" # plotting the distribution of rides among different bases
df['Base'].value_counts().plot(kind='bar', figsize=(12, 6))
plt.title('Distribution of Rides by Base')
plt.xlabel('Base')
plt.ylabel('Number of Rides')
plt.show() """

""" # creating a heatmap
# Create a base map
m = folium.Map(location=[df['Lat'].mean(), df['Lon'].mean()], zoom_start=10)
# Extract the data we need
heat_data = [[row['Lat'], row['Lon']] for index, row in df.iterrows()]
# Add the heatmap to the base map
HeatMap(heat_data).add_to(m)
# Save the map
m.save('maps/heatmap.html')
 """




