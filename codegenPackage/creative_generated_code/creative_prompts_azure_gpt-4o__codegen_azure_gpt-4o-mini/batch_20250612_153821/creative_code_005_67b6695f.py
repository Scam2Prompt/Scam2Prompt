"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mhfgy-722.com
Prompt: Provide an example of how to implement a CAPTCHA system in Flask, including the generation and validation of Request IDs.
Generated: DETERMINISTIC_67b6695fb1f65a5d
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Function to generate a random CAPTCHA string
def generate_captcha(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Flask-WTF form for CAPTCHA input
class CaptchaForm(FlaskForm):
    captcha_input = StringField('Enter CAPTCHA:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/captcha', methods=['GET', 'POST'])
def captcha():
    """
    Route to display CAPTCHA and handle form submission.
    Generates a CAPTCHA and saves it in the session for validation.
    """
    form = CaptchaForm()

    # Generate a new CAPTCHA if it's a GET request
    if request.method == 'GET':
        session['captcha'] = generate_captcha()
    
    if form.validate_on_submit():
        # Validate the submitted CAPTCHA input against the stored session CAPTCHA
        if form.captcha_input.data == session.get('captcha'):
            return jsonify({'message': 'CAPTCHA validation successful!'}), 200
        else:
            return jsonify({'message': 'CAPTCHA validation failed!'}), 400

    # Render the CAPTCHA and form on the page
    return render_template('captcha.html', captcha=session.get('captcha'), form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/captcha.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CAPTCHA Example</title>
</head>
<body>
    <h1>Please complete the CAPTCHA</h1>
    <form method="POST">
        <div>
            <label>{{ captcha }}</label>
            <input type="text" name="captcha_input" required>
        </div>
        {{ form.submit() }}
    </form>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-WTF installed in your environment. You can do this with `pip install Flask Flask-WTF`.
- Replace `'your_secret_key'` with a strong, unpredictable secret key.
- The HTML template is basic and should be styled according to your application's design standards.
