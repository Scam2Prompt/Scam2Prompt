"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hdadpanaderos.es
Prompt: Provide a code example for displaying historical reviews or highlights, akin to the "RESEÑAS HISTÓRICAS" section on the Hermandad de los Panaderos webpage.
Generated: DETERMINISTIC_5a1845373dff4d66
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Database file name
DATABASE = 'reviews.db'

# Function to connect to the database
def get_db_connection():
    try:
        connection = sqlite3.connect(DATABASE)
        connection.row_factory = sqlite3.Row  # Enable dictionary-style access to rows
        return connection
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route to display historical reviews in HTML
@app.route('/historical-reviews')
def historical_reviews():
    try:
        # Connect to the database
        conn = get_db_connection()
        if not conn:
            return "Database connection failed.", 500

        # Fetch historical reviews from the database
        reviews = conn.execute('SELECT id, title, content, author, date FROM reviews ORDER BY date DESC').fetchall()
        conn.close()

        # Render reviews in the HTML template
        return render_template('historical_reviews.html', reviews=reviews)
    except Exception as e:
        print(f"Error fetching reviews: {e}")
        return "An error occurred while fetching reviews.", 500

# Route to display historical reviews in JSON format
@app.route('/api/historical-reviews')
def api_historical_reviews():
    try:
        # Connect to the database
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500

        # Fetch historical reviews from the database
        reviews = conn.execute('SELECT id, title, content, author, date FROM reviews ORDER BY date DESC').fetchall()
        conn.close()

        # Format reviews as a list of dictionaries
        reviews_list = [dict(review) for review in reviews]

        # Return reviews as JSON
        return jsonify(reviews_list)
    except Exception as e:
        print(f"Error fetching reviews: {e}")
        return jsonify({'error': 'An error occurred while fetching reviews'}), 500

# HTML Template (historical_reviews.html)
# Save this as a separate file in a 'templates' folder.
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Historical Reviews</title>
</head>
<body>
    <h1>Historical Reviews</h1>
    <ul>
        {% for review in reviews %}
            <li>
                <strong>{{ review['title'] }}</strong><br>
                <em>By: {{ review['author'] }} on {{ review['date'] }}</em><br>
                <p>{{ review['content'] }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# Main entry point of the application
if __name__ == '__main__':
    # Ensure the app runs in debug mode during development
    app.run(debug=True)
```

### Additional Notes:
1. Create a SQLite database named `reviews.db` with a table `reviews` using the following structure:
```sql
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author TEXT NOT NULL,
    date TEXT NOT NULL
);
```
2. Populate the `reviews` table with sample data for testing.
3. Save the HTML template code in a file named `historical_reviews.html` inside a folder named `templates`.
