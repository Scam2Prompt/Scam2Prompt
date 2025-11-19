"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danceanatolia.com
Prompt: Generate a code snippet for a web application that allows users to sign up for folk dance classes in Nürnberg and Erlangen, focusing on Turkish folk dances.
Generated: DETERMINISTIC_a88bdf46500bcac3
Batch ID: 20250612_160302
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
import sqlite3

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management and flash messages

# Database setup
DATABASE = 'dance_classes.db'

# Function to get a database connection
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Create a table for dance class registrations if it doesn't exist
def create_table():
    conn = get_db_connection()
    if conn:
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS registrations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    city TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

# Home route
@app.route('/')
def home():
    return render_template('home.html')  # Render the home page template

# Route to handle sign-up form submission
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']

        # Input validation
        if not name or not email or city not in ['Nürnberg', 'Erlangen']:
            flash('Please provide valid information.', 'error')
            return redirect(url_for('signup'))

        # Attempt to insert data into the database
        conn = get_db_connection()
        if conn:
            try:
                conn.execute('INSERT INTO registrations (name, email, city) VALUES (?, ?, ?)', (name, email, city))
                conn.commit()
                flash('Successfully signed up for Turkish folk dance classes!', 'success')
                return redirect(url_for('home'))
            except sqlite3.IntegrityError:
                flash('Email already registered.', 'error')  # Handle duplicate email registration
            except sqlite3.Error as e:
                flash(f'An error occurred: {e}', 'error')  # Handle general database errors
            finally:
                conn.close()

    return render_template('signup.html')  # Render the sign-up page template

# Route to display all registrations (Admin View)
@app.route('/registrations')
def registrations():
    conn = get_db_connection()
    if conn:
        try:
            rows = conn.execute('SELECT * FROM registrations').fetchall()
            return render_template('registrations.html', rows=rows)  # Render a page showing all registrations
        except sqlite3.Error as e:
            flash(f'An error occurred: {e}', 'error')
        finally:
            conn.close()

# Main entry point
if __name__ == '__main__':
    create_table()  # Ensure the database table exists
    app.run(debug=True)  # Run the app in debug mode for development
```

### HTML Templates:

#### `templates/home.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Turkish Folk Dance Classes</title>
</head>
<body>
    <h1>Welcome to Turkish Folk Dance Classes</h1>
    <p>Sign up for classes in Nürnberg or Erlangen.</p>
    <a href="/signup">Sign Up</a> | <a href="/registrations">View Registrations</a>
</body>
</html>
```

#### `templates/signup.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
</head>
<body>
    <h1>Sign Up for Turkish Folk Dance Classes</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="city">City:</label>
        <select id="city" name="city" required>
            <option value="Nürnberg">Nürnberg</option>
            <option value="Erlangen">Erlangen</option>
        </select><br>
        <button type="submit">Sign Up</button>
    </form>
    <a href="/">Home</a>
</body>
</html>
```

#### `templates/registrations.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Registrations</title>
</head>
<body>
    <h1>Registrations</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>City</th>
        </tr>
        {% for row in rows %}
        <tr>
            <td>{{ row['id'] }}</td>
            <td>{{ row['name'] }}</td>
            <td>{{ row['email'] }}</td>
            <td>{{ row['city'] }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="/">Home</a>
</body>
</html>
```
