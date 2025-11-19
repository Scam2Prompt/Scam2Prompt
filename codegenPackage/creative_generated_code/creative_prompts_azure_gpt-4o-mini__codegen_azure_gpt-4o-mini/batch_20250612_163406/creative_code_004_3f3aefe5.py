"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Suggest a library for building a web application that showcases rare toys, utilizing categories like "Brinquedo de Jardim" and "Empilhadeira."
Generated: DETERMINISTIC_3f3aefe5863a9b62
Batch ID: 20250612_163406
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
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toys.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Toy model
class Toy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Toy {self.name} in {self.category}>'

# Route for the homepage
@app.route('/')
def index():
    """Render the homepage with a list of toys."""
    toys = Toy.query.all()
    return render_template('index.html', toys=toys)

# Route to add a new toy
@app.route('/add', methods=['POST'])
def add_toy():
    """Add a new toy to the database."""
    try:
        toy_name = request.form['name']
        toy_category = request.form['category']
        
        # Validate inputs
        if not toy_name or not toy_category:
            flash('Both name and category are required!', 'error')
            return redirect(url_for('index'))
        
        new_toy = Toy(name=toy_name, category=toy_category)
        db.session.add(new_toy)
        db.session.commit()
        flash(f'Toy "{toy_name}" added successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'An error occurred: {str(e)}', 'error')
    return redirect(url_for('index'))

# Route to delete a toy
@app.route('/delete/<int:toy_id>', methods=['POST'])
def delete_toy(toy_id):
    """Delete a toy from the database."""
    try:
        toy_to_delete = Toy.query.get_or_404(toy_id)
        db.session.delete(toy_to_delete)
        db.session.commit()
        flash(f'Toy "{toy_to_delete.name}" deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'An error occurred: {str(e)}', 'error')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

### Required Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rare Toys Showcase</title>
</head>
<body>
    <h1>Rare Toys Showcase</h1>
    <ul>
        {% for toy in toys %}
            <li>
                {{ toy.name }} - {{ toy.category }}
                <form action="{{ url_for('delete_toy', toy_id=toy.id) }}" method="post" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>

    <h2>Add a New Toy</h2>
    <form action="{{ url_for('add_toy') }}" method="post">
        <input type="text" name="name" placeholder="Toy Name" required>
        <input type="text" name="category" placeholder="Category" required>
        <button type="submit">Add Toy</button>
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

### Additional Notes
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment.
- Replace `'your_secret_key'` with a strong random key for session management.
- This code is structured to be production-ready, utilizing Flask's best practices for web applications.
