"""
Generated Code Metadata:
========================
Original URL: https://soltrove.com
Prompt: "Create a UX/UI design concept for an NFT platform that ensures user-friendly community engagement and digital asset management."
Generated: DETERMINISTIC_3d6482be4c40117f
Batch ID: 20250622_211805
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# nft_platform.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for NFT assets
class NFTAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<NFTAsset {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    """Render the home page with a list of NFTs."""
    nfts = NFTAsset.query.all()
    return render_template('index.html', nfts=nfts)

# Route to add a new NFT
@app.route('/add_nft', methods=['POST'])
def add_nft():
    """Add a new NFT asset to the platform."""
    try:
        data = request.json
        new_nft = NFTAsset(
            name=data['name'],
            owner=data['owner'],
            description=data.get('description', ''),
            image_url=data['image_url']
        )
        db.session.add(new_nft)
        db.session.commit()
        return jsonify({'message': 'NFT added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return a JSON response."""
    return jsonify({'error': e.description}), e.code

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Platform</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">NFT Platform</h1>
        <div class="row mt-4">
            {% for nft in nfts %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <img src="{{ nft.image_url }}" class="card-img-top" alt="{{ nft.name }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ nft.name }}</h5>
                            <p class="card-text">{{ nft.description }}</p>
                            <p class="card-text"><small class="text-muted">Owner: {{ nft.owner }}</small></p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
        <h2 class="mt-5">Add New NFT</h2>
        <form id="nftForm">
            <div class="mb-3">
                <label for="name" class="form-label">NFT Name</label>
                <input type="text" class="form-control" id="name" required>
            </div>
            <div class="mb-3">
                <label for="owner" class="form-label">Owner</label>
                <input type="text" class="form-control" id="owner" required>
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description"></textarea>
            </div>
            <div class="mb-3">
                <label for="image_url" class="form-label">Image URL</label>
                <input type="url" class="form-control" id="image_url" required>
            </div>
            <button type="submit" class="btn btn-primary">Add NFT</button>
        </form>
    </div>

    <script>
        document.getElementById('nftForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const nftData = {
                name: document.getElementById('name').value,
                owner: document.getElementById('owner').value,
                description: document.getElementById('description').value,
                image_url: document.getElementById('image_url').value
            };

            fetch('/add_nft', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(nftData)
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                if (data.message) {
                    location.reload(); // Reload to see the new NFT
                }
            })
            .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>
```
