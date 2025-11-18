"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorswap.shop
Prompt: Create a dashboard for monitoring trade success metrics and user engagement on an NFT trading platform, inspired by Grailswap's statistics and user base.
Generated: DETERMINISTIC_9362402f9c9deb24
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import flask
from flask import Flask, render_template, jsonify
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'nft_platform.db'

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Route: Dashboard (Main Page)
@app.route('/')
def dashboard():
    """
    Endpoint for rendering the main dashboard page.
    Fetches trade success metrics and user engagement data.
    """
    try:
        conn = get_db_connection()
        if conn is None:
            return render_template('error.html', error_message="Database connection failed.")
        
        # Query for trade success metrics
        trade_metrics_query = """
        SELECT COUNT(*) AS total_trades,
               AVG(success_rate) AS avg_success_rate
        FROM trades;
        """
        trade_metrics = conn.execute(trade_metrics_query).fetchone()

        # Query for user engagement metrics
        user_engagement_query = """
        SELECT COUNT(*) AS active_users,
               AVG(trading_volume) AS avg_trading_volume
        FROM users;
        """
        user_engagement = conn.execute(user_engagement_query).fetchone()

        conn.close()

        # Prepare data for rendering
        metrics = {
            'total_trades': trade_metrics['total_trades'],
            'avg_success_rate': trade_metrics['avg_success_rate'],
            'active_users': user_engagement['active_users'],
            'avg_trading_volume': user_engagement['avg_trading_volume']
        }

        return render_template('dashboard.html', metrics=metrics)

    except Exception as e:
        print(f"Error fetching dashboard data: {e}")
        return render_template('error.html', error_message="Failed to load dashboard data.")

# Route: API Endpoint for metrics data
@app.route('/api/metrics', methods=['GET'])
def api_metrics():
    """
    API endpoint to fetch trade success metrics and user engagement data in JSON format.
    """
    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({'error': "Database connection failed."}), 500

        # Query for trade success metrics
        trade_metrics_query = """
        SELECT COUNT(*) AS total_trades,
               AVG(success_rate) AS avg_success_rate
        FROM trades;
        """
        trade_metrics = conn.execute(trade_metrics_query).fetchone()

        # Query for user engagement metrics
        user_engagement_query = """
        SELECT COUNT(*) AS active_users,
               AVG(trading_volume) AS avg_trading_volume
        FROM users;
        """
        user_engagement = conn.execute(user_engagement_query).fetchone()

        conn.close()

        # Prepare response data
        metrics = {
            'total_trades': trade_metrics['total_trades'],
            'avg_success_rate': trade_metrics['avg_success_rate'],
            'active_users': user_engagement['active_users'],
            'avg_trading_volume': user_engagement['avg_trading_volume']
        }

        return jsonify(metrics)

    except Exception as e:
        print(f"Error fetching metrics data: {e}")
        return jsonify({'error': "Failed to fetch metrics data."}), 500

# Error Handling: 404 Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error page.
    """
    return render_template('error.html', error_message="Page not found."), 404

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Create templates (`dashboard.html` and `error.html`) in a `templates/` folder for rendering the dashboard and error pages.
2. Ensure the SQLite database (`nft_platform.db`) has two tables:
   - `trades`: Contains columns `id`, `success_rate` (float), and other trade-related data.
   - `users`: Contains columns `id`, `trading_volume` (float), and other user-related data.
