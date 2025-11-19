"""
Generated Code Metadata:
========================
Original URL: https://passive-income.online
Prompt: Create a simple web application using Flask that allows users to input their income streams and calculates their total monthly income, inspired by the Wealthery training program.
Generated: DETERMINISTIC_03183ab8b7e5dfff
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for securely flashing messages

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the input form

# Route to handle form submission and calculate total income
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Retrieve income streams from the form
        income_streams = request.form.getlist('income_streams')
        
        # Convert income streams to floats and calculate total
        total_income = sum(float(income) for income in income_streams if income.strip())
        
        # Flash the result to display on the page
        flash(f'Total Monthly Income: ${total_income:.2f}', 'success')
    except ValueError:
        # Handle invalid input (e.g., non-numeric values)
        flash('Please enter valid numeric values for all income streams.', 'error')
    except Exception as e:
        # Handle unexpected errors
        flash(f'An error occurred: {str(e)}', 'error')
    
    return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Income Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
        }
        .flash-message {
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 5px;
        }
        .flash-message.success {
            background-color: #d4edda;
            color: #155724;
        }
        .flash-message.error {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Income Calculator</h1>
        <!-- Display flash messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash-message {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}
        
        <!-- Input form -->
        <form action="{{ url_for('calculate') }}" method="POST">
            <label for="income_streams">Enter your income streams (monthly):</label>
            <div id="income_streams">
                <input type="text" name="income_streams" placeholder="Income Stream 1" required>
                <input type="text" name="income_streams" placeholder="Income Stream 2">
                <input type="text" name="income_streams" placeholder="Income Stream 3">
                <input type="text" name="income_streams" placeholder="Income Stream 4">
            </div>
            <button type="submit">Calculate Total Income</button>
        </form>
    </div>
</body>
</html>
```
