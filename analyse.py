import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
file = 'fatal-police-shootings-data.csv'
df = pd.read_csv(file)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows where date is NaT
df = df.dropna(subset=['date'])





# Extract year and month
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.to_period('M')

# Basic info
print("Dataset Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())

# Gender & Race Distribution
plt.figure(figsize=(10, 4))
sns.countplot(data=df, x='gender', hue='race', palette='Set2')
plt.title('Gender and Race Distribution')
plt.savefig("gender_race_distribution.png")
plt.close()

# Age Distribution
plt.figure(figsize=(10, 4))
sns.histplot(df['age'].dropna(), kde=True, bins=30)
plt.title("Age Distribution")
plt.savefig("age_distribution.png")
plt.close()

# Armed Status Count
plt.figure(figsize=(12, 4))
df['armed'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Weapons/Status")
plt.ylabel("Count")
plt.savefig("armed_status.png")
plt.close()

# Signs of Mental Illness
mental_illness_count = df['signs_of_mental_illness'].value_counts()
print("\nMental Illness Counts:\n", mental_illness_count)

# Flee vs Threat Level
pivot = pd.crosstab(df['flee'], df['threat_level'])
print("\nFlee vs Threat Level:\n", pivot)

# Monthly Incident Trend
monthly = df.groupby('month').size()
monthly.plot(figsize=(12, 5), title="Monthly Incidents")
plt.ylabel("Count")
plt.savefig("monthly_incidents.png")
plt.close()

# Top States
state_counts = df['state'].value_counts().head(10)
state_counts.plot(kind='barh', title='Top 10 States with Most Cases', color='tomato')
plt.xlabel("Count")
plt.savefig("top_states.png")
plt.close()

# Map Visualization
map_df = df.dropna(subset=['latitude', 'longitude'])
fig = px.scatter_mapbox(map_df,
                        lat="latitude",
                        lon="longitude",
                        hover_name="name",
                        color="race",
                        zoom=3,
                        height=500)
fig.update_layout(mapbox_style="open-street-map", title="Fatal Police Shootings (Map)")
fig.write_html("map.html")

# Correlation Matrix
num_df = df[['age', 'longitude', 'latitude']].dropna()
corr = num_df.corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix.png")
plt.close()

print("\nAnalysis complete. Graphs and map saved.")

# Body Camera Usage Pie
bodycam_counts = df['body_camera'].value_counts()
print("\nBody Camera Usage:\n", bodycam_counts)

plt.figure(figsize=(6, 6))
bodycam_counts.plot.pie(
    labels=['No Body Camera', 'Body Camera'] if False in bodycam_counts.index else ['Body Camera', 'No Body Camera'],
    autopct='%1.1f%%',
    startangle=90,
    colors=['#FF9999','#99CCFF']
)
plt.title("Deaths With vs Without Body Cameras")
plt.ylabel("")
plt.savefig("body_camera_pie.png")
plt.close()

# 🔍 Year-wise deaths with and without body cameras
year_bodycam = df.groupby(['year', 'body_camera']).size().unstack(fill_value=0)

# Bar plot
year_bodycam.plot(kind='bar', stacked=True, figsize=(12, 6), color=['#FF9999', '#99CCFF'])
plt.title("Year-wise Fatal Shootings: With vs Without Body Cameras")
plt.ylabel("Number of Fatalities")
plt.xlabel("Year")
plt.legend(['No Body Camera', 'Body Camera'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("yearwise_bodycam.png")
plt.close()

print("\nYear-wise body camera analysis saved as 'yearwise_bodycam.png'")
