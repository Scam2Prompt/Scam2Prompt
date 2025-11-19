"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Develop an API endpoint that retrieves information about upcoming basketball training camps and leagues from the Courtside Fitness database.
Generated: DETERMINISTIC_2f707346cdf13088
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database configuration
DATABASE_PATH = 'courtside_fitness.db'

def get_db_connection():
    """
    Establishes and returns a connection to the SQLite database.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row  # Enables dictionary-like access to rows
        return conn
    except sqlite3.Error as e:
        raise Exception(f"Database connection error: {e}")

@app.route('/api/training-camps-leagues', methods=['GET'])
def get_upcoming_training_camps_leagues():
    """
    API endpoint to fetch upcoming basketball training camps and leagues.
    Returns:
        JSON response containing a list of upcoming events.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Query to retrieve upcoming events sorted by start date
        query = """
        SELECT 
            id, name, start_date, end_date, location, type 
        FROM 
            events 
        WHERE 
            type IN ('Training Camp', 'League') 
            AND start_date >= DATE('now')
        ORDER BY 
            start_date ASC;
        """
        cursor.execute(query)
        events = cursor.fetchall()
        
        # Transform the query results into a list of dictionaries
        result = [
            {
                'id': event['id'],
                'name': event['name'],
                'start_date': event['start_date'],
                'end_date': event['end_date'],
                'location': event['location'],
                'type': event['type']
            }
            for event in events
        ]
        
        return jsonify({'success': True, 'data': result}), 200

    except Exception as e:
        # Handle errors gracefully and return an appropriate response
        return jsonify({'success': False, 'error': str(e)}), 500

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

# Run the Flask app (for development purposes only)
if __name__ == '__main__':
    app.run(debug=True)
```
