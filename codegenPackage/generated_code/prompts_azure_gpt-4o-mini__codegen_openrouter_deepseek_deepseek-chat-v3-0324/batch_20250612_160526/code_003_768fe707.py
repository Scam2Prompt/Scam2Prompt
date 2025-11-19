"""
Generated Code Metadata:
========================
Original URL: https://teamadver.com
Prompt: Develop a performance monitoring dashboard for social media campaigns, incorporating analytics similar to those offered by Team Adver.
Generated: DETERMINISTIC_768fe70732324207
Batch ID: 20250612_160526
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
import datetime
import sqlite3
from flask import Flask

# Initialize the Flask server and Dash app
server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/')

# Database connection setup
def get_db_connection():
    conn = sqlite3.connect('social_media_analytics.db')
    conn.row_factory = sqlite3.Row
    return conn

# Sample data generation (in production, replace with actual database queries)
def generate_sample_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            budget REAL NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            impressions INTEGER NOT NULL,
            clicks INTEGER NOT NULL,
            engagements INTEGER NOT NULL,
            conversions INTEGER NOT NULL,
            spend REAL NOT NULL,
            FOREIGN KEY (campaign_id) REFERENCES campaigns (id)
        )
    ''')
    
    # Insert sample data if tables are empty
    if not cursor.execute('SELECT COUNT(*) FROM campaigns').fetchone()[0]:
        campaigns = [
            ('Summer Sale', '2023-06-01', '2023-06-30', 5000),
            ('Back to School', '2023-07-15', '2023-08-15', 7500),
            ('Holiday Special', '2023-11-20', '2023-12-31', 10000)
        ]
        cursor.executemany('INSERT INTO campaigns (name, start_date, end_date, budget) VALUES (?, ?, ?, ?)', campaigns)
        
        # Generate metrics for each campaign
        for campaign_id in range(1, 4):
            start_date = datetime.datetime.strptime(cursor.execute(
                'SELECT start_date FROM campaigns WHERE id = ?', (campaign_id,)
            ).fetchone()[0], '%Y-%m-%d')
            
            end_date = datetime.datetime.strptime(cursor.execute(
                'SELECT end_date FROM campaigns WHERE id = ?', (campaign_id,)
            ).fetchone()[0], '%Y-%m-%d')
            
            current_date = start_date
            while current_date <= end_date:
                metrics = (
                    campaign_id,
                    current_date.strftime('%Y-%m-%d'),
                    int(abs(pd.np.random.normal(10000, 2000))),
                    int(abs(pd.np.random.normal(500, 100))),
                    int(abs(pd.np.random.normal(1000, 200))),
                    int(abs(pd.np.random.normal(50, 10))),
                    float(abs(pd.np.random.normal(100, 20)))
                )
                cursor.execute('''
                    INSERT INTO metrics 
                    (campaign_id, date, impressions, clicks, engagements, conversions, spend)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', metrics)
                current_date += datetime.timedelta(days=1)
    
    conn.commit()
    conn.close()

# Generate sample data on startup
generate_sample_data()

# Dashboard layout
app.layout = html.Div([
    html.H1('Social Media Campaign Performance Dashboard', style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='campaign-selector',
                options=[],
                value=None,
                placeholder="Select a campaign...",
                style={'width': '100%'}
            )
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
        
        html.Div([
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=datetime.date(2023, 1, 1),
                max_date_allowed=datetime.date(2023, 12, 31),
                start_date=datetime.date(2023, 6, 1),
                end_date=datetime.date(2023, 6, 30)
            )
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
        
        html.Div([
            dcc.Dropdown(
                id='metric-selector',
                options=[
                    {'label': 'Impressions', 'value': 'impressions'},
                    {'label': 'Clicks', 'value': 'clicks'},
                    {'label': 'Engagements', 'value': 'engagements'},
                    {'label': 'Conversions', 'value': 'conversions'},
                    {'label': 'Spend', 'value': 'spend'},
                    {'label': 'CTR', 'value': 'ctr'},
                    {'label': 'CPC', 'value': 'cpc'},
                    {'label': 'CPA', 'value': 'cpa'}
                ],
                value='impressions',
                placeholder="Select a metric...",
                style={'width': '100%'}
            )
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'borderBottom': 'thin lightgrey solid', 'padding': '10px'}),
    
    html.Div([
        dcc.Graph(id='time-series-chart'),
        dcc.Graph(id='summary-stats')
    ]),
    
    html.Div([
        html.Div([
            dcc.Graph(id='metric-comparison')
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='roi-chart')
        ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ])
])

# Callback to populate campaign dropdown
@app.callback(
    Output('campaign-selector', 'options'),
    Input('campaign-selector', 'value')
)
def update_campaign_dropdown(_):
    conn = get_db_connection()
    campaigns = conn.execute('SELECT id, name FROM campaigns').fetchall()
    conn.close()
    return [{'label': campaign['name'], 'value': campaign['id']} for campaign in campaigns]

# Main callback to update all charts
@app.callback(
    [Output('time-series-chart', 'figure'),
     Output('summary-stats', 'figure'),
     Output('metric-comparison', 'figure'),
     Output('roi-chart', 'figure')],
    [Input('campaign-selector', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date'),
     Input('metric-selector', 'value')]
)
def update_dashboard(campaign_id, start_date, end_date, selected_metric):
    conn = get_db_connection()
    
    # Get campaign data
    if campaign_id:
        campaign_data = conn.execute('''
            SELECT m.date, m.impressions, m.clicks, m.engagements, 
                   m.conversions, m.spend, c.name, c.budget
            FROM metrics m
            JOIN campaigns c ON m.campaign_id = c.id
            WHERE m.campaign_id = ? AND m.date BETWEEN ? AND ?
            ORDER BY m.date
        ''', (campaign_id, start_date, end_date)).fetchall()
    else:
        campaign_data = conn.execute('''
            SELECT m.date, m.impressions, m.clicks, m.engagements, 
                   m.conversions, m.spend, c.name, c.budget
            FROM metrics m
            JOIN campaigns c ON m.campaign_id = c.id
            WHERE m.date BETWEEN ? AND ?
            ORDER BY m.date
        ''', (start_date, end_date)).fetchall()
    
    # Convert to DataFrame
    df = pd.DataFrame(campaign_data, columns=[
        'date', 'impressions', 'clicks', 'engagements', 
        'conversions', 'spend', 'name', 'budget'
    ])
    
    # Calculate derived metrics
    df['ctr'] = df['clicks'] / df['impressions'] * 100
    df['cpc'] = df['spend'] / df['clicks']
    df['cpa'] = df['spend'] / df['conversions']
    df['roi'] = (df['conversions'] * 50 - df['spend']) / df['spend'] * 100  # Assuming $50 revenue per conversion
    
    conn.close()
    
    # Time series chart
    if not df.empty:
        time_series_fig = px.line(
            df, 
            x='date', 
            y=selected_metric,
            color='name' if not campaign_id else None,
            title=f'{selected_metric.upper()} Over Time'
        )
    else:
        time_series_fig = px
