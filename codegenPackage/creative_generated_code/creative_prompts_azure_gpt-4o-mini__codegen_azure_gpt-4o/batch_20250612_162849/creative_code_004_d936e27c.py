"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfoundation.com
Prompt: How can I create a user-friendly interface for domain buyers that includes transaction support, inspired by the features of tonfoundation.com?
Generated: DETERMINISTIC_d936e27ce6f77496
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This is a Python-based implementation of a user-friendly web interface for domain buyers.
# It includes functionality for browsing available domains and performing transactions.
# The code utilizes Flask for web server functionality and SQLite for database management.

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for flash messages

# Database setup
DATABASE = 'domain_marketplace.db'

def init_db():
    """Initialize the database with table setup."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price REAL NOT NULL,
            is_available BOOLEAN NOT NULL DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()

# Initialize the database when the script runs
init_db()

@app.route('/')
def index():
    """Render the homepage with available domains."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM domains WHERE is_available = 1")
        domains = cursor.fetchall()
        conn.close()
    except sqlite3.Error as e:
        flash(f"Database error: {e}", "error")
        domains = []

    return render_template('index.html', domains=domains)

@app.route('/buy/<int:domain_id>', methods=['POST'])
def buy_domain(domain_id):
    """Allow users to purchase a domain."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT is_available FROM domains WHERE id = ?", (domain_id,))
        domain = cursor.fetchone()

        if domain and domain[0]:  # Check if domain exists and is available
            cursor.execute("UPDATE domains SET is_available = 0 WHERE id = ?", (domain_id,))
            conn.commit()
            flash("Domain purchased successfully!", "success")
        else:
            flash("Domain is not available or does not exist.", "error")

        conn.close()
    except sqlite3.Error as e:
        flash(f"Transaction error: {e}", "error")

    return redirect(url_for('index'))

@app.route('/add-domain', methods=['GET', 'POST'])
def add_domain():
    """Admin functionality to add new domains."""
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')

        if not name or not price:
            flash("Name and price are required!", "error")
            return redirect(url_for('add_domain'))

        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO domains (name, price, is_available) VALUES (?, ?, ?)", (name, float(price), True))
            conn.commit()
            conn.close()
            flash("Domain added successfully!", "success")
            return redirect(url_for('index'))
        except sqlite3.Error as e:
            flash(f"Database error: {e}", "error")

    return render_template('add_domain.html')

# Error handling routes
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates
To make the above code functional, the following HTML templates are required:

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Domain Marketplace</title>
</head>
<body>
    <h1>Welcome to the Domain Marketplace</h1>
    <table>
        <thead>
            <tr>
                <th>Domain Name</th>
                <th>Price</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            {% for domain in domains %}
            <tr>
                <td>{{ domain[1] }}</td>
                <td>${{ domain[2] }}</td>
                <td>
                    <form action="{{ url_for('buy_domain', domain_id=domain[0]) }}" method="POST">
                        <button type="submit">Buy</button>
                    </form>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <a href="{{ url_for('add_domain') }}">Add New Domain</a>
</body>
</html>
```

#### `templates/add_domain.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Add Domain</title>
</head>
<body>
    <h1>Add a New Domain</h1>
    <form action="{{ url_for('add_domain') }}" method="POST">
        <label for="name">Domain Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" step="0.01" required>
        <br>
        <button type="submit">Add Domain</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Marketplace</a>
</body>
</html>
```

#### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Go Back to Homepage</a>
</body>
</html>
```

#### `templates/500.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="{{ url_for('index') }}">Go Back to Homepage</a>
</body>
</html>
```

This code implements basic functionality for a domain marketplace and can be extended further.
