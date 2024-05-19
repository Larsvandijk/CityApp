import pandas as pd

populationThreshold = 5000

# Read the CSV file
df = pd.read_csv('CityData.csv', delimiter=';')

# Remove the specified columns
columns_to_remove = ['Admin1 Code', 'Admin2 Code', 'Admin3 Code', 'Admin4 Code']
df = df.drop(columns=columns_to_remove)

# Remove records where the population is less than 5000
df = df[df['Population'] >= populationThreshold]

# Save the modified DataFrame back to a CSV file
df.to_csv('CityDate_cleaned.csv', index=False)
