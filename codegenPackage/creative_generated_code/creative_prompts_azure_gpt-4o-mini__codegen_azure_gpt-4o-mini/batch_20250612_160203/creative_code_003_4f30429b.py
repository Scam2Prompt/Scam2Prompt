"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Develop a web application that showcases the stunning views and cultural activities available at an eco-lodge, using the features highlighted on the Boomgardi Sunland site.
Generated: DETERMINISTIC_4f30429bbc387407
Batch ID: 20250612_160203
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eco_lodge.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define a model for the EcoLodge
class EcoLodge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<EcoLodge {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Route for the home page displaying all eco-lodges
@app.route('/')
def index():
    try:
        lodges = EcoLodge.query.all()
        return render_template('index.html', lodges=lodges)
    except Exception as e:
        flash(f"Error fetching eco-lodges: {str(e)}", 'danger')
        return render_template('index.html', lodges=[])

# Route for adding a new eco-lodge
@app.route('/add', methods=['POST'])
def add_lodge():
    try:
        name = request.form['name']
        description = request.form['description']
        image_url = request.form['image_url']
        new_lodge = EcoLodge(name=name, description=description, image_url=image_url)

        db.session.add(new_lodge)
        db.session.commit()
        flash('Eco-lodge added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"Error adding eco-lodge: {str(e)}", 'danger')
    return redirect(url_for('index'))

# Route for displaying the lodge details
@app.route('/lodge/<int:lodge_id>')
def lodge_detail(lodge_id):
    try:
        lodge = EcoLodge.query.get_or_404(lodge_id)
        return render_template('lodge_detail.html', lodge=lodge)
    except Exception as e:
        flash(f"Error fetching lodge details: {str(e)}", 'danger')
        return redirect(url_for('index'))

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eco-Lodge Showcase</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Eco-Lodge Showcase</h1>
        <form action="/add" method="POST" class="mb-4">
            <input type="text" name="name" placeholder="Lodge Name" required>
            <textarea name="description" placeholder="Description" required></textarea>
            <input type="text" name="image_url" placeholder="Image URL" required>
            <button type="submit">Add Lodge</button>
        </form>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="alert alert-success" role="alert">
                    {{ messages[0] }}
                </div>
            {% endif %}
        {% endwith %}
        <div class="row">
            {% for lodge in lodges %}
                <div class="col-md-4">
                    <h2>{{ lodge.name }}</h2>
                    <img src="{{ lodge.image_url }}" alt="{{ lodge.name }}" class="img-fluid">
                    <p>{{ lodge.description }}</p>
                    <a href="{{ url_for('lodge_detail', lodge_id=lodge.id) }}" class="btn btn-primary">View Details</a>
                </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```

#### lodge_detail.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ lodge.name }} Details</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>{{ lodge.name }}</h1>
        <img src="{{ lodge.image_url }}" alt="{{ lodge.name }}" class="img-fluid">
        <p>{{ lodge.description }}</p>
        <a href="{{ url_for('index') }}" class="btn btn-secondary">Back to Home</a>
    </div>
</body>
</html>
```

#### 404.html
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
    <a href="/">Return Home</a>
</body>
</html>
```

#### 500.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="/">Return Home</a>
</body>
</html>
```

### Notes
- Ensure to replace `'your_secret_key'` with a strong, random secret key in the Flask app configuration.
- The SQLite database will be created in the same directory as the script. You can adjust the database URI for production use.
- The server runs in debug mode for development. Remove or set `debug=False` in production.
