# -*- coding: utf-8 -*-
"""Air Quality

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ETALvJ5t6jQRg6bSjt5FdR69hAJIaxFp
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Sample Air Quality Data for Indian Cities
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Sample Air Quality Data for Indian Cities
data = {
    'city' : ['Delhi','Mumbai','Kolkata','Chennai','Banglore','Hyderabad','Pune','Ahmedabad','Jaipur','Lucknow'],
    'date' : pd.to_datetime(['23-01-2025','23-01-2025','23-01-2025','23-01-2025','23-01-2025','23-01-2025','23-01-2025','23-01-2025','23-01-2025','23-01-2025']),
    'pm2.5' :[257, 134, 235, 93, 86, 96, 158, 111, 123, 213 ],
    'no2' : [80,50,60,40,30,70,45,65,90,55],
    'so2' : [30, 20, 25, 15, 10, 25, 18, 28, 35, 22 ],
    }

air_quality_df = pd.DataFrame(data)

# 1. Basic Data Exploration
print(air_quality_df.head())
print(air_quality_df.info())

# 2.PM2.5 Anaysis
average_pm2_5 = air_quality_df['pm2.5'].mean()
print("\nAverage PM2.5 across cities:", average_pm2_5)

# 3. City with Highest NO2 Levels
city_with_highest_no2 = air_quality_df.loc[air_quality_df['no2'].idxmax(), 'city']
print("\nCity with the highest NO2 level:", city_with_highest_no2)

# 4. Correlation between Pollutants
correlation_pm25_no2 = air_quality_df['pm2.5'].corr(air_quality_df['no2'])
print("\nCorrelation between PM2.5 and NO2:", correlation_pm25_no2)

# 1. Bar Chart of PM2.5 Levels by City
plt.figure(figsize=(12, 6))
sns.barplot(x='city', y='pm2.5', data=air_quality_df)
plt.title('PM2.5 Levels by City')
plt.xlabel('City')
plt.ylabel('PM2.5 Level')
plt.xticks(rotation=45)
plt.show()

# 2.Scatter Plot of PM2.5 vs. NO2
plt.figure(figsize=(10, 6))
sns.scatterplot(x='pm2.5', y='no2', data=air_quality_df)
plt.title('PM2.5 vs. NO2 Levels')
plt.xlabel('PM2.5')
plt.ylabel('NO2')
plt.show()