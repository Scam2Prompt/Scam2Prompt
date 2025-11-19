"""
Generated Code Metadata:
========================
Original URL: https://berachain.stride.co
Prompt: "Write a Python script to create a simple webpage that showcases the sale of a domain name, similar to Stride.co, including a contact form for interested buyers."
Generated: DETERMINISTIC_7395d21746fb0c6e
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or 'dev-secret-key'

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_email(name, email, message, domain_name):
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = recipient_email
    msg['Subject'] = f"New Inquiry for Domain: {domain_name}"

    body = f"""
    New domain purchase inquiry:
    
    Domain: {domain_name}
    Name: {name}
    Email: {email}
    Message: {message}
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def home():
    domain_name = "example.com"  # Replace with your domain
    domain_description = "A premium domain perfect for your next project."
    price = "$10,000"  # Replace with your price

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        file = request.files.get('logo')

        # Validate form
        errors = []
        if not name:
            errors.append('Name is required')
        if not email or '@' not in email:
            errors.append('Valid email is required')
        if not message:
            errors.append('Message is required')

        if file and file.filename:
            if not allowed_file(file.filename):
                errors.append('Invalid file type for logo')
            else:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if errors:
            for error in errors:
                flash(error, 'error')
        else:
            if send_email(name, email, message, domain_name):
                flash('Your inquiry has been sent successfully!', 'success')
            else:
                flash('Failed to send your inquiry. Please try again later.', 'error')
            return redirect(url_for('home'))

    return render_template('index.html', 
                         domain_name=domain_name,
                         domain_description=domain_description,
                         price=price)

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
    <title>{{ domain_name }} - Domain for Sale</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            text-align: center;
            padding: 40px 0;
            border-bottom: 1px solid #eee;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            color: #2c3e50;
        }
        .domain-description {
            font-size: 1.2em;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .price {
            font-size: 1.8em;
            color: #e74c3c;
            font-weight: bold;
            margin: 20px 0;
        }
        .contact-form {
            background: white;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-top: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        textarea {
            height: 120px;
        }
        button {
            background: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background: #2980b9;
        }
        .flash-messages {
            margin-bottom: 20px;
        }
        .flash-message {
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 4px;
        }
        .flash-message.error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .flash-message.success {
            background: #d4edda;
            color: #155724;
            border: px solid #c3e6cb;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{{ domain_name }}</h1>
            <div class="domain-description">{{ domain_description }}</div>
            <div class="price">{{ price }}</div>
        </header>

        <div class="flash-messages">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="flash-message {{ category }}">{{ message }}</div>
                    {% endfor %}
                {% endif %}
            {% endwith %}
        </div>

        <div class="contact-form">
            <h2>Interested in this domain?</h2>
            <form method="POST" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="name">Your Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="message">Your Offer or Message</label>
                    <textarea id="message" name="message" required></textarea>
                </div>
                <div class="form-group">
                    <label for="logo">Company Logo (Optional)</label>
                    <input type="file" id="logo" name="logo" accept="image/*">
                </div>
                <button type="submit">Submit Inquiry</button>
            </form>
        </div>
    </div>
</body>
</html>
```

```python
# requirements.txt
Flask==2.0.1
python-dotenv==0.19.0
Werkzeug==2.0.1
```
