#  ​ Fatal Police Shootings Data Analysis

This repository offers a comprehensive **data analysis project on fatal police shootings** in the United States, leveraging data from *The Washington Post*. The project includes **data preprocessing**, **exploratory data analysis (EDA)**, and **visualization**, uncovering patterns across **demographics**, **geography**, **weapon usage**, and **time trends**.

---

##  Repository Structure

├── data/
│ ├── fatal-police-shootings-data.csv # Raw dataset
│ └── fatal-police-shootings-cleaned.csv # Cleaned dataset after preprocessing
│
├── scripts/
│ ├── prepros.py # Preprocessing: cleaning & formatting
│ ├── analyse.py # EDA & visualizations
│ ├── v3.py, v4.py # Experimental/extended analyses
│
├── reports/
│ ├── report_before_preprocessing.docx # Insights from raw dataset
│ └── report_after_preprocessing.docx # Findings post-cleanup
│
├── visuals/
│ ├── age_distribution.png
│ ├── armed_status.png
│ ├── body_camera_pie.png
│ ├── gender_race_distribution.png
│ ├── monthly_incidents.png
│ ├── top_states.png
│ ├── yearwise_bodycam.png
│ └── map.html # Interactive map using Folium
└── README.md

yaml
Copy
Edit

---

##  Key Insights

- **Demographic Trends**: Clear patterns in age, gender, and race distributions among victims  
- **Geographic Disparities**: Certain states report higher shooting counts than others  
- **Body Camera Usage**: Mixed adoption—some state variation over time  
- **Weapon Status**: Incidents vary depending on whether a victim was armed or unarmed  
- **Temporal Patterns**: Season and year-over-year variance in incident frequency

---

##  Preview of Visualizations

- **Age Distribution**  
  ![Age Distribution](visuals/age_distribution.png)

- **Body Camera Use**  
  ![Body Camera Usage](visuals/body_camera_pie.png)

- **Top Performing States**  
  ![Top States](visuals/top_states.png)

- **Incident Map (Interactive)**  
  [View Map](visuals/map.html)

---

