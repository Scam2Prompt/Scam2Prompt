"""
Generated Code Metadata:
========================
Original URL: https://inceptiontrades.net
Prompt: Develop a simple web application that allows users to manage their multi-assets portfolio, inspired by the services provided by Inception Trades.
Generated: DETERMINISTIC_5456e329c5969cf3
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Portfolio model
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Portfolio {self.asset_name}>'

# Route to render the main portfolio page
@app.route('/')
def index():
    portfolios = Portfolio.query.all()
    return render_template('index.html', portfolios=portfolios)

# Route to add a new asset to the portfolio
@app.route('/add', methods=['POST'])
def add_asset():
    try:
        data = request.get_json()
        new_asset = Portfolio(
            asset_name=data['asset_name'],
            quantity=data['quantity'],
            purchase_price=data['purchase_price']
        )
        db.session.add(new_asset)
        db.session.commit()
        return jsonify({'message': 'Asset added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to update an existing asset
@app.route('/update/<int:id>', methods=['PUT'])
def update_asset(id):
    try:
        asset = Portfolio.query.get_or_404(id)
        data = request.get_json()
        asset.asset_name = data.get('asset_name', asset.asset_name)
        asset.quantity = data.get('quantity', asset.quantity)
        asset.purchase_price = data.get('purchase_price', asset.purchase_price)
        db.session.commit()
        return jsonify({'message': 'Asset updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete an asset from the portfolio
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_asset(id):
    try:
        asset = Portfolio.query.get_or_404(id)
        db.session.delete(asset)
        db.session.commit()
        return jsonify({'message': 'Asset deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio Management</title>
</head>
<body>
    <h1>My Portfolio</h1>
    <form id="addAssetForm">
        <input type="text" id="asset_name" placeholder="Asset Name" required>
        <input type="number" id="quantity" placeholder="Quantity" required>
        <input type="number" id="purchase_price" placeholder="Purchase Price" required>
        <button type="submit">Add Asset</button>
    </form>
    <ul id="portfolioList">
        {% for asset in portfolios %}
            <li>{{ asset.asset_name }} - {{ asset.quantity }} - ${{ asset.purchase_price }}</li>
        {% endfor %}
    </ul>
    <script>
        document.getElementById('addAssetForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const assetName = document.getElementById('asset_name').value;
            const quantity = document.getElementById('quantity').value;
            const purchasePrice = document.getElementById('purchase_price').value;

            fetch('/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    asset_name: assetName,
                    quantity: quantity,
                    purchase_price: purchasePrice
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    location.reload();
                } else {
                    alert(data.error);
                }
            });
        });
    </script>
</body>
</html>
```

**Note:** Ensure you have Flask, Flask-SQLAlchemy, and Flask-Migrate installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

To initialize the database, run the following commands in your terminal:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

This code provides a simple web application for managing a multi-assets portfolio, including routes for adding, updating, and deleting assets, along with a basic HTML interface.
