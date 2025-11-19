"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasclub.xyz
Prompt: "Design a simple web application using Flask or Django to display tech product promotions, inspired by the耳机促销价639元 announcement on this site."
Generated: DETERMINISTIC_4453ff96dee2fd1d
Batch ID: 20250622_210718
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///promotions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the Promotion model
class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Promotion {self.product_name} - {self.price}>'

# Route to display all promotions
@app.route('/')
def index():
    promotions = Promotion.query.all()
    return render_template('index.html', promotions=promotions)

# Route to add a new promotion
@app.route('/add', methods=['POST'])
def add_promotion():
    try:
        product_name = request.form['product_name']
        price = float(request.form['price'])
        new_promotion = Promotion(product_name=product_name, price=price)
        db.session.add(new_promotion)
        db.session.commit()
        flash('Promotion added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding promotion: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Route to delete a promotion
@app.route('/delete/<int:id>')
def delete_promotion(id):
    try:
        promotion = Promotion.query.get_or_404(id)
        db.session.delete(promotion)
        db.session.commit()
        flash('Promotion deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting promotion: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production

```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Product Promotions</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Tech Product Promotions</h1>
        <form action="/add" method="POST" class="mt-3">
            <div class="form-group">
                <input type="text" name="product_name" class="form-control" placeholder="Product Name" required>
            </div>
            <div class="form-group">
                <input type="number" step="0.01" name="price" class="form-control" placeholder="Price (in Yuan)" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Promotion</button>
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

        <h2 class="mt-5">Current Promotions</h2>
        <ul class="list-group">
            {% for promotion in promotions %}
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    {{ promotion.product_name }} - ¥{{ promotion.price }}
                    <a href="{{ url_for('delete_promotion', id=promotion.id) }}" class="btn btn-danger btn-sm">Delete</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

### Instructions to Run the Application:
1. Ensure you have Python and Flask installed. You can install Flask and Flask-SQLAlchemy using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the Python code in a file named `app.py` and the HTML code in a folder named `templates` as `index.html`.
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.
