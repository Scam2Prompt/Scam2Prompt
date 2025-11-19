"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Create a data visualization dashboard using Tableau or Power BI to showcase Child Nepal's impact on children's education and wellbeing.
Generated: DETERMINISTIC_67057f3cfd6de0ae
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since Tableau and Power BI are primarily GUI-based tools with minimal code requirements (mostly for calculated fields or custom scripts), I'll provide a Python alternative using Plotly Dash, which allows for programmatic creation of interactive dashboards with similar capabilities.

```python
# Import required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import os
from datetime import datetime

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server  # Expose the server variable for production deployment

# Sample data (in production, replace with actual data source)
def load_sample_data():
    # Education metrics
    years = list(range(2015, 2023))
    districts = ['Kathmandu', 'Pokhara', 'Chitwan', 'Biratnagar', 'Dharan']
    
    education_data = pd.DataFrame({
        'Year': np.random.choice(years, 100),
        'District': np.random.choice(districts, 100),
        'Enrollment_Rate': np.random.uniform(70, 95, 100),
        'Dropout_Rate': np.random.uniform(1, 15, 100),
        'Test_Scores': np.random.uniform(50, 90, 100),
        'Program_Type': np.random.choice(['Scholarship', 'School Supplies', 'Teacher Training', 'Infrastructure'], 100)
    })
    
    # Wellbeing metrics
    wellbeing_data = pd.DataFrame({
        'Year': np.random.choice(years, 100),
        'District': np.random.choice(districts, 100),
        'Nutrition_Status': np.random.choice(['Good', 'Fair', 'Poor'], 100, p=[0.6, 0.3, 0.1]),
        'Health_Access': np.random.uniform(50, 95, 100),
        'Child_Labor': np.random.uniform(1, 20, 100),
        'Intervention': np.random.choice(['Health Camp', 'Nutrition Program', 'Awareness Campaign'], 100)
    })
    
    return education_data, wellbeing_data

# Load data
try:
    education_df, wellbeing_df = load_sample_data()
except Exception as e:
    print(f"Error loading data: {e}")
    # In production, implement proper error handling and logging

# Define app layout
app.layout = html.Div([
    html.Div([
        html.H1("Child Nepal Impact Dashboard", style={'text-align': 'center'}),
        html.P("Visualizing the impact on children's education and wellbeing", 
              style={'text-align': 'center', 'margin-bottom': '30px'})
    ]),
    
    dcc.Tabs([
        dcc.Tab(label='Education Metrics', children=[
            html.Div([
                dcc.Dropdown(
                    id='district-selector-edu',
                    options=[{'label': d, 'value': d} for d in education_df['District'].unique()],
                    value=['Kathmandu', 'Pokhara'],
                    multi=True,
                    placeholder="Select districts..."
                ),
                dcc.RangeSlider(
                    id='year-slider-edu',
                    min=education_df['Year'].min(),
                    max=education_df['Year'].max(),
                    value=[education_df['Year'].min(), education_df['Year'].max()],
                    marks={str(year): str(year) for year in education_df['Year'].unique()},
                    step=None
                )
            ], style={'margin': '20px'}),
            
            html.Div([
                dcc.Graph(id='enrollment-chart'),
                dcc.Graph(id='dropout-chart'),
                dcc.Graph(id='scores-chart')
            ], style={'display': 'flex', 'flex-wrap': 'wrap'})
        ]),
        
        dcc.Tab(label='Wellbeing Metrics', children=[
            html.Div([
                dcc.Dropdown(
                    id='district-selector-wb',
                    options=[{'label': d, 'value': d} for d in wellbeing_df['District'].unique()],
                    value=['Kathmandu', 'Pokhara'],
                    multi=True,
                    placeholder="Select districts..."
                ),
                dcc.RangeSlider(
                    id='year-slider-wb',
                    min=wellbeing_df['Year'].min(),
                    max=wellbeing_df['Year'].max(),
                    value=[wellbeing_df['Year'].min(), wellbeing_df['Year'].max()],
                    marks={str(year): str(year) for year in wellbeing_df['Year'].unique()},
                    step=None
                )
            ], style={'margin': '20px'}),
            
            html.Div([
                dcc.Graph(id='nutrition-chart'),
                dcc.Graph(id='health-chart'),
                dcc.Graph(id='labor-chart')
            ], style={'display': 'flex', 'flex-wrap': 'wrap'})
        ])
    ]),
    
    html.Div([
        html.P("Data last updated: " + datetime.now().strftime("%Y-%m-%d"), 
              style={'text-align': 'right', 'font-size': '12px', 'color': 'gray'})
    ], style={'margin-top': '30px'})
])

# Education tab callbacks
@app.callback(
    [Output('enrollment-chart', 'figure'),
     Output('dropout-chart', 'figure'),
     Output('scores-chart', 'figure')],
    [Input('district-selector-edu', 'value'),
     Input('year-slider-edu', 'value')]
)
def update_education_charts(selected_districts, selected_years):
    filtered_df = education_df[
        (education_df['District'].isin(selected_districts)) & 
        (education_df['Year'].between(selected_years[0], selected_years[1]))
    ]
    
    enrollment_fig = px.line(
        filtered_df.groupby(['Year', 'Program_Type'])['Enrollment_Rate'].mean().reset_index(),
        x='Year', y='Enrollment_Rate', color='Program_Type',
        title='Average Enrollment Rate by Program Type',
        labels={'Enrollment_Rate': 'Enrollment Rate (%)'}
    )
    
    dropout_fig = px.bar(
        filtered_df.groupby('District')['Dropout_Rate'].mean().reset_index(),
        x='District', y='Dropout_Rate', color='District',
        title='Average Dropout Rate by District',
        labels={'Dropout_Rate': 'Dropout Rate (%)'}
    )
    
    scores_fig = px.box(
        filtered_df,
        x='Program_Type', y='Test_Scores', color='Program_Type',
        title='Distribution of Test Scores by Program Type',
        labels={'Test_Scores': 'Test Scores (%)'}
    )
    
    return enrollment_fig, dropout_fig, scores_fig

# Wellbeing tab callbacks
@app.callback(
    [Output('nutrition-chart', 'figure'),
     Output('health-chart', 'figure'),
     Output('labor-chart', 'figure')],
    [Input('district-selector-wb', 'value'),
     Input('year-slider-wb', 'value')]
)
def update_wellbeing_charts(selected_districts, selected_years):
    filtered_df = wellbeing_df[
        (wellbeing_df['District'].isin(selected_districts)) & 
        (wellbeing_df['Year'].between(selected_years[0], selected_years[1]))
    ]
    
    nutrition_fig = px.pie(
        filtered_df, names='Nutrition_Status', 
        title='Nutrition Status Distribution',
        hole=0.3
    )
    
    health_fig = px.line(
        filtered_df.groupby(['Year', 'Intervention'])['Health_Access'].mean().reset_index(),
        x='Year', y='Health_Access', color='Intervention',
        title='Health Access Rate by Intervention Type',
        labels={'Health_Access': 'Health Access (%)'}
    )
    
    labor_fig = px.scatter(
        filtered_df.groupby(['District', 'Year'])['Child_Labor'].mean().reset_index(),
        x='Year', y='Child_Labor', color='District',
        title='Child Labor Rates Over Time',
        labels={'Child_Labor': 'Child Labor Rate (%)'}
    )
    
    return nutrition_fig, health_fig, labor_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)  # Set debug=False in production
```
