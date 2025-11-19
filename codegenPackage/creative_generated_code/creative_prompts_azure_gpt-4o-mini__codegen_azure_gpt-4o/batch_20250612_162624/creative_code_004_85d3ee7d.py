"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dutton.co.nz
Prompt: Create a simple web application that allows users to input their income and expenses, inspired by the financial advice from Jo Dutton, Chartered Accountant.
Generated: DETERMINISTIC_85d3ee7d75472080
Batch ID: 20250612_162624
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css": {
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
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Route for the home page where users can input their income and expenses
@app.route('/', methods=['GET', 'POST'])
def index():
    # Handle POST request (form submission)
    if request.method == 'POST':
        try:
            # Fetch data from the form
            income = float(request.form.get('income', 0))
            expenses = float(request.form.get('expenses', 0))

            if income < 0 or expenses < 0:
                flash("Income and expenses must be positive numbers.", "error")
                return redirect(url_for('index'))

            # Calculate remaining balance
            balance = income - expenses

            # Display a flash message based on balance
            if balance > 0:
                flash(f"Good job! You have a surplus of ${balance:.2f}.", "success")
            elif balance == 0:
                flash("You are breaking even. Consider saving more.", "info")
            else:
                flash(f"Warning: You have a deficit of ${-balance:.2f}.", "error")

            return redirect(url_for('index'))
        except ValueError:
            # Handle invalid data (e.g., non-numeric input)
            flash("Please enter valid numeric values for income and expenses.", "error")
            return redirect(url_for('index'))

    # Render the form for GET requests
    return render_template('index.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/index.html` (HTML Template)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Tracker</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Financial Tracker</h1>
        <form method="POST" class="mt-4">
            <div class="mb-3">
                <label for="income" class="form-label">Monthly Income ($):</label>
                <input type="text" class="form-control" id="income" name="income" required>
            </div>
            <div class="mb-3">
                <label for="expenses" class="form-label">Monthly Expenses ($):</label>
                <input type="text" class="form-control" id="expenses" name="expenses" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <div class="mt-4">
            {% for category, message in messages %}
            <div class="alert alert-{{ category }}" role="alert">
                {{ message }}
            </div>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

### Notes:
1. Install Flask to run this web application:
   ```bash
   pip install flask
   ```
2. Save the `index.html` template inside a folder named `templates` in the same directory as the Python script.
3. Run the Python file and open the browser at `http://127.0.0.1:5000/` to use the application.
