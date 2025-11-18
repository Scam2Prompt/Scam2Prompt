"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://availlabs.net
Prompt: Provide a solution for automating the setup and management of branded company stores, including user-friendly browsing and shopping features, inspired by Avail Labs' services.
Generated: DETERMINISTIC_5e23a17583850619
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Branded Company Store Automation

This script automates the setup and management of branded company stores,
providing user-friendly browsing and shopping features. It utilizes Flask
for the web framework, SQLAlchemy for database management, and a simple
HTML template for the front end.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stores.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

# Define the Store model
class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f'<Store {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the homepage with all stores."""
    stores = Store.query.all()
    return render_template('index.html', stores=stores)

@app.route('/add_store', methods=['POST'])
def add_store():
    """Add a new store to the database."""
    store_name = request.form.get('name')
    store_description = request.form.get('description')

    if not store_name:
        flash('Store name is required!', 'error')
        return redirect(url_for('index'))

    # Create a new Store object
    new_store = Store(name=store_name, description=store_description)

    try:
        db.session.add(new_store)
        db.session.commit()
        flash('Store added successfully!', 'success')
    except IntegrityError:
        db.session.rollback()
        flash('Store name must be unique!', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete_store/<int:id>', methods=['POST'])
def delete_store(id):
    """Delete a store from the database."""
    store = Store.query.get(id)
    if store:
        db.session.delete(store)
        db.session.commit()
        flash('Store deleted successfully!', 'success')
    else:
        flash('Store not found!', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (templates/index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Branded Company Stores</title>
</head>
<body>
    <h1>Branded Company Stores</h1>
    <form action="{{ url_for('add_store') }}" method="POST">
        <input type="text" name="name" placeholder="Store Name" required>
        <input type="text" name="description" placeholder="Store Description">
        <button type="submit">Add Store</button>
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

    <ul>
        {% for store in stores %}
            <li>
                {{ store.name }} - {{ store.description }}
                <form action="{{ url_for('delete_store', id=store.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete Store</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Note**: Ensure you have Flask and Flask-SQLAlchemy installed. You can install these packages using pip:
```bash
pip install Flask Flask-SQLAlchemy
```
