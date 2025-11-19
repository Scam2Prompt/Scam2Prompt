"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trade-verified.com
Prompt: Generate a code snippet that integrates supplier assessment data into a dashboard for real-time monitoring of supply chain risks.
Generated: DETERMINISTIC_bb5347134911435c
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import sqlite3
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend integration

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection details
DATABASE = 'supplier_assessment.db'

def init_db():
    """Initialize the database schema for supplier assessments."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS supplier_assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_name TEXT NOT NULL,
                risk_score INTEGER NOT NULL,
                last_assessment_date TEXT NOT NULL
            )
        ''')
        conn.commit()
    except Exception as e:
        logging.error(f"Error initializing database: {e}")
    finally:
        conn.close()

# Initialize database on application startup
init_db()

@app.route('/add_assessment', methods=['POST'])
def add_assessment():
    """
    API endpoint to add supplier assessment data.
    Expects JSON payload with `supplier_name`, `risk_score`, and `last_assessment_date`.
    """
    try:
        data = request.json
        supplier_name = data.get('supplier_name')
        risk_score = data.get('risk_score')
        last_assessment_date = data.get('last_assessment_date')

        # Validate input data
        if not supplier_name or not risk_score or not last_assessment_date:
            return jsonify({"error": "Invalid input data"}), 400

        # Save to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO supplier_assessments (supplier_name, risk_score, last_assessment_date)
            VALUES (?, ?, ?)
        ''', (supplier_name, risk_score, last_assessment_date))
        conn.commit()
        return jsonify({"message": "Assessment added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding assessment: {e}")
        return jsonify({"error": "Failed to add assessment"}), 500
    finally:
        conn.close()

@app.route('/get_assessments', methods=['GET'])
def get_assessments():
    """
    API endpoint to retrieve all supplier assessments.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM supplier_assessments')
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        assessments = []
        for row in rows:
            assessments.append({
                "id": row[0],
                "supplier_name": row[1],
                "risk_score": row[2],
                "last_assessment_date": row[3]
            })
        return jsonify({"assessments": assessments}), 200
    except Exception as e:
        logging.error(f"Error retrieving assessments: {e}")
        return jsonify({"error": "Failed to retrieve assessments"}), 500
    finally:
        conn.close()

@app.route('/dashboard', methods=['GET'])
def dashboard():
    """
    API endpoint to provide real-time monitoring data for supply chain risks.
    Aggregates data for high-risk suppliers.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT supplier_name, risk_score, last_assessment_date
            FROM supplier_assessments
            WHERE risk_score > 70
            ORDER BY risk_score DESC
        ''')
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        high_risk_suppliers = []
        for row in rows:
            high_risk_suppliers.append({
                "supplier_name": row[0],
                "risk_score": row[1],
                "last_assessment_date": row[2]
            })
        return jsonify({"high_risk_suppliers": high_risk_suppliers}), 200
    except Exception as e:
        logging.error(f"Error generating dashboard data: {e}")
        return jsonify({"error": "Failed to generate dashboard data"}), 500
    finally:
        conn.close()

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
