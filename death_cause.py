import pandas as pd


df = pd.read_csv('deaths/annual_deaths_numbers.csv')
print(df.head())

# First, we will clean the data by removing any rows with missing values
df_cleaned = df.dropna()

# Next, we will filter Uzbekistan's data
uzbekistan_data = df_cleaned[df_cleaned['Entity'] == 'Uzbekistan']
print(uzbekistan_data)

death_cause_columns = df.columns[df.columns.astype(str).str.startswith('Deaths -')]
print(death_cause_columns) 
print(death_cause_columns[:10])  # Print the first 10 death cause columns

print(uzbekistan_data[death_cause_columns].dtypes)
print(uzbekistan_data[death_cause_columns].head(10))  # Print the first 10 rows of the death cause columns for 

death_cause_columns = df.columns[df.columns.astype(str).str.startswith('Deaths -')] # identify for uzbekistan the columns that start with 'Deaths -'
print(death_cause_columns)  # Print the identified death cause columns
# Now we will convert the identified death cause columns to numeric, coercing errors to NaN
uzbekistan_data[death_cause_columns] = uzbekistan_data[death_cause_columns].apply(pd.to_numeric, errors = 'coerce')
print(uzbekistan_data[death_cause_columns].dtypes) # Print the data types of the death cause columns after conversion
print(uzbekistan_data[death_cause_columns].head(10)) # Print the first 10 rows of the death cause columns after conversion
print(uzbekistan_data.shape)  # Print the shape of the filtered Uzbekistan data
print(uzbekistan_data[death_cause_columns[0]].head())
print(uzbekistan_data[death_cause_columns[0]].sum())
uzbekistan_data = df_cleaned[df_cleaned['Entity'] == 'Uzbekistan']
print(uzbekistan_data)

# let's check if uzbekistan_data is empty
if uzbekistan_data.empty:
    print("No data available for Uzbekistan.")
else:
    print("Data for Uzbekistan is available.")
print(df.shape)  # Print the shape of the original DataFrame
print(df_cleaned.shape)  # Print the shape of the cleaned DataFrame

uzbekistan_data = df[df['Entity'] == 'Uzbekistan']
print(uzbekistan_data)  # Print the shape of the filtered Uzbekistan data
# Now we will calculate the total number of deaths for each cause in Uzbekistan by summing the values in the identified death cause columns
totals = uzbekistan_data[death_cause_columns].sum()
print(totals) # Print the total number of deaths for each cause in Uzbekistan
# Finally, we will identify the top 5 causes of death in Uzbekistan by sorting the totals in descending order and selecting the top 5
top_5_causes = totals.sort_values(ascending = False).head(5)
print(top_5_causes)  # Print the top 5 causes of death in Uzbekistan
# Now we will to know how the number of deaths for each cause has changed over time in Uzbekistan since 1990 and until 2019 and visualize the trends using a line plot
# let's filter the data for the years 1990 to 2019
uzbekistan_data_time_filtered = uzbekistan_data[(uzbekistan_data['Year'] >= 1990) & (uzbekistan_data['Year'] <= 2019)]
print(uzbekistan_data_time_filtered)  # Print the filtered Uzbekistan data for the years 1990 to 2019
import matplotlib.pyplot as plt

# We need to know the changes in the rate of mortality for only the top 5 causes of death in Uzbekistan between 1990 and 2019. 
# We will need to plot line graph
# Let's filter the data for the top 5 causes of death in Uzbekistan and visualize the changes in the rate of mortality for 
# these causes between 1990 and 2019 using a line plot.
top_5_causes_columns = top_5_causes.index
plt.figure(figsize = (12, 6))
for cause in top_5_causes_columns:
    plt.plot(uzbekistan_data_time_filtered['Year'], uzbekistan_data_time_filtered[cause], label = cause)
plt.title('Trends in Top 5 Mortality Causes in Uzbekistan (1990-2019)')
plt.xlabel('Year')
plt.ylabel('Mortality Rate')
plt.legend()
plt.grid()
plt.show()

# Now we will calculate the average number of deaths for each cause in Uzbekistan between 1990 and 2019 and visualize the averages using a bar plot.
average_deaths = uzbekistan_data_time_filtered[top_5_causes_columns].mean()
plt.figure(figsize = (10, 5))
plt.bar(average_deaths.index, average_deaths.values)
plt.title('Average Number of Deaths for Top 5 Causes in Uzbekistan (1990-2019)')
plt.xlabel('Cause of Death')
plt.ylabel('Average Number of Deaths')
plt.xticks(rotation = 45)
plt.grid(axis = 'y')
plt.show() 

# Finally, we will compare the trends in Cardiovascular disease of uzbekistan, france and niger
france_data = df[df['Entity'] == 'France']
france_data_time_filtered = france_data[(france_data['Year'] >= 1990) & (france_data['Year'] <= 2019)]

# Nigeria
niger_data = df[df['Entity'] == 'Niger']
niger_data_time_filtered = niger_data[(niger_data['Year'] >= 1990) & (niger_data['Year'] <= 2019)]

plt.figure(figsize = (12, 6))
plt.plot(uzbekistan_data_time_filtered['Year'], uzbekistan_data_time_filtered['Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)'], label = 'Uzbekistan')
plt.plot(france_data_time_filtered['Year'], france_data_time_filtered['Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)'], label = 'France')
plt.plot(niger_data_time_filtered['Year'], niger_data_time_filtered['Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)'], label = 'Niger')
plt.title('Trends in Cardiovascular Disease Mortality in Uzbekistan, France and Niger (1990-2019)')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.legend()
plt.grid()
plt.show()