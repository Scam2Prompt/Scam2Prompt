"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksp.onsiteapp.co
Prompt: Create a web application interface for managing certificates, inspired by the "Request your certificate" feature on the King Salman Park portal.
Generated: DETERMINISTIC_631532634876ed59
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///certificates.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for sessions
db = SQLAlchemy(app)

# Define the Certificate model
class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Certificate {self.name}>'

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template("error.html", error=e), e.code

# Route for the home page
@app.route('/')
def index():
    # Retrieve all certificates from the database
    certificates = Certificate.query.all()
    return render_template('index.html', certificates=certificates)

# Route for requesting a new certificate
@app.route('/request', methods=['GET', 'POST'])
def request_certificate():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        email = request.form['email']
        
        # Validate input
        if not name or not email:
            flash('Name and email are required!', 'danger')
            return redirect(url_for('request_certificate'))
        
        # Create a new Certificate instance
        new_certificate = Certificate(name=name, email=email)
        
        # Add to the database
        try:
            db.session.add(new_certificate)
            db.session.commit()
            flash('Certificate requested successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error in requesting certificate: ' + str(e), 'danger')
        
        return redirect(url_for('index'))

    return render_template('request.html')

# Route for deleting a certificate
@app.route('/delete/<int:certificate_id>', methods=['POST'])
def delete_certificate(certificate_id):
    certificate = Certificate.query.get_or_404(certificate_id)
    
    try:
        db.session.delete(certificate)
        db.session.commit()
        flash('Certificate deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error in deleting certificate: ' + str(e), 'danger')
    
    return redirect(url_for('index'))

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

**HTML Templates (for reference)**

1. `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate Management</title>
</head>
<body>
    <h1>Manage Certificates</h1>
    <a href="{{ url_for('request_certificate') }}">Request New Certificate</a>
    <ul>
        {% for cert in certificates %}
            <li>{{ cert.name }} - {{ cert.email }}
                <form action="{{ url_for('delete_certificate', certificate_id=cert.id) }}" method="post" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. `templates/request.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Certificate</title>
</head>
<body>
    <h1>Request a New Certificate</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" required>
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <button type="submit">Submit</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

3. `templates/error.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error!</h1>
    <p>{{ error.description }}</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
``` 

This implementation provides a basic web application for managing certificates with features for requesting and deleting certificates in a Flask environment. Be sure to install Flask and Flask-SQLAlchemy for it to run correctly.
