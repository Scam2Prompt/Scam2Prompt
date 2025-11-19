"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://semillasplantae.com
Prompt: Design a small web application using Flask that allows users to browse and filter the unique seed varieties offered by Semillas Plantae, focusing on their organic and local products.
Generated: DETERMINISTIC_0922d63fe6cdb627
Batch ID: 20250612_140024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`": {
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
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seeds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Seed model for the database
class Seed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variety = db.Column(db.String(100), nullable=False)
    organic = db.Column(db.Boolean, default=False)
    local = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Seed {self.variety}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def home():
    # Get filter criteria from request arguments
    organic = request.args.get('organic', 'false').lower() == 'true'
    local = request.args.get('local', 'false').lower() == 'true'

    # Query the database for seeds based on filter criteria
    query = Seed.query
    if organic:
        query = query.filter_by(organic=True)
    if local:
        query = query.filter_by(local=True)

    seeds = query.all()  # Get all matching seeds
    return render_template('home.html', seeds=seeds)

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Error handling for other server errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seed Varieties</title>
</head>
<body>
    <h1>Available Seed Varieties</h1>
    
    <form method="get">
        <label for="organic">Organic:</label>
        <input type="checkbox" name="organic" id="organic" value="true">
        
        <label for="local">Local:</label>
        <input type="checkbox" name="local" id="local" value="true">
        
        <button type="submit">Filter</button>
    </form>

    <ul>
        {% for seed in seeds %}
            <li>{{ seed.variety }} - 
                {% if seed.organic %}Organic{% else %}Non-Organic{% endif %} - 
                {% if seed.local %}Local{% else %}Non-Local{% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```

**500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
</body>
</html>
``` 

To set up the application, ensure you have Flask and SQLAlchemy installed. You can use pip to install them:
```bash
pip install Flask Flask-SQLAlchemy
```

After setting up the project, run the application and navigate to `http://127.0.0.1:5000/` in your browser. Make sure to populate the SQLite database with some seed data to see results.
