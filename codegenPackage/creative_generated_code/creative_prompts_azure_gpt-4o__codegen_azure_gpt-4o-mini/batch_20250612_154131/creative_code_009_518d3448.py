"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a web application to showcase services for automatic garage doors, including repair, installation, and compliance with European standards, similar to Trimatic Puertas Automáticas' offerings.
Generated: DETERMINISTIC_518d344853826c14
Batch ID: 20250612_154131
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a database model for services
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Service {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Define the route for the homepage
@app.route('/')
def home():
    services = Service.query.all()  # Fetch all services from the database
    return render_template('home.html', services=services)

# Define the route for adding a new service
@app.route('/add_service', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')

        # Error handling for empty fields
        if not name or not description or not price:
            flash('All fields are required!', 'danger')
            return redirect(url_for('add_service'))

        try:
            # Create a new service object
            new_service = Service(name=name, description=description, price=float(price))
            db.session.add(new_service)  # Add to session
            db.session.commit()  # Commit to the database
            flash('Service added successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error occurred: {str(e)}', 'danger')
            return redirect(url_for('add_service'))

    return render_template('add_service.html')

# Define the route for service details
@app.route('/service/<int:service_id>')
def service_detail(service_id):
    service = Service.query.get_or_404(service_id)  # Fetch service or 404
    return render_template('service_detail.html', service=service)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

1. **home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Garage Door Services</title>
</head>
<body>
    <h1>Our Services</h1>
    <a href="{{ url_for('add_service') }}">Add New Service</a>
    <ul>
        {% for service in services %}
            <li>
                <a href="{{ url_for('service_detail', service_id=service.id) }}">{{ service.name }}</a>: {{ service.price }}€
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **add_service.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Service</title>
</head>
<body>
    <h1>Add New Service</h1>
    <form method="POST">
        <label for="name">Service Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <label for="price">Price (€):</label>
        <input type="number" id="price" name="price" required step="0.01">
        <button type="submit">Submit</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

3. **service_detail.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ service.name }}</title>
</head>
<body>
    <h1>{{ service.name }}</h1>
    <p>{{ service.description }}</p>
    <p>Price: {{ service.price }}€</p>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Notes
- Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
- Replace `'your_secret_key'` with a secure key for production use.
- The SQLite database is used for simplicity; consider a more robust solution (like PostgreSQL) for production.
- You may want to implement user authentication, CSS, and JavaScript for a better user experience.
- Make sure to handle security concerns such as SQL injection, cross-site scripting (XSS), and use HTTPS for production.
