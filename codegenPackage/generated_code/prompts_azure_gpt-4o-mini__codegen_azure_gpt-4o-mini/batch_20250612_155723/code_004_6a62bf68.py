"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Suggest a framework for building a community-focused website that highlights local entrepreneurs and their stories, akin to the content on The Faces of Sedona and the Verde Valley.
Generated: DETERMINISTIC_6a62bf6869ff846a
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the application with a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entrepreneurs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Entrepreneur model
class Entrepreneur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    story = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Entrepreneur {self.name}>'

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template("error.html", error=e), e.code

# Route to display all entrepreneurs
@app.route('/')
def index():
    entrepreneurs = Entrepreneur.query.all()
    return render_template('index.html', entrepreneurs=entrepreneurs)

# Route to add a new entrepreneur
@app.route('/add', methods=['GET', 'POST'])
def add_entrepreneur():
    if request.method == 'POST':
        name = request.form['name']
        story = request.form['story']
        
        # Basic validation
        if not name or not story:
            flash('Name and story are required!', 'error')
            return redirect(url_for('add_entrepreneur'))

        new_entrepreneur = Entrepreneur(name=name, story=story)
        db.session.add(new_entrepreneur)
        db.session.commit()
        flash('Entrepreneur added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add.html')

# Route to delete an entrepreneur
@app.route('/delete/<int:id>', methods=['POST'])
def delete_entrepreneur(id):
    entrepreneur = Entrepreneur.query.get_or_404(id)
    db.session.delete(entrepreneur)
    db.session.commit()
    flash('Entrepreneur deleted successfully!', 'success')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entrepreneurs</title>
</head>
<body>
    <h1>Local Entrepreneurs</h1>
    <a href="{{ url_for('add_entrepreneur') }}">Add Entrepreneur</a>
    <ul>
        {% for entrepreneur in entrepreneurs %}
            <li>
                <strong>{{ entrepreneur.name }}</strong>: {{ entrepreneur.story }}
                <form action="{{ url_for('delete_entrepreneur', id=entrepreneur.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Entrepreneur</title>
</head>
<body>
    <h1>Add Entrepreneur</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="story">Story:</label>
        <textarea id="story" name="story" required></textarea>
        <br>
        <button type="submit">Add</button>
    </form>
    <a href="{{ url_for('index') }}">Back to list</a>
</body>
</html>
```

**error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error {{ error.code }}</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('index') }}">Back to home</a>
</body>
</html>
```

### Notes
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment.
- Run `flask db init`, `flask db migrate`, and `flask db upgrade` to set up the database.
- Replace `'your_secret_key'` with a secure random key for production use.
