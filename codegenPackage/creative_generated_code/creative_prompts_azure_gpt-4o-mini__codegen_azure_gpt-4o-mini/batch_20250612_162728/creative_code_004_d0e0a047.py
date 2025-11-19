"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workspace-207.com
Prompt: How can I customize the CAPTCHA challenge to enhance user experience while ensuring security?
Generated: DETERMINISTIC_d0e0a0473b6d7f25
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
from flask import Flask, request, jsonify, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Custom CAPTCHA class to generate simple text-based CAPTCHA
class CustomCaptcha:
    def __init__(self, length=6):
        self.length = length
        self.captcha_text = self.generate_captcha()

    def generate_captcha(self):
        """Generate a random string of letters and digits for the CAPTCHA."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.length))

    def get_captcha(self):
        """Return the generated CAPTCHA."""
        return self.captcha_text

# Form for user input including CAPTCHA
class CaptchaForm(FlaskForm):
    captcha_input = StringField('Enter CAPTCHA:', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Route to display the form and CAPTCHA
@app.route('/captcha', methods=['GET', 'POST'])
def captcha():
    """Display CAPTCHA and handle user input."""
    form = CaptchaForm()
    captcha_instance = CustomCaptcha()
    
    if form.validate_on_submit():
        # Check if user input matches the generated CAPTCHA
        if form.captcha_input.data == captcha_instance.get_captcha():
            return jsonify({'message': 'CAPTCHA verified successfully!'}), 200
        else:
            return jsonify({'error': 'CAPTCHA verification failed. Please try again.'}), 400
    
    # Render the form with CAPTCHA
    return render_template('captcha.html', form=form, captcha=captcha_instance.get_captcha())

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (`captcha.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CAPTCHA Example</title>
</head>
<body>
    <h1>CAPTCHA Verification</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <label for="captcha_input">Enter CAPTCHA: {{ captcha }}</label>
        {{ form.captcha_input(size=32) }}<br>
        {{ form.submit() }}
    </form>
    {% if form.captcha_input.errors %}
        <ul>
            {% for error in form.captcha_input.errors %}
                <li>{{ error }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
```

Make sure to install Flask and Flask-WTF if you haven't already:

```bash
pip install Flask Flask-WTF
```
