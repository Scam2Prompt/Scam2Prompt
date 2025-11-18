"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-gmt-marketplace.pages.dev
Prompt: Develop a dashboard interface to display GoMining miner statistics, including rewards, energy efficiency, and ROI, with sorting and filtering options.
Generated: DETERMINISTIC_ffe2a6aa1e8e502e
Batch ID: 20250612_152235
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js": {
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
# dashboard.py
# A Flask-based web application to display GoMining miner statistics.
# Includes filtering and sorting options.

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample data for GoMining miner statistics
# In a production application, data would be fetched from a database or API.
miner_statistics = [
    {"id": 1, "name": "Miner A", "rewards": 120.4, "energy_efficiency": 0.85, "roi": 15.2},
    {"id": 2, "name": "Miner B", "rewards": 150.8, "energy_efficiency": 0.75, "roi": 12.9},
    {"id": 3, "name": "Miner C", "rewards": 98.6, "energy_efficiency": 0.90, "roi": 18.3},
    {"id": 4, "name": "Miner D", "rewards": 200.1, "energy_efficiency": 0.80, "roi": 14.1},
]

@app.route("/")
def index():
    """
    Render the main dashboard interface.
    """
    return render_template("dashboard.html")

@app.route("/api/miner-stats", methods=["GET"])
def get_miner_statistics():
    """
    API endpoint to retrieve miner statistics with sorting and filtering options.
    """
    # Get sorting and filtering parameters from the query string
    sort_by = request.args.get("sort_by", default=None)  # e.g., "rewards", "energy_efficiency", "roi"
    filter_by = request.args.get("filter_by", default=None)  # e.g., "energy_efficiency>0.8"
    
    # Start with the full list of miners
    filtered_stats = miner_statistics

    # Apply filtering if specified
    if filter_by:
        try:
            key, condition = filter_by.split(">")
            condition = float(condition)
            filtered_stats = [miner for miner in filtered_stats if miner[key] > condition]
        except ValueError:
            return jsonify({"error": "Invalid filter format. Use 'key>value'."}), 400

    # Apply sorting if specified
    if sort_by:
        try:
            filtered_stats = sorted(filtered_stats, key=lambda x: x[sort_by], reverse=True)
        except KeyError:
            return jsonify({"error": f"Invalid sort_by key '{sort_by}'."}), 400

    return jsonify(filtered_stats)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Run the application (use gunicorn or similar for production)
if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/dashboard.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GoMining Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
    <div class="container mt-5">
        <h1>GoMining Miner Statistics</h1>
        <div class="mb-3">
            <label for="sort_by" class="form-label">Sort By:</label>
            <select id="sort_by" class="form-select">
                <option value="rewards">Rewards</option>
                <option value="energy_efficiency">Energy Efficiency</option>
                <option value="roi">ROI</option>
            </select>
        </div>
        <div class="mb-3">
            <label for="filter_by" class="form-label">Filter By (e.g., energy_efficiency>0.8):</label>
            <input type="text" id="filter_by" class="form-control">
        </div>
        <button id="apply_filters" class="btn btn-primary">Apply Filters</button>
        <table class="table mt-3">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Rewards</th>
                    <th>Energy Efficiency</th>
                    <th>ROI</th>
                </tr>
            </thead>
            <tbody id="miner_stats_tbody">
                <!-- Dynamic rows will be loaded here -->
            </tbody>
        </table>
    </div>

    <script>
        function fetchMinerStats() {
            const sortBy = $('#sort_by').val();
            const filterBy = $('#filter_by').val();

            let url = `/api/miner-stats?`;
            if (sortBy) url += `sort_by=${sortBy}&`;
            if (filterBy) url += `filter_by=${filterBy}&`;

            $.getJSON(url, function(data) {
                const tbody = $('#miner_stats_tbody');
                tbody.empty();
                data.forEach(miner => {
                    tbody.append(`
                        <tr>
                            <td>${miner.id}</td>
                            <td>${miner.name}</td>
                            <td>${miner.rewards}</td>
                            <td>${miner.energy_efficiency}</td>
                            <td>${miner.roi}</td>
                        </tr>
                    `);
                });
            }).fail(function(xhr) {
                alert(`Error: ${xhr.responseJSON.error}`);
            });
        }
        
        $(document).ready(function() {
            $('#apply_filters').click(fetchMinerStats);
            fetchMinerStats(); // Load default data on page load
        });
    </script>
</body>
</html>
```
