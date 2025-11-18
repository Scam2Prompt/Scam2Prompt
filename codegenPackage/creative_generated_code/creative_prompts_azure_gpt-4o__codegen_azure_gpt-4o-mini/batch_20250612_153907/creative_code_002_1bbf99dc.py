"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate code using Flask to implement a "Nominate" feature where users can submit profiles for inclusion in categories like "Teacher" or "Medical" on a community-driven website.
Generated: DETERMINISTIC_1bbf99dc896d0d1d
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Configuring the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nominations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model for storing nominations
class Nomination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Nomination {self.name} - {self.category}>'

# Route to display the nomination form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle nomination submissions
@app.route('/nominate', methods=['POST'])
def nominate():
    try:
        # Extracting submitted data
        name = request.form['name']
        category = request.form['category']
        description = request.form.get('description', '')

        # Basic validation
        if not name or not category:
            raise BadRequest("Name and category are required fields.")

        # Create a new nomination
        new_nomination = Nomination(name=name, category=category, description=description)

        # Add new nomination to the database
        db.session.add(new_nomination)
        db.session.commit()

        return redirect(url_for('index')), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

# Route to view all nominations
@app.route('/nominations', methods=['GET'])
def view_nominations():
    nominations = Nomination.query.all()
    return render_template('nominations.html', nominations=nominations)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

**HTML Templates (index.html and nominations.html)**

`index.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nominate</title>
</head>
<body>
    <h1>Nominate a Profile</h1>
    <form action="/nominate" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="category">Category:</label>
        <input type="text" id="category" name="category" required>
        
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea>
        
        <button type="submit">Submit Nomination</button>
    </form>
    <a href="/nominations">View All Nominations</a>
</body>
</html>
```

`nominations.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nominations</title>
</head>
<body>
    <h1>All Nominations</h1>
    <ul>
        {% for nomination in nominations %}
            <li>{{ nomination.name }} - {{ nomination.category }}: {{ nomination.description }}</li>
        {% endfor %}
    </ul>
    <a href="/">Nominate Another</a>
</body>
</html>
``` 

**Notes**: 
- Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment.
- Create the SQLite database automatically when running the app for the first time.
