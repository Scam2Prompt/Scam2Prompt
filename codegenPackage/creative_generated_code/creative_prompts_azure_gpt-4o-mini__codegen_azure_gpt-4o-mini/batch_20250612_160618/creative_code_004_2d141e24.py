"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Develop a web application that showcases success stories of women leaders from Sauti Kenya, highlighting their contributions to community advocacy and sustainability.
Generated: DETERMINISTIC_2d141e24bd0b2184
Batch ID: 20250612_160618
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
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
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sauti_kenya.db'  # Database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)

# Model for storing success stories of women leaders
class SuccessStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contribution = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<SuccessStory {self.name}>'

@app.route('/')
def index():
    """Render the homepage with a list of success stories."""
    stories = SuccessStory.query.all()  # Fetch all success stories from the database
    return render_template('index.html', stories=stories)

@app.route('/add_story', methods=['GET', 'POST'])
def add_story():
    """Handle the addition of a new success story."""
    if request.method == 'POST':
        name = request.form.get('name')
        contribution = request.form.get('contribution')
        image_url = request.form.get('image_url')

        if not name or not contribution:
            flash('Name and contribution are required!', 'error')
            return redirect(url_for('add_story'))

        # Create a new success story instance
        new_story = SuccessStory(name=name, contribution=contribution, image_url=image_url)
        db.session.add(new_story)  # Add the instance to the session
        db.session.commit()  # Commit the changes to the database
        flash('Success story added!', 'success')
        return redirect(url_for('index'))

    return render_template('add_story.html')  # Render the form for adding a story

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sauti Kenya - Success Stories</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Success Stories of Women Leaders</h1>
        <a href="{{ url_for('add_story') }}" class="btn btn-primary mb-3">Add a New Story</a>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <div class="row">
            {% for story in stories %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <img src="{{ story.image_url }}" class="card-img-top" alt="{{ story.name }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ story.name }}</h5>
                            <p class="card-text">{{ story.contribution }}</p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/add_story.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Success Story</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Add a New Success Story</h1>
        <form method="POST">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="contribution">Contribution</label>
                <textarea class="form-control" id="contribution" name="contribution" rows="3" required></textarea>
            </div>
            <div class="form-group">
                <label for="image_url">Image URL</label>
                <input type="url" class="form-control" id="image_url" name="image_url">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
            <a href="{{ url_for('index') }}" class="btn btn-secondary">Cancel</a>
        </form>
    </div>
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
    <title>404 Not Found</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">404 - Page Not Found</h1>
        <p>The page you are looking for does not exist.</p>
        <a href="{{ url_for('index') }}" class="btn btn-primary">Return to Home</a>
    </div>
</body>
</html>
``` 

```bash
# requirements.txt

Flask==2.0.1
Flask-SQLAlchemy==2.5.1
```

### Instructions to set up the project:
1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Access the web application at `http://127.0.0.1:5000`.
