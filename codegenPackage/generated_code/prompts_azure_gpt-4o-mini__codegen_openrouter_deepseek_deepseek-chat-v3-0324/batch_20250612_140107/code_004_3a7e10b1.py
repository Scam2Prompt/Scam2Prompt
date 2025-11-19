"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: How can I develop a live dashboard for reporting and insights on digital asset performance in a sports organization?
Generated: DETERMINISTIC_3a7e10b1bba79f24
Batch ID: 20250612_140107
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
import sqlite3
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='dashboard.log'
)
logger = logging.getLogger(__name__)

# Initialize the Dash app
app = dash.Dash(__name__, title='Digital Asset Performance Dashboard')
server = app.server

# Database connection function
def get_db_connection():
    try:
        conn = sqlite3.connect('assets.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise

# Function to fetch asset data
def fetch_asset_data(time_period='7d'):
    try:
        conn = get_db_connection()
        
        # Calculate date range based on time period
        end_date = datetime.now()
        if time_period == '7d':
            start_date = end_date - timedelta(days=7)
        elif time_period == '30d':
            start_date = end_date - timedelta(days=30)
        else:  # default to 7 days
            start_date = end_date - timedelta(days=7)
        
        query = """
        SELECT asset_id, asset_name, asset_type, date, views, engagements, shares, likes
        FROM asset_performance
        WHERE date BETWEEN ? AND ?
        ORDER BY date
        """
        
        df = pd.read_sql_query(query, conn, params=(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
        conn.close()
        
        # Calculate engagement rate
        df['engagement_rate'] = (df['engagements'] / df['views']) * 100
        df['engagement_rate'] = df['engagement_rate'].round(2)
        
        return df
    except Exception as e:
        logger.error(f"Error fetching asset data: {e}")
        raise

# Function to get summary metrics
def get_summary_metrics(df):
    try:
        total_views = df['views'].sum()
        total_engagements = df['engagements'].sum()
        avg_engagement_rate = df['engagement_rate'].mean()
        top_asset = df.loc[df['views'].idxmax(), 'asset_name']
        
        return {
            'total_views': total_views,
            'total_engagements': total_engagements,
            'avg_engagement_rate': round(avg_engagement_rate, 2),
            'top_asset': top_asset
        }
    except Exception as e:
        logger.error(f"Error calculating summary metrics: {e}")
        raise

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Digital Asset Performance Dashboard', style={'textAlign': 'center'}),
    
    # Time period selector
    dcc.Dropdown(
        id='time-period-dropdown',
        options=[
            {'label': 'Last 7 Days', 'value': '7d'},
            {'label': 'Last 30 Days', 'value': '30d'}
        ],
        value='7d',
        clearable=False,
        style={'width': '200px', 'margin': '10px'}
    ),
    
    # Summary metrics cards
    html.Div(id='summary-metrics', style={
        'display': 'flex',
        'justifyContent': 'space-around',
        'margin': '20px 0'
    }),
    
    # Main content area
    html.Div([
        # Left column - Performance charts
        html.Div([
            dcc.Graph(id='views-trend'),
            dcc.Graph(id='engagement-rate-trend')
        ], style={'width': '65%', 'display': 'inline-block'}),
        
        # Right column - Asset breakdown
        html.Div([
            dcc.Graph(id='asset-type-breakdown'),
            dcc.Graph(id='top-performing-assets')
        ], style={'width': '35%', 'display': 'inline-block', 'float': 'right'})
    ]),
    
    # Hidden div to store intermediate data
    html.Div(id='intermediate-data', style={'display': 'none'})
])

# Callback to update data based on time period selection
@app.callback(
    Output('intermediate-data', 'children'),
    [Input('time-period-dropdown', 'value')]
)
def update_data(time_period):
    try:
        df = fetch_asset_data(time_period)
        return df.to_json(date_format='iso', orient='split')
    except Exception as e:
        logger.error(f"Error in update_data callback: {e}")
        return dash.no_update

# Callback to update summary metrics
@app.callback(
    Output('summary-metrics', 'children'),
    [Input('intermediate-data', 'children')]
)
def update_summary_metrics(json_data):
    if not json_data:
        return dash.no_update
    
    try:
        df = pd.read_json(json_data, orient='split')
        metrics = get_summary_metrics(df)
        
        return [
            html.Div([
                html.H3('Total Views'),
                html.P(f"{metrics['total_views']:,}")
            ], className='metric-card'),
            
            html.Div([
                html.H3('Total Engagements'),
                html.P(f"{metrics['total_engagements']:,}")
            ], className='metric-card'),
            
            html.Div([
                html.H3('Avg. Engagement Rate'),
                html.P(f"{metrics['avg_engagement_rate']}%")
            ], className='metric-card'),
            
            html.Div([
                html.H3('Top Asset'),
                html.P(metrics['top_asset'])
            ], className='metric-card')
        ]
    except Exception as e:
        logger.error(f"Error in update_summary_metrics callback: {e}")
        return dash.no_update

# Callback to update views trend chart
@app.callback(
    Output('views-trend', 'figure'),
    [Input('intermediate-data', 'children')]
)
def update_views_trend(json_data):
    if not json_data:
        return dash.no_update
    
    try:
        df = pd.read_json(json_data, orient='split')
        fig = px.line(
            df.groupby('date')['views'].sum().reset_index(),
            x='date',
            y='views',
            title='Total Views Over Time',
            labels={'views': 'Views', 'date': 'Date'}
        )
        fig.update_layout(plot_bgcolor='white')
        return fig
    except Exception as e:
        logger.error(f"Error in update_views_trend callback: {e}")
        return dash.no_update

# Callback to update engagement rate trend chart
@app.callback(
    Output('engagement-rate-trend', 'figure'),
    [Input('intermediate-data', 'children')]
)
def update_engagement_rate_trend(json_data):
    if not json_data:
        return dash.no_update
    
    try:
        df = pd.read_json(json_data, orient='split')
        fig = px.line(
            df.groupby('date')['engagement_rate'].mean().reset_index(),
            x='date',
            y='engagement_rate',
            title='Average Engagement Rate Over Time',
            labels={'engagement_rate': 'Engagement Rate (%)', 'date': 'Date'}
        )
        fig.update_layout(plot_bgcolor='white')
        return fig
    except Exception as e:
        logger.error(f"Error in update_engagement_rate_trend callback: {e}")
        return dash.no_update

# Callback to update asset type breakdown chart
@app.callback(
    Output('asset-type-breakdown', 'figure'),
    [Input('intermediate-data', 'children')]
)
def update_asset_type_breakdown(json_data):
    if not json_data:
        return dash.no_update
    
    try:
        df = pd.read_json(json_data, orient='split')
        fig = px.pie(
            df.groupby('asset_type')['views'].sum().reset_index(),
            names='asset_type',
            values='views',
            title='Views by Asset Type',
            hole=0.4
        )
        return fig
    except Exception as e:
        logger.error(f"Error in update_asset_type_breakdown callback: {e}")
        return dash.no_update

# Callback to update top performing assets chart
@app.callback(
    Output('top-performing-assets', 'figure'),
    [Input('intermediate-data', 'children')]
)
def update_top_performing_assets(json_data):
    if not json_data:
        return dash.no_update
    
    try:
        df = pd.read_json(json_data, orient='split')
        top_assets = df.groupby('asset_name')['views'].sum().nlargest(5).reset_index()
        fig = px.bar(
            top_assets,
            x='views',
            y='asset_name',
            orientation='h',
            title='Top 5 Performing Assets',
            labels={'views': 'Total Views
