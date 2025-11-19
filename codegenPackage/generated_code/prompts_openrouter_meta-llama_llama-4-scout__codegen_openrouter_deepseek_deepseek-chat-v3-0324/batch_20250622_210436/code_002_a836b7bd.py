"""
Generated Code Metadata:
========================
Original URL: https://dogegovnews.pages.dev
Prompt: Generate a code snippet to create a simple dashboard displaying US government spending and debt metrics, inspired by the Department of Government Efficiency's mission and data visualizations.
Generated: DETERMINISTIC_a836b7bd3970d6ce
Batch ID: 20250622_210436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from datetime import datetime

# Initialize the Dash app
app = Dash(__name__)

# Sample data - in production, this would come from an API or database
def get_spending_data():
    years = list(range(2010, 2023))
    spending = [
        3.52, 3.60, 3.54, 3.45, 3.51, 3.65, 3.82, 4.11, 4.45, 4.70, 6.55, 6.82, 6.27
    ]  # in trillions
    debt = [
        13.56, 14.76, 16.05, 16.73, 17.81, 18.15, 19.95, 21.52, 22.72, 26.94, 28.43, 30.93, 31.38
    ]  # in trillions
    deficit = [
        1.29, 1.30, 1.09, 0.48, 0.44, 0.44, 0.59, 0.78, 0.98, 3.13, 2.77, 2.77, 1.38
    ]  # in trillions
    
    return pd.DataFrame({
        'Year': years,
        'Spending (Trillions)': spending,
        'Debt (Trillions)': debt,
        'Deficit (Trillions)': deficit
    })

# Create layout for the dashboard
app.layout = html.Div([
    html.H1("US Government Spending & Debt Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='metric-selector',
                options=[
                    {'label': 'Spending', 'value': 'Spending (Trillions)'},
                    {'label': 'Debt', 'value': 'Debt (Trillions)'},
                    {'label': 'Deficit', 'value': 'Deficit (Trillions)'}
                ],
                value='Spending (Trillions)',
                clearable=False
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.RangeSlider(
                id='year-slider',
                min=2010,
                max=2022,
                step=1,
                marks={year: str(year) for year in range(2010, 2023, 2)},
                value=[2010, 2022]
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    
    dcc.Graph(id='main-graph'),
    
    html.Div([
        dcc.Graph(id='debt-to-spending-ratio'),
    ], style={'width': '100%', 'display': 'inline-block'}),
    
    html.Footer([
        html.P("Data Source: US Treasury Department (Sample Data)", style={'textAlign': 'center'}),
        html.P(f"Last Updated: {datetime.now().strftime('%Y-%m-%d')}", style={'textAlign': 'center'})
    ])
])

# Callbacks for interactive components
@app.callback(
    Output('main-graph', 'figure'),
    [Input('metric-selector', 'value'),
     Input('year-slider', 'value')]
)
def update_main_graph(selected_metric, selected_years):
    df = get_spending_data()
    filtered_df = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]
    
    fig = px.line(
        filtered_df,
        x='Year',
        y=selected_metric,
        title=f"US Government {selected_metric.split(' ')[0]} Over Time",
        labels={'Year': 'Year', 'value': selected_metric}
    )
    
    fig.update_layout(
        transition_duration=500,
        hovermode='x unified'
    )
    
    return fig

@app.callback(
    Output('debt-to-spending-ratio', 'figure'),
    [Input('year-slider', 'value')]
)
def update_ratio_graph(selected_years):
    df = get_spending_data()
    filtered_df = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]
    filtered_df['Debt/Spending Ratio'] = filtered_df['Debt (Trillions)'] / filtered_df['Spending (Trillions)']
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=filtered_df['Year'],
        y=filtered_df['Debt/Spending Ratio'],
        name='Debt to Spending Ratio'
    ))
    
    fig.update_layout(
        title='Debt to Annual Spending Ratio',
        xaxis_title='Year',
        yaxis_title='Ratio',
        hovermode='x unified'
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
