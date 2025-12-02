import sqlite3
import pandas as pd

# Load cleaned CSV
df = pd.read_csv("smmh_clean.csv")

# Connect to SQLite (creates db if not exists)
conn = sqlite3.connect("mental_health.db")
cur = conn.cursor()

# Save dataframe to SQL table
df.to_sql("mental_health", conn, if_exists="replace", index=False)

# Example SQL queries
print("\nAverage mental health score by age group:")
query1 = """
SELECT 
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        ELSE '46+'
    END AS age_group,
    AVG(mh_score) AS avg_mh_score
FROM mental_health
GROUP BY age_group
"""
print(pd.read_sql(query1, conn))

print("\nHigh risk counts by gender:")
query2 = "SELECT Gender, SUM(high_risk) AS high_risk_count, COUNT(*) AS total FROM mental_health GROUP BY Gender"
print(pd.read_sql(query2, conn))

print("\nAverage daily screen time by high risk:")
query3 = "SELECT high_risk, AVG(\"Daily_Screen_Time(hrs)\") AS avg_screen_time FROM mental_health GROUP BY high_risk"
print(pd.read_sql(query3, conn))

print("\nAverage by social media platform:")
query4 = """
SELECT 
    Social_Media_Platform,
    AVG("Stress_Level(1-10)") AS avg_stress,
    AVG("Happiness_Index(1-10)") AS avg_happiness,
    AVG("Daily_Screen_Time(hrs)") AS avg_screen_time
FROM mental_health
GROUP BY Social_Media_Platform
"""
print(pd.read_sql(query4, conn))


# Close connection
conn.close()