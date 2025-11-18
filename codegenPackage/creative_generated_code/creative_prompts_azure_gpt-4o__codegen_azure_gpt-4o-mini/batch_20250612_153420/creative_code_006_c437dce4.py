"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Develop a web application prototype for managing daily meme contests with prizes, as described in the "Rich Pepe" Frogmap Phase 2.
Generated: DETERMINISTIC_c437dce4f567af0e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///memes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Meme model
class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Meme {self.title}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to display the homepage with meme submissions
@app.route('/')
def index():
    memes = Meme.query.all()
    return render_template('index.html', memes=memes)

# Route to submit a new meme
@app.route('/submit', methods=['POST'])
def submit_meme():
    try:
        data = request.get_json()
        new_meme = Meme(title=data['title'], image_url=data['image_url'])
        db.session.add(new_meme)
        db.session.commit()
        return jsonify({'message': 'Meme submitted successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get the list of memes
@app.route('/memes', methods=['GET'])
def get_memes():
    try:
        memes = Meme.query.all()
        return jsonify([{'id': meme.id, 'title': meme.title, 'image_url': meme.image_url} for meme in memes]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a meme
@app.route('/memes/<int:meme_id>', methods=['DELETE'])
def delete_meme(meme_id):
    try:
        meme = Meme.query.get_or_404(meme_id)
        db.session.delete(meme)
        db.session.commit()
        return jsonify({'message': 'Meme deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', True))
```

**HTML Template ("templates/index.html"):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meme Contest</title>
</head>
<body>
    <h1>Daily Meme Contest</h1>
    <form id="memeForm">
        <input type="text" id="title" placeholder="Meme Title" required>
        <input type="url" id="image_url" placeholder="Image URL" required>
        <button type="submit">Submit Meme</button>
    </form>
    <h2>Submitted Memes</h2>
    <div id="memesList"></div>

    <script>
        document.getElementById('memeForm').onsubmit = async function(e) {
            e.preventDefault();
            const title = document.getElementById('title').value;
            const imageUrl = document.getElementById('image_url').value;

            const response = await fetch('/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title: title, image_url: imageUrl })
            });

            if (response.ok) {
                alert('Meme submitted successfully!');
                location.reload();
            } else {
                alert('Error submitting meme: ' + (await response.json()).error);
            }
        };

        async function loadMemes() {
            const response = await fetch('/memes');
            const memes = await response.json();
            const memesList = document.getElementById('memesList');
            memes.forEach(meme => {
                const memeDiv = document.createElement('div');
                memeDiv.innerHTML = `<h3>${meme.title}</h3><img src="${meme.image_url}" alt="${meme.title}" style="max-width:200px;"><button onclick="deleteMeme(${meme.id})">Delete</button>`;
                memesList.appendChild(memeDiv);
            });
        }

        async function deleteMeme(memeId) {
            const response = await fetch(`/memes/${memeId}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                alert('Meme deleted successfully!');
                location.reload();
            } else {
                alert('Error deleting meme: ' + (await response.json()).error);
            }
        }

        // Load memes when the page is loaded
        window.onload = loadMemes;
    </script>
</body>
</html>
```

**Note:** Before running this application, ensure you have Flask and Flask SQLAlchemy installed, and set up your environment variables as needed.
