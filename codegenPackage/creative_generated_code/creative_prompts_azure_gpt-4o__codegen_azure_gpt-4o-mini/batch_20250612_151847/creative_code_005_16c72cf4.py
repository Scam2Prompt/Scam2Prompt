"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Develop a Python script using Flask to handle inquiries submitted via the "Kontak Kami" form on Sekolah Quran Indonesia's website, including email notifications to adminsqi@gmail.com.
Generated: DETERMINISTIC_16c72cf44e59528c
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')  # Set your email user
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')  # Set your email password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_USER')

# Initialize the Mail extension
mail = Mail(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/kontak', methods=['POST'])
def kontak():
    """
    Handle inquiries submitted via the 'Kontak Kami' form.
    Expects a JSON payload with 'name', 'email', and 'message'.

    Returns:
        JSON response with status and message.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input
        if not data or not all(key in data for key in ('name', 'email', 'message')):
            return jsonify({'status': 'error', 'message': 'Invalid input'}), 400
        
        name = data['name']
        email = data['email']
        message = data['message']

        # Log the inquiry
        logging.info(f"Received inquiry from {name} ({email}): {message}")

        # Create and send the email
        msg = Message(subject='New Inquiry from Kontak Kami',
                      recipients=['adminqi@gmail.com'],
                      body=f'Name: {name}\nEmail: {email}\nMessage:\n{message}')
        mail.send(msg)

        return jsonify({'status': 'success', 'message': 'Inquiry submitted successfully'}), 200
    
    except Exception as e:
        logging.error(f"Error processing inquiry: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

Make sure to set the environment variables `EMAIL_USER` and `EMAIL_PASS` with the appropriate values before running the application.
