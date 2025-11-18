"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stader.pages.dev
Prompt: Develop a dashboard using Dune Analytics to visualize the decentralization stats of ETHx, including the total node operators and node operator bond.
Generated: DETERMINISTIC_4db6662c1eabd3a2
Batch ID: 20250612_151158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dune.com/api/v1": {
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
"""
Script to generate a dashboard using Dune Analytics API to visualize decentralization stats of ETHx,
including the total node operators and node operator bond.

This example assumes that the Dune Analytics API is accessible and you have valid credentials
to interact with it. You'll need to replace placeholders with your own API keys and query IDs.
"""

import requests
import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Constants for Dune Analytics API
DUNE_API_BASE_URL = "https://api.dune.com/api/v1"
DUNE_API_KEY = "your_api_key_here"  # Replace with your Dune API key
TOTAL_NODE_OPERATORS_QUERY_ID = "query_id_for_total_node_operators"  # Replace with the query ID
NODE_OPERATOR_BOND_QUERY_ID = "query_id_for_node_operator_bond"  # Replace with the query ID

# Function to execute a query on Dune Analytics
def execute_dune_query(query_id):
    """
    Executes a Dune Analytics query and returns the results.
    :param query_id: The ID of the Dune Analytics query to execute.
    :return: Parsed JSON response containing the query results.
    """
    url = f"{DUNE_API_BASE_URL}/query/{query_id}/results"
    headers = {"Authorization": f"Bearer {DUNE_API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Dune Analytics API: {e}")
        return None

# Fetch decentralization stats
def fetch_dec_stats():
    """
    Fetches decentralization stats from Dune Analytics using predefined queries.
    :return: A dictionary containing the stats.
    """
    total_node_operators_data = execute_dune_query(TOTAL_NODE_OPERATORS_QUERY_ID)
    node_operator_bond_data = execute_dune_query(NODE_OPERATOR_BOND_QUERY_ID)

    if not total_node_operators_data or not node_operator_bond_data:
        return {"error": "Failed to fetch data from Dune Analytics"}

    try:
        total_node_operators = total_node_operators_data["data"]["result"]["rows"][0]["total_node_operators"]
        node_operator_bond = node_operator_bond_data["data"]["result"]["rows"][0]["node_operator_bond"]

        return {
            "total_node_operators": total_node_operators,
            "node_operator_bond": node_operator_bond
        }
    except (KeyError, IndexError) as e:
        print(f"Error parsing response data: {e}")
        return {"error": "Failed to parse response data"}

@app.route("/")
def dashboard():
    """
    Dashboard endpoint to render decentralization data for ETHx.
    """
    stats = fetch_dec_stats()

    if "error" in stats:
        return render_template("error.html", error=stats["error"])
    return render_template("dashboard.html", stats=stats)

@app.route("/api/stats")
def api_stats():
    """
    API endpoint to fetch decentralization stats in JSON format.
    """
    stats = fetch_dec_stats()
    return jsonify(stats)

if __name__ == "__main__":
    """
    Start the Flask application.
    """
    app.run(debug=True)

"""
HTML Templates:

1. Create a `templates` folder in the same directory as this script.
2. Add `dashboard.html` and `error.html` files inside the `templates` folder.

Example `dashboard.html`:
--------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ETHx Decentralization Dashboard</title>
</head>
<body>
    <h1>ETHx Decentralization Stats</h1>
    <p>Total Node Operators: {{ stats["total_node_operators"] }}</p>
    <p>Node Operator Bond: {{ stats["node_operator_bond"] }}</p>
</body>
</html>

Example `error.html`:
----------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>
"""
```
