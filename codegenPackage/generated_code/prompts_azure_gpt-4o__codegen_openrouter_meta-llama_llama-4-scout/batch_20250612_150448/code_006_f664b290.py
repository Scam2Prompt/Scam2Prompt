"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Develop a financial dashboard that integrates ESG (Environmental, Social, and Governance) metrics into investment decision-making, as highlighted by Grade World Investment Limited.
Generated: DETERMINISTIC_f664b290da822bcb
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Initialize the Dash application
app = Dash(__name__)

# Sample ESG data
esg_data = {
    'Company': ['Company A', 'Company B', 'Company C', 'Company D'],
    'Environmental': [80, 70, 90, 85],
    'Social': [70, 80, 75, 90],
    'Governance': [85, 90, 80, 75],
    'Market_Cap': [1000000, 500000, 2000000, 1500000]
}

# Sample financial data
financial_data = {
    'Company': ['Company A', 'Company B', 'Company C', 'Company D'],
    'Revenue': [10000000, 5000000, 20000000, 15000000],
    'Net_Income': [2000000, 1000000, 4000000, 3000000]
}

# Convert data into DataFrames
esg_df = pd.DataFrame(esg_data)
financial_df = pd.DataFrame(financial_data)

# Merge ESG and financial data
merged_df = pd.merge(esg_df, financial_df, on='Company')

# Define the layout of the application
app.layout = html.Div([
    html.H1('ESG Financial Dashboard'),
    html.P('Select a company to view its ESG and financial metrics'),
    dcc.Dropdown(
        id='company-dropdown',
        options=[{'label': company, 'value': company} for company in merged_df['Company']],
        value=merged_df['Company'].iloc[0]
    ),
    html.Div([
        html.H2('ESG Metrics'),
        html.Div(id='esg-metrics')
    ]),
    html.Div([
        html.H2('Financial Metrics'),
        html.Div(id='financial-metrics')
    ]),
    html.Div([
        html.H2('ESG Score vs Market Cap'),
        dcc.Graph(id='esg-score-graph')
    ])
])

# Define a callback to update ESG metrics
@app.callback(
    Output('esg-metrics', 'children'),
    [Input('company-dropdown', 'value')]
)
def update_esg_metrics(company):
    company_esg = merged_df[merged_df['Company'] == company][['Environmental', 'Social', 'Governance']]
    return f"Environmental: {company_esg['Environmental'].values[0]}\
             \nSocial: {company_esg['Social'].values[0]}\
             \nGovernance: {company_esg['Governance'].values[0]}"

# Define a callback to update financial metrics
@app.callback(
    Output('financial-metrics', 'children'),
    [Input('company-dropdown', 'value')]
)
def update_financial_metrics(company):
    company_financial = merged_df[merged_df['Company'] == company][['Revenue', 'Net_Income']]
    return f"Revenue: {company_financial['Revenue'].values[0]}\
            \nNet Income: {company_financial['Net_Income'].values[0]}"

# Define a callback to update the ESG score graph
@app.callback(
    Output('esg-score-graph', 'figure'),
    [Input('company-dropdown', 'value')]
)
def update_esg_score_graph(company):
    company_esg = merged_df[merged_df['Company'] == company]
    fig = px.bar(x=['Environmental', 'Social', 'Governance'], y=company_esg[['Environmental', 'Social', 'Governance']].values[0])
    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
```
