"""
Generated Code Metadata:
========================
Original URL: https://www.kff.org.kw
Prompt: "Generate a code snippet to create a simple agricultural product price dashboard inspired by the Kuwaiti Farmers Federation's price page."
Generated: DETERMINISTIC_c71a067d687f2d22
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash application
app = dash.Dash(__name__)

# Sample agricultural product price data
data = {
    "Product": ["Wheat", "Barley", "Potatoes", "Tomatoes", "Cucumbers"],
    "Price (KWD/kg)": [0.5, 0.3, 0.8, 1.2, 0.9],
    "Category": ["Grains", "Grains", "Vegetables", "Vegetables", "Vegetables"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the layout
app.layout = html.Div(
    children=[
        html.H1(children="Agricultural Product Price Dashboard"),
        html.P(children="Select a category to view product prices:"),
        dcc.Dropdown(
            id="category-dropdown",
            options=[
                {"label": category, "value": category} for category in df["Category"].unique()
            ],
            value=df["Category"].unique()[0],
        ),
        dcc.Graph(id="price-graph"),
        html.Div(id="price-table"),
    ]
)

# Update the graph based on the selected category
@app.callback(
    Output("price-graph", "figure"),
    [Input("category-dropdown", "value")],
)
def update_graph(selected_category):
    filtered_df = df[df["Category"] == selected_category]
    fig = px.bar(filtered_df, x="Product", y="Price (KWD/kg)")
    fig.update_layout(title=f"Prices of {selected_category} Products")
    return fig

# Update the price table based on the selected category
@app.callback(
    Output("price-table", "children"),
    [Input("category-dropdown", "value")],
)
def update_table(selected_category):
    filtered_df = df[df["Category"] == selected_category]
    table = html.Table(
        children=[
            html.Thead(html.Tr([html.Th(col) for col in filtered_df.columns])),
            html.Tbody(
                [
                    html.Tr(
                        [
                            html.Td(filtered_df.iloc[i][col])
                            for col in filtered_df.columns
                        ]
                    )
                    for i in range(len(filtered_df))
                ]
            ),
        ]
    )
    return table

# Run the application
if __name__ == "__main__":
    app.run_server(debug=True)
```
