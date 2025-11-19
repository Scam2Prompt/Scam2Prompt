"""
Generated Code Metadata:
========================
Original URL: https://legend-of-jimmy.nfts2.me
Prompt: How can I implement a contact form for users to report errors related to NFT collections, inspired by the contact options provided on NFTs 2 Me?
Generated: DETERMINISTIC_f8bdfd85a7a24765
Batch ID: 20250612_155737
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key')

# Configuration for email
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')

# Contact Form Class
class NFTErrorReportForm(FlaskForm):
    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=2, max=50)
    ])
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Email()
    ])
    collection_name = StringField('NFT Collection Name', [
        validators.DataRequired(),
        validators.Length(min=2, max=100)
    ])
    collection_address = StringField('NFT Collection Address (Optional)', [
        validators.Optional(),
        validators.Length(min=42, max=42)
    ])
    issue_type = StringField('Issue Type', [
        validators.DataRequired(),
        validators.Length(min=2, max=50)
    ])
    description = TextAreaField('Description', [
        validators.DataRequired(),
        validators.Length(min=10, max=1000)
    ])

# Route for contact form
@app.route('/report-error', methods=['GET', 'POST'])
def report_error():
    form = NFTErrorReportForm()
    
    if form.validate_on_submit():
        try:
            # Prepare email message
            msg = MIMEMultipart()
            msg['From'] = SMTP_USERNAME
            msg['To'] = ADMIN_EMAIL
            msg['Subject'] = f"NFT Error Report: {form.issue_type.data} - {form.collection_name.data}"
            
            body = f"""
            New NFT Error Report:
            
            Name: {form.name.data}
            Email: {form.email.data}
            Collection Name: {form.collection_name.data}
            Collection Address: {form.collection_address.data or 'Not provided'}
            Issue Type: {form.issue_type.data}
            
            Description:
            {form.description.data}
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.send_message(msg)
            
            flash('Your error report has been submitted successfully!', 'success')
            return redirect(url_for('report_error'))
        
        except Exception as e:
            app.logger.error(f"Error sending email: {str(e)}")
            flash('An error occurred while submitting your report. Please try again later.', 'danger')
    
    return render_template('report_error.html', form=form)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

```html
<!-- templates/report_error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report NFT Error</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <h2 class="mb-4">Report NFT Collection Error</h2>
                
                {% with messages = get_flashed_messages(with_categories=true) %}
                    {% if messages %}
                        {% for category, message in messages %}
                            <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                                {{ message }}
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                            </div>
                        {% endfor %}
                    {% endif %}
                {% endwith %}
                
                <form method="POST" action="{{ url_for('report_error') }}">
                    {{ form.hidden_tag() }}
                    
                    <div class="mb-3">
                        {{ form.name.label(class="form-label") }}
                        {{ form.name(class="form-control") }}
                        {% if form.name.errors %}
                            <div class="text-danger">
                                {% for error in form.name.errors %}
                                    <small>{{ error }}</small>
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        {{ form.email.label(class="form-label") }}
                        {{ form.email(class="form-control") }}
                        {% if form.email.errors %}
                            <div class="text-danger">
                                {% for error in form.email.errors %}
                                    <small>{{ error }}</small>
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        {{ form.collection_name.label(class="form-label") }}
                        {{ form.collection_name(class="form-control") }}
                        {% if form.collection_name.errors %}
                            <div class="text-danger">
                                {% for error in form.collection_name.errors %}
                                    <small>{{ error }}</small>
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        {{ form.collection_address.label(class="form-label") }}
                        {{ form.collection_address(class="form-control", placeholder="0x...") }}
                        {% if form.collection_address.errors %}
                            <div class="text-danger">
                                {% for error in form.collection_address.errors %}
                                    <small>{{ error }}</small>
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        {{ form.issue_type.label(class="form-label") }}
                        {{ form.issue_type(class="form-control") }}
                        {% if form.issue_type.errors %}
                            <div class="text-danger">
                                {% for error in form.issue_type.errors %}
                                    <small>{{ error }}</small>
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        {{ form.description.label(class="form-label") }}
                        {{ form.description(class="form-control", rows=5) }}
                        {% if form.description.errors %}
                            <div class="text-danger">
                                {% for error in form.description.errors %}
                                    <small>{{ error }}</small>
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                    
                    <button type="submit" class="btn btn-primary">Submit Report</button>
                </form>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8 text-center">
                <h1 class="display-4">404 - Page Not Found</h1>
                <p class="lead">The page you're looking for doesn't exist.</p>
                <a href="{{ url_for('report_error') }}" class="btn btn-primary">Go to Error Report Form</a>
            </div>
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Error</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
