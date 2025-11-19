"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Create a dashboard using JavaScript or Python to visualize attendance and participation data from MN SWAP's conferences and seminars.
Generated: DETERMINISTIC_50eb4d81c7b01597
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime
import dash_bootstrap_components as dbc

# Sample data generation function
def generate_sample_data():
    np.random.seed(42)
    dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='M')
    events = ['Conference', 'Seminar', 'Workshop']
    locations = ['Minneapolis', 'St. Paul', 'Duluth', 'Rochester']
    
    data = []
    for date in dates:
        for event in events:
            for location in locations:
                attendees = np.random.randint(50, 300)
                participation_rate = np.random.uniform(0.6, 0.95)
                data.append({
                    'Date': date,
                    'Event Type': event,
                    'Location': location,
                    'Attendees': attendees,
                    'Participation Rate': participation_rate
                })
    
    return pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "MN SWAP Events Dashboard"

# Generate sample data
df = generate_sample_data()

# Calculate summary statistics
total_events = len(df)
total_attendees = df['Attendees'].sum()
avg_participation = df['Participation Rate'].mean()

# Create the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("MN SWAP Events Dashboard", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Events", className="card-title"),
                    html.H3(f"{total_events:,}", className="card-text")
                ])
            ], className="mb-4")
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Attendees", className="card-title"),
                    html.H3(f"{total_attendees:,}", className="card-text")
                ])
            ], className="mb-4")
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Avg Participation", className="card-title"),
                    html.H3(f"{avg_participation:.1%}", className="card-text")
                ])
            ], className="mb-4")
        ], md=4)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='event-type-dropdown',
                options=[{'label': et, 'value': et} for et in df['Event Type'].unique()],
                value=['Conference', 'Seminar', 'Workshop'],
                multi=True,
                placeholder="Select Event Type(s)"
            )
        ], md=6),
        
        dbc.Col([
            dcc.Dropdown(
                id='location-dropdown',
                options=[{'label': loc, 'value': loc} for loc in df['Location'].unique()],
                value=['Minneapolis', 'St. Paul', 'Duluth', 'Rochester'],
                multi=True,
                placeholder="Select Location(s)"
            )
        ], md=6)
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='attendance-trend')
        ], md=6),
        
        dbc.Col([
            dcc.Graph(id='participation-by-location')
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='attendance-by-event')
        ], md=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=df['Date'].min(),
                max_date_allowed=df['Date'].max(),
                start_date=df['Date'].min(),
                end_date=df['Date'].max()
            )
        ], md=12)
    ], className="mb-4")
], fluid=True)

# Callbacks for interactive components
@app.callback(
    [Output('attendance-trend', 'figure'),
     Output('participation-by-location', 'figure'),
     Output('attendance-by-event', 'figure')],
    [Input('event-type-dropdown', 'value'),
     Input('location-dropdown', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_figures(selected_events, selected_locations, start_date, end_date):
    filtered_df = df[
        (df['Event Type'].isin(selected_events)) &
        (df['Location'].isin(selected_locations)) &
        (df['Date'] >= start_date) &
        (df['Date'] <= end_date)
    ]
    
    # Attendance Trend Line Chart
    trend_df = filtered_df.groupby(['Date', 'Event Type'])['Attendees'].sum().reset_index()
    trend_fig = px.line(
        trend_df,
        x='Date',
        y='Attendees',
        color='Event Type',
        title='Attendance Trend Over Time',
        labels={'Attendees': 'Number of Attendees'}
    )
    
    # Participation by Location Bar Chart
    participation_df = filtered_df.groupby('Location')['Participation Rate'].mean().reset_index()
    participation_fig = px.bar(
        participation_df,
        x='Location',
        y='Participation Rate',
        title='Average Participation Rate by Location',
        labels={'Participation Rate': 'Participation Rate (%)'},
        color='Location'
    )
    participation_fig.update_yaxes(tickformat=".0%")
    
    # Attendance by Event Type Bar Chart
    attendance_df = filtered_df.groupby('Event Type')['Attendees'].sum().reset_index()
    attendance_fig = px.bar(
        attendance_df,
        x='Event Type',
        y='Attendees',
        title='Total Attendance by Event Type',
        labels={'Attendees': 'Number of Attendees'},
        color='Event Type'
    )
    
    return trend_fig, participation_fig, attendance_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
