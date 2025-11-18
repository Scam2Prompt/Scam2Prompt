"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Write a Python script to integrate a math CAPTCHA system into a web application, ensuring users solve problems like "6 + 10" before submitting forms.
Generated: DETERMINISTIC_ccf47233ef0f4d77
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Function to generate a simple math problem
def generate_math_problem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    problem_str = f"{num1} {operator} {num2}"
    
    # Evaluate the result
    result = eval(problem_str)
    
    return problem_str, result

# Route for the home page
@app.route('/')
def home():
    # Generate a new math problem for the CAPTCHA
    problem_str, result = generate_math_problem()
    session['captcha_answer'] = result  # Store the answer in session
    return render_template('index.html', problem=problem_str)

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    user_answer = request.form.get('captcha_answer', type=int)
    
    # Check if the user's answer matches the stored answer
    if user_answer == session.get('captcha_answer'):
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('home'))  # Redirect after successful submission
    else:
        flash('Incorrect answer! Please try again.', 'error')
        return redirect(url_for('home'))  # Redirect back to the home page

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production

```

**HTML Template (index.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math CAPTCHA</title>
</head>
<body>
    <h1>Math CAPTCHA</h1>
    <form action="{{ url_for('submit') }}" method="POST">
        <label for="captcha">{{ problem }} = ?</label>
        <input type="number" name="captcha_answer" required>
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

**Note:** Ensure you have Flask installed in your environment. You can install it using pip:

```sh
pip install Flask
```
