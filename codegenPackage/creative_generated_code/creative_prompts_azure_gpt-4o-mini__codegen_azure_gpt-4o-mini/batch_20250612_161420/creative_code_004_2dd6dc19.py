"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://del-pinar.com.ar
Prompt: Suggest a library for building a user-friendly interface to showcase the unique features of an apart hotel, such as nature walks and bike rentals.
Generated: DETERMINISTIC_2dd6dc191c083d18
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initializing the Flask application
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apart_hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Defining a model for unique features of the apart hotel
class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feature {self.title}>'

# Route for the main page showcasing features
@app.route('/')
def index():
    try:
        # Querying all features from the database
        features = Feature.query.all()
        return render_template('index.html', features=features)
    except Exception as e:
        # Error handling for database queries
        return f"An error occurred while fetching features: {e}"

# Route for adding a new feature (admin functionality)
@app.route('/add_feature', methods=['GET', 'POST'])
def add_feature():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_feature = Feature(title=title, description=description)

        try:
            # Adding the new feature to the database
            db.session.add(new_feature)
            db.session.commit()
            return f"Feature '{title}' added successfully!"
        except Exception as e:
            # Error handling for database operations
            return f"An error occurred while adding the feature: {e}"

    return render_template('add_feature.html')

# Main block to run the Flask application
if __name__ == '__main__':
    # Create all database tables
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

**HTML Templates (index.html and add_feature.html)**

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apart Hotel Features</title>
</head>
<body>
    <h1>Unique Features of Our Apart Hotel</h1>
    <ul>
        {% for feature in features %}
            <li><strong>{{ feature.title }}:</strong> {{ feature.description }}</li>
        {% endfor %}
    </ul>
    <a href="/add_feature">Add a New Feature</a>
</body>
</html>
```

```html
<!-- add_feature.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add New Feature</title>
</head>
<body>
    <h1>Add a New Feature</h1>
    <form method="POST">
        <label for="title">Feature Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Feature Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <button type="submit">Add Feature</button>
    </form>
    <a href="/">Back to Features</a>
</body>
</html>
```
