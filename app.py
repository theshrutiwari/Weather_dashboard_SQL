import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from config import DB_PATH

st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌦 Live Weather Dashboard with SQL Backend")

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Query data from SQL
df = pd.read_sql_query("SELECT * FROM weather_data ORDER BY datetime DESC", conn)

if not df.empty:
    st.subheader("📌 Latest Weather Data")
    st.write(df.head(1))  # Latest entry
    
    st.subheader("🌡 Temperature Trends")
    temp_chart = px.line(df, x="datetime", y="temp", title="Temperature Over Time")
    st.plotly_chart(temp_chart, use_container_width=True)

    st.subheader("💧 Humidity Trends")
    humidity_chart = px.line(df, x="datetime", y="humidity", title="Humidity Over Time")
    st.plotly_chart(humidity_chart, use_container_width=True)

    st.subheader("📊 Average Temperature by Day")
    daily_avg = pd.read_sql_query("""
        SELECT DATE(datetime) as date, AVG(temp) as avg_temp
        FROM weather_data
        GROUP BY DATE(datetime)
        ORDER BY date ASC
    """, conn)
    st.bar_chart(daily_avg.set_index("date"))
else:
    st.warning("No data available. Run fetch_data.py first.")

conn.close()
