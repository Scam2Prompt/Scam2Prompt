"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hawksight-v2.vercel.app
Prompt: Create a dashboard that displays HawkFi pool metrics, including TVL, fees, and balance, with options to refresh and sort data.
Generated: DETERMINISTIC_2e36d039f7bb3c9b
Batch ID: 20250612_153702
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hawkfi.com/v1/pools": {
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
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Constants for the HawkFi API endpoint
HAWKFI_API_URL = "https://api.hawkfi.com/v1/pools"

def fetch_pool_metrics():
    """
    Fetches pool metrics from the HawkFi API.
    
    Returns:
        DataFrame: A pandas DataFrame containing pool metrics like TVL, fees, and balance.
    """
    try:
        response = requests.get(HAWKFI_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        if not data:
            return pd.DataFrame()  # Return empty DataFrame if no data
        
        # Convert the fetched data into a DataFrame
        df = pd.DataFrame(data)
        return df[["name", "tvl", "fees", "balance"]]  # Select relevant columns
    except requests.RequestException as e:
        print(f"Error fetching data from HawkFi API: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

@app.route('/')
def index():
    """
    Renders the main dashboard page.
    
    Returns:
        str: The rendered HTML template for the dashboard.
    """
    return render_template('dashboard.html')

@app.route('/api/pools', methods=['GET'])
def get_pool_data():
    """
    API endpoint to get pool metrics.
    
    Returns:
        JSON: JSON response containing pool metrics.
    """
    metrics_df = fetch_pool_metrics()
    return jsonify(metrics_df.to_dict(orient='records'))

if __name__ == '__main__':
    # Start the Flask web server
    app.run(debug=True)
```

**HTML Template (dashboard.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HawkFi Pool Dashboard</title>
    <script>
        async function fetchPoolData() {
            try {
                const response = await fetch('/api/pools');
                const data = await response.json();
                displayData(data);
            } catch (error) {
                console.error('Error fetching pool data:', error);
            }
        }

        function displayData(data) {
            const tableBody = document.getElementById('pool-data');
            tableBody.innerHTML = '';  // Clear existing data
            
            data.forEach(pool => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${pool.name}</td>
                    <td>${pool.tvl}</td>
                    <td>${pool.fees}</td>
                    <td>${pool.balance}</td>
                `;
                tableBody.appendChild(row);
            });
        }

        function refreshData() {
            fetchPoolData();
        }

        window.onload = fetchPoolData; // Fetch data on page load
    </script>
</head>
<body>
    <h1>HawkFi Pool Metrics Dashboard</h1>
    <button onclick="refreshData()">Refresh Data</button>
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Total Value Locked (TVL)</th>
                <th>Fees</th>
                <th>Balance</th>
            </tr>
        </thead>
        <tbody id="pool-data">
            <!-- Pool data will be populated here -->
        </tbody>
    </table>
</body>
</html>
```

**Note**: Ensure you have Flask and Pandas installed in your environment. You can install them using:
```bash
pip install Flask pandas requests
```
