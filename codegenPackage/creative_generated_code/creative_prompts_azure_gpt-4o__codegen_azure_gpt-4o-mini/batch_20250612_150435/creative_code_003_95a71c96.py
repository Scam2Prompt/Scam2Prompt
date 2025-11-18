"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piclink.me
Prompt: Create a web application that mimics PicLink's functionality, enabling users to connect and customize links for social media and music platforms.
Generated: DETERMINISTIC_95a71c96595c8e27
Batch ID: 20250612_150435
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///piclink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Initialize the database and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Link model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Link {self.platform}>'

# Route for the home page
@app.route('/')
def index():
    links = Link.query.all()  # Fetch all links from the database
    return render_template('index.html', links=links)

# Route for adding a new link
@app.route('/add', methods=['POST'])
def add_link():
    platform = request.form.get('platform')
    url = request.form.get('url')

    # Input validation
    if not platform or not url:
        flash('Platform and URL are required!', 'danger')
        return redirect(url_for('index'))

    new_link = Link(platform=platform, url=url)
    db.session.add(new_link)

    try:
        db.session.commit()  # Commit the new link to the database
        flash('Link added successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback on error
        flash(f'Error adding link: {str(e)}', 'danger')

    return redirect(url_for('index'))

# Route for deleting a link
@app.route('/delete/<int:link_id>', methods=['POST'])
def delete_link(link_id):
    link = Link.query.get_or_404(link_id)  # Fetch the link or return 404
    db.session.delete(link)

    try:
        db.session.commit()  # Commit the deletion to the database
        flash('Link deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback on error
        flash(f'Error deleting link: {str(e)}', 'danger')

    return redirect(url_for('index'))

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return render_template("error.html", error=e), e.code

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PicLink Clone</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Manage Your Links</h1>
        <form method="POST" action="/add" class="mb-3">
            <input type="text" name="platform" placeholder="Platform" required>
            <input type="url" name="url" placeholder="URL" required>
            <button type="submit" class="btn btn-primary">Add Link</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}
        <ul class="list-group">
            {% for link in links %}
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    {{ link.platform }} - <a href="{{ link.url }}" target="_blank">{{ link.url }}</a>
                    <form method="POST" action="/delete/{{ link.id }}" style="display: inline;">
                        <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                    </form>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

#### `templates/error.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>An Error Occurred</h1>
        <p>{{ error.description }}</p>
        <a href="/" class="btn btn-primary">Return Home</a>
    </div>
</body>
</html>
```

### Instructions to Run the Application
1. Ensure you have Python and Flask installed.
2. Create a virtual environment and activate it.
3. Install the required packages using:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
4. Create the database and run migrations:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
5. Run the application:
   ```bash
   python app.py
   ```

Make sure to replace `your_secret_key` with a strong, random string for production use.
