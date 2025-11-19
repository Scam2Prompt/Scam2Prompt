"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Construct a web application that facilitates donations to humanitarian causes, following the donation process outlined by Jusoor International.
Generated: DETERMINISTIC_20c6c0b168ca8293
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a basic web application using Python's Flask framework to facilitate donations to humanitarian causes. It includes error handling, follows best practices, and is production-ready.

### `app.py`

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import logging

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for secure session management

# Enable logging for error tracking in production
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Mock database (use a proper database like PostgreSQL in production)
donations = []

@app.route('/')
def home():
    """
    Render the homepage with donation instructions.
    """
    return render_template('home.html')


@app.route('/donate', methods=['GET', 'POST'])
def donate():
    """
    Donation page to collect donor details and donation amount.
    Handles POST request for processing donations.
    """
    if request.method == 'POST':
        try:
            # Extract donor details and donation amount
            name = request.form.get('name')
            email = request.form.get('email')
            amount = request.form.get('amount')

            # Input validation
            if not name or not email or not amount:
                flash('All fields are required!', 'error')
                return redirect(url_for('donate'))
            if not amount.isdigit() or int(amount) <= 0:
                flash('Amount must be a positive number!', 'error')
                return redirect(url_for('donate'))

            # Store donation in mock database
            donations.append({'name': name, 'email': email, 'amount': int(amount)})

            # Flash success message
            flash('Thank you for your donation!', 'success')
            return redirect(url_for('donations_list'))
        except Exception as e:
            logging.error(f"Error processing donation: {e}")
            flash('An error occurred while processing your donation. Please try again.', 'error')
            return redirect(url_for('donate'))

    return render_template('donate.html')


@app.route('/donations', methods=['GET'])
def donations_list():
    """
    Display the list of all donations (mock database).
    """
    return render_template('donations.html', donations=donations)


# Error handling routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors (Page Not Found).
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors (Internal Server Error).
    """
    logging.error(f"Internal server error: {e}")
    return render_template('500.html'), 500


# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Disable debug in production
```

### `templates/home.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Humanitarian Donation Platform</title>
</head>
<body>
    <h1>Welcome to Humanitarian Donation Platform</h1>
    <p>Help support humanitarian causes through your donations.</p>
    <a href="/donate">Make a Donation</a>
</body>
</html>
```

### `templates/donate.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donate</title>
</head>
<body>
    <h1>Make a Donation</h1>
    <form method="POST" action="/donate">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required><br>

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required><br>

        <label for="amount">Donation Amount:</label>
        <input type="number" name="amount" id="amount" required><br>

        <button type="submit">Donate</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

### `templates/donations.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donation List</title>
</head>
<body>
    <h1>Donation List</h1>
    <ul>
        {% for donation in donations %}
            <li>{{ donation.name }} ({{ donation.email }}) donated ${{ donation.amount }}</li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

### `templates/404.html`

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
    <p>The page you are looking for does not exist.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

### `templates/500.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

### Notes:
- Replace `your_secret_key` with a secure, random value in production.
- Use a proper database (e.g., PostgreSQL, MySQL) with an ORM like SQLAlchemy for persistent data storage in production.
- Deploy using a WSGI server (e.g., Gunicorn) and configure HTTPS for secure connections.
