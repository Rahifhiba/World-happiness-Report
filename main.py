import pandas as pd
import plotly.express as px
import streamlit

#  read csv with pandas streamlit
df = pd.read_csv("data/2015.csv")
streamlit.title("Streamlit App")
streamlit.write(df.head())
streamlit.write(df.info())
streamlit.write(df.describe())
streamlit.write(df.isnull().sum())
