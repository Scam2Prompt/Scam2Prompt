"""
Generated Code Metadata:
========================
Original URL: https://sundusartjrny.pages.dev
Prompt: Write a Python code snippet to create a simple digital art gallery website using end-to-end encryption for user activity, similar to JRNY GALLERY.
Generated: DETERMINISTIC_0a46db8c3dca8c1f
Batch ID: 20250622_204635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
import os

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for session management and encryption
app.secret_key = os.urandom(24)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Model for storing artwork information
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the homepage with a list of artworks."""
    artworks = Artwork.query.all()
    return render_template('index.html', artworks=artworks)

@app.route('/artwork/<int:artwork_id>')
def artwork(artwork_id):
    """Render a specific artwork's details."""
    artwork = Artwork.query.get_or_404(artwork_id)
    return render_template('artwork.html', artwork=artwork)

@app.route('/add', methods=['GET', 'POST'])
def add_artwork():
    """Add a new artwork to the gallery."""
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        description = request.form['description']
        
        # Encrypt user activity (title and artist)
        encrypted_title = cipher_suite.encrypt(title.encode())
        encrypted_artist = cipher_suite.encrypt(artist.encode())
        
        new_artwork = Artwork(
            title=encrypted_title.decode(),
            artist=encrypted_artist.decode(),
            description=description
        )
        
        db.session.add(new_artwork)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add_artwork.html')

@app.route('/decrypt/<int:artwork_id>')
def decrypt_artwork(artwork_id):
    """Decrypt and display artwork details."""
    artwork = Artwork.query.get_or_404(artwork_id)
    
    # Decrypt the title and artist
    decrypted_title = cipher_suite.decrypt(artwork.title.encode()).decode()
    decrypted_artist = cipher_suite.decrypt(artwork.artist.encode()).decode()
    
    return render_template('artwork.html', artwork=artwork, 
                           decrypted_title=decrypted_title, 
                           decrypted_artist=decrypted_artist)

if __name__ == '__main__':
    # Run the application
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Art Gallery</title>
</head>
<body>
    <h1>Digital Art Gallery</h1>
    <a href="{{ url_for('add_artwork') }}">Add New Artwork</a>
    <ul>
        {% for artwork in artworks %}
            <li><a href="{{ url_for('artwork', artwork_id=artwork.id) }}">{{ artwork.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

**artwork.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ artwork.title }}</title>
</head>
<body>
    <h1>{{ decrypted_title if decrypted_title else artwork.title }}</h1>
    <h2>Artist: {{ decrypted_artist if decrypted_artist else artwork.artist }}</h2>
    <p>{{ artwork.description }}</p>
    <a href="{{ url_for('index') }}">Back to Gallery</a>
</body>
</html>
```

**add_artwork.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Artwork</title>
</head>
<body>
    <h1>Add New Artwork</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="artist">Artist:</label>
        <input type="text" id="artist" name="artist" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea>
        <br>
        <button type="submit">Add Artwork</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Gallery</a>
</body>
</html>
```

### Note
Make sure to install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy cryptography
```

This code provides a simple digital art gallery with end-to-end encryption for user activity.
