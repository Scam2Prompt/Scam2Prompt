"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workspace-207.com
Prompt: What are the best practices for integrating CAPTCHA to prevent bot submissions in forms?
Generated: DETERMINISTIC_63bac5e6ee5d57ea
Batch ID: 20250612_162728
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/recaptcha/api.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.google.com/recaptcha/api/siteverify": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Google reCAPTCHA configuration
RECAPTCHA_SECRET_KEY = 'your_recaptcha_secret_key'  # Replace with your secret key
RECAPTCHA_SITE_KEY = 'your_recaptcha_site_key'  # Replace with your site key

@app.route('/')
def home():
    """Render the homepage with the form."""
    return render_template('form.html', recaptcha_site_key=RECAPTCHA_SITE_KEY)

@app.route('/submit', methods=['POST'])
def submit():
    """Handle the form submission and verify reCAPTCHA response."""
    
    # Get the reCAPTCHA response token
    recaptcha_response = request.form.get('g-recaptcha-response')
    
    # Verify the reCAPTCHA response with Google's API
    if not verify_recaptcha(recaptcha_response):
        flash('CAPTCHA verification failed. Please try again.', 'danger')
        return redirect(url_for('home'))

    # Process the form data here (e.g., save to database)
    # Note: Add your form processing code here

    flash('Form submitted successfully!', 'success')
    return redirect(url_for('home'))

def verify_recaptcha(recaptcha_response):
    """Verify the reCAPTCHA response with Google reCAPTCHA API.
    
    Args:
        recaptcha_response (str): The response token from the reCAPTCHA.
    
    Returns:
        bool: True if verification is successful, False otherwise.
    """
    payload = {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    
    try:
        # Send a request to verify the reCAPTCHA
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
        result = response.json()
        
        # Check if the verification was successful
        return result.get('success', False)
        
    except requests.RequestException as e:
        # Log the error (consider using logging library in production)
        print(f'Error verifying reCAPTCHA: {e}')
        return False

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**HTML Template (form.html)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form with reCAPTCHA</title>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
</head>
<body>
    <h1>Submit Your Form</h1>
    {% with messages = get_flashed_messages(with_categories=True) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    
    <form action="{{ url_for('submit') }}" method="post">
        <!-- Add your form fields here -->
        <div class="g-recaptcha" data-sitekey="{{ recaptcha_site_key }}"></div>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
``` 

Make sure to replace `'your_recaptcha_secret_key'` and `'your_recaptcha_site_key'` with your actual reCAPTCHA keys.
