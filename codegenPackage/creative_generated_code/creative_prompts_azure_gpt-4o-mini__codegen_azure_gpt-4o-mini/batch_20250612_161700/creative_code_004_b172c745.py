"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Illustrate how to implement a social media marketing strategy using a web platform, as discussed in the services of Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_b172c745726e6783
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web framework and database handling
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI and secret key for sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing_strategy.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

# Define the Strategy model
class Strategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(100), nullable=False)
    goals = db.Column(db.String(200), nullable=False)
    tactics = db.Column(db.String(500), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main page with a list of strategies."""
    strategies = Strategy.query.all()
    return render_template('index.html', strategies=strategies)

@app.route('/add_strategy', methods=['GET', 'POST'])
def add_strategy():
    """Handle the creation of a new social media strategy."""
    if request.method == 'POST':
        platform = request.form.get('platform')
        goals = request.form.get('goals')
        tactics = request.form.get('tactics')
        
        # Validate input
        if not platform or not goals or not tactics:
            flash('All fields are required.', 'error')
            return redirect(url_for('add_strategy'))
        
        # Add new strategy to the database
        new_strategy = Strategy(platform=platform, goals=goals, tactics=tactics)
        try:
            db.session.add(new_strategy)
            db.session.commit()
            flash('Strategy added successfully!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            flash('Error adding strategy. Please try again.', 'error')
            db.session.rollback()
    
    return render_template('add_strategy.html')

@app.route('/delete_strategy/<int:id>', methods=['POST'])
def delete_strategy(id):
    """Handle the deletion of a social media strategy."""
    strategy_to_delete = Strategy.query.get_or_404(id)
    db.session.delete(strategy_to_delete)
    db.session.commit()
    flash('Strategy deleted successfully!', 'success')
    return redirect(url_for('index'))

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error page."""
    return render_template('404.html'), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketing Strategy</title>
</head>
<body>
    <h1>Social Media Marketing Strategies</h1>
    <a href="{{ url_for('add_strategy') }}">Add New Strategy</a>
    <ul>
        {% for strategy in strategies %}
        <li>
            <strong>{{ strategy.platform }}</strong>: {{ strategy.goals }}
            <form action="{{ url_for('delete_strategy', id=strategy.id) }}" method="POST" style="display:inline;">
                <button type="submit">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### add_strategy.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Strategy</title>
</head>
<body>
    <h1>Add a New Social Media Strategy</h1>
    <form action="{{ url_for('add_strategy') }}" method="POST">
        <label for="platform">Platform:</label>
        <input type="text" id="platform" name="platform" required>
        <br>
        <label for="goals">Goals:</label>
        <input type="text" id="goals" name="goals" required>
        <br>
        <label for="tactics">Tactics:</label>
        <textarea id="tactics" name="tactics" required></textarea>
        <br>
        <button type="submit">Add Strategy</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Strategies</a>
</body>
</html>
```

#### 404.html
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
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Note
- Please ensure you have Flask and Flask-SQLAlchemy installed in your environment to run this code.
- You may need to set up a virtual environment and install the necessary packages via pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
