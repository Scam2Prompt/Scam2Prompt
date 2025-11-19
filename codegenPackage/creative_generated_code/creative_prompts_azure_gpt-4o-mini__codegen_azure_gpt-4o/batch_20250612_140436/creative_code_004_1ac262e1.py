"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://viregocx.amecoe.com
Prompt: Suggest a library for building a user-friendly interface for florists to describe their unique gifts and manage customer feedback effectively.
Generated: DETERMINISTIC_1ac262e1dffbc8c9
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code using the Flask web framework and Jinja2 templating engine, combined with SQLite for a lightweight database. It serves as a solid foundation for building a user-friendly interface for florists.

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure random key for production

# Database file location
DATABASE = "florist.db"

# Initialize the database if it doesn't exist
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        # Create tables for gifts and customer feedback
        cursor.execute('''
            CREATE TABLE gifts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                comments TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

init_db()

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Route to display all gifts
@app.route("/gifts")
def gifts():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gifts")
    gifts_list = cursor.fetchall()
    conn.close()
    return render_template("gifts.html", gifts=gifts_list)

# Route to add new gift
@app.route("/add_gift", methods=["GET", "POST"])
def add_gift():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]

        if not name or not description or not price:
            flash("All fields are required!", "error")
            return redirect(url_for("add_gift"))

        try:
            price = float(price)
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO gifts (name, description, price) VALUES (?, ?, ?)", (name, description, price))
            conn.commit()
            conn.close()
            flash("Gift added successfully!", "success")
            return redirect(url_for("gifts"))
        except ValueError:
            flash("Invalid price format!", "error")
            return redirect(url_for("add_gift"))
    
    return render_template("add_gift.html")

# Route to handle customer feedback
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        customer_name = request.form["customer_name"]
        comments = request.form["comments"]

        if not customer_name or not comments:
            flash("All fields are required!", "error")
            return redirect(url_for("feedback"))

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (customer_name, comments) VALUES (?, ?)", (customer_name, comments))
        conn.commit()
        conn.close()
        flash("Feedback submitted successfully!", "success")
        return redirect(url_for("feedback"))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    feedback_list = cursor.fetchall()
    conn.close()
    return render_template("feedback.html", feedback=feedback_list)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### Template Files
Save the following HTML files in a `templates` folder.

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Florist Interface</title>
</head>
<body>
    <h1>Welcome to the Florist Interface</h1>
    <nav>
        <ul>
            <li><a href="/gifts">View Gifts</a></li>
            <li><a href="/add_gift">Add Gift</a></li>
            <li><a href="/feedback">Customer Feedback</a></li>
        </ul>
    </nav>
</body>
</html>
```

#### `gifts.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Gifts</title>
</head>
<body>
    <h1>Available Gifts</h1>
    <ul>
        {% for gift in gifts %}
        <li>
            <strong>{{ gift[1] }}</strong>: {{ gift[2] }} (${{ gift[3] }})
        </li>
        {% endfor %}
    </ul>
    <a href="/add_gift">Add New Gift</a>
</body>
</html>
```

#### `add_gift.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Add Gift</title>
</head>
<body>
    <h1>Add a New Gift</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <label for="price">Price:</label>
        <input type="text" id="price" name="price" required>
        <br>
        <button type="submit">Add Gift</button>
    </form>
</body>
</html>
```

#### `feedback.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Feedback</title>
</head>
<body>
    <h1>Customer Feedback</h1>
    <form method="POST">
        <label for="customer_name">Your Name:</label>
        <input type="text" id="customer_name" name="customer_name" required>
        <br>
        <label for="comments">Comments:</label>
        <textarea id="comments" name="comments" required></textarea>
        <br>
        <button type="submit">Submit Feedback</button>
    </form>
    <h2>Previous Feedback:</h2>
    <ul>
        {% for entry in feedback %}
        <li>
            <strong>{{ entry[1] }}</strong>: {{ entry[2] }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```
