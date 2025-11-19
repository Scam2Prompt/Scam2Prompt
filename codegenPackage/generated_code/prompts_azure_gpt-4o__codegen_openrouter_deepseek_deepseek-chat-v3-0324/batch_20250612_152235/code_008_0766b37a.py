"""
Generated Code Metadata:
========================
Original URL: https://kakaxa.pages.dev
Prompt: Develop a marketing dashboard for tracking airdrop campaigns and pre-sale progress for a meme cryptocurrency like $KAKAXA.
Generated: DETERMINISTIC_0766b37a24220c4d
Batch ID: 20250612_152235
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
from sqlite3 import Error

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "$KAKAXA Marketing Dashboard"

# Database setup
def create_connection():
    """Create a database connection to SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect('kakaxa_marketing.db')
        print(f"SQLite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn

def initialize_database():
    """Initialize database tables if they don't exist"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            # Airdrop campaigns table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS airdrop_campaigns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    campaign_name TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    total_tokens INTEGER NOT NULL,
                    distributed_tokens INTEGER DEFAULT 0,
                    participants INTEGER DEFAULT 0,
                    status TEXT DEFAULT 'active'
                )
            ''')
            
            # Presale progress table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS presale_progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phase INTEGER NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    target_amount REAL NOT NULL,
                    raised_amount REAL DEFAULT 0,
                    token_price REAL NOT NULL,
                    status TEXT DEFAULT 'active'
                )
            ''')
            
            # Social metrics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS social_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    twitter_followers INTEGER DEFAULT 0,
                    telegram_members INTEGER DEFAULT 0,
                    discord_members INTEGER DEFAULT 0,
                    website_visits INTEGER DEFAULT 0
                )
            ''')
            
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

# Initialize database on startup
initialize_database()

# Sample data insertion (for demo purposes)
def insert_sample_data():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            # Check if data already exists
            cursor.execute("SELECT COUNT(*) FROM airdrop_campaigns")
            if cursor.fetchone()[0] == 0:
                # Insert sample airdrop data
                airdrops = [
                    ('KAKAXA Airdrop #1', '2023-01-01', '2023-01-31', 1000000, 750000, 12500, 'completed'),
                    ('KAKAXA Airdrop #2', '2023-02-15', '2023-03-15', 1500000, 900000, 18000, 'active'),
                    ('KAKAXA Airdrop #3', '2023-04-01', '2023-04-30', 2000000, 0, 0, 'upcoming')
                ]
                cursor.executemany('''
                    INSERT INTO airdrop_campaigns 
                    (campaign_name, start_date, end_date, total_tokens, distributed_tokens, participants, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', airdrops)
                
                # Insert sample presale data
                presales = [
                    (1, '2023-01-01', '2023-01-31', 500000, 450000, 0.0001, 'completed'),
                    (2, '2023-02-01', '2023-02-28', 750000, 600000, 0.00015, 'active'),
                    (3, '2023-03-01', '2023-03-31', 1000000, 0, 0.0002, 'upcoming')
                ]
                cursor.executemany('''
                    INSERT INTO presale_progress 
                    (phase, start_date, end_date, target_amount, raised_amount, token_price, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', presales)
                
                # Insert sample social metrics
                today = datetime.now().strftime('%Y-%m-%d')
                yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
                week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
                
                social_data = [
                    (week_ago, 1250, 3200, 1800, 4500),
                    (yesterday, 3800, 7500, 4200, 12500),
                    (today, 4200, 8200, 4800, 15000)
                ]
                cursor.executemany('''
                    INSERT INTO social_metrics 
                    (date, twitter_followers, telegram_members, discord_members, website_visits)
                    VALUES (?, ?, ?, ?, ?)
                ''', social_data)
                
                conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

insert_sample_data()

# Helper functions
def get_airdrop_data():
    """Fetch airdrop campaign data from database"""
    conn = create_connection()
    df = pd.read_sql("SELECT * FROM airdrop_campaigns", conn)
    conn.close()
    return df

def get_presale_data():
    """Fetch presale data from database"""
    conn = create_connection()
    df = pd.read_sql("SELECT * FROM presale_progress", conn)
    conn.close()
    return df

def get_social_metrics():
    """Fetch social metrics data from database"""
    conn = create_connection()
    df = pd.read_sql("SELECT * FROM social_metrics ORDER BY date DESC LIMIT 7", conn)
    conn.close()
    return df

# Dashboard layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("$KAKAXA Marketing Dashboard", className="text-center my-4"), width=12)
    ]),
    
    # Summary Cards Row
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Total Airdrop Participants"),
            dbc.CardBody([
                html.H4(id='total-participants', className="card-title"),
                html.P("Across all campaigns", className="card-text")
            ])
        ], color="primary", inverse=True), md=4),
        
        dbc.Col(dbc.Card([
            dbc.CardHeader("Total Presale Raised"),
            dbc.CardBody([
                html.H4(id='total-raised', className="card-title"),
                html.P("Current phase progress", className="card-text")
            ])
        ], color="success", inverse=True), md=4),
        
        dbc.Col(dbc.Card([
            dbc.CardHeader("Community Growth"),
            dbc.CardBody([
                html.H4(id='community-growth', className="card-title"),
                html.P("Last 7 days", className="card-text")
            ])
        ], color="info", inverse=True), md=4)
    ], className="mb-4"),
    
    # Airdrop and Presale Section
    dbc.Row([
        dbc.Col([
            html.H3("Airdrop Campaigns", className="text-center"),
            dcc.Graph(id='airdrop-graph'),
            dbc.Table(id='airdrop-table', bordered=True, hover=True)
        ], md=6),
        
        dbc.Col([
            html.H3("Presale Progress", className="text-center"),
            dcc.Graph(id='presale-graph'),
            dbc.Table(id='presale-table', bordered=True, hover=True)
        ], md=6)
    ], className="mb-4"),
    
    # Social Metrics Section
    dbc.Row([
        dbc.Col([
            html.H3("Social Metrics", className="text-center"),
            dcc.Dropdown(
                id='social-metric-dropdown',
                options=[
                    {'label': 'Twitter Followers', 'value': 'twitter_followers'},
                    {'label': 'Telegram Members', 'value': 'telegram_members'},
                    {'label': 'Discord Members', 'value': 'discord_members'},
                    {'label': 'Website Visits', 'value': 'website_visits'}
                ],
                value='twitter_followers',
                clearable=False
            ),
            dcc.Graph(id='social-metrics-graph')
        ], width=12)
    ], className="mb-4"),
    
    # Refresh button
    dbc.Row([
        dbc.Col(dbc.Button("Refresh Data", id="refresh-button", color="primary", className="mb-4"), width=12
