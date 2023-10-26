import pandas as pd
import numpy as np

df = pd.read_csv('data/demographic/demographic_CA.csv')

# delete unnecessary columns
del df['lastpage. Last page']
del df['FCV, BEV Dummy']
del df['Month Year[subm...Date submitted]']

# Renmae columns
df = df.rename(columns={'id. Response ID': 'Id'})
df = df.rename(columns={'submitdate. Date submitted': 'Submit Date'})
df = df.rename(columns={'Month[Month Yea...ate submitted]]': 'Submit Month'})
df = df.rename(columns={'Year[Month Year...ate submitted]]': 'Submit Year'})
df = df.rename(columns={'Gender (Male 1)': 'Gender'})

# Columns
# Id
# Submit Date
# Submit Month
# Submit Year
# Carmain
# Previous PHEVs
# Previous BEVs
# Previous HEVs
# Previous CNGs
# Household Income
# Importance of reducing greenhouse gas emissions (-3 not important, 3 important)
# Home ownership (own 1)
# Home Type (detached 1)
# Highest Level of Education
# Longest trip in the last 12 months
# Number of trips over 200 miles in the last 12 months
# One-way commute distance
# Number of people in the household
# Age
# Gender
# Number of vehicles in the household
# Annual VMT Estimate 

# Delete if the submit date is empty
df = df.dropna(subset=['Submit Date'])
df = df.reset_index(drop=True)

# Replace empty cells with NaN
df = df.replace('', np.nan)
df['Gender'] = df['Gender'].replace(0, 'Female')
df['Gender'] = df['Gender'].replace(1, 'Male')

# Sort by date
df = df.sort_values(by='Submit Date')

average_by_age = df.groupby('Submit Year')['Age'].mean()
print(average_by_age)
average_by_age = df.groupby('Submit Year')['Gender'].value_counts()
print(average_by_age)
average_by_income = df.groupby('Submit Year')['Household Income'].mean()
print(average_by_income)


# Export to a CSV file
# df.to_csv('demographic_CA_updated.csv', index=False, float_format='%.0f')