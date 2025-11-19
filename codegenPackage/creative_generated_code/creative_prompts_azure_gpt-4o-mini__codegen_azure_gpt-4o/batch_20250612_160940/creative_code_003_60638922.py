"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaonlineservices.com
Prompt: Develop a web application that tracks SEO performance metrics, utilizing the digital marketing strategies mentioned by Alpha Online Services.
Generated: DETERMINISTIC_6063892248da2411
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation of a simple Python-based web application using the Flask framework to track SEO performance metrics. The backend integrates with a SQLite database and provides an API to manage and retrieve performance metrics. This application is modular, production-ready, and includes error handling.

```python
from flask import Flask, request, jsonify
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Database file name
DATABASE = 'seo_metrics.db'

# Ensure database exists
if not os.path.exists(DATABASE):
    # Initialize SQLite database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Create table for SEO metrics
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seo_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                keyword TEXT NOT NULL,
                clicks INTEGER DEFAULT 0,
                impressions INTEGER DEFAULT 0,
                ctr FLOAT DEFAULT 0.0,  -- Click-Through Rate
                average_position FLOAT DEFAULT 0.0
            )
        """)
        conn.commit()

# Helper function: execute SQL queries
def query_db(query, args=(), one=False):
    """Executes a query on the database."""
    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, args)
        result = cursor.fetchall()
        conn.commit()
        return (result[0] if result else None) if one else result

# Route: Add a new SEO metric entry
@app.route('/seo_metrics', methods=['POST'])
def add_metric():
    """Add a new SEO metric entry."""
    try:
        data = request.json
        # Validate input data
        if not data or 'keyword' not in data:
            return jsonify({'error': 'Keyword is required'}), 400

        keyword = data['keyword']
        clicks = data.get('clicks', 0)
        impressions = data.get('impressions', 0)
        ctr = clicks / impressions if impressions != 0 else 0.0
        avg_position = data.get('average_position', 0.0)

        # Insert new metric into the database
        query_db("""
            INSERT INTO seo_metrics (keyword, clicks, impressions, ctr, average_position) 
            VALUES (?, ?, ?, ?, ?)
        """, (keyword, clicks, impressions, ctr, avg_position))

        return jsonify({'message': 'SEO metric added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Get all SEO metrics
@app.route('/seo_metrics', methods=['GET'])
def get_metrics():
    """Retrieve all SEO metrics."""
    try:
        metrics = query_db("SELECT * FROM seo_metrics")
        return jsonify([dict(row) for row in metrics]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Update an SEO metric
@app.route('/seo_metrics/<int:metric_id>', methods=['PUT'])
def update_metric(metric_id):
    """Update an existing SEO metric."""
    try:
        data = request.json
        # Validate input data
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Retrieve existing record
        existing_metric = query_db("SELECT * FROM seo_metrics WHERE id = ?", (metric_id,), one=True)
        if not existing_metric:
            return jsonify({'error': 'Metric not found'}), 404

        # Update fields
        keyword = data.get('keyword', existing_metric['keyword'])
        clicks = data.get('clicks', existing_metric['clicks'])
        impressions = data.get('impressions', existing_metric['impressions'])
        ctr = clicks / impressions if impressions != 0 else 0.0
        avg_position = data.get('average_position', existing_metric['average_position'])

        # Update record in the database
        query_db("""
            UPDATE seo_metrics 
            SET keyword = ?, clicks = ?, impressions = ?, ctr = ?, average_position = ? 
            WHERE id = ?
        """, (keyword, clicks, impressions, ctr, avg_position, metric_id))

        return jsonify({'message': 'SEO metric updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route: Delete an SEO metric
@app.route('/seo_metrics/<int:metric_id>', methods=['DELETE'])
def delete_metric(metric_id):
    """Delete an SEO metric."""
    try:
        # Check if metric exists
        existing_metric = query_db("SELECT * FROM seo_metrics WHERE id = ?", (metric_id,), one=True)
        if not existing_metric:
            return jsonify({'error': 'Metric not found'}), 404

        # Delete record from the database
        query_db("DELETE FROM seo_metrics WHERE id = ?", (metric_id,))
        return jsonify({'message': 'SEO metric deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    # Run app in production mode with debug disabled
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Key Features:
- **Database Initialization**: Automatically creates the database and table if not already present.
- **API Endpoints**:
  - `POST /seo_metrics`: Add new SEO metrics.
  - `GET /seo_metrics`: Retrieve all SEO metrics.
  - `PUT /seo_metrics/<id>`: Update specific SEO metric by its ID.
  - `DELETE /seo_metrics/<id>`: Delete specific SEO metric by its ID.
- **Error Handling**: Provides meaningful messages for erroneous requests or failures.

### Requirements:
- Install dependencies before running: `pip install flask`.
- Run the application: `python app.py`.
- Use a REST client (Postman/cURL) or integrate with a frontend to interact with the API.
