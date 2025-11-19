"""
Generated Code Metadata:
========================
Original URL: https://genoverde.com
Prompt: Create a data visualization dashboard to display GenoVerde's plant diagnostic testing results and cultivar library data.
Generated: DETERMINISTIC_2abc8a22960305e8
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap components
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Sample data loading (replace with actual data sources)
def load_diagnostic_data():
    # In production, this would connect to a database or API
    return pd.DataFrame({
        'TestID': ['T001', 'T002', 'T003', 'T004'],
        'PlantType': ['Tomato', 'Pepper', 'Tomato', 'Cucumber'],
        'Disease': ['Blight', 'Mosaic Virus', 'Blight', 'Powdery Mildew'],
        'Result': ['Positive', 'Negative', 'Positive', 'Positive'],
        'Date': ['2023-01-15', '2023-01-18', '2023-01-20', '2023-01-22'],
        'Severity': [3, 0, 2, 1]
    })

def load_cultivar_data():
    return pd.DataFrame({
        'CultivarID': ['C001', 'C002', 'C003', 'C004'],
        'Name': ['Golden Delight', 'Ruby Red', 'Emerald Green', 'Sunny Yellow'],
        'Species': ['Tomato', 'Pepper', 'Cucumber', 'Tomato'],
        'DiseaseResistance': ['Blight', 'Mosaic Virus', 'Powdery Mildew', 'Blight'],
        'YieldPotential': [8, 7, 9, 8],
        'DaysToMaturity': [75, 80, 60, 70]
    })

# Load data
diagnostic_data = load_diagnostic_data()
cultivar_data = load_cultivar_data()

# Define app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("GenoVerde Plant Analytics Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Tabs([
        dbc.Tab(label="Diagnostic Results", children=[
            dbc.Row([
                dbc.Col([
                    html.H3("Test Results Overview", className="text-center"),
                    dcc.Graph(id='test-results-pie')
                ], md=6),
                dbc.Col([
                    html.H3("Severity by Plant Type", className="text-center"),
                    dcc.Graph(id='severity-bar')
                ], md=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H3("Filter Data"),
                    dcc.Dropdown(
                        id='plant-type-filter',
                        options=[{'label': pt, 'value': pt} for pt in diagnostic_data['PlantType'].unique()],
                        multi=True,
                        placeholder="Select Plant Type(s)"
                    ),
                    dcc.Dropdown(
                        id='disease-filter',
                        options=[{'label': d, 'value': d} for d in diagnostic_data['Disease'].unique()],
                        multi=True,
                        placeholder="Select Disease(s)"
                    ),
                    dcc.DatePickerRange(
                        id='date-range',
                        min_date_allowed=diagnostic_data['Date'].min(),
                        max_date_allowed=diagnostic_data['Date'].max(),
                        start_date=diagnostic_data['Date'].min(),
                        end_date=diagnostic_data['Date'].max()
                    )
                ], md=4),
                
                dbc.Col([
                    html.H3("Detailed Test Results"),
                    html.Div(id='test-results-table')
                ], md=8)
            ])
        ]),
        
        dbc.Tab(label="Cultivar Library", children=[
            dbc.Row([
                dbc.Col([
                    html.H3("Cultivar Distribution by Species", className="text-center"),
                    dcc.Graph(id='cultivar-pie')
                ], md=6),
                dbc.Col([
                    html.H3("Yield Potential vs Days to Maturity", className="text-center"),
                    dcc.Graph(id='yield-scatter')
                ], md=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H3("Filter Cultivars"),
                    dcc.Dropdown(
                        id='species-filter',
                        options=[{'label': s, 'value': s} for s in cultivar_data['Species'].unique()],
                        multi=True,
                        placeholder="Select Species"
                    ),
                    dcc.Dropdown(
                        id='resistance-filter',
                        options=[{'label': r, 'value': r} for r in cultivar_data['DiseaseResistance'].unique()],
                        multi=True,
                        placeholder="Select Disease Resistance"
                    )
                ], md=4),
                
                dbc.Col([
                    html.H3("Cultivar Details"),
                    html.Div(id='cultivar-table')
                ], md=8)
            ])
        ])
    ])
], fluid=True)

# Callbacks for Diagnostic Results tab
@callback(
    [Output('test-results-pie', 'figure'),
     Output('severity-bar', 'figure'),
     Output('test-results-table', 'children')],
    [Input('plant-type-filter', 'value'),
     Input('disease-filter', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_diagnostic_results(plant_types, diseases, start_date, end_date):
    filtered_data = diagnostic_data.copy()
    
    # Apply filters
    if plant_types:
        filtered_data = filtered_data[filtered_data['PlantType'].isin(plant_types)]
    if diseases:
        filtered_data = filtered_data[filtered_data['Disease'].isin(diseases)]
    if start_date:
        filtered_data = filtered_data[filtered_data['Date'] >= start_date]
    if end_date:
        filtered_data = filtered_data[filtered_data['Date'] <= end_date]
    
    # Create pie chart
    pie_fig = px.pie(
        filtered_data,
        names='Result',
        title='Test Results Distribution',
        color='Result',
        color_discrete_map={'Positive': 'red', 'Negative': 'green'}
    )
    
    # Create bar chart
    bar_fig = px.bar(
        filtered_data.groupby('PlantType')['Severity'].mean().reset_index(),
        x='PlantType',
        y='Severity',
        title='Average Severity by Plant Type',
        color='PlantType'
    )
    
    # Create table
    table = dbc.Table.from_dataframe(
        filtered_data,
        striped=True,
        bordered=True,
        hover=True,
        responsive=True
    )
    
    return pie_fig, bar_fig, table

# Callbacks for Cultivar Library tab
@callback(
    [Output('cultivar-pie', 'figure'),
     Output('yield-scatter', 'figure'),
     Output('cultivar-table', 'children')],
    [Input('species-filter', 'value'),
     Input('resistance-filter', 'value')]
)
def update_cultivar_data(species, resistances):
    filtered_data = cultivar_data.copy()
    
    # Apply filters
    if species:
        filtered_data = filtered_data[filtered_data['Species'].isin(species)]
    if resistances:
        filtered_data = filtered_data[filtered_data['DiseaseResistance'].isin(resistances)]
    
    # Create pie chart
    pie_fig = px.pie(
        filtered_data,
        names='Species',
        title='Cultivar Distribution by Species'
    )
    
    # Create scatter plot
    scatter_fig = px.scatter(
        filtered_data,
        x='DaysToMaturity',
        y='YieldPotential',
        color='Species',
        hover_name='Name',
        title='Yield Potential vs Days to Maturity'
    )
    
    # Create table
    table = dbc.Table.from_dataframe(
        filtered_data,
        striped=True,
        bordered=True,
        hover=True,
        responsive=True
    )
    
    return pie_fig, scatter_fig, table

if __name__ == '__main__':
    app.run_server(debug=True)
```
