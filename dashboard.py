import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import sqlite3
from datetime import datetime


# Get data from Database
database = sqlite3.connect("Dummy_data.db")
df = pd.read_sql_query("SELECT * FROM localization_projects", database)

# Earliest Date
min_date_query = "SELECT MIN(start_date) FROM localization_projects"
min_date = pd.read_sql_query(min_date_query, database)
min_date = min_date.iloc[0]["MIN(start_date)"]
min_date_object = datetime.strptime(min_date, "%Y-%m-%d %H:%M:%S.%f")

# Max Date
max_date_query = "SELECT MAX(end_date) FROM localization_projects"
max_date = pd.read_sql_query(max_date_query, database)
max_date = max_date.iloc[0]["MAX(end_date)"]
max_date_object = datetime.strptime(max_date, "%Y-%m-%d %H:%M:%S.%f")

# Total number of projects
total_projects_query = "SELECT COUNT(DISTINCT project_id) FROM localization_projects"
total_projects = pd.read_sql_query(total_projects_query, database)
total_projects = total_projects.iloc[0]["COUNT(DISTINCT project_id)"]

# of projects completed by PM
projects_by_pm_query = ""


# Initialize Dashboard
st.title("Localization Metrics")
left_column, right_column = st.columns(2)

# Total Projects
st.subheader("Total Projects")
# st.metric(label="Total Projects", value=total_projects, label_visibility="collapsed")
st.info(total_projects)

# Create Side bar and filter
st.sidebar.header("Select date range:")
Start_date_filter = st.sidebar.date_input("", (min_date_object, max_date_object))
st.sidebar.subheader("Raw data")
if st.sidebar.checkbox("Show raw data"):
    st.write(df)
