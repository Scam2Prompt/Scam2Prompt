"""
Generated Code Metadata:
========================
Original URL: https://fullteco.cl
Prompt: Generate code for a simple web calculator that estimates the cost of illumination for a residential project in the Los Lagos region.
Generated: DETERMINISTIC_8dda7d9129317c4b
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

class IlluminationCostForm(FlaskForm):
    """Form for calculating illumination cost."""
    wattage = FloatField('Wattage (in Watts)', validators=[DataRequired()])
    hours_per_day = FloatField('Hours of Use per Day', validators=[DataRequired()])
    days_per_month = FloatField('Days of Use per Month', validators=[DataRequired()])
    cost_per_kwh = FloatField('Cost per kWh (in currency)', validators=[DataRequired()])
    submit = SubmitField('Calculate Cost')

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the main page and handle form submission."""
    form = IlluminationCostForm()
    total_cost = None

    if form.validate_on_submit():
        try:
            # Retrieve form data
            wattage = form.wattage.data
            hours_per_day = form.hours_per_day.data
            days_per_month = form.days_per_month.data
            cost_per_kwh = form.cost_per_kwh.data
            
            # Calculate the total cost of illumination
            monthly_kwh = (wattage / 1000) * hours_per_day * days_per_month
            total_cost = monthly_kwh * cost_per_kwh
            
        except Exception as e:
            # Handle any unexpected errors
            total_cost = f"Error calculating cost: {str(e)}"

    return render_template('index.html', form=form, total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Illumination Cost Calculator</title>
</head>
<body>
    <h1>Illumination Cost Calculator</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.wattage.label }} {{ form.wattage() }}
        </div>
        <div>
            {{ form.hours_per_day.label }} {{ form.hours_per_day() }}
        </div>
        <div>
            {{ form.days_per_month.label }} {{ form.days_per_month() }}
        </div>
        <div>
            {{ form.cost_per_kwh.label }} {{ form.cost_per_kwh() }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    {% if total_cost is not none %}
        <h2>Total Monthly Cost: {{ total_cost }}</h2>
    {% endif %}
</body>
</html>
```

**Requirements:**
- Install Flask and Flask-WTF:
```bash
pip install Flask Flask-WTF
```

**Run the Application:**
- Save the Python code in a file (e.g., `app.py`) and the HTML code in a folder named `templates` as `index.html`.
- Run the application using:
```bash
python app.py
```
