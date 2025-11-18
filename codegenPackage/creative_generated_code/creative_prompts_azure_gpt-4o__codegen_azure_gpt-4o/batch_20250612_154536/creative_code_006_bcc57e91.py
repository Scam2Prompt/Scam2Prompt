"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.optimism.rs
Prompt: Develop a web application that allows users to browse and purchase .rs domains, using optimism.rs as a reference for domain examples.
Generated: DETERMINISTIC_bcc57e916462e84e
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Secret key for flash messages

DATABASE = "domains.db"

# Ensure database exists
if not os.path.exists(DATABASE):
    def initialize_db():
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE domains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                purchased BOOLEAN NOT NULL DEFAULT FALSE
            )
            """
        )
        # Add some example .rs domains
        cursor.executemany(
            "INSERT INTO domains (name, price, purchased) VALUES (?, ?, ?)",
            [
                ("optimism.rs", 19.99, False),
                ("example.rs", 12.99, False),
                ("future.rs", 25.99, False),
                ("tech.rs", 15.50, False),
            ],
        )
        conn.commit()
        conn.close()

    initialize_db()

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    """
    Homepage: Displays a list of available .rs domains.
    """
    conn = get_db_connection()
    domains = conn.execute("SELECT * FROM domains WHERE purchased = 0").fetchall()
    conn.close()
    return render_template("index.html", domains=domains)


@app.route("/purchase/<int:domain_id>", methods=["POST"])
def purchase_domain(domain_id):
    """
    Handles purchasing a domain by its ID.
    """
    conn = get_db_connection()
    domain = conn.execute(
        "SELECT * FROM domains WHERE id = ? AND purchased = 0", (domain_id,)
    ).fetchone()

    if domain:
        conn.execute(
            "UPDATE domains SET purchased = 1 WHERE id = ?", (domain_id,)
        )
        conn.commit()
        conn.close()
        flash(f"Domain '{domain['name']}' purchased successfully!", "success")
    else:
        conn.close()
        flash("Domain is unavailable or already purchased.", "danger")

    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors gracefully by displaying a custom error page.
    """
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
``` 

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>.rs Domains</title>
</head>
<body>
    <h1>Available .rs Domains</h1>
    <ul>
        {% for domain in domains %}
        <li>
            <strong>{{ domain["name"] }}</strong> - ${{ domain["price"] }} 
            <form style="display:inline;" method="POST" action="{{ url_for('purchase_domain', domain_id=domain['id']) }}">
                <button type="submit">Purchase</button>
            </form>
        </li>
        {% endfor %}
    </ul>
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
    <ul>
        {% for category, message in messages %}
        <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    {% endwith %}
</body>
</html>
```

#### `templates/404.html`
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
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Return to Homepage</a>
</body>
</html>
```
