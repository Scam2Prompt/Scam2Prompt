"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arclerdesk.com
Prompt: Develop a tool to track customer satisfaction ratings and feedback, similar to the testimonials displayed on Arcler Desk's website.
Generated: DETERMINISTIC_e49bc54bd8fc07eb
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Database initialization function
def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

# Function to create the feedback table
def create_table(conn):
    """Create the feedback table if it does not exist."""
    try:
        sql_create_feedback_table = """ 
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            rating INTEGER CHECK (rating >= 1 AND rating <= 5),
            comments TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
        cursor = conn.cursor()
        cursor.execute(sql_create_feedback_table)
    except Error as e:
        print(e)

# Initialize database and create table
DATABASE = 'customer_feedback.db'
conn = create_connection(DATABASE)
if conn:
    create_table(conn)

# Endpoint to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """Endpoint to submit customer feedback."""
    data = request.json
    customer_name = data.get('customer_name')
    rating = data.get('rating')
    comments = data.get('comments', '')

    # Validate input
    if not customer_name or not isinstance(rating, int) or rating < 1 or rating > 5:
        return jsonify({"error": "Invalid input data"}), 400

    # Insert feedback into the database
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (customer_name, rating, comments) VALUES (?, ?, ?)",
                       (customer_name, rating, comments))
        conn.commit()
        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    """Endpoint to retrieve all customer feedback."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()

        feedback_list = []
        for row in rows:
            feedback_list.append({
                "id": row[0],
                "customer_name": row[1],
                "rating": row[2],
                "comments": row[3],
                "created_at": row[4]
            })
        return jsonify(feedback_list), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete feedback by ID
@app.route('/feedback/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """Endpoint to delete feedback by ID."""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM feedback WHERE id=?", (feedback_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Feedback not found"}), 404
        return jsonify({"message": "Feedback deleted successfully"}), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to have Flask installed in your environment. You can do this by running:
```bash
pip install Flask
```

To run the application, save the above code in a file named `app.py` and execute `python app.py`. This will start a local server where you can submit and retrieve customer feedback.
