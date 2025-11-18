"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-playpixiz-io.pages.dev
Prompt: Suggest tools or frameworks to create a dashboard similar to Pixiz Mint for managing NFT and token allocations.
Generated: DETERMINISTIC_c33634b823661625
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_allocations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the NFT Allocation model
class NFTAllocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), nullable=False)
    token_id = db.Column(db.String(64), nullable=False)
    allocation_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<NFTAllocation {self.wallet_address} {self.token_id} {self.allocation_amount}>'

# Home route to display dashboard
@app.route('/')
def home():
    try:
        allocations = NFTAllocation.query.all()
        return render_template('dashboard.html', allocations=allocations)
    except Exception as e:
        # Log the error and return an error message
        app.logger.error(f"Error fetching allocations: {e}")
        return "An error occurred while fetching allocations.", 500

# Function to connect to Ethereum
def connect_to_ethereum(rpc_url):
    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        if not w3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum node.")
        return w3
    except Exception as e:
        # Log connection errors
        app.logger.error(f"Error connecting to Ethereum: {e}")
        raise

# Endpoint to add a new NFT allocation
@app.route('/add_allocation', methods=['POST'])
def add_allocation():
    try:
        wallet_address = request.form['wallet_address']
        token_id = request.form['token_id']
        allocation_amount = float(request.form['allocation_amount'])
        
        new_allocation = NFTAllocation(
            wallet_address=wallet_address,
            token_id=token_id,
            allocation_amount=allocation_amount
        )
        db.session.add(new_allocation)
        db.session.commit()
        return "Allocation added successfully!", 201
    except Exception as e:
        # Log any errors during allocation addition
        app.logger.error(f"Error adding allocation: {e}")
        return "An error occurred while adding the allocation.", 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- dashboard.html: HTML template for the dashboard -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Allocation Dashboard</title>
</head>
<body>
    <h1>NFT Allocation Dashboard</h1>
    <table>
        <thead>
            <tr>
                <th>Wallet Address</th>
                <th>Token ID</th>
                <th>Allocation Amount</th>
            </tr>
        </thead>
        <tbody>
            {% for allocation in allocations %}
            <tr>
                <td>{{ allocation.wallet_address }}</td>
                <td>{{ allocation.token_id }}</td>
                <td>{{ allocation.allocation_amount }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <form action="/add_allocation" method="POST">
        <h2>Add New Allocation</h2>
        <label for="wallet_address">Wallet Address:</label>
        <input type="text" name="wallet_address" required>
        <label for="token_id">Token ID:</label>
        <input type="text" name="token_id" required>
        <label for="allocation_amount">Allocation Amount:</label>
        <input type="number" name="allocation_amount" step="0.01" required>
        <button type="submit">Add Allocation</button>
    </form>
</body>
</html>
```

### Note:
Make sure to install the necessary dependencies using:
```bash
pip install Flask Flask-SQLAlchemy web3
```
Also, ensure that you have a running SQLite database or change the database URI as needed for your environment.
