"""
Generated Code Metadata:
========================
Original URL: https://moon5.org
Prompt: Develop a simple web application that allows users to track their earnings from multiple crypto faucets, inspired by the features of Moon5.
Generated: DETERMINISTIC_af045a5028761da4
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a simple web application using Python's Flask framework. This app allows users to track their earnings from multiple crypto faucets.

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Database file path
DATABASE = 'crypto_faucet_tracker.db'

# Ensure the database exists
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE earnings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            faucet_name TEXT NOT NULL,
            crypto_type TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.route('/')
def index():
    """
    Home page that displays all earnings.
    """
    conn = get_db_connection()
    if conn:
        earnings = conn.execute('SELECT * FROM earnings').fetchall()
        conn.close()
        return render_template('index.html', earnings=earnings)
    else:
        flash('Error connecting to the database.', 'danger')
        return render_template('index.html', earnings=[])

@app.route('/add', methods=['GET', 'POST'])
def add_earning():
    """
    Page to add a new earning entry.
    """
    if request.method == 'POST':
        faucet_name = request.form['faucet_name']
        crypto_type = request.form['crypto_type']
        amount = request.form['amount']
        date = request.form['date']

        # Validate input
        if not faucet_name or not crypto_type or not amount or not date:
            flash('All fields are required.', 'danger')
            return redirect(url_for('add_earning'))

        try:
            amount = float(amount)
        except ValueError:
            flash('Amount must be a valid number.', 'danger')
            return redirect(url_for('add_earning'))

        conn = get_db_connection()
        if conn:
            conn.execute('INSERT INTO earnings (faucet_name, crypto_type, amount, date) VALUES (?, ?, ?, ?)',
                         (faucet_name, crypto_type, amount, date))
            conn.commit()
            conn.close()
            flash('Earning added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Error connecting to the database.', 'danger')
            return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_earning(id):
    """
    Delete an earning entry by ID.
    """
    conn = get_db_connection()
    if conn:
        conn.execute('DELETE FROM earnings WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash('Earning deleted successfully!', 'success')
    else:
        flash('Error connecting to the database.', 'danger')
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Faucet Tracker</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Crypto Faucet Tracker</h1>
        <a href="/add" class="btn btn-primary mb-3">Add Earning</a>
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Faucet Name</th>
                    <th>Crypto Type</th>
                    <th>Amount</th>
                    <th>Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for earning in earnings %}
                <tr>
                    <td>{{ earning.id }}</td>
                    <td>{{ earning.faucet_name }}</td>
                    <td>{{ earning.crypto_type }}</td>
                    <td>{{ earning.amount }}</td>
                    <td>{{ earning.date }}</td>
                    <td>
                        <form action="/delete/{{ earning.id }}" method="post" style="display:inline;">
                            <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                        </form>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```

#### `templates/add.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Earning</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Add Earning</h1>
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}
        <form method="post">
            <div class="mb-3">
                <label for="faucet_name" class="form-label">Faucet Name</label>
                <input type="text" class="form-control" id="faucet_name" name="faucet_name" required>
            </div>
            <div class="mb-3">
                <label for="crypto_type" class="form-label">Crypto Type</label>
                <input type="text" class="form-control" id="crypto_type" name="crypto_type" required>
            </div>
            <div class="mb-3">
                <label for="amount" class="form-label">Amount</label>
                <input type="number" step="0.0001" class="form-control" id="amount" name="amount" required>
            </div>
            <div class="mb-3">
                <label for="date" class="form-label">Date</label>
                <input type="date" class="form-control" id="date" name="date" required>
            </div>
            <button type="submit" class="btn btn-success">Add</button>
            <a href="/" class="btn btn-secondary">Cancel</a>
        </form>
    </div>
</body>
</html>
```

### Notes:
- Replace `your_secret_key` with a secure key for production.
- Use a proper database management system (e.g., PostgreSQL) for scalability in production.
- Add authentication and authorization for security in a real-world application.
