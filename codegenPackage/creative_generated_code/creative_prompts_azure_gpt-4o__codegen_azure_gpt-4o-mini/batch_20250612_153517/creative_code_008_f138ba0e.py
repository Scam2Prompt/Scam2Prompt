"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lounchmenftx.web.app
Prompt: Develop a web application feature to explore and filter NFT collections, inspired by the "Collections Explore Hot Latest" section on LaunchMyNFT.
Generated: DETERMINISTIC_f138ba0e7beaae7a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries for web development
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and the SQLAlchemy database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the NFT Collection model
class NFTCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    creator = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    hot = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<NFTCollection {self.name}>"

# Route to render the NFT collections page
@app.route('/')
def index():
    return render_template('index.html')

# API route to fetch NFT collections with filtering options
@app.route('/api/collections', methods=['GET'])
def get_collections():
    try:
        # Get query parameters for filtering
        category = request.args.get('category')
        hot = request.args.get('hot', type=bool)

        # Build the query
        query = NFTCollection.query
        
        if category:
            query = query.filter(NFTCollection.category == category)
        if hot is not None:
            query = query.filter(NFTCollection.hot == hot)

        # Get results
        collections = query.all()
        return jsonify([{
            'id': collection.id,
            'name': collection.name,
            'creator': collection.creator,
            'created_at': collection.created_at.isoformat(),
            'category': collection.category,
            'hot': collection.hot
        } for collection in collections]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Entry point for the application
if __name__ == '__main__':
    # Create the database tables (if needed)
    db.create_all()
    # Run the application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Collections Explorer</title>
    <script>
        async function fetchCollections() {
            const category = document.getElementById("category").value;
            const hot = document.getElementById("hot").checked;
            const response = await fetch(`/api/collections?category=${category}&hot=${hot}`);
            const data = await response.json();
            const results = document.getElementById("results");
            results.innerHTML = '';

            if (data.error) {
                results.innerHTML = `<p>${data.error}</p>`;
            } else {
                data.forEach(collection => {
                    results.innerHTML += `<p>${collection.name} by ${collection.creator}</p>`;
                });
            }
        }
    </script>
</head>
<body>
    <h1>NFT Collections Explorer</h1>
    <label for="category">Category:</label>
    <input type="text" id="category" placeholder="Enter category">
    <label for="hot">Hot Collections:</label>
    <input type="checkbox" id="hot">
    <button onclick="fetchCollections()">Explore Collections</button>
    <div id="results"></div>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment (`pip install Flask Flask-SQLAlchemy`).
- The SQLite database is used for simplicity; you can modify the database URI for production use.
- The HTML file should be stored in a `templates` directory within your project folder.
- The application is set to run in debug mode for development; remove `debug=True` in production.
