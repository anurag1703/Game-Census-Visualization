import pandas as pd
from ydata_profiling import ProfileReport

# Load the dataset
df = pd.read_csv(r'C:/Users/anura/Desktop/Project 2- Big game Census Analytics/Notebook/final_cleaned_big_game_data.csv')


# Generate the profile report
profile = ProfileReport(df, title="Exploratory Data Analysis Report", explorative=True)

# Save the report to an HTML file
profile.to_file("eda_report.html")
