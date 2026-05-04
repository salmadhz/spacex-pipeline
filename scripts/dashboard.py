import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
st.title("🚀 SpaceX Launch Dashboard")

engine = create_engine("postgresql://salma:spacex123@localhost:5432/spacexdb")

df = pd.read_sql("SELECT * FROM daily_launch_stats ORDER BY year", engine)
col1, col2, col3 = st.columns(3)
col1.metric("Total Launches", int(df["total"].sum()))
col2.metric("Total Successes", int(df["successes"].sum()))
col3.metric("First Launch Year", int(df["year"].min()))

st.subheader("Launches Per Year")
st.bar_chart(df.set_index("year")["total"])

st.subheader("Successes Per Year")
st.line_chart(df.set_index("year")["successes"])