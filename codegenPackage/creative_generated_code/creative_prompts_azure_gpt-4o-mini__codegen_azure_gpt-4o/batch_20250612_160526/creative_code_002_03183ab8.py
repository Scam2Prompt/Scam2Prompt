"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passive-income.online
Prompt: Create a simple web application using Flask that allows users to input their income streams and calculates their total monthly income, inspired by the Wealthery training program.
Generated: DETERMINISTIC_03183ab8b7e5dfff
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used for session management and flash messages

# Route for the home page
@app.route('/')
def home():
    """
    Render the home page where users can input their income streams.
    """
    return render_template('index.html')

# Route to handle income submission
@app.route('/submit_income', methods=['POST'])
def submit_income():
    """
    Handle the submission of income streams and calculate the total monthly income.
    """
    try:
        # Retrieve input values from the form
        income_streams = request.form.getlist('income_stream[]')

        # Ensure all inputs are valid numbers
        try:
            income_streams = [float(income) for income in income_streams if income.strip()]
        except ValueError:
            flash('Please enter valid numeric values for all income streams.', 'error')
            return redirect(url_for('home'))

        # Calculate the total monthly income
        total_income = sum(income_streams)

        # Render the results page with the calculated total income
        return render_template('results.html', total_income=total_income)
    except Exception as e:
        # Handle any unexpected errors
        flash(f"An error occurred: {str(e)}", 'error')
        return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Income Calculator</title>
</head>
<body>
    <h1>Monthly Income Calculator</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li style="color: {% if category == 'error' %}red{% else %}black{% endif %};">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form action="{{ url_for('submit_income') }}" method="POST">
        <label>Enter your income streams (monthly):</label>
        <div id="income-inputs">
            <input type="text" name="income_stream[]">
        </div>
        <button type="button" onclick="addIncomeInput()">Add Another Income Stream</button><br><br>
        <button type="submit">Calculate Total Income</button>
    </form>
    <script>
        // JavaScript function to dynamically add more input fields for income streams
        function addIncomeInput() {
            const inputDiv = document.createElement('div');
            const inputField = document.createElement('input');
            inputField.type = 'text';
            inputField.name = 'income_stream[]';
            inputDiv.appendChild(inputField);
            document.getElementById('income-inputs').appendChild(inputDiv);
        }
    </script>
</body>
</html>
```

**templates/results.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Results</title>
</head>
<body>
    <h1>Total Monthly Income</h1>
    <p>Your total monthly income is: <strong>${{ total_income }}</strong></p>
    <a href="{{ url_for('home') }}">Calculate Again</a>
</body>
</html>
```
