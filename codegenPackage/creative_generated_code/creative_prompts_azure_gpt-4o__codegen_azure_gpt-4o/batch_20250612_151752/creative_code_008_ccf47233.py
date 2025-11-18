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
from flask import Flask, request, render_template_string, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure this is set for session management

# Generate a random math problem
def generate_captcha():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-'])
    question = f"{num1} {operation} {num2}"
    
    # Compute the correct answer
    if operation == '+':
        answer = num1 + num2
    else:
        answer = num1 - num2
    
    return question, answer

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve user input and correct answer from session
        user_answer = request.form.get('captcha_answer')
        correct_answer = session.get('captcha_answer')

        try:
            if not user_answer:
                raise ValueError("CAPTCHA answer is required.")

            # Compare user's answer with the correct answer
            if int(user_answer) == correct_answer:
                return redirect(url_for('success'))
            else:
                return render_template_string(template, error="Incorrect CAPTCHA, please try again.")
        except ValueError as e:
            # Handle invalid input or missing data
            return render_template_string(template, error=str(e))

    # Generate a new CAPTCHA for each GET request
    question, answer = generate_captcha()
    session['captcha_question'] = question
    session['captcha_answer'] = answer  # Store the correct answer in the session

    return render_template_string(template)

@app.route('/success')
def success():
    return "Form submitted successfully!"

# Template for rendering the form
template = """
<!doctype html>
<html lang="en">
<head>
    <title>CAPTCHA Example</title>
</head>
<body>
    <h1>CAPTCHA Form</h1>
    <form method="post">
        <div>
            <label>CAPTCHA: Solve {{ session['captcha_question'] }}</label><br>
            <input type="text" name="captcha_answer" required>
        </div>
        {% if error %}
        <p style="color: red;">{{ error }}</p>
        {% endif %}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
```
