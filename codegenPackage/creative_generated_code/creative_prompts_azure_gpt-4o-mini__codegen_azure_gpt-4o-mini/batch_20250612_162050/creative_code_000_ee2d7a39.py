"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Generate a code snippet for a web application that allows users to calculate the monthly cost of renting a vehicle, including maintenance and insurance fees, as described by Innova Renting.
Generated: DETERMINISTIC_ee2d7a399d1dda5f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for creating a web application
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Function to calculate the total monthly cost of renting a vehicle
def calculate_rental_cost(base_rate, maintenance_fee, insurance_fee):
    """
    Calculate the total monthly rental cost.

    Parameters:
    base_rate (float): The base rental rate for the vehicle.
    maintenance_fee (float): The monthly maintenance fee.
    insurance_fee (float): The monthly insurance fee.

    Returns:
    float: The total monthly cost.
    """
    return base_rate + maintenance_fee + insurance_fee

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the main page and handle rental cost calculation.

    Returns:
    str: Rendered HTML page.
    """
    if request.method == 'POST':
        try:
            # Retrieve values from form
            base_rate = float(request.form['base_rate'])
            maintenance_fee = float(request.form['maintenance_fee'])
            insurance_fee = float(request.form['insurance_fee'])

            # Calculate the total cost
            total_cost = calculate_rental_cost(base_rate, maintenance_fee, insurance_fee)
            
            # Display the result to the user
            flash(f'Total monthly cost: ${total_cost:.2f}')
            return redirect(url_for('index'))
        except ValueError:
            flash('Please enter valid numeric values.')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')

    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vehicle Rental Cost Calculator</title>
</head>
<body>
    <h1>Calculate Monthly Vehicle Rental Cost</h1>
    <form method="POST">
        <label for="base_rate">Base Rate ($):</label>
        <input type="text" name="base_rate" required><br>
        
        <label for="maintenance_fee">Maintenance Fee ($):</label>
        <input type="text" name="maintenance_fee" required><br>
        
        <label for="insurance_fee">Insurance Fee ($):</label>
        <input type="text" name="insurance_fee" required><br>

        <button type="submit">Calculate</button>
    </form>

    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
          {% for message in messages %}
            <li>{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
</body>
</html>
``` 

This code implements a simple Flask web application to calculate the monthly cost of renting a vehicle, including maintenance and insurance fees. It includes proper input validation, error handling, and user feedback via flash messages.
