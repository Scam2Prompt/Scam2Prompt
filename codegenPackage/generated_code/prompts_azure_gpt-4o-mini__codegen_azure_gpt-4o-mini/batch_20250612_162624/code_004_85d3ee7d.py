"""
Generated Code Metadata:
========================
Original URL: https://dutton.co.nz
Prompt: Create a simple web application that allows users to input their income and expenses, inspired by the financial advice from Jo Dutton, Chartered Accountant.
Generated: DETERMINISTIC_85d3ee7d75472080
Batch ID: 20250612_162624
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finances.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db = SQLAlchemy(app)

# Define the database model for Income and Expenses
class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float, nullable=False)
    expenses = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Finance {self.id}: Income={self.income}, Expenses={self.expenses}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get income and expenses from the form
            income = float(request.form['income'])
            expenses = float(request.form['expenses'])

            # Create a new Finance record
            new_finance = Finance(income=income, expenses=expenses)
            db.session.add(new_finance)
            db.session.commit()

            flash('Financial data added successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Please enter valid numbers for income and expenses.', 'danger')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')

    # Retrieve all finance records
    finances = Finance.query.all()
    return render_template('index.html', finances=finances)

# Route for deleting a finance record
@app.route('/delete/<int:id>')
def delete(id):
    try:
        finance_to_delete = Finance.query.get_or_404(id)
        db.session.delete(finance_to_delete)
        db.session.commit()
        flash('Financial record deleted successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (templates/index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Finance Tracker</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Finance Tracker</h1>
        <form method="POST" class="mt-4">
            <div class="form-group">
                <label for="income">Income</label>
                <input type="number" step="0.01" class="form-control" name="income" required>
            </div>
            <div class="form-group">
                <label for="expenses">Expenses</label>
                <input type="number" step="0.01" class="form-control" name="expenses" required>
            </div>
            <button type="submit" class="btn btn-primary">Add Financial Data</button>
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

        <h2 class="mt-5">Financial Records</h2>
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Income</th>
                    <th>Expenses</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for finance in finances %}
                    <tr>
                        <td>{{ finance.id }}</td>
                        <td>{{ finance.income }}</td>
                        <td>{{ finance.expenses }}</td>
                        <td>
                            <a href="{{ url_for('delete', id=finance.id) }}" class="btn btn-danger">Delete</a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```

**Instructions**:
1. Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
2. Save the Python code in a file named `app.py`.
3. Create a folder named `templates` in the same directory as `app.py` and save the HTML code in a file named `index.html` inside the `templates` folder.
4. Run the application using `python app.py` and access it at `http://127.0.0.1:5000/`.
