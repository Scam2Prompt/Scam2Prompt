"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.betterbooking.pk
Prompt: Write a code example for a web application that allows users to view and compare international tour packages from Better Booking.
Generated: DETERMINISTIC_5e72853fef5d4676
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (replace with your database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tour_packages.db'
db = SQLAlchemy(app)

# Define the TourPackage model
class TourPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<TourPackage {self.name}>'

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to render the home page with available tour packages
@app.route('/')
def index():
    try:
        packages = TourPackage.query.all()  # Retrieve all tour packages from the database
        return render_template('index.html', packages=packages)  # Render the index template with packages
    except Exception as e:
        # Handle any error that occurs during database access
        return jsonify({"error": str(e)}), 500

# Route to view the details of a selected tour package
@app.route('/package/<int:package_id>')
def package_detail(package_id):
    try:
        package = TourPackage.query.get_or_404(package_id)  # Retrieve the package by ID or return 404
        return render_template('package_detail.html', package=package)  # Render the detail template
    except Exception as e:
        # Handle any error that occurs during database access
        return jsonify({"error": str(e)}), 500

# Route to compare selected tour packages
@app.route('/compare', methods=['POST'])
def compare_packages():
    try:
        # Get the list of package IDs from the request
        package_ids = request.json.get('package_ids', [])
        packages = TourPackage.query.filter(TourPackage.id.in_(package_ids)).all()  # Query the selected packages
        return render_template('compare.html', packages=packages)  # Render the comparison template
    except Exception as e:
        # Handle any error that occurs during database access
        return jsonify({"error": str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
```

### HTML Templates (index.html and package_detail.html must be created in a 'templates' directory)

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tour Packages</title>
</head>
<body>
    <h1>Available Tour Packages</h1>
    <ul>
        {% for package in packages %}
        <li>
            <a href="{{ url_for('package_detail', package_id=package.id) }}">{{ package.name }}</a> - {{ package.destination }} - ${{ package.price }}
        </li>
        {% endfor %}
    </ul>
    <script>
        // JavaScript functionality to handle package comparison can be added here
    </script>
</body>
</html>
```

#### package_detail.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ package.name }}</title>
</head>
<body>
    <h1>{{ package.name }}</h1>
    <p><strong>Destination:</strong> {{ package.destination }}</p>
    <p><strong>Price:</strong> ${{ package.price }}</p>
    <p><strong>Duration:</strong> {{ package.duration }}</p>
    <p><strong>Description:</strong> {{ package.description }}</p>
    <a href="/">Back to Packages</a>
</body>
</html>
```

### Note:
Make sure to create the database and the `TourPackage` entries beforehand to test the application effectively.
