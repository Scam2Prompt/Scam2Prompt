"""
Generated Code Metadata:
========================
Original URL: https://mesogia.com
Prompt: Recommend a library or framework for building a multilingual directory website with categories like "Ωδεία" and "Ψυχίατροι," and provide an example of how to structure the database.
Generated: DETERMINISTIC_f5a374774dc57044
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Recommended Framework:** 
Flask or Django for Python, or Laravel for PHP. Here, I'll provide an example using Flask and Python.

**Required Libraries:**
- Flask
- Flask-SQLAlchemy for database operations
- Flask-Babel for multilingual support

**Installation:**
```bash
pip install Flask Flask-SQLAlchemy Flask-Babel
```

**Code:**
```python
# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///directory.db'
db = SQLAlchemy(app)
babel = Babel(app)

# Define a Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Category('{self.name}', '{self.slug}')"

# Define a Listing model
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('listings', lazy=True))

    def __repr__(self):
        return f"Listing('{self.title}', '{self.description}')"

# Define a Translation model for multilingual support
class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)
    listing = db.relationship('Listing', backref=db.backref('translations', lazy=True))
    language = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Translation('{self.language}', '{self.title}')"

@babel.localeselector
def get_locale():
    # Implement locale selection logic here
    return 'el'  # Default locale

@app.route('/')
def index():
    categories = Category.query.all()
    return render_template('index.html', categories=categories)

@app.route('/category/<slug>')
def category(slug):
    category = Category.query.filter_by(slug=slug).first_or_404()
    listings = category.listings
    return render_template('category.html', category=category, listings=listings)

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# models.py (not required but good practice)
from app import db

# All models defined in app.py
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Directory</title>
</head>
<body>
    <nav>
        <ul>
            {% for category in categories %}
                <li><a href="{{ url_for('category', slug=category.slug) }}">{{ category.name }}</a></li>
            {% endfor %}
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Directory</h1>
    <ul>
        {% for category in categories %}
            <li><a href="{{ url_for('category', slug=category.slug) }}">{{ category.name }}</a></li>
        {% endfor %}
    </ul>
{% endblock %}
```

```html
<!-- templates/category.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>{{ category.name }}</h1>
    <ul>
        {% for listing in listings %}
            <li>{{ listing.title }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

```python
# Create database tables
with app.app_context():
    db.create_all()
```

```python
# Add example categories and listings
with app.app_context():
    category1 = Category(name='Ωδεία', slug='odeia')
    category2 = Category(name='Ψυχίατροι', slug='psychiatroi')
    db.session.add_all([category1, category2])
    db.session.commit()

    listing1 = Listing(title='Example Listing 1', description='This is an example listing.', category=category1)
    listing2 = Listing(title='Example Listing 2', description='This is another example listing.', category=category2)
    db.session.add_all([listing1, listing2])
    db.session.commit()
```
