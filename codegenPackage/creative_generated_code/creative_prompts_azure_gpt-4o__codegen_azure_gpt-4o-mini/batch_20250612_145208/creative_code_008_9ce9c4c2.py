"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Create a dashboard application that uses Instadapp Lite's API to display active vaults, estimated yearly yields, and earnings for a connected wallet.
Generated: DETERMINISTIC_9ce9c4c2f63a4c40
Batch ID: 20250612_145208
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.instadapp.io/v1": {
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
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the base URL for the Instadapp Lite API
BASE_URL = "https://api.instadapp.io/v1"

# Function to get active vaults for a given wallet address
def get_active_vaults(wallet_address):
    try:
        response = requests.get(f"{BASE_URL}/vaults/{wallet_address}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching vaults: {e}")
        return None

# Function to get estimated yearly yields for a given vault ID
def get_estimated_yields(vault_id):
    try:
        response = requests.get(f"{BASE_URL}/yields/{vault_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching yields for vault {vault_id}: {e}")
        return None

# Function to get earnings for a given wallet address
def get_earnings(wallet_address):
    try:
        response = requests.get(f"{BASE_URL}/earnings/{wallet_address}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching earnings: {e}")
        return None

@app.route('/')
def dashboard():
    # Render the dashboard template
    return render_template('dashboard.html')

@app.route('/api/vaults', methods=['GET'])
def api_vaults():
    wallet_address = request.args.get('address')
    if not wallet_address:
        return jsonify({"error": "Wallet address is required"}), 400

    vaults = get_active_vaults(wallet_address)
    if vaults is None:
        return jsonify({"error": "Failed to fetch active vaults"}), 500

    vault_data = []
    for vault in vaults:
        yield_data = get_estimated_yields(vault['id'])
        vault_data.append({
            "vault_id": vault['id'],
            "name": vault['name'],
            "yearly_yield": yield_data['estimated_yield'] if yield_data else "N/A"
        })

    earnings = get_earnings(wallet_address)
    if earnings is None:
        return jsonify({"error": "Failed to fetch earnings"}), 500

    return jsonify({
        "vaults": vault_data,
        "earnings": earnings
    })

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instadapp Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Instadapp Dashboard</h1>
        <form id="walletForm" class="mt-4">
            <div class="form-group">
                <label for="walletAddress">Wallet Address:</label>
                <input type="text" class="form-control" id="walletAddress" required>
            </div>
            <button type="submit" class="btn btn-primary">Get Vaults</button>
        </form>
        
        <div id="vaults" class="mt-4"></div>
    </div>

    <script>
        document.getElementById('walletForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const walletAddress = document.getElementById('walletAddress').value;

            fetch(`/api/vaults?address=${walletAddress}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('vaults').innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
                    } else {
                        let vaultList = '<h2>Active Vaults</h2><ul>';
                        data.vaults.forEach(vault => {
                            vaultList += `<li>${vault.name} - Estimated Yearly Yield: ${vault.yearly_yield}</li>`;
                        });
                        vaultList += '</ul>';
                        vaultList += `<h3>Earnings: ${data.earnings}</h3>`;
                        document.getElementById('vaults').innerHTML = vaultList;
                    }
                })
                .catch(error => {
                    document.getElementById('vaults').innerHTML = `<div class="alert alert-danger">Error fetching data: ${error.message}</div>`;
                });
        });
    </script>
</body>
</html>
```
