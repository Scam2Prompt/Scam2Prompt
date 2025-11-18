"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a simple web application using Flask that implements a "Thought Movie" visualization technique, allowing users to input their goals and generate a visual representation of their aspirations.
Generated: DETERMINISTIC_e0b93e952fd36fc9
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/images'

class GoalForm(FlaskForm):
    goal = StringField('Enter Your Goal', validators=[DataRequired()])
    submit = SubmitField('Generate Visualization')

def generate_visualization(goal):
    """Generate a simple pie chart visualization for the user goal."""
    labels = [goal, 'Other']
    sizes = [70, 30]
    explode = (0.1, 0)  # explode the 1st slice
    colors = ['gold', 'lightcoral']

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    
    # Save the figure to the specified folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'goal_visualization.png')
    plt.savefig(file_path)
    plt.close()  # Close the figure to prevent memory issues

    return file_path

@app.route('/', methods=['GET', 'POST'])
def index():
    form = GoalForm()
    if form.validate_on_submit():
        goal = form.goal.data
        try:
            image_path = generate_visualization(goal)
            flash('Visualization generated successfully!', 'success')
            return render_template('index.html', form=form, image_path=image_path)
        except Exception as e:
            flash(f'An error occurred while generating visualization: {str(e)}', 'danger')
    return render_template('index.html', form=form, image_path=None)

if __name__ == '__main__':
    # Create the upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```

**HTML Template (templates/index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thought Movie Visualization</title>
</head>
<body>
    <h1>Thought Movie Visualization</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.goal.label }}<br>
            {{ form.goal(size=40) }}<br>
            {% for message in get_flashed_messages(with_categories=true) %}
                <div class="alert alert-{{ message[0] }}">{{ message[1] }}</div>
            {% endfor %}
            {{ form.submit() }}
        </div>
    </form>
    {% if image_path %}
        <h2>Your Visualization:</h2>
        <img src="{{ image_path }}" alt="Goal Visualization">
    {% endif %}
</body>
</html>
```

**Requirements:**
You need to install Flask and Flask-WTF along with Matplotlib. You can do this via pip:

```bash
pip install Flask Flask-WTF matplotlib
```

**Run the application:**
Make sure to run this Flask application in an environment where you can access the web server. You may run the application using:

```bash
python your_flask_app.py
```

**Note:** Replace `your_flask_app.py` with the filename of your script.
