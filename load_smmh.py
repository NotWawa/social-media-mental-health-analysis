import pandas as pd

# Load the dataset
df = pd.read_csv("social_media_and_mental_health_balance.csv")

# Quick look
print("First 5 rows:")
print(df.head())

# Drop rows with missing values
df = df.dropna()

# Columns to use for mental health score
mh_columns = ['Stress_Level(1-10)', 'Sleep_Quality(1-10)', 'Happiness_Index(1-10)', 'Daily_Screen_Time(hrs)']

# Make sure they are numeric
for col in mh_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Create a simple mental health score
# Example: higher stress + more screen time → higher risk, higher sleep & happiness → lower risk
df['mh_score'] = df['Stress_Level(1-10)'] + df['Daily_Screen_Time(hrs)'] - df['Sleep_Quality(1-10)'] - df['Happiness_Index(1-10)']

# Create a binary column for high risk (you can adjust the threshold)
df['high_risk'] = (df['mh_score'] > df['mh_score'].median()).astype(int)

# Save cleaned CSV
df.to_csv("smmh_clean.csv", index=False)
print("\nCleaned CSV saved as 'smmh_clean.csv'")

# Optional summary
print("\nMental health score stats:")
print(df['mh_score'].describe())
print("\nCounts of high risk:")
print(df['high_risk'].value_counts())
