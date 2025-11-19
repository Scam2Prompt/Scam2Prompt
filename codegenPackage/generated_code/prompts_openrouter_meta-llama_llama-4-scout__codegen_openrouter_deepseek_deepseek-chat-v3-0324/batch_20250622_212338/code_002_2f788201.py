"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Generate a code example for creating a simple dashboard to track training metrics, inspired by Romain Rissoan's experience in forming and advising over 2835 people.
Generated: DETERMINISTIC_2f7882013c2a2e26
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample data generation function
def generate_training_data(num_records=2835):
    np.random.seed(42)
    start_date = datetime.now() - timedelta(days=365)
    
    data = {
        "id": range(1, num_records + 1),
        "training_date": [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(num_records)],
        "training_type": np.random.choice(["Workshop", "Bootcamp", "Mentorship", "Consulting"], num_records),
        "duration_hours": np.random.randint(1, 24, num_records),
        "satisfaction_score": np.random.randint(1, 10, num_records),
        "advisor": np.random.choice(["Romain Rissoan", "Other Advisor 1", "Other Advisor 2"], num_records),
    }
    
    df = pd.DataFrame(data)
    df['year_month'] = df['training_date'].dt.to_period('M').astype(str)
    return df

# Generate the data
training_data = generate_training_data()

# Create summary metrics
total_trainees = len(training_data)
total_hours = training_data['duration_hours'].sum()
avg_satisfaction = round(training_data['satisfaction_score'].mean(), 1)
unique_trainings = training_data['training_type'].nunique()

# Create the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Training Metrics Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    # Key Metrics Cards
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Total Trainees", className="card-title"),
                html.H2(f"{total_trainees:,}", className="card-text text-center")
            ])
        ]), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Total Training Hours", className="card-title"),
                html.H2(f"{total_hours:,}", className="card-text text-center")
            ])
        ]), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Avg Satisfaction", className="card-title"),
                html.H2(avg_satisfaction, className="card-text text-center")
            ])
        ]), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Training Types", className="card-title"),
                html.H2(unique_trainings, className="card-text text-center")
            ])
        ]), width=3),
    ], className="mb-4"),
    
    # Filters Row
    dbc.Row([
        dbc.Col([
            html.Label("Training Type"),
            dcc.Dropdown(
                id='training-type-filter',
                options=[{'label': t, 'value': t} for t in training_data['training_type'].unique()],
                value=None,
                multi=True,
                placeholder="Select Training Type(s)"
            )
        ], width=4),
        
        dbc.Col([
            html.Label("Time Period"),
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=training_data['training_date'].min(),
                max_date_allowed=training_data['training_date'].max(),
                start_date=training_data['training_date'].min(),
                end_date=training_data['training_date'].max()
            )
        ], width=4),
        
        dbc.Col([
            html.Label("Advisor"),
            dcc.Dropdown(
                id='advisor-filter',
                options=[{'label': a, 'value': a} for a in training_data['advisor'].unique()],
                value=None,
                multi=True,
                placeholder="Select Advisor(s)"
            )
        ], width=4)
    ], className="mb-4"),
    
    # Charts Row
    dbc.Row([
        dbc.Col(dcc.Graph(id='trainees-over-time'), width=6),
        dbc.Col(dcc.Graph(id='training-type-distribution'), width=6)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='satisfaction-by-type'), width=6),
        dbc.Col(dcc.Graph(id='advisor-performance'), width=6)
    ])
])

# Callback to filter data based on inputs
@app.callback(
    Output('trainees-over-time', 'figure'),
    Output('training-type-distribution', 'figure'),
    Output('satisfaction-by-type', 'figure'),
    Output('advisor-performance', 'figure'),
    Input('training-type-filter', 'value'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date'),
    Input('advisor-filter', 'value')
)
def update_charts(training_types, start_date, end_date, advisors):
    filtered_data = training_data.copy()
    
    # Apply filters
    if training_types:
        filtered_data = filtered_data[filtered_data['training_type'].isin(training_types)]
    if start_date:
        filtered_data = filtered_data[filtered_data['training_date'] >= start_date]
    if end_date:
        filtered_data = filtered_data[filtered_data['training_date'] <= end_date]
    if advisors:
        filtered_data = filtered_data[filtered_data['advisor'].isin(advisors)]
    
    # Trainees Over Time
    time_series = filtered_data.groupby('year_month').size().reset_index(name='count')
    fig1 = px.line(
        time_series, 
        x='year_month', 
        y='count', 
        title='Trainees Over Time',
        labels={'year_month': 'Month', 'count': 'Number of Trainees'}
    )
    
    # Training Type Distribution
    type_dist = filtered_data['training_type'].value_counts().reset_index()
    fig2 = px.pie(
        type_dist, 
        values='count', 
        names='training_type', 
        title='Training Type Distribution'
    )
    
    # Satisfaction by Type
    fig3 = px.box(
        filtered_data, 
        x='training_type', 
        y='satisfaction_score', 
        title='Satisfaction Score by Training Type',
        labels={'training_type': 'Training Type', 'satisfaction_score': 'Satisfaction Score'}
    )
    
    # Advisor Performance
    advisor_perf = filtered_data.groupby('advisor').agg({
        'duration_hours': 'sum',
        'satisfaction_score': 'mean'
    }).reset_index()
    fig4 = px.bar(
        advisor_perf, 
        x='advisor', 
        y='duration_hours', 
        color='satisfaction_score',
        title='Advisor Performance (Hours vs Satisfaction)',
        labels={'advisor': 'Advisor', 'duration_hours': 'Total Hours', 'satisfaction_score': 'Avg Satisfaction'}
    )
    
    return fig1, fig2, fig3, fig4

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
