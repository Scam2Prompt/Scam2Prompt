"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon5.org
Prompt: Develop a simple web application that allows users to track their earnings from multiple crypto faucets, inspired by the features of Moon5.
Generated: DETERMINISTIC_af045a5028761da4
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code for a simple web application using Python's Flask framework. This application allows users to track their earnings from multiple crypto faucets. You'll need Python installed and the required dependencies to run it.

```python
# app.py - Flask-based Crypto Faucet Earnings Tracker

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

# Initialize Flask application
app = Flask(__name__)

# Set a secret key for session management (used for flash messages)
app.secret_key = 'your_secret_key_here'

# Database file name
DB_FILE = 'crypto_earnings.db'

# Ensure the SQLite database exists
def init_db():
    """Initialize the SQLite database if it doesn't already exist."""
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Create a table for earnings
        cursor.execute('''
            CREATE TABLE earnings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                faucet_name TEXT NOT NULL,
                crypto_type TEXT NOT NULL,
                amount REAL NOT NULL,
                date_added DATE DEFAULT CURRENT_DATE
            )
        ''')
        conn.commit()
        conn.close()

# Route: Home page
@app.route('/')
def index():
    """Home page that displays all tracked earnings."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM earnings')
    earnings = cursor.fetchall()  # Fetch all rows
    conn.close()
    return render_template('index.html', earnings=earnings)

# Route: Add earnings
@app.route('/add', methods=['GET', 'POST'])
def add_earning():
    """Page for adding a new faucet earning."""
    if request.method == 'POST':
        # Extract form data
        faucet_name = request.form['faucet_name']
        crypto_type = request.form['crypto_type']
        try:
            amount = float(request.form['amount'])
        except ValueError:
            flash('Amount must be a valid number', 'error')
            return redirect(url_for('add_earning'))
        
        # Insert into database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO earnings (faucet_name, crypto_type, amount) VALUES (?, ?, ?)',
                       (faucet_name, crypto_type, amount))
        conn.commit()
        conn.close()

        flash('Earning added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add.html')

# Route: Delete earnings
@app.route('/delete/<int:id>')
def delete_earning(id):
    """Delete an earning entry by its ID."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM earnings WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    flash('Earning deleted successfully!', 'success')
    return redirect(url_for('index'))

# Error handling: 404 page
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page."""
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    init_db()  # Ensure the database is initialized
    app.run(debug=True)  # Run the application in debug mode
```

### Folder Structure:
```
crypto_faucet_tracker/
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── 404.html
├── app.py
```

### Templates:
#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Faucet Tracker</title>
</head>
<body>
    <h1>Crypto Faucet Tracker</h1>
    <a href="/add">Add New Earning</a>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Faucet Name</th>
                <th>Crypto Type</th>
                <th>Amount</th>
                <th>Date Added</th>
                <th>Delete</th>
            </tr>
        </thead>
        <tbody>
            {% for earning in earnings %}
            <tr>
                <td>{{ earning[0] }}</td>
                <td>{{ earning[1] }}</td>
                <td>{{ earning[2] }}</td>
                <td>{{ earning[3] }}</td>
                <td>{{ earning[4] }}</td>
                <td><a href="/delete/{{ earning[0] }}">Delete</a></td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

#### `add.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Earning</title>
</head>
<body>
    <h1>Add New Earning</h1>
    <form method="POST" action="/add">
        <label for="faucet_name">Faucet Name:</label>
        <input type="text" id="faucet_name" name="faucet_name" required>
        <br>
        
        <label for="crypto_type">Crypto Type:</label>
        <input type="text" id="crypto_type" name="crypto_type" required>
        <br>

        <label for="amount">Amount:</label>
        <input type="number" step="0.00000001" id="amount" name="amount" required>
        <br>

        <button type="submit">Add</button>
    </form>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Go Back Home</a>
</body>
</html>
```

### Dependencies:
Install required dependencies:
```bash
pip install flask
```

### Run the Application:
```bash
python app.py
```

Visit the app in your browser at `http://127.0.0.1:5000`.
