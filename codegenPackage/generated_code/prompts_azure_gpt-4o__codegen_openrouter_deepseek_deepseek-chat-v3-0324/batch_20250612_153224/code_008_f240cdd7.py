"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Generate code to create a dashboard for tracking hectares monitored, visits registered, and food production metrics, inspired by Azagros' success cases.
Generated: DETERMINISTIC_f240cdd7074ad0cb
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://codepen.io/chriddyp/pen/bWLwgP.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Agro Monitoring Dashboard"

# Database connection function
def get_db_connection():
    try:
        conn = sqlite3.connect('agro_monitoring.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise

# Create sample data if database doesn't exist
def initialize_database():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hectares (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT NOT NULL,
                hectares_monitored REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS visits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT NOT NULL,
                visits_count INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS production (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT NOT NULL,
                crop_type TEXT NOT NULL,
                yield_per_hectare REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        
        # Check if tables are empty and insert sample data
        cursor.execute("SELECT COUNT(*) FROM hectares")
        if cursor.fetchone()[0] == 0:
            sample_hectares = [
                ('North', 150.5, '2023-01-01'),
                ('South', 200.2, '2023-01-01'),
                ('East', 180.7, '2023-01-01'),
                ('West', 220.3, '2023-01-01'),
                ('North', 160.2, '2023-02-01'),
                ('South', 210.5, '2023-02-01'),
                ('East', 190.1, '2023-02-01'),
                ('West', 230.8, '2023-02-01'),
            ]
            cursor.executemany("INSERT INTO hectares (region, hectares_monitored, date) VALUES (?, ?, ?)", sample_hectares)
            
        cursor.execute("SELECT COUNT(*) FROM visits")
        if cursor.fetchone()[0] == 0:
            sample_visits = [
                ('North', 45, '2023-01-01'),
                ('South', 60, '2023-01-01'),
                ('East', 55, '2023-01-01'),
                ('West', 70, '2023-01-01'),
                ('North', 50, '2023-02-01'),
                ('South', 65, '2023-02-01'),
                ('East', 60, '2023-02-01'),
                ('West', 75, '2023-02-01'),
            ]
            cursor.executemany("INSERT INTO visits (region, visits_count, date) VALUES (?, ?, ?)", sample_visits)
            
        cursor.execute("SELECT COUNT(*) FROM production")
        if cursor.fetchone()[0] == 0:
            sample_production = [
                ('North', 'Wheat', 3.5, '2023-01-01'),
                ('South', 'Wheat', 4.2, '2023-01-01'),
                ('East', 'Corn', 5.1, '2023-01-01'),
                ('West', 'Corn', 5.8, '2023-01-01'),
                ('North', 'Wheat', 3.8, '2023-02-01'),
                ('South', 'Wheat', 4.5, '2023-02-01'),
                ('East', 'Corn', 5.4, '2023-02-01'),
                ('West', 'Corn', 6.0, '2023-02-01'),
            ]
            cursor.executemany("INSERT INTO production (region, crop_type, yield_per_hectare, date) VALUES (?, ?, ?, ?)", sample_production)
            
        conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")
        raise
    finally:
        conn.close()

# Initialize database
initialize_database()

# Helper function to fetch data
def fetch_data(query, params=None):
    try:
        conn = get_db_connection()
        if params:
            df = pd.read_sql_query(query, conn, params=params)
        else:
            df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        raise
    finally:
        conn.close()

# App layout
app.layout = html.Div([
    html.H1("Agro Monitoring Dashboard", style={'textAlign': 'center'}),
    
    # Filters
    html.Div([
        html.Div([
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=datetime(2023, 1, 1),
                max_date_allowed=datetime(2023, 12, 31),
                start_date=datetime(2023, 1, 1),
                end_date=datetime(2023, 2, 1)
            ),
        ], style={'width': '30%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Dropdown(
                id='region-filter',
                options=[
                    {'label': 'All Regions', 'value': 'all'},
                    {'label': 'North', 'value': 'North'},
                    {'label': 'South', 'value': 'South'},
                    {'label': 'East', 'value': 'East'},
                    {'label': 'West', 'value': 'West'}
                ],
                value='all',
                clearable=False
            )
        ], style={'width': '20%', 'display': 'inline-block', 'marginLeft': '10px'}),
        
        html.Div([
            dcc.Dropdown(
                id='crop-filter',
                options=[
                    {'label': 'All Crops', 'value': 'all'},
                    {'label': 'Wheat', 'value': 'Wheat'},
                    {'label': 'Corn', 'value': 'Corn'}
                ],
                value='all',
                clearable=False
            )
        ], style={'width': '20%', 'display': 'inline-block', 'marginLeft': '10px'}),
    ], style={'marginBottom': '20px'}),
    
    # KPI Cards
    html.Div([
        html.Div([
            html.Div(id='total-hectares', className='kpi-card'),
        ], className='kpi-container'),
        
        html.Div([
            html.Div(id='total-visits', className='kpi-card'),
        ], className='kpi-container'),
        
        html.Div([
            html.Div(id='avg-yield', className='kpi-card'),
        ], className='kpi-container'),
    ], className='kpi-row'),
    
    # Charts
    html.Div([
        dcc.Graph(id='hectares-chart'),
    ], style={'width': '49%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='visits-chart'),
    ], style={'width': '49%', 'display': 'inline-block', 'float': 'right'}),
    
    html.Div([
        dcc.Graph(id='yield-chart'),
    ], style={'width': '100%'}),
    
    # Hidden div for storing intermediate data
    html.Div(id='intermediate-data', style={'display': 'none'})
])

# CSS styles
app.css.append_css({
    'external_url': 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'
})

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# Custom CSS
app.css.append_css({
    'external_url': (
        '.kpi-card {'
        '  background: white;'
        '  border-radius: 5px;'
        '  padding: 20px;'
        '  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);'
        '  text-align: center;'
        '}'
        '.kpi-container {'
        '  padding: 10px;'
        '}'
        '.kpi-row {'
        '  display: flex;'
        '  justify-content: space-between;
