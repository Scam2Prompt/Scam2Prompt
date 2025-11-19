"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.manatoken.net
Prompt: How can I build a web application that mimics the functionality of Stumble! for discovering and rating websites?
Generated: DETERMINISTIC_eb957733f580229a
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean, runnable Python web application using Flask that mimics the functionality of Stumble! for discovering and rating websites:

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import random

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set your secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web_discovery.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing websites
class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True, nullable=False)
    rating = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Website {self.url}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the homepage which shows a random website
@app.route('/')
def index():
    """Render the homepage with a random website."""
    websites = Website.query.all()
    if not websites:
        return render_template('index.html', website=None)
    
    website = random.choice(websites)
    return render_template('index.html', website=website)

# Route for rating a website
@app.route('/rate/<int:website_id>', methods=['POST'])
def rate_website(website_id):
    """Rate a website."""
    rating = request.form.get('rating', type=float)
    if rating is None or not (0 <= rating <= 5):
        flash('Rating must be between 0 and 5.', 'error')
        return redirect(url_for('index'))

    website = Website.query.get_or_404(website_id)
    website.rating = rating  # Update the rating
    db.session.commit()
    flash('Thank you for your rating!', 'success')

    return redirect(url_for('index'))

# Route for adding a new website
@app.route('/add', methods=['POST'])
def add_website():
    """Add a new website to the database."""
    url = request.form.get('url')
    if not url:
        flash('URL cannot be empty.', 'error')
        return redirect(url_for('index'))

    new_website = Website(url=url)
    try:
        db.session.add(new_website)
        db.session.commit()
        flash('Website added successfully!', 'success')
    except IntegrityError:
        db.session.rollback()
        flash('This website already exists.', 'error')
    
    return redirect(url_for('index'))

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Files:**

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Discovery</title>
</head>
<body>
    <h1>Discover a Website</h1>
    {% if website %}
        <p>Check this out: <a href="{{ website.url }}">{{ website.url }}</a></p>
        <form action="{{ url_for('rate_website', website_id=website.id) }}" method="post">
            <label for="rating">Rate this website (0 to 5):</label>
            <input type="number" name="rating" min="0" max="5" step="0.1" required>
            <button type="submit">Submit Rating</button>
        </form>
    {% else %}
        <p>No websites available. Add one!</p>
    {% endif %}
    
    <h2>Add a New Website</h2>
    <form action="{{ url_for('add_website') }}" method="post">
        <label for="url">Website URL:</label>
        <input type="text" name="url" required>
        <button type="submit">Add Website</button>
    </form>

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

2. **404.html**
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
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
```

**Notes:**
- Ensure you have Flask and SQLAlchemy installed in your Python environment.
- Replace `'your_secret_key'` with an actual secret key for production use.
- The database is SQLite for simplicity; for production, consider using a more robust database like PostgreSQL or MySQL.
