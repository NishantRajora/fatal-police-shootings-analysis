import pandas as pd

# Load the CSV file
df = pd.read_csv("fatal-police-shootings-data.csv")

# Drop rows with missing values and create a full copy
df_cleaned = df.dropna().copy()

# Standardize column names
df_cleaned.columns = [col.replace('.', '_').lower() for col in df_cleaned.columns]

# Drop 'id' column if it exists
if 'id' in df_cleaned.columns:
    df_cleaned.drop(columns=['id'], inplace=True)

# Convert 'date' to datetime and rename it to 'incident_date'
df_cleaned['incident_date'] = pd.to_datetime(df_cleaned['date'], errors='coerce')

# Drop original 'date' column after conversion
df_cleaned.drop(columns=['date'], inplace=True)

# Drop rows with invalid or missing date
df_cleaned.dropna(subset=["incident_date"], inplace=True)

# Derive new date-related columns
df_cleaned["incident_year"] = df_cleaned["incident_date"].dt.year
df_cleaned["incident_month"] = df_cleaned["incident_date"].dt.month
df_cleaned["incident_day"] = df_cleaned["incident_date"].dt.day
df_cleaned["incident_weekday"] = df_cleaned["incident_date"].dt.day_name()

# Save final cleaned file
df_cleaned.to_csv("fatal-police-shootings-cleaned.csv", index=False)

print("Cleaned data with reference 'incident_date' column saved as 'fatal-police-shootings-cleaned.csv'")
