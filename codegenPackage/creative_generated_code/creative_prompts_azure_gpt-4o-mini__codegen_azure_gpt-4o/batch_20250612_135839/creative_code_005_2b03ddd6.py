"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Provide an example of how to display verified dealer profiles on a car dealership website, taking cues from DriveCities' approach.
Generated: DETERMINISTIC_2b03ddd689542056
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

# Database connection and initialization
DATABASE = 'dealership.db'


def create_dealers_table():
    """Create the dealers table if it doesn't exist."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dealers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            contact TEXT NOT NULL,
            is_verified BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    connection.commit()
    connection.close()


create_dealers_table()


def get_verified_dealers():
    """Fetch verified dealer profiles from the database."""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('SELECT id, name, location, contact FROM dealers WHERE is_verified = 1')
        dealers = cursor.fetchall()
        connection.close()
        return dealers
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []


# Routes
@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')


@app.route('/api/dealers', methods=['GET'])
def fetch_dealers():
    """
    API endpoint to fetch verified dealer profiles.
    
    Returns:
        JSON response containing the verified dealers.
    """
    try:
        verified_dealers = get_verified_dealers()
        dealers_list = [
            {'id': dealer[0], 'name': dealer[1], 'location': dealer[2], 'contact': dealer[3]}
            for dealer in verified_dealers
        ]
        return jsonify({'status': 'success', 'data': dealers_list}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


# HTML Rendering (optional for demonstration purposes)
@app.route('/dealers')
def display_dealers():
    """
    Render verified dealer profiles on the website.
    
    Returns:
        HTML page displaying the verified dealers.
    """
    try:
        verified_dealers = get_verified_dealers()
        return render_template('dealers.html', dealers=verified_dealers)
    except Exception as e:
        return f"An error occurred: {e}", 500


# Starting the Flask application
if __name__ == '__main__':
    # Application must be run in debug mode for development purposes
    app.run(debug=True)
```

### `dealers.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verified Dealers</title>
</head>
<body>
    <h1>Verified Dealer Profiles</h1>
    <ul>
        {% for dealer in dealers %}
        <li>
            <strong>{{ dealer[1] }}</strong><br>
            Location: {{ dealer[2] }}<br>
            Contact: {{ dealer[3] }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
1. Ensure the SQLite database (`dealership.db`) is placed in the correct directory.
2. Populate the `dealers` table with appropriate data, ensuring `is_verified = 1` for verified dealers.
3. Install Flask (`pip install flask`) before running the script.
