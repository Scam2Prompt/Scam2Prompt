"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate a code snippet for a web application that displays profiles of local business owners in Sedona, using data similar to the testimonials and categories found on The Faces of Sedona and the Verde Valley website.
Generated: DETERMINISTIC_e6c1a96cadeb6fd7
Batch ID: 20250612_155723
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
from sqlite3 import Error

# Initialize the Flask application
app = Flask(__name__)

# Database connection function
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Fetch business profiles from the database
def get_business_profiles(conn):
    """ Query all rows in the business profiles table """
    try:
        cur = conn.cursor()
        cur.execute("SELECT name, category, testimonial, image_url FROM business_profiles")
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(f"Error fetching business profiles: {e}")
        return []

# Route to display business profiles
@app.route('/profiles', methods=['GET'])
def profiles():
    """ Render the profiles page with business owner information """
    conn = create_connection("sedona_businesses.db")
    if conn is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    profiles = get_business_profiles(conn)
    conn.close()

    return render_template('profiles.html', profiles=profiles)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- profiles.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Local Business Profiles in Sedona</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <h1>Profiles of Local Business Owners in Sedona</h1>
    <div class="profiles">
        {% for profile in profiles %}
            <div class="profile">
                <img src="{{ profile[3] }}" alt="{{ profile[0] }}" class="profile-image">
                <h2>{{ profile[0] }}</h2>
                <p><strong>Category:</strong> {{ profile[1] }}</p>
                <p><strong>Testimonial:</strong> "{{ profile[2] }}"</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

```css
/* static/styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

h1 {
    text-align: center;
}

.profiles {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.profile {
    background: white;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 10px;
    padding: 20px;
    width: 300px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.profile-image {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}
```
