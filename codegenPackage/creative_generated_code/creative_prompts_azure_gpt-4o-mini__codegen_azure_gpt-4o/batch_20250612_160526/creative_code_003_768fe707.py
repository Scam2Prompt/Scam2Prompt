"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamadver.com
Prompt: Develop a performance monitoring dashboard for social media campaigns, incorporating analytics similar to those offered by Team Adver.
Generated: DETERMINISTIC_768fe70732324207
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import flask
from flask import Flask, render_template, request, jsonify
import sqlite3
import datetime
import random

# Initialize the Flask application
app = Flask(__name__)

# Database setup
DB_NAME = 'social_media_analytics.db'

def initialize_database():
    """Initialize the database with necessary tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            platform TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            impressions INTEGER NOT NULL,
            clicks INTEGER NOT NULL,
            conversions INTEGER NOT NULL,
            spend REAL NOT NULL,
            FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
        )
    ''')
    conn.commit()
    conn.close()

# Helper functions
def get_campaign_data(campaign_id):
    """Fetch campaign metrics from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = '''
        SELECT date, impressions, clicks, conversions, spend
        FROM metrics
        WHERE campaign_id = ?
        ORDER BY date ASC
    '''
    cursor.execute(query, (campaign_id,))
    data = cursor.fetchall()
    conn.close()
    return data

def add_sample_data():
    """Add sample campaigns and metrics to the database for testing."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Adding sample campaigns
    campaigns = [
        ("Summer Sale", "Facebook", "2023-10-01", "2023-10-31"),
        ("Winter Clearance", "Instagram", "2023-11-01", "2023-11-30")
    ]
    cursor.executemany('''
        INSERT INTO campaigns (name, platform, start_date, end_date)
        VALUES (?, ?, ?, ?)
    ''', campaigns)
    
    conn.commit()
    
    # Adding sample metrics
    campaign_ids = [1, 2]
    for campaign_id in campaign_ids:
        metrics = []
        for i in range(1, 31):
            date = (datetime.date.today() - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
            impressions = random.randint(1000, 5000)
            clicks = random.randint(100, 500)
            conversions = random.randint(10, 100)
            spend = round(random.uniform(20, 200), 2)
            metrics.append((campaign_id, date, impressions, clicks, conversions, spend))
        cursor.executemany('''
            INSERT INTO metrics (campaign_id, date, impressions, clicks, conversions, spend)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', metrics)
    
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def dashboard():
    """Render the main dashboard page."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, platform, start_date, end_date FROM campaigns')
    campaigns = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', campaigns=campaigns)

@app.route('/campaign/<int:campaign_id>')
def campaign_details(campaign_id):
    """Render detailed analytics for a specific campaign."""
    data = get_campaign_data(campaign_id)
    return render_template('campaign_details.html', metrics=data)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Initialize the database and add sample data
    initialize_database()
    add_sample_data()
    
    # Start the Flask application
    app.run(debug=True)
```

You'll need HTML templates for `dashboard.html` and `campaign_details.html` to render the frontend components.
