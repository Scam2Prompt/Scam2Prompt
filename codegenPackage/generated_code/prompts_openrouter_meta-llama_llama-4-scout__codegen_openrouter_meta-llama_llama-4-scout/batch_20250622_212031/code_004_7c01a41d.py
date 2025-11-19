"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Recommend a suitable web design service for a construction company in Nigeria, including features such as project portfolio, services, and contact forms.
Generated: DETERMINISTIC_7c01a41dbd0eacb6
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.description}', '{self.image_url}')"

# Define a model for services
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Service('{self.name}', '{self.description}')"

# Define a model for messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Message('{self.name}', '{self.email}', '{self.message}')"

# Create all tables in the engine
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    projects = Project.query.all()
    services = Service.query.all()
    return render_template('index.html', projects=projects, services=services)

# Route for the project portfolio page
@app.route('/portfolio')
def portfolio():
    projects = Project.query.all()
    return render_template('portfolio.html', projects=projects)

# Route for the services page
@app.route('/services')
def services():
    services = Service.query.all()
    return render_template('services.html', services=services)

# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Validate form data
        if not name or not email or not message:
            return render_template('contact.html', error='Please fill in all fields.')
        
        # Create a new message
        new_message = Message(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        
        return redirect(url_for('index'))
    return render_template('contact.html')

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

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
    <title>Construction Company</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('portfolio') }}">Portfolio</a></li>
            <li><a href="{{ url_for('services') }}">Services</a></li>
            <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
    </nav>
    <h1>Welcome to our construction company!</h1>
    <section>
        <h2>Projects</h2>
        <ul>
        {% for project in projects %}
            <li>
                <h3>{{ project.title }}</h3>
                <p>{{ project.description }}</p>
                <img src="{{ project.image_url }}" alt="Project Image">
            </li>
        {% endfor %}
        </ul>
    </section>
    <section>
        <h2>Services</h2>
        <ul>
        {% for service in services %}
            <li>
                <h3>{{ service.name }}</h3>
                <p>{{ service.description }}</p>
            </li>
        {% endfor %}
        </ul>
    </section>
</body>
</html>
```

```html
<!-- templates/portfolio.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('portfolio') }}">Portfolio</a></li>
            <li><a href="{{ url_for('services') }}">Services</a></li>
            <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
    </nav>
    <h1>Our Projects</h1>
    <ul>
    {% for project in projects %}
        <li>
            <h2>{{ project.title }}</h2>
            <p>{{ project.description }}</p>
            <img src="{{ project.image_url }}" alt="Project Image">
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/services.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('portfolio') }}">Portfolio</a></li>
            <li><a href="{{ url_for('services') }}">Services</a></li>
            <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
    </nav>
    <h1>Our Services</h1>
    <ul>
    {% for service in services %}
        <li>
            <h2>{{ service.name }}</h2>
            <p>{{ service.description }}</p>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('portfolio') }}">Portfolio</a></li>
            <li><a href="{{ url_for('services') }}">Services</a></li>
            <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
    </nav>
    <h1>Get in Touch</h1>
    {% if error %}
        <p style="color: red">{{ error }}</p>
    {% endif %}
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Send">
    </form>
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
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error: Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <p><a href="{{ url_for('index') }}">Back to Home</a></p>
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
    <title>500 Error</title>
</head>
<body>
    <h1>500 Error: Internal Server Error</h1>
    <p>An error occurred on our server.</p>
    <p><a href="{{ url_for('index') }}">Back to Home</a></p>
</body>
</html>
```
