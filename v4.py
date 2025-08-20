import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- LOAD DATA ---
df = pd.read_csv("fatal-police-shootings-cleaned.csv")

# --- CLEAN & PREP ---
df['incident_date'] = pd.to_datetime(df['incident_date'], errors='coerce')
df['incident_year'] = df['incident_date'].dt.year
df['incident_month'] = df['incident_date'].dt.month_name()
df['incident_weekday'] = df['incident_date'].dt.day_name()

# --- OVERVIEW ---
print(f"Dataset Shape: {df.shape}")
print(f"Date Range: {df['incident_date'].min().date()} to {df['incident_date'].max().date()}")
print(f"Total Incidents: {len(df)}")

# --- POPULATION DATA (US Census 2020 approx, in millions) ---
us_pop_by_race = {
    'W': 197,   # White
    'B': 42,    # Black
    'H': 63,    # Hispanic/Latino
    'A': 20,    # Asian
    'N': 4,     # Native American
    'O': 10     # Other / multiracial
}

# Killings per race per million population
race_counts = df['race'].value_counts()
rate_per_million = (race_counts / pd.Series(us_pop_by_race) * 1_000_000).dropna()

# Plot rate per million (fixed palette warning)
plt.figure(figsize=(8, 5))
sns.barplot(x=rate_per_million.index, y=rate_per_million.values, hue=rate_per_million.index, palette="coolwarm", legend=False)
plt.title("Police Shootings per Million People by Race")
plt.xlabel("Race")
plt.ylabel("Incidents per Million")
plt.tight_layout()
plt.show()

# --- YEARLY TREND ---
plt.figure(figsize=(8, 5))
df['incident_year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Shootings per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# --- WEEKDAY TREND by Race ---
plt.figure(figsize=(10, 6))
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(
    data=df,
    x='incident_weekday',
    order=order,
    hue='race',
    palette='Set2'  # Different colors for each race
)
plt.title('Shootings by Day of Week and Race')
plt.xlabel('Day')
plt.ylabel('Count')
plt.legend(title='Race')
plt.tight_layout()
plt.show()


# --- AGE DISTRIBUTION ---
plt.figure(figsize=(8, 5))
sns.histplot(df['age'], bins=20, kde=False, color='orange')
plt.title('Age Distribution of Victims')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# --- GENDER DISTRIBUTION ---
plt.figure(figsize=(5, 5))
df['gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'])
plt.title('Gender Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()

# --- TOP STATES WITH RACE DISTRIBUTION ---
plt.figure(figsize=(12, 6))
top_states = df['state'].value_counts().head(10).index
sns.countplot(
    data=df[df['state'].isin(top_states)],
    x='state',
    order=top_states,
    hue='race',  # Different colors for each race
    palette="tab10"  # Or "Set2", "Paired" etc.
)
plt.title('Top 10 States by Shootings (Race Distribution)')
plt.xlabel('State')
plt.ylabel('Number of Shootings')
plt.legend(title='Race')
plt.tight_layout()
plt.show()

# --- MENTAL ILLNESS FLAG ---
plt.figure(figsize=(5, 5))
df['signs_of_mental_illness'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
plt.title('Victims with Signs of Mental Illness')
plt.ylabel('')
plt.tight_layout()
plt.show()

# --- CORRELATION HEATMAP ---
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()


