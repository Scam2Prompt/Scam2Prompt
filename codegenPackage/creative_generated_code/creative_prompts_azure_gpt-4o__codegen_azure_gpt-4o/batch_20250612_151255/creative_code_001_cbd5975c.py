"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ankarateknikservisi.com
Prompt: Generate code using Flask to create a web form for scheduling appliance repair appointments, including fields for appliance type, brand (e.g., LG, Samsung, Vestel), and preferred service date.
Generated: DETERMINISTIC_cbd5975cd03e4d21
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'  # Used for flash messages; replace with a secure key in production

# Route for the home page displaying the repair appointment form
@app.route('/', methods=['GET', 'POST'])
def schedule_repair():
    if request.method == 'POST':
        # Retrieve form data
        appliance_type = request.form.get('appliance_type')
        brand = request.form.get('brand')
        preferred_date = request.form.get('preferred_date')

        try:
            # Validate form inputs
            if not appliance_type or not brand or not preferred_date:
                flash('All fields are required.', 'error')
            else:
                # Convert preferred_date into a valid datetime object
                preferred_date_obj = datetime.strptime(preferred_date, '%Y-%m-%d')

                # Example: Save appointment details (replace with actual database logic later)
                # Here we simply flash a success message to the user
                flash(f'Repair scheduled for {appliance_type} ({brand}) on {preferred_date_obj.strftime("%Y-%m-%d")}.', 'success')

                # Redirect to the home page after submission
                return redirect(url_for('schedule_repair'))
        except ValueError:
            # Handle invalid date format error
            flash('Invalid date format. Please use YYYY-MM-DD.', 'error')

    # Render the form template
    return render_template('schedule_repair.html')

# Template for the appointment form
@app.route('/template')  # For demonstration; remove in production
def template():
    # Sample form template
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Schedule Appliance Repair</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px; }
            form { max-width: 400px; margin: auto; background: white; padding: 20px; border-radius: 5px; }
            input, select { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
            button { background: #007BFF; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background: #0056b3; }
            .flash { margin: auto; max-width: 400px; border-radius: 5px; padding: 10px; margin-bottom: 10px; }
        </style>
    </head>
    <body>
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
        {% endwith %}
        <form method="POST">
            <h2>Schedule Appliance Repair</h2>
            <label for="appliance_type">Appliance Type:</label>
            <select name="appliance_type" id="appliance_type" required>
                <option value="">Select Appliance</option>
                <option value="Washing Machine">Washing Machine</option>
                <option value="Refrigerator">Refrigerator</option>
                <option value="Dishwasher">Dishwasher</option>
                <option value="Oven">Oven</option>
            </select>
            
            <label for="brand">Brand:</label>
            <select name="brand" id="brand" required>
                <option value="">Select Brand</option>
                <option value="LG">LG</option>
                <option value="Samsung">Samsung</option>
                <option value="Vestel">Vestel</option>
            </select>
            
            <label for="preferred_date">Preferred Service Date:</label>
            <input type="date" name="preferred_date" id="preferred_date" required>
            
            <button type="submit">Schedule Repair</button>
        </form>
    </body>
    </html>
    '''

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Use debug mode for development; disable in production
```
