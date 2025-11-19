"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Generate a code snippet for a registration form that allows users to sign up for basketball leagues at Courtside Fitness, incorporating fields for name, email, skill level, and preferred league.
Generated: DETERMINISTIC_361b6d13918c8406
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for a registration form for basketball leagues at Courtside Fitness

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

# Available skill levels and leagues
SKILL_LEVELS = ["Beginner", "Intermediate", "Advanced"]
LEAGUES = ["Morning League", "Afternoon League", "Evening League"]

@app.route('/')
def home():
    """
    Render the registration form page.
    """
    return render_template('register.html', skill_levels=SKILL_LEVELS, leagues=LEAGUES)

@app.route('/register', methods=['POST'])
def register():
    """
    Handle form submission for user registration.
    """
    try:
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        skill_level = request.form.get('skill_level')
        preferred_league = request.form.get('preferred_league')

        # Validation
        if not name or not email or not skill_level or not preferred_league:
            flash("All fields are required.", "error")
            return redirect(url_for('home'))
        
        if skill_level not in SKILL_LEVELS:
            flash("Invalid skill level selected.", "error")
            return redirect(url_for('home'))
        
        if preferred_league not in LEAGUES:
            flash("Invalid league selected.", "error")
            return redirect(url_for('home'))

        # (Simulated) Save registration details to database
        # Here you would insert code to save to a database or file
        # For now, we simulate success
        flash(f"Successfully registered {name} for the {preferred_league}.", "success")
        return redirect(url_for('home'))
    
    except HTTPException as e:
        # Handle HTTP exceptions (e.g., invalid requests)
        flash("An error occurred while processing your registration. Please try again.", "error")
        return redirect(url_for('home'))

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### HTML Template (register.html)
Save this as `templates/register.html` in the same directory as your Python app.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basketball League Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, select {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .flash-message {
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 4px;
        }
        .flash-message.error {
            background-color: #f44336;
            color: white;
        }
        .flash-message.success {
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Basketball League Registration</h1>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash-message {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    <form action="{{ url_for('register') }}" method="POST">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="skill_level">Skill Level:</label>
            <select id="skill_level" name="skill_level" required>
                <option value="">-- Select Skill Level --</option>
                {% for level in skill_levels %}
                    <option value="{{ level }}">{{ level }}</option>
                {% endfor %}
            </select>
        </div>
        <div class="form-group">
            <label for="preferred_league">Preferred League:</label>
            <select id="preferred_league" name="preferred_league" required>
                <option value="">-- Select League --</option>
                {% for league in leagues %}
                    <option value="{{ league }}">{{ league }}</option>
                {% endfor %}
            </select>
        </div>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```
