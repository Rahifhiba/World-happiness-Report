import pandas as pd
import plotly.express as px
import streamlit as st
from helper import *
from chart import *

#  read csv with pandas streamlit
df = pd.read_csv("data/output.csv")
df["Year"] = df["Year"].astype(str)
year = st.sidebar.selectbox("Select a year", ["2015", "2016", "2017", "2018", "2019"])
filtred_data = df[df["Year"] == year]
st.title("Data Visualization of World Happiness Report (2015-2019)")
st.subheader(f"Filtered Data for {year}")
st.write(filtred_data)
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
st.subheader(type_chart)
choose(type_chart, filtred_data, x, y)

st.header("Map of happiness score")
fig = px.choropleth(
    filtred_data,
    locations="Country",
    locationmode="country names",
    color="Happiness Score",
    hover_name="Country",
    color_continuous_scale=px.colors.sequential.Plasma,
)
fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig)
#*****************************************************  tabs for happinest  ****************************************************

st.subheader("Happinest Factors")
st.write(
    "There is a positive correlation between Happiness Score and key factors such as "
    "Economy (GDP per Capita), Health (Life Expectancy), and Freedom. Below are scatter plots "
    "highlighting these relationships."
)

tab1, tab2, tab3 = st.tabs(
    [
        "Happinest score with Economy (GDP per Capita)",
        "Happinest score with Health (Life Expectancy)",
        "Happinest score with Freedom",
    ]
)
with tab1:
    st.write(f"Scatter Plot: Happiness Score vs Economy (GDP per Capita)")
    choose("Scatter plot", filtred_data, "Happiness Score", "Economy (GDP per Capita)")
with tab2:
    st.write(f"Scatter Plot: Happiness Score vs Health (Life Expectancy)")
    choose("Scatter plot", filtred_data, "Happiness Score", "Health (Life Expectancy)")
with tab3:
    st.write(f"Scatter Plot: Happiness Score vs Freedom")
    choose("Scatter plot", filtred_data, "Happiness Score", "Freedom")


#*****************************************************  tabs for unhappinest  ****************************************************
st.subheader("Unhappiness Factors")
st.write(
    "There is a negative correlation between Happiness Rank and key factors such as "
    "Economy (GDP per Capita), Health (Life Expectancy), and Freedom. Below are scatter plots "
    "highlighting these relationships."
)
tab4, tab5, tab6 = st.tabs(
    [
        "Happinest Rank with Economy (GDP per Capita)",
        "Happinest Rank with Health (Life Expectancy)",
        "Happinest Rank with Freedom",
    ]
)
with tab4:
    st.write(f"Scatter Plot: Happiness Rank vs Economy (GDP per Capita)")
    choose("Scatter plot", filtred_data, "Happiness Rank", "Economy (GDP per Capita)")
with tab5:
    st.write(f"Scatter Plot: Happiness Rank vs Health (Life Expectancy)")
    choose("Scatter plot", filtred_data, "Happiness Rank", "Health (Life Expectancy)")
with tab6:
    st.write(f"Scatter Plot: Happiness Rank vs Freedom")
    choose("Scatter plot", filtred_data, "Happiness Rank", "Freedom")


#*****************************************************  about  ****************************************************
about = st.sidebar.expander("About")
about.write(
    """
    - **Data source**: [World Happiness Report](https://www.kaggle.com/unsdsn/world-happiness)
    - **FAQ World happiness report**: [FAQ](https://worldhappiness.report/faq/)
"""
)
