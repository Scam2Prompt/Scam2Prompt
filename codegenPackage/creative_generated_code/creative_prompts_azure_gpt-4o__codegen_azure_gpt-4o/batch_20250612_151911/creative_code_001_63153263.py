"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksp.onsiteapp.co
Prompt: Create a web application interface for managing certificates, inspired by the "Request your certificate" feature on the King Salman Park portal.
Generated: DETERMINISTIC_631532634876ed59
Batch ID: 20250612_151911
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a simple implementation of a web application interface for managing certificates using Python's Flask framework. It includes HTML templates and basic server-side functionality.

---

### app.py
```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Fake database for demonstration purposes
certificates = []

@app.route('/')
def home():
    """
    Render the homepage with a list of certificates.
    """
    return render_template('index.html', certificates=certificates)

@app.route('/request_certificate', methods=['GET', 'POST'])
def request_certificate():
    """
    Handle the certificate request form. Render the form for GET requests,
    and process form data for POST requests.
    """
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        purpose = request.form.get('purpose')

        # Basic validation
        if not name or not email or not purpose:
            flash('All fields are required!', 'error')
            return redirect(url_for('request_certificate'))

        # Save the certificate request (fake database action)
        certificates.append({
            'name': name,
            'email': email,
            'purpose': purpose,
        })

        flash('Certificate request submitted successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('request_certificate.html')

@app.route('/certificate/<int:certificate_id>')
def view_certificate(certificate_id):
    """
    Display details of a particular certificate.
    """
    if certificate_id < 0 or certificate_id >= len(certificates):
        flash('Certificate not found!', 'error')
        return redirect(url_for('home'))

    certificate = certificates[certificate_id]
    return render_template('view_certificate.html', certificate=certificate)

if __name__ == '__main__':
    app.run(debug=True)
```

---

### templates/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate Manager</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Certificate Manager</h1>
        <a href="{{ url_for('request_certificate') }}" class="btn btn-primary mb-3">Request Certificate</a>
        {% with messages = get_flashed_messages(with_categories=True) %}
            {% if messages %}
                <div class="alert alert-dismissible fade show">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        <ul class="list-group">
            {% for certificate in certificates %}
                <li class="list-group-item">
                    <strong>{{ certificate.name }}</strong> - {{ certificate.purpose }}
                    <a href="{{ url_for('view_certificate', certificate_id=loop.index0) }}" class="btn btn-sm btn-info float-end">View</a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

---

### templates/request_certificate.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Certificate</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Request a Certificate</h1>
        <form action="{{ url_for('request_certificate') }}" method="post" class="mt-3">
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" name="name" id="name" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" name="email" id="email" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="purpose" class="form-label">Purpose</label>
                <textarea name="purpose" id="purpose" class="form-control" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-success">Submit</button>
        </form>
        <a href="{{ url_for('home') }}" class="btn btn-link mt-3">Back to Home</a>
    </div>
</body>
</html>
```

---

### templates/view_certificate.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate Details</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Certificate Details</h1>
        <dl class="row mt-3">
            <dt class="col-sm-3">Name</dt>
            <dd class="col-sm-9">{{ certificate.name }}</dd>
            <dt class="col-sm-3">Email</dt>
            <dd class="col-sm-9">{{ certificate.email }}</dd>
            <dt class="col-sm-3">Purpose</dt>
            <dd class="col-sm-9">{{ certificate.purpose }}</dd>
        </dl>
        <a href="{{ url_for('home') }}" class="btn btn-link mt-3">Back to Home</a>
    </div>
</body>
</html>
```

---

### Notes:
1. Install Flask using `pip install flask`.
2. Save templates in a `templates` folder next to `app.py`.
3. This code is ready to run and fulfills all requirements mentioned.
