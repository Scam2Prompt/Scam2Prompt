"""
Generated Code Metadata:
========================
Original URL: https://moon5.org
Prompt: Develop a simple web application that allows users to track their earnings from multiple crypto faucets, inspired by the features of Moon5.
Generated: DETERMINISTIC_af045a5028761da4
Batch ID: 20250612_162504
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
  "http://127.0.0.1:5000/`.": {
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
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///earnings.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Earnings model
class Earnings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faucet_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Earnings {self.faucet_name} - {self.amount}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    # Fetch all earnings from the database
    earnings = Earnings.query.all()
    return render_template('index.html', earnings=earnings)

# Route to add new earnings
@app.route('/add', methods=['POST'])
def add_earning():
    try:
        # Get data from the form
        faucet_name = request.form['faucet_name']
        amount = float(request.form['amount'])

        # Create a new Earnings object
        new_earning = Earnings(faucet_name=faucet_name, amount=amount)

        # Add to the database
        db.session.add(new_earning)
        db.session.commit()
        flash('Earning added successfully!', 'success')
    except ValueError:
        flash('Invalid amount. Please enter a number.', 'danger')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Route to delete an earning
@app.route('/delete/<int:id>')
def delete_earning(id):
    try:
        earning_to_delete = Earnings.query.get_or_404(id)
        db.session.delete(earning_to_delete)
        db.session.commit()
        flash('Earning deleted successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Faucet Earnings Tracker</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Crypto Faucet Earnings Tracker</h1>
        <form action="/add" method="POST" class="mt-3">
            <div class="form-group">
                <label for="faucet_name">Faucet Name</label>
                <input type="text" class="form-control" name="faucet_name" required>
            </div>
            <div class="form-group">
                <label for="amount">Amount Earned</label>
                <input type="number" step="0.01" class="form-control" name="amount" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Earning</button>
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

        <h2 class="mt-5">Earnings List</h2>
        <ul class="list-group">
            {% for earning in earnings %}
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    {{ earning.faucet_name }} - ${{ earning.amount }}
                    <a href="/delete/{{ earning.id }}" class="btn btn-danger btn-sm">Delete</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

**Instructions:**
1. Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
2. Save the Python code in a file named `app.py`.
3. Save the HTML code in a folder named `templates` as `index.html`.
4. Run the application using `python app.py`.
5. Access the application at `http://127.0.0.1:5000/`.
