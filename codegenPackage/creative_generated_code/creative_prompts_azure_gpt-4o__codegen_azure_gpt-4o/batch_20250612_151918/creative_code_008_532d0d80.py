"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asdadw3qqd.pages.dev
Prompt: Develop a dashboard to visualize user engagement and reward distribution for Chapter 3 of the Puffy Rewards program.
Generated: DETERMINISTIC_532d0d807fc0e6b2
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code to create a simple dashboard using Flask and Matplotlib for visualizing user engagement and reward distribution. It assumes the data is stored in a database and fetched via SQL queries.

```python
# dashboard.py

from flask import Flask, render_template, jsonify
import sqlite3
import matplotlib.pyplot as plt
import os

# Initialize Flask app
app = Flask(__name__)

# Database connection details (update with your DB path)
DATABASE = 'puffy_rewards.db'

# Ensure output directory for charts exists
CHARTS_DIR = 'static/charts'
os.makedirs(CHARTS_DIR, exist_ok=True)

def get_db_connection():
    """
    Create a connection to the SQLite database.
    Returns:
        conn: SQLite connection object
    """
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def fetch_user_engagement_data():
    """
    Fetch user engagement data for Chapter 3 from the database.
    Returns:
        List of tuples with user engagement data
    """
    conn = get_db_connection()
    if conn:
        try:
            query = """
            SELECT user_id, engagement_score 
            FROM user_engagement 
            WHERE chapter_id = 3;
            """
            data = conn.execute(query).fetchall()
            conn.close()
            return data
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []
    return []

def fetch_reward_distribution_data():
    """
    Fetch reward distribution data for Chapter 3 from the database.
    Returns:
        List of tuples with reward distribution data
    """
    conn = get_db_connection()
    if conn:
        try:
            query = """
            SELECT reward_type, COUNT(*) as count 
            FROM rewards 
            WHERE chapter_id = 3 
            GROUP BY reward_type;
            """
            data = conn.execute(query).fetchall()
            conn.close()
            return data
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
            return []
    return []

def generate_user_engagement_chart(data):
    """
    Generate a bar chart for user engagement and save it to the static folder.
    Args:
        data: List of tuples containing user engagement data
    """
    user_ids = [row['user_id'] for row in data]
    scores = [row['engagement_score'] for row in data]

    plt.figure(figsize=(10, 6))
    plt.bar(user_ids, scores, color='skyblue')
    plt.title('User Engagement - Chapter 3')
    plt.xlabel('User ID')
    plt.ylabel('Engagement Score')
    plt.xticks(rotation=45)
    plt.tight_layout()

    chart_path = os.path.join(CHARTS_DIR, 'user_engagement_chart.png')
    plt.savefig(chart_path)
    plt.close()

def generate_reward_distribution_chart(data):
    """
    Generate a pie chart for reward distribution and save it to the static folder.
    Args:
        data: List of tuples containing reward distribution data
    """
    reward_types = [row['reward_type'] for row in data]
    counts = [row['count'] for row in data]

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=reward_types, autopct='%1.1f%%', startangle=140)
    plt.title('Reward Distribution - Chapter 3')
    plt.tight_layout()

    chart_path = os.path.join(CHARTS_DIR, 'reward_distribution_chart.png')
    plt.savefig(chart_path)
    plt.close()

@app.route('/')
def dashboard():
    """
    Render the dashboard page with user engagement and reward distribution charts.
    """
    # Fetch data
    engagement_data = fetch_user_engagement_data()
    reward_data = fetch_reward_distribution_data()

    # Generate charts
    if engagement_data:
        generate_user_engagement_chart(engagement_data)
    if reward_data:
        generate_reward_distribution_chart(reward_data)

    # Render template
    return render_template('dashboard.html')

@app.route('/api/engagement')
def api_engagement():
    """
    API endpoint to fetch user engagement data as JSON.
    """
    data = fetch_user_engagement_data()
    return jsonify([dict(row) for row in data])

@app.route('/api/rewards')
def api_rewards():
    """
    API endpoint to fetch reward distribution data as JSON.
    """
    data = fetch_reward_distribution_data()
    return jsonify([dict(row) for row in data])

if __name__ == '__main__':
    app.run(debug=True)
```

Additionally, create a simple HTML template `templates/dashboard.html`:

```html
<!-- dashboard.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puffy Rewards Dashboard</title>
</head>
<body>
    <h1>Puffy Rewards Dashboard - Chapter 3</h1>
    <h2>User Engagement</h2>
    <img src="/static/charts/user_engagement_chart.png" alt="User Engagement Chart">

    <h2>Reward Distribution</h2>
    <img src="/static/charts/reward_distribution_chart.png" alt="Reward Distribution Chart">
</body>
</html>
```

This code provides a Flask-based web application with user engagement and reward distribution visualization for Chapter 3 of the Puffy Rewards program. Make sure to replace the database schema and content with your actual data.
