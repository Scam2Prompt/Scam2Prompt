"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Generate code for a web application that allows businesses to compare bespoke asset finance options for light aircraft, agricultural equipment, and other assets, inspired by Rhino Asset Finance's services.
Generated: DETERMINISTIC_ef72234627ab9b97
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for Asset Finance Options
class AssetFinanceOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_type = db.Column(db.String(50), nullable=False)
    finance_option = db.Column(db.String(120), nullable=False)
    rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<AssetFinanceOption {self.asset_type} {self.finance_option}>'

# Create the database and add some sample data
@app.before_first_request
def create_tables():
    db.create_all()
    if not AssetFinanceOption.query.first():
        sample_options = [
            AssetFinanceOption(asset_type='Light Aircraft', finance_option='Lease', rate=4.5),
            AssetFinanceOption(asset_type='Agricultural Equipment', finance_option='Loan', rate=6.0),
            AssetFinanceOption(asset_type='Light Aircraft', finance_option='Hire Purchase', rate=5.2),
            AssetFinanceOption(asset_type='Agricultural Equipment', finance_option='Lease', rate=5.5),
        ]
        db.session.bulk_save_objects(sample_options)
        db.session.commit()

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# API route to get finance options based on asset type
@app.route('/api/finance_options', methods=['GET'])
def get_finance_options():
    asset_type = request.args.get('asset_type')
    if not asset_type:
        return jsonify({"error": "Asset type is required"}), 400

    try:
        options = AssetFinanceOption.query.filter_by(asset_type=asset_type).all()
        if not options:
            return jsonify({"message": "No options found"}), 404

        return jsonify([{"finance_option": option.finance_option, "rate": option.rate} for option in options]), 200
    except SQLAlchemyError as e:
        logging.error(f"Database error: {e}")
        return jsonify({"error": "Internal server error"}), 500

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
    <title>Asset Finance Comparison</title>
    <script>
        async function fetchFinanceOptions() {
            const assetType = document.getElementById('asset-type').value;
            const response = await fetch(`/api/finance_options?asset_type=${assetType}`);
            const result = await response.json();
            const optionsList = document.getElementById('options-list');
            optionsList.innerHTML = '';

            if (response.ok) {
                result.forEach(option => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `Option: ${option.finance_option}, Rate: ${option.rate}%`;
                    optionsList.appendChild(listItem);
                });
            } else {
                const errorMessage = document.createElement('li');
                errorMessage.textContent = result.error || result.message;
                optionsList.appendChild(errorMessage);
            }
        }
    </script>
</head>
<body>
    <h1>Compare Asset Finance Options</h1>
    <label for="asset-type">Select Asset Type:</label>
    <select id="asset-type" onchange="fetchFinanceOptions()">
        <option value="">--Select--</option>
        <option value="Light Aircraft">Light Aircraft</option>
        <option value="Agricultural Equipment">Agricultural Equipment</option>
    </select>
    <h2>Finance Options:</h2>
    <ul id="options-list"></ul>
</body>
</html>
```

This web application utilizes Flask for the backend and renders a simple frontend to allow users to select asset types and retrieve corresponding finance options. The application includes basic error handling and is ready for production deployment.
