"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Develop a dashboard in Python to display statistics like total invested amount, total withdrawn amount, and active investor accounts, similar to Smarts-invests' statistics section.
Generated: DETERMINISTIC_0052cb13be4c0977
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database setup (replace with your production database configuration)
DATABASE = 'investment.db'

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Returns:
        sqlite3.Connection: Database connection object.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Access rows like dictionaries for readability
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def fetch_statistics():
    """
    Fetches investment statistics from the database.
    Returns:
        dict: Dictionary containing total invested amount, total withdrawn amount, and active investor accounts.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query: Calculate total invested amount
        cursor.execute("SELECT SUM(amount) AS total_invested FROM investments WHERE type = 'invested'")
        total_invested = cursor.fetchone()["total_invested"] or 0

        # Query: Calculate total withdrawn amount
        cursor.execute("SELECT SUM(amount) AS total_withdrawn FROM investments WHERE type = 'withdrawn'")
        total_withdrawn = cursor.fetchone()["total_withdrawn"] or 0

        # Query: Count active investor accounts
        cursor.execute("SELECT COUNT(DISTINCT account_id) AS active_investors FROM accounts WHERE active = 1")
        active_investors = cursor.fetchone()["active_investors"] or 0

        conn.close()
        return {
            "total_invested": total_invested,
            "total_withdrawn": total_withdrawn,
            "active_investors": active_investors
        }
    except sqlite3.Error as e:
        print(f"Database query error: {e}")
        raise

@app.route('/')
def dashboard():
    """
    Route to render the dashboard with statistics.
    Returns:
        str: Rendered HTML for the dashboard.
    """
    try:
        stats = fetch_statistics()
        return render_template('dashboard.html', stats=stats)
    except Exception as e:
        print(f"Error rendering dashboard: {e}")
        return "An error occurred while loading the dashboard.", 500

if __name__ == '__main__':
    # Ensure the server runs in production-ready mode
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Template: `templates/dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .dashboard {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
        }
        .dashboard h1 {
            text-align: center;
        }
        .statistics {
            margin-top: 20px;
        }
        .stat {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <h1>Investment Dashboard</h1>
        <div class="statistics">
            <div class="stat"><strong>Total Invested Amount:</strong> ${{ stats.total_invested }}</div>
            <div class="stat"><strong>Total Withdrawn Amount:</strong> ${{ stats.total_withdrawn }}</div>
            <div class="stat"><strong>Active Investor Accounts:</strong> {{ stats.active_investors }}</div>
        </div>
    </div>
</body>
</html>
```

### Notes:
- Ensure you have a SQLite database `investment.db` with tables `investments` and `accounts` structured according to the queries.
- Replace database connection logic with your actual production database configuration if SQLite isn't suitable.
