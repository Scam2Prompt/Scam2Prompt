"""
Generated Code Metadata:
========================
Original URL: https://seedify.cloud
Prompt: Write a Flask application that includes a math CAPTCHA verification step (e.g., "6 + 10") before allowing users to proceed.
Generated: DETERMINISTIC_f34d634bc4d978b3
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

def generate_captcha():
    """Generate a simple math CAPTCHA question and answer."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operator} {num2}"
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return question, str(answer)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_answer = request.form.get('captcha_answer', '').strip()
        correct_answer = session.get('captcha_answer')
        
        if not user_answer:
            error = "Please answer the CAPTCHA"
        elif user_answer != correct_answer:
            error = "Incorrect answer. Please try again."
        else:
            session['captcha_verified'] = True
            return redirect(url_for('verified'))
        
        return render_template('index.html', 
                            captcha_question=session.get('captcha_question'),
                            error=error)
    
    # Generate new CAPTCHA for GET request
    question, answer = generate_captcha()
    session['captcha_question'] = question
    session['captcha_answer'] = answer
    session['captcha_verified'] = False
    
    return render_template('index.html', captcha_question=question)

@app.route('/verified')
def verified():
    if not session.get('captcha_verified'):
        return redirect(url_for('index'))
    return render_template('verified.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Math CAPTCHA Verification</title>
</head>
<body>
    <h1>Math CAPTCHA Verification</h1>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="POST">
        <p>Please solve the following: {{ captcha_question }} = ?</p>
        <input type="text" name="captcha_answer" required>
        <button type="submit">Verify</button>
    </form>
</body>
</html>
```

```html
<!-- templates/verified.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Verified</title>
</head>
<body>
    <h1>Verification Successful!</h1>
    <p>You have successfully solved the CAPTCHA.</p>
    <a href="{{ url_for('index') }}">Try again</a>
</body>
</html>
```
