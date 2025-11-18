"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: Generate code for a web application that integrates digital marketing strategies to reach a broader audience, inspired by the services provided by the Canadian Tech-Institute for Academic Research.
Generated: DETERMINISTIC_6eed505bbe506d46
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for the web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key

# Initialize the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the database model for marketing strategies
class MarketingStrategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<MarketingStrategy {self.title}>'

# Route to display all marketing strategies
@app.route('/')
def index():
    strategies = MarketingStrategy.query.all()
    return render_template('index.html', strategies=strategies)

# Route to add a new marketing strategy
@app.route('/add', methods=['GET', 'POST'])
def add_strategy():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        # Input validation
        if not title or not description:
            flash('Title and description are required!', 'danger')
            return redirect(url_for('add_strategy'))

        # Create a new MarketingStrategy instance
        new_strategy = MarketingStrategy(title=title, description=description)
        
        # Add to the database and commit
        try:
            db.session.add(new_strategy)
            db.session.commit()
            flash('Marketing strategy added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding strategy: {str(e)}', 'danger')
        
        return redirect(url_for('index'))

    return render_template('add_strategy.html')

# Route to delete a marketing strategy
@app.route('/delete/<int:id>', methods=['POST'])
def delete_strategy(id):
    strategy = MarketingStrategy.query.get_or_404(id)
    try:
        db.session.delete(strategy)
        db.session.commit()
        flash('Marketing strategy deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting strategy: {str(e)}', 'danger')
    
    return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Turn off debug for production use
```

### HTML Templates
**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketing Strategies</title>
</head>
<body>
    <h1>Marketing Strategies</h1>
    <a href="{{ url_for('add_strategy') }}">Add New Strategy</a>

    {% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}

    <ul>
        {% for strategy in strategies %}
            <li>{{ strategy.title }} - {{ strategy.description }}
                <form action="{{ url_for('delete_strategy', id=strategy.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_strategy.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Marketing Strategy</title>
</head>
<body>
    <h1>Add Marketing Strategy</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <button type="submit">Add Strategy</button>
    </form>
    <a href="{{ url_for('index') }}">Back</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Return to Home</a>
</body>
</html>
``` 

This code provides a simple web application using Flask that allows users to add, view, and delete marketing strategies. It includes input validation, error handling, and feedback messages for user interactions.
