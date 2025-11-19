"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterkuroro.pages.dev
Prompt: Develop a simple web application that displays the unique elemental powers of Kuroro Beasts and allows users to filter by element.
Generated: DETERMINISTIC_576b2beeeef8d0d6
Batch ID: 20250612_155140
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

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kuroro_beasts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the Kuroro Beasts
class KuroroBeast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    element = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<KuroroBeast {self.name}, Element: {self.element}>'

# Create the database and add some sample data
@app.before_first_request
def create_tables():
    db.create_all()
    if KuroroBeast.query.count() == 0:  # Only add sample data if empty
        sample_beasts = [
            KuroroBeast(name='Fire Beast', element='Fire'),
            KuroroBeast(name='Water Beast', element='Water'),
            KuroroBeast(name='Earth Beast', element='Earth'),
            KuroroBeast(name='Air Beast', element='Air'),
            KuroroBeast(name='Lightning Beast', element='Lightning'),
        ]
        db.session.bulk_save_objects(sample_beasts)
        db.session.commit()

# Route to display the beasts
@app.route('/', methods=['GET'])
def index():
    element_filter = request.args.get('element')
    if element_filter:
        beasts = KuroroBeast.query.filter_by(element=element_filter).all()
    else:
        beasts = KuroroBeast.query.all()
    
    return render_template('index.html', beasts=beasts)

# Error handler for 404 not found
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**HTML Template (index.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kuroro Beasts</title>
</head>
<body>
    <h1>Kuroro Beasts</h1>
    <form method="GET">
        <label for="element">Filter by Element:</label>
        <select name="element" id="element">
            <option value="">All</option>
            <option value="Fire">Fire</option>
            <option value="Water">Water</option>
            <option value="Earth">Earth</option>
            <option value="Air">Air</option>
            <option value="Lightning">Lightning</option>
        </select>
        <button type="submit">Filter</button>
    </form>
    <ul>
        {% for beast in beasts %}
            <li>{{ beast.name }} - Element: {{ beast.element }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**HTML Template (404.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

**Note**: Remember to create a virtual environment, install Flask and Flask-SQLAlchemy, and set up the database with the above code to run the application.
