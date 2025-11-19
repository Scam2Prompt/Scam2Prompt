"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Develop a web application that showcases the history and symbols of an educational institution, inspired by the content from I.E. Benjamín Correa Álvarez.
Generated: DETERMINISTIC_0e7f39774e336b57
Batch ID: 20250612_140309
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initializing the Flask application
app = Flask(__name__)

# Configuring the database URI and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///institution_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initializing the SQLAlchemy database
db = SQLAlchemy(app)

# Defining the model for storing history and symbols
class HistorySymbol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<HistorySymbol {self.title}>'

# Creating the database tables
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    # Fetching all history and symbols from the database
    symbols = HistorySymbol.query.all()
    return render_template('index.html', symbols=symbols)

# Route for adding a new history/symbol
@app.route('/add', methods=['POST'])
def add_symbol():
    # Retrieving data from form submission
    title = request.form.get('title')
    description = request.form.get('description')

    # Error handling for empty fields
    if not title or not description:
        flash('Title and description are required!', 'error')
        return redirect(url_for('index'))

    # Creating a new history/symbol entry
    new_symbol = HistorySymbol(title=title, description=description)

    # Adding to the database
    try:
        db.session.add(new_symbol)
        db.session.commit()
        flash('New symbol added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding symbol: {e}', 'error')
    return redirect(url_for('index'))

# Route for deleting a symbol
@app.route('/delete/<int:symbol_id>')
def delete_symbol(symbol_id):
    # Fetching the symbol to be deleted
    symbol_to_delete = HistorySymbol.query.get_or_404(symbol_id)

    # Deleting the symbol from the database
    try:
        db.session.delete(symbol_to_delete)
        db.session.commit()
        flash('Symbol deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting symbol: {e}', 'error')
    return redirect(url_for('index'))

# Running the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Institution History and Symbols</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">History and Symbols of the Institution</h1>
        <form method="POST" action="/add" class="mt-3">
            <div class="form-group">
                <input type="text" name="title" class="form-control" placeholder="Symbol Title" required>
            </div>
            <div class="form-group">
                <textarea name="description" class="form-control" placeholder="Description" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Add Symbol</button>
        </form>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="mt-3">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}

        <h2 class="mt-5">Symbols List</h2>
        <ul class="list-group mt-3">
            {% for symbol in symbols %}
                <li class="list-group-item">
                    <h5>{{ symbol.title }}</h5>
                    <p>{{ symbol.description }}</p>
                    <a href="{{ url_for('delete_symbol', symbol_id=symbol.id) }}" class="btn btn-danger">Delete</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

### Notes:
- Ensure you have Flask and SQLAlchemy installed in your environment.
- Replace `'your_secret_key_here'` with an actual secret key for production.
- SQLite is used for simplicity; consider using a more robust database in production.
- Run the application with the command `python app.py`.
