import streamlit as st
from PIL import Image
import os

# Function to show the EDA page
def show_eda_page():
    """Render the EDA report interface."""
    st.title("Exploratory Data Analysis Report")

    # Path to the EDA HTML report
    html_file_path = "EDA report/eda_report.html"

    # Check if the HTML report file exists
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            report_html = f.read()
        # Render the EDA report HTML content
        st.components.v1.html(report_html, height=1000, scrolling=True)
    else:
        st.error("The HTML report file was not found. Please ensure the path is correct.")

    # Back to data visualization page
    if st.button("Back to Data Visualizations And Insights"):
        st.session_state.show_eda = False

# Function to show the Data Visualization page
def show_visualizations_page():
    """Render the data visualizations page."""
    st.title("Exploratory Data Analysis, Data Visualizations And Insights")

    # Player Distribution by State
    st.subheader("Player Distribution by State")
    img1 = Image.open('Visualizations/Player Distribution by State.png')
    st.image(img1, caption='Player Distribution by State')

    # Players Per Capita by State
    st.subheader("Players Per Capita by State")
    img2 = Image.open('Visualizations/Players Per Capita by State.png')
    st.image(img2, caption='Players Per Capita by State')

    # Players Distribution by Team
    st.subheader("Players Distribution by Team")
    img3 = Image.open('Visualizations/Players Distribution by Team.png')
    st.image(img3, caption='Players Distribution by Team')

    # Distribution of Positions Across States
    st.subheader("Distribution of Positions Across States")
    img4 = Image.open('Visualizations/Distribution of Positions Across States.png')
    st.image(img4, caption='Distribution of Positions Across States')

    # Population and Player Growth
    st.subheader("Population and Player Growth Over Time (2010-2017)")
    img5 = Image.open('Visualizations/Population and Player Growth Over Time (2010-2017).png')
    st.image(img5, caption='Population and Player Growth')

    # Population Growth vs Player Count
    st.subheader("Population Growth vs Player count")
    img6 = Image.open('Visualizations/Population Growth vs. Player Count.png')
    st.image(img6, caption='Population Growth vs Player count')

    # Population vs. Player Count for Top 10 States
    st.subheader("Population vs. Player Count for Top 10 States")
    img7 = Image.open('Visualizations/Population vs. Player Count for Top 10 States.png')
    st.image(img7, caption='Population vs Player Count for Top 10 States')
    
    

    # Button to navigate to EDA page
    if st.button("Go to EDA Report"):
        st.session_state.show_eda = True

# Page navigation logic
if "show_eda" not in st.session_state:
    st.session_state.show_eda = False

# Render the appropriate page based on the session state
if st.session_state.show_eda:
    show_eda_page()
else:
    show_visualizations_page()

