"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legend-of-jimmy.nfts2.me
Prompt: How can I implement a contact form for users to report errors related to NFT collections, inspired by the contact options provided on NFTs 2 Me?
Generated: DETERMINISTIC_f8bdfd85a7a24765
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
import re
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)

# Configure email settings
SMTP_SERVER = 'smtp.your-email-provider.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'
ADMIN_EMAIL = 'admin@example.com'

# Validate email function
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/')
def index():
    # Render contact form template (HTML file must exist in 'templates' folder)
    return render_template('contact_form.html')

@app.route('/submit_error_report', methods=['POST'])
def submit_error_report():
    try:
        # Extract form fields
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        nft_collection = request.form.get('nft_collection', '').strip()
        error_details = request.form.get('error_details', '').strip()

        # Validate required fields
        if not name or not email or not nft_collection or not error_details:
            return jsonify({'error': 'All fields are required.'}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format.'}), 400

        # Create email content
        email_subject = f'Error Report: {nft_collection}'
        email_body = f"""
        A user has reported an issue with an NFT collection.

        Name: {name}
        Email: {email}
        NFT Collection: {nft_collection}
        Error Details: {error_details}
        """

        # Send email to admin
        msg = MIMEText(email_body)
        msg['Subject'] = email_subject
        msg['From'] = EMAIL_USERNAME
        msg['To'] = ADMIN_EMAIL

        # SMTP connection and email sending
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, ADMIN_EMAIL, msg.as_string())

        # Return success response
        return jsonify({'message': 'Error report submitted successfully.'}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred while submitting the report.'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

HTML (`templates/contact_form.html`):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error Report Form</title>
</head>
<body>
    <h1>Report an Issue with NFT Collection</h1>
    <form action="/submit_error_report" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="nft_collection">NFT Collection:</label>
        <input type="text" id="nft_collection" name="nft_collection" required><br><br>
        
        <label for="error_details">Error Details:</label><br>
        <textarea id="error_details" name="error_details" rows="5" required></textarea><br><br>
        
        <button type="submit">Submit Report</button>
    </form>
</body>
</html>
```
