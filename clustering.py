import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import folium
from folium.plugins import HeatMap

# Load the structured data
df = pd.read_csv('data\structured_data.csv')

# quantile extreme outlier removal
lower_bound_lat = df['Lat'].quantile(0.001)  
upper_bound_lat = df['Lat'].quantile(0.999)  

lower_bound_lon = df['Lon'].quantile(0.001)  
upper_bound_lon = df['Lon'].quantile(0.999)  

# Filter the dataframe based on the boundaries
filtered_df = df[
    (df['Lat'] > lower_bound_lat) & 
    (df['Lat'] < upper_bound_lat) & 
    (df['Lon'] > lower_bound_lon) & 
    (df['Lon'] < upper_bound_lon)
]

print(f"Original data: {len(df)} rows")
print(f"Data after outlier removal: {len(filtered_df)} rows")


"""  # find the optimal number of clusters
wcss = []

# Let's check for up to 15 clusters
for i in range(1, 16):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(filtered_df[['Lat', 'Lon']])
    wcss.append(kmeans.inertia_)

# Plotting the results on a graph
plt.figure(figsize=(10,5))
plt.plot(range(1, 16), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Sum of Squares in cluster')
plt.show()
 """

 # Using KMeans for clustering
kmeans = KMeans(n_clusters=6, n_init=10)

filtered_df['Cluster'] = kmeans.fit_predict(filtered_df[['Lat', 'Lon']])

# Visualizing the clusters on a scatter plot
plt.figure(figsize=(12, 10))
plt.scatter(filtered_df['Lon'], filtered_df['Lat'], c=filtered_df['Cluster'], cmap='rainbow')
plt.title('K-Means Clustering of Taxi Pickups')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show() 

# save new dataset
filtered_df.to_csv('filtered_data.csv', index=False)