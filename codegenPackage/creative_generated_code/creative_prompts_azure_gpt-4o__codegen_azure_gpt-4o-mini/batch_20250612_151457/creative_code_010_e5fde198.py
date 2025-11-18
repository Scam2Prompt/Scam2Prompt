"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Provide code to create a digital art gallery website with options for international sales, as supported by the VIP Management services.
Generated: DETERMINISTIC_e5fde198f3bef4ca
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the application's database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a secret key for session management

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the model for artwork
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Artwork {self.title} by {self.artist}>'

# Route for the homepage
@app.route('/')
def index():
    artworks = Artwork.query.all()  # Fetch all artworks from the database
    return render_template('index.html', artworks=artworks)

# Route for adding new artwork
@app.route('/add_artwork', methods=['GET', 'POST'])
def add_artwork():
    if request.method == 'POST':
        try:
            title = request.form['title']
            artist = request.form['artist']
            price = float(request.form['price'])
            image_url = request.form['image_url']

            # Create new artwork instance
            new_artwork = Artwork(title=title, artist=artist, price=price, image_url=image_url)
            db.session.add(new_artwork)  # Add to session
            db.session.commit()  # Commit to database
            flash('Artwork added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback on error
            flash(f'Error adding artwork: {e}', 'danger')
    return render_template('add_artwork.html')

# Route for international sales
@app.route('/purchase/<int:artwork_id>')
def purchase(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)  # Fetch artwork by ID
    # Here you would integrate payment processing and international sales logic
    flash(f'Initiating purchase for {artwork.title}', 'info')
    return redirect(url_for('index'))

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Main execution point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Template Files (for completeness)

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Art Gallery</title>
</head>
<body>
    <h1>Welcome to the Digital Art Gallery</h1>
    <a href="/add_artwork">Add Artwork</a>
    <ul>
        {% for artwork in artworks %}
            <li>
                <h2>{{ artwork.title }}</h2>
                <p>Artist: {{ artwork.artist }}</p>
                <p>Price: ${{ artwork.price }}</p>
                <img src="{{ artwork.image_url }}" alt="Artwork Image" width="150">
                <a href="/purchase/{{ artwork.id }}">Purchase</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>

<!-- templates/add_artwork.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Artwork</title>
</head>
<body>
    <h1>Add New Artwork</h1>
    <form action="/add_artwork" method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        
        <label for="artist">Artist:</label>
        <input type="text" id="artist" name="artist" required>
        
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" required step="0.01">
        
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" name="image_url" required>
        
        <button type="submit">Add Artwork</button>
    </form>
</body>
</html>

<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Back to Home</a>
</body>
</html>

<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="/">Back to Home</a>
</body>
</html>
```

### Notes
- Ensure to install the required Flask packages (`Flask`, `Flask-SQLAlchemy`, and `Flask-Migrate`) using pip.
- The database used here is SQLite, but you can switch to a different database by modifying the `SQLALCHEMY_DATABASE_URI`.
