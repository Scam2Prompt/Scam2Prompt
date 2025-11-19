"""
Generated Code Metadata:
========================
Original URL: https://www.hypersteakin.site
Prompt: Create a data analytics dashboard for the HyperSteakin Awards, tracking innovation, creativity, and excellence in German game development.
Generated: DETERMINISTIC_c9c00cc099f3553d
Batch ID: 20250622_212813
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
app = dash.Dash(__name__, title="HyperSteakin Awards Dashboard")
server = app.server

# Database connection
def get_db_connection():
    try:
        conn = sqlite3.connect('hypersteakin_awards.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise

# Create database tables if they don't exist
def initialize_database():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                developer TEXT NOT NULL,
                release_date DATE,
                platform TEXT,
                innovation_score INTEGER CHECK(innovation_score BETWEEN 0 AND 100),
                creativity_score INTEGER CHECK(creativity_score BETWEEN 0 AND 100),
                excellence_score INTEGER CHECK(excellence_score BETWEEN 0 AND 100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS awards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_id INTEGER,
                award_type TEXT,
                year INTEGER,
                FOREIGN KEY(game_id) REFERENCES games(id)
            )
        ''')
        
        conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")
        raise
    finally:
        if conn:
            conn.close()

# Sample data insertion (for demo purposes)
def insert_sample_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if sample data already exists
        cursor.execute("SELECT COUNT(*) FROM games")
        count = cursor.fetchone()[0]
        
        if count == 0:
            games = [
                ('CyberPunk 2077', 'CD Projekt Red', '2020-12-10', 'PC/Console', 85, 90, 88),
                ('Anno 1800', 'Ubisoft Blue Byte', '2019-04-16', 'PC', 78, 82, 85),
                ('The Witcher 3', 'CD Projekt Red', '2015-05-19', 'PC/Console', 92, 95, 97),
                ('Gothic', 'Piranha Bytes', '2001-03-15', 'PC', 88, 85, 82),
                ('Deponia', 'Daedalic Entertainment', '2012-08-30', 'PC', 75, 90, 80)
            ]
            
            cursor.executemany('''
                INSERT INTO games (name, developer, release_date, platform, innovation_score, creativity_score, excellence_score)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', games)
            
            awards = [
                (1, 'Innovation', 2020),
                (1, 'Excellence', 2020),
                (2, 'Creativity', 2019),
                (3, 'Innovation', 2015),
                (3, 'Excellence', 2015),
                (4, 'Creativity', 2001),
                (5, 'Creativity', 2012)
            ]
            
            cursor.executemany('''
                INSERT INTO awards (game_id, award_type, year)
                VALUES (?, ?, ?)
            ''', awards)
            
            conn.commit()
            logger.info("Sample data inserted successfully")
    except sqlite3.Error as e:
        logger.error(f"Sample data insertion error: {e}")
        raise
    finally:
        if conn:
            conn.close()

# Initialize database and insert sample data
initialize_database()
insert_sample_data()

# Layout of the dashboard
app.layout = html.Div([
    html.H1("HyperSteakin Awards Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='developer-dropdown',
                options=[],
                multi=True,
                placeholder="Select Developer(s)"
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Dropdown(
                id='platform-dropdown',
                options=[],
                multi=True,
                placeholder="Select Platform(s)"
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    
    html.Div([
        dcc.Graph(id='score-distribution'),
        dcc.Graph(id='awards-by-year')
    ], style={'display': 'flex', 'flex-wrap': 'wrap'}),
    
    html.Div([
        dcc.Graph(id='innovation-creativity-scatter'),
        dcc.Graph(id='excellence-trend')
    ], style={'display': 'flex', 'flex-wrap': 'wrap'}),
    
    html.Div([
        html.H3("Top Performing Games"),
        html.Div(id='top-games-table')
    ]),
    
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Update every minute
        n_intervals=0
    )
])

# Populate dropdown options
@app.callback(
    [Output('developer-dropdown', 'options'),
     Output('platform-dropdown', 'options')],
    [Input('interval-component', 'n_intervals')]
)
def update_dropdowns(n):
    try:
        conn = get_db_connection()
        
        # Get unique developers
        developers = pd.read_sql("SELECT DISTINCT developer FROM games ORDER BY developer", conn)
        dev_options = [{'label': dev, 'value': dev} for dev in developers['developer']]
        
        # Get unique platforms
        platforms = pd.read_sql("SELECT DISTINCT platform FROM games ORDER BY platform", conn)
        platform_options = [{'label': plat, 'value': plat} for plat in platforms['platform']]
        
        return dev_options, platform_options
    except Exception as e:
        logger.error(f"Error updating dropdowns: {e}")
        return [], []
    finally:
        if conn:
            conn.close()

# Update graphs based on filters
@app.callback(
    [Output('score-distribution', 'figure'),
     Output('awards-by-year', 'figure'),
     Output('innovation-creativity-scatter', 'figure'),
     Output('excellence-trend', 'figure'),
     Output('top-games-table', 'children')],
    [Input('developer-dropdown', 'value'),
     Input('platform-dropdown', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_graphs(selected_developers, selected_platforms, n):
    try:
        conn = get_db_connection()
        
        # Base query
        query = "SELECT * FROM games"
        conditions = []
        params = []
        
        # Apply filters if selected
        if selected_developers:
            placeholders = ','.join(['?'] * len(selected_developers))
            conditions.append(f"developer IN ({placeholders})")
            params.extend(selected_developers)
            
        if selected_platforms:
            placeholders = ','.join(['?'] * len(selected_platforms))
            conditions.append(f"platform IN ({placeholders})")
            params.extend(selected_platforms)
            
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
            
        # Get filtered games data
        games_df = pd.read_sql(query, conn, params=params if params else None)
        
        # Get awards data
        awards_query = '''
            SELECT a.*, g.name as game_name 
            FROM awards a
            JOIN games g ON a.game_id = g.id
        '''
        awards_df = pd.read_sql(awards_query, conn)
        
        # Score distribution chart
        score_fig = px.box(games_df, 
                          y=['innovation_score', 'creativity_score', 'excellence_score'],
                          title="Score Distribution Across Categories")
        
        # Awards by year chart
        awards_by_year = awards_df.groupby(['year', 'award_type']).size().reset_index(name='count')
        awards_fig = px.bar(awards_by_year, 
                           x='year', y='count', color='award_type',
                           title="Awards Given by Year",
                           labels={'count': 'Number of Awards', 'year': 'Year'})
        
        # Innovation vs Creativity scatter plot
        scatter_fig = px.scatter(games_df, 
                                x='innovation_score', y='creativity_score',
                                color='developer', hover_name='name',
                                title="Innovation vs Creativity Scores",
                                trendline="ols")
        
        # Excellence trend over time
