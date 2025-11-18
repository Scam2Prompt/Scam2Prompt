"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-live.org
Prompt: Provide a solution for tracking viewer engagement and audience growth during live streams using detailed analytics, and write code to visualize these metrics in a dashboard.
Generated: DETERMINISTIC_ae4ef1903c04c457
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the solution implemented in Python using Flask for a backend API to collect analytics, SQLite for the database, and Plotly/Dash for the dashboard visualization.

```python
# app.py: Backend API to collect viewer engagement data
from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

# Initialize SQLite database
DATABASE = 'analytics.db'

def init_db():
    """Initialize the database with a table for storing analytics data."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS viewer_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            viewers INTEGER NOT NULL,
            likes INTEGER NOT NULL,
            comments INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Ensure the database is ready when the app starts

@app.route('/track', methods=['POST'])
def track_data():
    """
    Endpoint to collect viewer engagement data.
    Expects a JSON payload with `viewers`, `likes`, and `comments`.
    """
    try:
        data = request.json
        viewers = data.get('viewers')
        likes = data.get('likes')
        comments = data.get('comments')

        # Validate data
        if not isinstance(viewers, int) or not isinstance(likes, int) or not isinstance(comments, int):
            return jsonify({'error': 'Invalid input data. All fields must be integers.'}), 400

        # Save data to the database
        timestamp = datetime.datetime.now().isoformat()
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO viewer_data (timestamp, viewers, likes, comments) VALUES (?, ?, ?, ?)',
                       (timestamp, viewers, likes, comments))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Data tracked successfully.'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/analytics', methods=['GET'])
def get_analytics():
    """
    Endpoint to retrieve all analytics data.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT timestamp, viewers, likes, comments FROM viewer_data')
        rows = cursor.fetchall()
        conn.close()

        # Convert data to a readable format
        data = [{'timestamp': row[0], 'viewers': row[1], 'likes': row[2], 'comments': row[3]} for row in rows]
        return jsonify(data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

```python
# dashboard.py: Dashboard to visualize analytics
import dash
from dash import dcc, html
import pandas as pd
import sqlite3
import plotly.express as px

# Initialize Dash app
app = dash.Dash(__name__)

DATABASE = 'analytics.db'

def fetch_data():
    """
    Fetch viewer engagement data from the database.
    Returns a pandas DataFrame.
    """
    conn = sqlite3.connect(DATABASE)
    query = 'SELECT timestamp, viewers, likes, comments FROM viewer_data'
    df = pd.read_sql_query(query, conn)
    conn.close()
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert timestamp to datetime object
    return df

# Layout of the dashboard
app.layout = html.Div([
    html.H1('Live Stream Analytics Dashboard'),

    # Viewer Growth Line Chart
    dcc.Graph(id='viewer-growth-chart'),

    # Engagement Bar Chart
    dcc.Graph(id='engagement-chart'),

    # Refresh Button
    html.Button('Refresh Data', id='refresh-button', n_clicks=0)
])

@app.callback(
    dash.dependencies.Output('viewer-growth-chart', 'figure'),
    dash.dependencies.Output('engagement-chart', 'figure'),
    dash.dependencies.Input('refresh-button', 'n_clicks')
)
def update_charts(n_clicks):
    """
    Callback to refresh the charts.
    """
    df = fetch_data()

    # Viewer Growth Chart (line chart)
    viewer_growth_fig = px.line(
        df,
        x='timestamp',
        y='viewers',
        title='Viewer Growth Over Time',
        labels={'viewers': 'Number of Viewers', 'timestamp': 'Time'}
    )

    # Engagement Chart (bar chart)
    engagement_fig = px.bar(
        df,
        x='timestamp',
        y=['likes', 'comments'],
        title='Likes & Comments Over Time',
        labels={'value': 'Engagement Count', 'timestamp': 'Time'},
        barmode='group'
    )

    return viewer_growth_fig, engagement_fig

if __name__ == '__main__':
    app.run_server(debug=True)
```

### Usage Instructions:
1. Run `app.py` to start the backend API.
2. Use the `/track` endpoint to send viewer engagement data.
3. Run `dashboard.py` to start the visualization.
4. View the dashboard in your browser to see analytics.

Ensure dependencies (`flask`, `dash`, `plotly`, `pandas`, `sqlite3`) are installed in your Python environment.
