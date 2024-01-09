
# aggregate data
import pandas as pd

# Load the data
df = pd.read_csv('data/filtered_data.csv')

# enhancing model accuracy by adding additional features
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Weekday'] = df['Date/Time'].dt.dayofweek  # 0 = Monday, 6 = Sunday
df['IsWeekend'] = df['Weekday'].apply(lambda x: 1 if x >= 5 else 0)  # 1 for weekends, 0 for weekdays
df['Month'] = df['Date/Time'].dt.month

# aggregate data by cluster and hour to find the average demand
aggregate_data = df.groupby(['Cluster', 'Hour', 'IsWeekend', 'Month']).size().reset_index(name='Average_Demand')

print(aggregate_data.head())


# split the data into training and testing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


X = aggregate_data[['Cluster', 'Hour', 'IsWeekend', 'Month']]
Y = aggregate_data['Average_Demand']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)


# train a random forest regressor
regressor = RandomForestRegressor(n_estimators=100, random_state=0)

regressor.fit(X_train, Y_train)

# make predictions
Y_pred = regressor.predict(X_test)

# evaluate the model
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R2 Score: {r2}')
#print(f'predicted values: {Y_pred}')
#print(f'actual values: {Y_test}')

# save the model
from joblib import dump

dump(regressor, 'models/regressor_model.joblib')

# detailed model evaluation
from sklearn.metrics import mean_absolute_error, explained_variance_score

mae = mean_absolute_error(Y_test, Y_pred)
rmse = mean_squared_error(Y_test, Y_pred, squared=False)
explained_variance = explained_variance_score(Y_test, Y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'Root Mean Squared Error: {rmse}')
print(f'Explained Variance Score: {explained_variance}')




