Fatal Police Shootings Data Analysis
This repository contains a data analysis project on fatal police shootings in the United States, using the dataset from the Washington Post and related sources. The project focuses on data preprocessing, exploratory data analysis (EDA), and visualization of key patterns such as demographics, geographic distribution, weapon status, and temporal trends.

📂 Repository Contents
Data Files

fatal-police-shootings-data.csv → Raw dataset

fatal-police-shootings-cleaned.csv → Cleaned dataset after preprocessing

Python Scripts

prepros.py → Script for data preprocessing (handling missing values, cleaning, and formatting)

analyse.py → Exploratory Data Analysis (EDA) and visualization script

v3.py, v4.py → Additional analysis/experimentation scripts

Reports

report before preprocessing.docx → Initial observations from raw dataset

report after preprocessing.docx → Findings and insights after data cleaning

Visualizations (generated using Matplotlib/Seaborn/Folium)

age_distribution.png → Distribution of victims’ ages

armed_status.png → Weapon/armed status distribution

body_camera_pie.png → Body camera usage by incidents

gender_race_distribution.png → Gender and race distribution

monthly_incidents.png → Incidents over months

top_states.png → States with the highest number of cases

yearwise_bodycam.png → Body camera usage across years

map.html → Interactive map of incidents


📊 Key Insights
Demographics: Analysis shows strong trends in age, gender, and race distribution of victims.

Geography: Certain states contribute disproportionately to fatal shootings.

Body Cameras: Adoption of body cameras has increased over the years but varies widely by state.

Weapons: Armed vs. unarmed status significantly impacts the frequency and reporting of incidents.

Trends Over Time: Seasonal and yearly patterns reveal fluctuations in incidents.

🌍 Visualization Preview
Below are some sample outputs (see repo for all):

Age distribution of victims

Body camera usage pie chart

Heatmap of top states

Interactive map (map.html)

📌 Future Work
Add machine learning models for predictive analysis.

Perform clustering of states/incidents by patterns.

Automate preprocessing pipeline.

Deploy interactive dashboard (e.g., Streamlit).

