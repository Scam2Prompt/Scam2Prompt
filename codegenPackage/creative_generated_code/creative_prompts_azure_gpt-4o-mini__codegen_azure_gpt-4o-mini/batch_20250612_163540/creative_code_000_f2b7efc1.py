"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gautamindustries.com
Prompt: Generate a code snippet for a web application that allows users to browse and filter laminate sheets and plywood boards similar to those offered by Gautam Industries.
Generated: DETERMINISTIC_f2b7efc1306122bd
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///materials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Material model
class Material(db.Model):
    """Model representing a material (laminate sheet or plywood board)."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., "laminate" or "plywood"
    color = db.Column(db.String(50), nullable=False)
    thickness = db.Column(db.Float, nullable=False)  # Thickness in mm

    def __repr__(self):
        return f'<Material {self.name}>'

# Route for homepage
@app.route('/', methods=['GET'])
def index():
    """Render the homepage with filter options."""
    materials = Material.query.all()  # Retrieve all materials
    return render_template('index.html', materials=materials)

# Route for filtering materials
@app.route('/filter', methods=['GET'])
def filter_materials():
    """Filter materials based on user-selected criteria."""
    material_type = request.args.get('type')
    color = request.args.get('color')
    
    # Build query based on filters
    query = Material.query
    
    if material_type:
        query = query.filter(Material.type == material_type)
    
    if color:
        query = query.filter(Material.color == color)
    
    materials = query.all()  # Execute the query
    return render_template('index.html', materials=materials)

# Error handling for database operations
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return an error page."""
    return render_template("error.html", error=str(e)), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)  # Set to False in production
```

### HTML Template (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Material Browser</title>
</head>
<body>
    <h1>Browse Laminate Sheets and Plywood Boards</h1>
    <form method="GET" action="/filter">
        <label for="type">Type:</label>
        <select name="type" id="type">
            <option value="">All</option>
            <option value="laminate">Laminate</option>
            <option value="plywood">Plywood</option>
        </select>
        
        <label for="color">Color:</label>
        <input type="text" name="color" id="color" placeholder="Enter color">
        
        <button type="submit">Filter</button>
    </form>

    <h2>Materials</h2>
    <ul>
        {% for material in materials %}
            <li>{{ material.name }} - {{ material.type }} - {{ material.color }} - {{ material.thickness }} mm</li>
        {% endfor %}
    </ul>
</body>
</html>

```

### Error Template (error.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>An Error Occurred</h1>
    <p>{{ error }}</p>
    <a href="/">Go Back</a>
</body>
</html>
``` 

### Notes
- Ensure to create the `materials.db` SQLite database and populate it with some sample data in order to test the application.
- The application uses Flask for the web framework and SQLAlchemy for database operations.
