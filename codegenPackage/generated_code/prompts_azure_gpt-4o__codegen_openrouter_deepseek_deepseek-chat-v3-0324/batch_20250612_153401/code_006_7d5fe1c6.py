"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Develop a dashboard interface for tracking client satisfaction metrics in a CMS system designed for cooperative businesses.
Generated: DETERMINISTIC_7d5fe1c634bb37ac
Batch ID: 20250612_153401
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
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import sqlite3
from typing import Optional, Dict, List, Tuple

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Cooperative CMS - Client Satisfaction Dashboard"

# Database connection function
def get_db_connection():
    """Create and return a connection to the SQLite database."""
    try:
        conn = sqlite3.connect('cooperative_cms.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        raise

# Sample data initialization (in a real app, this would be in the database)
def initialize_sample_data():
    """Initialize sample data if database is empty."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS satisfaction_surveys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            score INTEGER NOT NULL CHECK(score BETWEEN 1 AND 5),
            feedback TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            category TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            join_date DATE NOT NULL,
            cooperative_member BOOLEAN NOT NULL
        )
    ''')
    
    # Check if data exists
    cursor.execute("SELECT COUNT(*) FROM satisfaction_surveys")
    if cursor.fetchone()[0] == 0:
        # Insert sample data
        sample_scores = [
            (1, 4, "Good service", "support", "2023-01-15"),
            (2, 5, "Excellent!", "sales", "2023-01-16"),
            (3, 3, "Could be better", "support", "2023-01-17"),
            (1, 5, "Very satisfied", "product", "2023-01-18"),
            (2, 2, "Poor response time", "support", "2023-01-19"),
            (3, 4, None, "sales", "2023-01-20"),
            (1, 1, "Terrible experience", "product", "2023-01-21"),
            (2, 5, "Will recommend", "support", "2023-01-22"),
            (3, 3, "Average", "sales", "2023-01-23"),
        ]
        
        sample_clients = [
            (1, "ABC Cooperative", "2022-05-10", True),
            (2, "XYZ Collective", "2022-08-15", True),
            (3, "Acme Inc", "2023-01-01", False),
        ]
        
        cursor.executemany(
            "INSERT INTO satisfaction_surveys (client_id, score, feedback, category, timestamp) VALUES (?, ?, ?, ?, ?)",
            sample_scores
        )
        
        cursor.executemany(
            "INSERT INTO clients (id, name, join_date, cooperative_member) VALUES (?, ?, ?, ?)",
            sample_clients
        )
        
        conn.commit()
    
    conn.close()

# Call the initialization function
initialize_sample_data()

def fetch_satisfaction_data(days_back: Optional[int] = None) -> pd.DataFrame:
    """Fetch satisfaction survey data from the database.
    
    Args:
        days_back: Number of days to look back. If None, fetch all data.
    
    Returns:
        DataFrame containing the survey data.
    """
    query = """
        SELECT s.*, c.name as client_name, c.cooperative_member
        FROM satisfaction_surveys s
        JOIN clients c ON s.client_id = c.id
    """
    
    if days_back is not None:
        cutoff_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
        query += f" WHERE s.timestamp >= '{cutoff_date}'"
    
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    
    return df

def calculate_metrics(df: pd.DataFrame) -> Dict[str, float]:
    """Calculate key satisfaction metrics from the data.
    
    Args:
        df: DataFrame containing survey data.
    
    Returns:
        Dictionary of calculated metrics.
    """
    if df.empty:
        return {
            'average_score': 0,
            'response_count': 0,
            'promoter_percentage': 0,
            'detractor_percentage': 0
        }
    
    avg_score = df['score'].mean()
    response_count = len(df)
    
    # NPS calculation (Promoters - Detractors)
    promoters = len(df[df['score'] >= 4])
    detractors = len(df[df['score'] <= 2])
    nps = ((promoters - detractors) / response_count) * 100 if response_count > 0 else 0
    
    return {
        'average_score': round(avg_score, 1),
        'response_count': response_count,
        'nps': round(nps, 1),
        'promoter_percentage': round((promoters / response_count) * 100, 1) if response_count > 0 else 0,
        'detractor_percentage': round((detractors / response_count) * 100, 1) if response_count > 0 else 0
    }

def get_time_series_data() -> pd.DataFrame:
    """Get data aggregated by time for trend analysis."""
    df = fetch_satisfaction_data()
    if df.empty:
        return pd.DataFrame()
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    time_series = df.groupby('date').agg({
        'score': 'mean',
        'id': 'count'
    }).rename(columns={'id': 'response_count'}).reset_index()
    
    return time_series

# Layout components
def create_metric_card(title: str, value: str, delta: Optional[str] = None) -> dbc.Card:
    """Create a metric card component."""
    return dbc.Card(
        dbc.CardBody([
            html.H6(title, className="card-title"),
            html.H4(value, className="card-value"),
            html.Small(delta, className="card-delta") if delta else None
        ]),
        className="metric-card"
    )

def create_feedback_table() -> dbc.Table:
    """Create a table showing recent feedback."""
    df = fetch_satisfaction_data(days_back=30)
    if df.empty:
        return dbc.Table([html.Tr(html.Td("No feedback data available"))])
    
    # Get most recent feedback with comments
    feedback_df = df[df['feedback'].notna()].sort_values('timestamp', ascending=False).head(5)
    
    rows = []
    for _, row in feedback_df.iterrows():
        rows.append(html.Tr([
            html.Td(row['client_name']),
            html.Td(row['score']),
            html.Td(row['feedback']),
            html.Td(row['timestamp'].split()[0])  # Just the date part
        ]))
    
    return dbc.Table(
        [html.Thead(html.Tr([
            html.Th("Client"),
            html.Th("Score"),
            html.Th("Feedback"),
            html.Th("Date")
        ]))] + rows,
        striped=True,
        bordered=True,
        hover=True
    )

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Client Satisfaction Dashboard", className="text-center my-4"), width=12)
    ]),
    
    # Time period selector
    dbc.Row([
        dbc.Col([
            html.Label("Time Period:"),
            dcc.Dropdown(
                id='time-period-dropdown',
                options=[
                    {'label': 'Last 7 days', 'value': 7},
                    {'label': 'Last 30 days', 'value': 30},
                    {'label': 'Last 90 days', 'value': 90},
                    {'label': 'All time', 'value': None}
                ],
                value=30,
                clearable=False
            )
        ], width=12, md=4)
    ], className="mb-4"),
    
    # Key metrics row
    dbc.Row([
        dbc.Col(create_metric_card("Average Score", "0", "+0.5 from last period"), md=3, id='avg-score-card'),
        dbc.Col(create_metric_card("Responses", "0", "+3 from last period"), md=2, id='responses-card'),
        dbc.Col(create_metric_card("NPS Score", "0", "+
