import streamlit as st
import pandas as pd
import plotly.express as px


"""charts"""
WARN_ICON = "⚠️"


def validate_columns(data, x, y=None, x_types=None, y_types=None, allow_same=False):
    """
    Validates the column types for the given data and raises an error if invalid."""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype if y else None

    if not allow_same and x == y:
        st.error("X and Y should be different columns.", icon=WARN_ICON)
        return False

    if x_types and x_dtype not in x_types:
        st.error(f"X should be one of the types: {x_types}.", icon=WARN_ICON)
        return False

    if y and y_types and y_dtype not in y_types:
        st.error(f"Y should be one of the types: {y_types}.", icon=WARN_ICON)
        return False

    return True


def pie_chart(data, x, y):
    """Create a pie chart."""
    if validate_columns(
        data, x, y, x_types=["object", "category"], y_types=["float64", "int64"]
    ):
        fig = px.pie(data, names=x, values=y)
        st.plotly_chart(fig)


def line_chart(data, x, y):
    """Create a line chart."""
    if validate_columns(
        data,
        x,
        y,
        x_types=["float64", "int64", "datetime64[ns]"],
        y_types=["float64", "int64"],
    ):
        st.line_chart(data, x=x, y=y)


def histogram(data, x, y=None):
    """Create a histogram."""
    if validate_columns(
        data,
        x,
        y,
        x_types=["float64", "int64"],
        y_types=["float64", "int64", None],
        allow_same=False,
    ):
        fig = px.histogram(data, x=x, y=y) if y else px.histogram(data, x=x)
        st.plotly_chart(fig, use_container_width=True)


def box_plot(data, x, y):
    """Create a box plot."""
    if validate_columns(
        data, x, y, x_types=["object", "category"], y_types=["float64", "int64"]
    ):
        fig = px.box(data, x=x, y=y, points="all")
        st.plotly_chart(fig)


def bar_chart(data, x, y):
    """Create a bar chart."""
    if validate_columns(
        data, x, y, x_types=["object", "category"], y_types=["float64", "int64"]
    ):
        st.bar_chart(data=data, x=x, y=y)


def kde_chart(data, x, y):
    """Create a KDE plot."""
    if validate_columns(
        data, x, y, x_types=["float64", "int64"], y_types=["float64", "int64"]
    ):
        fig = px.density_contour(data, x=x, y=y)
        st.plotly_chart(fig)


def scatter_chart(data, x, y):
    """Create a scatter plot."""
    if validate_columns(
        data, x, y, x_types=["float64", "int64"], y_types=["float64", "int64"]
    ):
        fig = px.scatter(data, x=x, y=y)
        st.plotly_chart(fig)


def violin_plot(data, x, y):
    """Create a violin plot."""
    if validate_columns(
        data, x, y, x_types=["object", "category"], y_types=["float64", "int64"]
    ):
        fig = px.violin(data, x=x, y=y)
        st.plotly_chart(fig)


def heatmap(data):
    """Create a heatmap."""
    fig = px.imshow(data)
    st.plotly_chart(fig, theme="streamlit")
