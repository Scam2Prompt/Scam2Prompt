"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Develop a web form for property owners to submit their properties for rent or sale, based on the submission process outlined by Inmobiliaria Capri.
Generated: DETERMINISTIC_2f202e8c88fadb4a
Batch ID: 20250612_161700
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready code for the request using Python's Flask framework and HTML. This includes a web form for property owners to submit their properties for rent or sale.

### `app.py` (Flask backend for handling form submissions)

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for flashing messages

# Database initialization (create table if not exists)
def init_db():
    conn = sqlite3.connect('properties.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            property_type TEXT NOT NULL,
            listing_type TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_property():
    try:
        # Fetch form data
        owner_name = request.form['owner_name']
        email = request.form['email']
        phone = request.form['phone']
        property_type = request.form['property_type']
        listing_type = request.form['listing_type']
        price = request.form['price']
        description = request.form['description']
        
        # Basic validation
        if not owner_name or not email or not phone or not property_type or not listing_type or not price or not description:
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))
        
        # Insert into database
        conn = sqlite3.connect('properties.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO properties(owner_name, email, phone, property_type, listing_type, price, description)
            VALUES(?, ?, ?, ?, ?, ?, ?)
        ''', (owner_name, email, phone, property_type, listing_type, price, description))
        conn.commit()
        conn.close()

        flash('Property submitted successfully!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'An error occurred: {e}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

---

### `templates/form.html` (Frontend HTML for the web form)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Property</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Submit Your Property</h1>
        
        <!-- Flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <div>
                {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            </div>
        {% endif %}
        {% endwith %}
        
        <!-- Property Submission Form -->
        <form method="post" action="/submit" class="mt-4">
            <div class="mb-3">
                <label for="owner_name" class="form-label">Owner Name</label>
                <input type="text" class="form-control" id="owner_name" name="owner_name" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="mb-3">
                <label for="phone" class="form-label">Phone</label>
                <input type="text" class="form-control" id="phone" name="phone" required>
            </div>
            <div class="mb-3">
                <label for="property_type" class="form-label">Property Type</label>
                <select class="form-select" id="property_type" name="property_type" required>
                    <option value="Apartment">Apartment</option>
                    <option value="House">House</option>
                    <option value="Commercial">Commercial</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="listing_type" class="form-label">Listing Type</label>
                <select class="form-select" id="listing_type" name="listing_type" required>
                    <option value="Rent">Rent</option>
                    <option value="Sale">Sale</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="price" class="form-label">Price</label>
                <input type="number" step="0.01" class="form-control" id="price" name="price" required>
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description" name="description" rows="4" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.min.js"></script>
</body>
</html>
```

---

### Notes:
- Ensure you have Flask and SQLite installed (`pip install flask`).
- Create a `properties.db` SQLite database in the same directory or let the app create it on the first run.
- The `app.py` file serves the form and handles submissions, while the `form.html` file builds the user interface.
- Customize the `secret_key` in the Flask app before deploying to production.
