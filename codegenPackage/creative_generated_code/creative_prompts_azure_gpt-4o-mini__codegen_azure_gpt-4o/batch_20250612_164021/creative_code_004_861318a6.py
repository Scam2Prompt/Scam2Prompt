"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfcosmetics.com.ua
Prompt: Construct a code example that implements a user registration form for the ELF Cosmetics website, ensuring it captures essential details like email and password.
Generated: DETERMINISTIC_861318a60432a762
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
import re
import sqlite3

# Initialize Flask application
app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Secret key for session management

# Database setup
DATABASE = 'elf_cosmetics.db'

def init_db():
    """Initialize the database and create the users table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/', methods=['GET'])
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email format.", "danger")
            return redirect(url_for('register'))

        # Validate password length
        if len(password) < 8:
            flash("Password must be at least 8 characters long.", "danger")
            return redirect(url_for('register'))

        try:
            # Hash the password for secure storage
            hashed_password = generate_password_hash(password)

            # Store user details in the database
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
            conn.commit()
            conn.close()

            # Redirect on successful registration
            flash("Registration successful.", "success")
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            # Handle duplicate email error
            flash("Email already registered.", "danger")
            return redirect(url_for('register'))
        except Exception as e:
            # Handle other database errors
            flash("An error occurred during registration. Please try again.", "danger")
            print(f"Error: {e}")
            return redirect(url_for('register'))

    # Render the registration form if GET request
    return render_template('register.html')

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

**`templates/index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ELF Cosmetics</title>
</head>
<body>
    <h1>Welcome to ELF Cosmetics</h1>
    <a href="/register">Register Here</a>
</body>
</html>
```

**`templates/register.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - ELF Cosmetics</title>
</head>
<body>
    <h1>Register for ELF Cosmetics</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li style="color: {% if category == 'danger' %}red{% else %}green{% endif %};">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form method="POST" action="/register">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```
