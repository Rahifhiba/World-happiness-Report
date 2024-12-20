from chart import *
from statistics import median, mean, mode


def choose(type_chart, data, x, y):
    """cases of selectbox"""

    match type_chart:
        case "Histogram":
            histogram(data, x, y)
        case "Pie chart":
            pie_chart(data, x, y)
        case "Line chart":
            line_chart(data, x, y)
        case "Scatter plot":
            scatter_chart(data, x, y)
        case "Boxplot":
            box_plot(data, x, y)
        case "Bar chart":
            bar_chart(data, x, y)
        case "KDE chart":
            kde_chart(data, x, y)
        case "Violin plot":
            violin_plot(data, x, y)
        case "Heatmap":
            heatmap(data)
        case _:
            st.error("Invalid chart type selected.")


# def table_stat(df, col):
#     """Statistics of columns"""
#     col_dtype = df[col].dtype
#     if col_dtype != "object":
#         col_stats = {
#             "Mean": mean(df[col]),
#             "Median": median(df[col]),
#             "Mode": mode(df[col]),
#         }
#         st.write(f"Statistics for {col}:")
#         st.table(col_stats)


# def fix_coltype(df):
#     """fix column types"""
#     for col in df.columns:
#         if pd.api.types.is_string_dtype(df[col]):
#             try:
#                 df[col] = pd.to_numeric(df[col])
#                 print(col, "modified")
#             except:
#                 pass
#     return df
