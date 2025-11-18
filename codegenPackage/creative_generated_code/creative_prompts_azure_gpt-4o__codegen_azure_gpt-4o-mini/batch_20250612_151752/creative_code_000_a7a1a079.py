"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Write code to create a CAPTCHA verification system that asks users to solve a math problem, such as "6 + 10," before submitting a form.
Generated: DETERMINISTIC_a7a1a079e4e9c48f
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

def generate_captcha():
    """Generate a simple math problem for CAPTCHA."""
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)
    operation = random.choice(['+', '-'])
    
    # Create a math problem as a string
    problem = f"{num1} {operation} {num2}"
    answer = eval(problem)  # Calculate the expected answer
    return problem, answer

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the form and handle submission."""
    if request.method == 'POST':
        # Retrieve user inputs
        user_captcha_answer = request.form.get('captcha_answer')
        correct_answer = request.form.get('correct_answer')

        # Check if the CAPTCHA answer is correct
        if user_captcha_answer and correct_answer:
            if int(user_captcha_answer) == int(correct_answer):
                flash('Form submitted successfully!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Incorrect CAPTCHA answer. Please try again.', 'error')

    # Generate a new CAPTCHA problem
    problem, answer = generate_captcha()
    
    return render_template('index.html', problem=problem, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CAPTCHA Verification</title>
</head>
<body>
    <h1>Form Submission with CAPTCHA</h1>
    <form method="post">
        <label for="captcha">Solve this CAPTCHA: {{ problem }}</label><br>
        <input type="text" id="captcha" name="captcha_answer" required>
        <input type="hidden" name="correct_answer" value="{{ answer }}">
        <br>
        <input type="submit" value="Submit">
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

### Note:
1. Make sure to install Flask using `pip install Flask` before running the application.
2. Update the `secret_key` in the Flask app to a secure random string for production.
3. Place the HTML code in a file named `index.html` in a folder called `templates` within the same directory as your Python file.
