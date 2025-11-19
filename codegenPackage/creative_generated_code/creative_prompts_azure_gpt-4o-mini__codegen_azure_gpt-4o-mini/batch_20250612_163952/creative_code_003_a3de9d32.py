"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.seedify.cloud
Prompt: Generate a script that submits a verification form with a math challenge, similar to the one found on Seedify.cloud.
Generated: DETERMINISTIC_a3de9d320760830f
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, render_template, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Function to generate a simple math challenge
def generate_math_challenge():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    
    # Calculate the correct answer based on the operation
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:  # operation == '*'
        answer = num1 * num2

    challenge = f"What is {num1} {operation} {num2}?"
    return challenge, answer

@app.route('/')
def index():
    # Generate a math challenge for the user
    challenge, answer = generate_math_challenge()
    # Store the answer in session for verification later
    request.session['answer'] = answer
    return render_template('index.html', challenge=challenge)

@app.route('/submit', methods=['POST'])
def submit():
    user_answer = request.form.get('answer')
    correct_answer = request.session.get('answer')

    # Validate the user's answer
    if user_answer is None or not user_answer.isdigit():
        flash('Please provide a valid answer.', 'error')
        return redirect(url_for('index'))
    
    if int(user_answer) == correct_answer:
        flash('Verification successful!', 'success')
        return redirect(url_for('success'))
    else:
        flash('Incorrect answer. Please try again.', 'error')
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Templates Required:**

1. `index.html` (for the main form):
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Verification Form</title>
</head>
<body>
    <h1>Math Verification Challenge</h1>
    <form action="{{ url_for('submit') }}" method="post">
        <p>{{ challenge }}</p>
        <input type="text" name="answer" placeholder="Your answer" required>
        <button type="submit">Submit</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
        {% for category, message in messages %}
          <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
</body>
</html>
```

2. `success.html` (for the success message):
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Success</title>
</head>
<body>
    <h1>Success!</h1>
    <p>Your verification was successful.</p>
    <a href="{{ url_for('index') }}">Go back</a>
</body>
</html>
```

**Note:** Make sure to have Flask installed and configure session management correctly for the application. You may also want to set up a proper production environment for deployment.
