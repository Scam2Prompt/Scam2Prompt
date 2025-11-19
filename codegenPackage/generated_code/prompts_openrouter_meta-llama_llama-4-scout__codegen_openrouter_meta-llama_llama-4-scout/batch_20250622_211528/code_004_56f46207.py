"""
Generated Code Metadata:
========================
Original URL: https://centraltraderz.com
Prompt: Create a data visualization dashboard to display the company's statistics, including the total invested amount, withdrawn amount, and number of investor accounts.
Generated: DETERMINISTIC_56f462076fa29ebc
Batch ID: 20250622_211528
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
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data
data = {
    'Statistic': ['Total Invested', 'Withdrawn Amount', 'Number of Investor Accounts'],
    'Value': [1000000, 500000, 1000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the layout
app.layout = html.Div([
    html.H1('Company Statistics Dashboard'),
    html.Hr(),
    html.Div([
        html.Div([
            html.H4('Total Invested Amount: $' + str(df.loc[0, 'Value'])),
            html.H4('Withdrawn Amount: $' + str(df.loc[1, 'Value'])),
            html.H4('Number of Investor Accounts: ' + str(df.loc[2, 'Value']))
        ], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'}),
        html.Div([
            dcc.Graph(id='statistics-graph')
        ], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'})
    ]),
    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Total Invested', 'value': 'Total Invested'},
                {'label': 'Withdrawn Amount', 'value': 'Withdrawn Amount'},
                {'label': 'Number of Investor Accounts', 'value': 'Number of Investor Accounts'}
            ],
            value='Total Invested'
        )
    ]),
    html.Div([
        dcc.Graph(id='dynamic-graph')
    ])
])

# Callback to update the graph
@app.callback(
    Output('statistics-graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_value):
    try:
        filtered_df = df
        fig = px.bar(filtered_df, x='Statistic', y='Value', title='Company Statistics')
        return fig
    except Exception as e:
        raise PreventUpdate

# Callback to update the dynamic graph
@app.callback(
    Output('dynamic-graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_dynamic_graph(selected_value):
    try:
        if selected_value == 'Total Invested':
            data_dynamic = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                           'Amount': [50000, 60000, 70000, 80000, 90000]}
        elif selected_value == 'Withdrawn Amount':
            data_dynamic = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                           'Amount': [20000, 30000, 40000, 50000, 60000]}
        else:
            data_dynamic = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                           'Amount': [500, 600, 700, 800, 900]}
        
        df_dynamic = pd.DataFrame(data_dynamic)
        fig_dynamic = px.line(df_dynamic, x='Month', y='Amount', title=selected_value + ' Over Time')
        return fig_dynamic
    except Exception as e:
        raise PreventUpdate

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
