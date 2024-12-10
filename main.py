import pandas as pd
import plotly.express as px
import streamlit as st
from helper import *
from chart import *

#  read csv with pandas streamlit
df = pd.read_csv("data/output.csv")
df['Year'] = df['Year'].astype(str)
year = st.sidebar.selectbox("Select a year", ["2015", "2016", "2017", "2018", "2019"])

st.title("Data Visualization of World Happiness Report (2015-2019)")
st.write(df[df["Year"] == year])
x = st.sidebar.selectbox("Select X value", df.columns)
y = st.sidebar.selectbox("Select Y value", df.columns)
#  plotly express
# fig = px.scatter(df, x='x', y='y', color='z')
# years

type_chart = st.sidebar.selectbox(
    "Select chart type",
    [
        "Histogram",
        "Line chart",
        "Pie chart",
        "Boxplot",
        "KDE chart",
        "Bar chart",
        "Scatter plot",
        "Heatmap",
        "Violin plot",
    ],
)
st.header(type_chart)
choose(type_chart, df[df["Year"] == year], x, y)

st.header("Map of happiness score")
fig = px.choropleth(
    df[df["Year"] == year],
    locations="Country",
    locationmode="country names",
    color="Happiness Score",
    hover_name="Country",
    color_continuous_scale=px.colors.sequential.Plasma,
)
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'  )

st.plotly_chart(fig)







about =  st.sidebar.expander("About")
about.write('''
    Data source: [World Happiness Report](https://www.kaggle.com/unsdsn/world-happiness)
''')