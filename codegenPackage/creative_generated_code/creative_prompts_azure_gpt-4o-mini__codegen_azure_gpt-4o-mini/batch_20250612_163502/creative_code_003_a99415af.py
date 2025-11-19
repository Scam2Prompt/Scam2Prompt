"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testing-ipfs.pages.dev
Prompt: How do I set up a verification process in a web application to ensure users are not bots when submitting forms?
Generated: DETERMINISTIC_a99415af8dab2b93
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a strong secret key

# Function to generate a simple CAPTCHA challenge
def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Form class for handling user submissions
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    captcha = StringField('CAPTCHA', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Store the CAPTCHA in-memory for demonstration purposes
captcha_storage = {}

@app.route('/form', methods=['GET', 'POST'])
def form_submission():
    form = UserForm()
    if request.method == 'POST':
        # Retrieve CAPTCHA from the storage
        stored_captcha = captcha_storage.get(request.remote_addr)

        if stored_captcha and form.validate_on_submit():
            # Check if the CAPTCHA is correct
            if form.captcha.data == stored_captcha:
                # Process the form data (e.g., save to database)
                return jsonify({"message": "Form submitted successfully!"}), 200
            else:
                return jsonify({"error": "Invalid CAPTCHA. Please try again."}), 400

        return jsonify({"error": "Invalid form submission."}), 400

    # Generate a new CAPTCHA and store it
    captcha_value = generate_captcha()
    captcha_storage[request.remote_addr] = captcha_value

    return f"""
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" name="username" required>
            <br>
            <label for="captcha">CAPTCHA (Enter: {captcha_value}):</label>
            <input type="text" name="captcha" required>
            <br>
            <input type="submit" value="Submit">
        </form>
    """

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found."}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
1. This code uses Flask and Flask-WTF for web forms. Make sure to install the required libraries using `pip install Flask Flask-WTF`.
2. The CAPTCHA generation is simplistic and should be replaced with a more robust solution (like Google reCAPTCHA) for production use.
3. In production, consider using a more secure method for storing and validating CAPTCHA (e.g., use server-side sessions or a database instead of in-memory storage).
