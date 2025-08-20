import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("fatal-police-shootings-cleaned.csv")

# Set Seaborn style
sns.set(style="whitegrid", palette="Set2")

# Overview
print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nBasic Description:\n", df.describe(include='all'))

# ---------------- TIME-BASED ANALYSIS ---------------- #

# Yearly trend (Bar Plot)
plt.figure(figsize=(8, 5))
df['incident_year'].value_counts().sort_index().plot(kind='bar')
plt.title('Shootings per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Monthly trend (Pie Chart)
monthly_counts = df['incident_month'].value_counts()
plt.figure(figsize=(8, 8))
monthly_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Shootings per Month')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Weekday trend (Box Plot)
plt.figure(figsize=(8, 5))
sns.boxplot(x='incident_weekday', y='age', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Age Distribution by Weekday')
plt.xlabel('Day')
plt.ylabel('Age')
plt.tight_layout()
plt.show()

# ---------------- DEMOGRAPHIC ANALYSIS ---------------- #

# Gender Distribution (Pie Chart)
gender_counts = df['gender'].value_counts()
plt.figure(figsize=(8, 8))
gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Race Distribution (Box Plot)
plt.figure(figsize=(8, 5))
sns.boxplot(x='race', y='age', data=df)
plt.title('Age Distribution by Race')
plt.xticks(rotation=45)
plt.ylabel('Age')
plt.tight_layout()
plt.show()

# Age Distribution (Histogram)
plt.figure(figsize=(8, 5))
plt.hist(df['age'], bins=20, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Age Groups (Bar Plot)
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 30, 50, 100], labels=['<18', '18-30', '31-50', '50+'])
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='age_group', order=['<18', '18-30', '31-50', '50+'])
plt.title('Age Group Distribution')
plt.show()

# ---------------- INCIDENT DETAILS ---------------- #

# Top 10 weapons (Horizontal Bar Plot)
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='armed', order=df['armed'].value_counts().head(10).index)
plt.title('Top 10 Types of Weapons Used')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Mental illness (Count Plot)
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='signs_of_mental_illness')
plt.title('Mental Illness Flag')
plt.xticks([0, 1], ['False', 'True'])
plt.tight_layout()
plt.show()

# Fleeing (Count Plot)
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='flee', order=df['flee'].value_counts().index)
plt.title('Fleeing Status at Time of Incident')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Body camera usage (Count Plot)
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='body_camera')
plt.title('Body Camera Used')
plt.xticks([0, 1], ['False', 'True'])
plt.tight_layout()
plt.show()

# ---------------- LOCATION ANALYSIS ---------------- #

# Top 10 States (Horizontal Bar Plot)
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='state', order=df['state'].value_counts().head(10).index)
plt.title('Top 10 States by Shootings')
plt.tight_layout()
plt.show()

# Top 10 Cities (Horizontal Bar Plot)
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='city', order=df['city'].value_counts().head(10).index)
plt.title('Top 10 Cities by Shootings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------- RELATIONSHIP PLOTS ---------------- #

# Race vs Weapon (Top 5 races and top 5 weapons)
top_races = df['race'].value_counts().head(5).index
top_weapons = df['armed'].value_counts().head(5).index
subset = df[df['race'].isin(top_races) & df['armed'].isin(top_weapons)]

plt.figure(figsize=(10, 6))
sns.countplot(data=subset, x='armed', hue='race')
plt.title('Weapon Type vs Race')
plt.tight_layout()
plt.show()

# Mental illness vs Body camera (Count Plot)
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='signs_of_mental_illness', hue='body_camera')
plt.title('Mental Illness vs Body Camera Usage')
plt.xticks([0, 1], ['False', 'True'])
plt.tight_layout()
plt.show()

# Fleeing vs Threat Level (Count Plot)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='flee', hue='threat_level', order=df['flee'].value_counts().index)
plt.title('Fleeing Status vs Threat Level')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------- CORRELATION ---------------- #

# Numeric correlation (Heatmap)
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# RACE PERCENTAGE (Pie Chart)
race_counts = df['race'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 8))
race_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Victims by Race')
plt.ylabel('')
plt.tight_layout()
plt.show()

# MONTHLY KILLINGS FOR 2020 (Line Plot)
df_2020 = df[df['incident_year'] == 2020]
monthly_2020 = df_2020['incident_month'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
monthly_2020.plot(kind='line', marker='o')
plt.title('Monthly Police Shootings in 2020')
plt.xlabel('Month')
plt.ylabel('Number of Shootings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# THREAT LEVEL vs FLEEING (Bar Plot)
top_combos = df.groupby(['threat_level', 'flee']).size().reset_index(name='count')
plt.figure(figsize=(10, 6))
sns.barplot(data=top_combos, x='threat_level', y='count', hue='flee')
plt.title("Threat Level vs Fleeing Status")
plt.tight_layout()
plt.show()

# WEAPON vs BODY CAMERA (Count Plot)
top_armed = df['armed'].value_counts().head(5).index
subset_armed = df[df['armed'].isin(top_armed)]

plt.figure(figsize=(10, 6))
sns.countplot(data=subset_armed, x='armed', hue='body_camera')
plt.title('Top Weapons vs Body Camera Usage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# MENTAL ILLNESS BY RACE (Count Plot)
mental_race = df[df['signs_of_mental_illness'] == True]

plt.figure(figsize=(8, 5))
sns.countplot(data=mental_race, x='race', order=mental_race['race'].value_counts().index)
plt.title('Race Distribution (With Signs of Mental Illness)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# RACE vs THREAT LEVEL (Count Plot)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='race', hue='threat_level', order=df['race'].value_counts().index)
plt.title('Race vs Threat Level')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# WEEKDAY vs GENDER (Count Plot)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='incident_weekday', hue='gender', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title("Weekday vs Gender")
plt.tight_layout()
plt.show()
