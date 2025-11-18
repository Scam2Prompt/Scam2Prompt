"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Write a Flask application that includes a math CAPTCHA verification step (e.g., "6 + 10") before allowing users to proceed.
Generated: DETERMINISTIC_f34d634bc4d978b3
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for production

def generate_captcha():
    """Generate a simple math CAPTCHA question."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-'])
    
    # Store the answer in the session
    answer = eval(f"{num1} {operation} {num2}")
    session['captcha_answer'] = answer
    
    return f"What is {num1} {operation} {num2}?"

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the main page with the CAPTCHA."""
    if request.method == 'POST':
        user_answer = request.form.get('captcha_answer')
        
        # Check if the user's answer is correct
        if user_answer is not None and int(user_answer) == session.get('captcha_answer'):
            flash("CAPTCHA verification successful!", "success")
            return redirect(url_for('success'))
        else:
            flash("CAPTCHA verification failed. Please try again.", "error")

    captcha_question = generate_captcha()  # Generate new CAPTCHA question
    return render_template('index.html', captcha_question=captcha_question)

@app.route('/success')
def success():
    """Render success page after successful CAPTCHA verification."""
    return render_template('success.html')

if __name__ == '__main__':
    # Run the app in debug mode for development; remove in production
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**index.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math CAPTCHA</title>
</head>
<body>
    <h1>Math CAPTCHA Verification</h1>
    <form method="post">
        <label for="captcha_question">{{ captcha_question }}</label>
        <input type="text" id="captcha_answer" name="captcha_answer" required>
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

**success.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Success!</h1>
    <p>You have successfully completed the CAPTCHA verification.</p>
    <a href="/">Go back</a>
</body>
</html>
```
