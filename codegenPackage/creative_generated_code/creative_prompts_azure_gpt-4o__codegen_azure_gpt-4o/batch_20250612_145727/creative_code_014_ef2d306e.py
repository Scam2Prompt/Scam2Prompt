"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlinelender.online
Prompt: "Develop a dashboard to visualize loan offers from onlinelender.online, including filters for age and loan amount requirements."
Generated: DETERMINISTIC_ef2d306edaaff72f
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import pandas as pd
import random

# Initialize Flask app
app = Flask(__name__)

# Mock data for loan offers (In production, replace with actual data source).
loan_offers = [
    {"id": 1, "lender": "Lender A", "age_min": 21, "age_max": 60, "loan_min": 5000, "loan_max": 50000, "rate": 5.5},
    {"id": 2, "lender": "Lender B", "age_min": 25, "age_max": 65, "loan_min": 10000, "loan_max": 100000, "rate": 4.8},
    {"id": 3, "lender": "Lender C", "age_min": 18, "age_max": 50, "loan_min": 2000, "loan_max": 20000, "rate": 6.2},
    # Add more mock data as needed
]

# Route to render the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')  # Render the HTML dashboard page

# API endpoint to filter and return loan offers
@app.route('/api/filter-loans', methods=['POST'])
def filter_loans():
    try:
        # Parse filter parameters from request
        data = request.json
        age = data.get('age', None)
        loan_amount = data.get('loan_amount', None)

        # Validate inputs
        if age is None or loan_amount is None:
            return jsonify({"error": "Age and loan amount are required"}), 400

        # Convert to integer for comparison, with error handling
        try:
            age = int(age)
            loan_amount = float(loan_amount)
        except ValueError:
            return jsonify({"error": "Invalid age or loan amount format"}), 400

        # Filter loan offers based on criteria
        filtered_offers = [
            offer for offer in loan_offers
            if offer['age_min'] <= age <= offer['age_max'] and offer['loan_min'] <= loan_amount <= offer['loan_max']
        ]

        # Return filtered offers
        return jsonify(filtered_offers)

    except Exception as e:
        # Return error response in case of any exception
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# HTML template for dashboard (embedded here for simplicity)
dashboard_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Loan Offers Dashboard</title>
    <script>
        async function filterLoans() {
            const age = document.getElementById('age').value;
            const loanAmount = document.getElementById('loan_amount').value;
            const response = await fetch('/api/filter-loans', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ age, loan_amount: loanAmount })
            });
            const results = await response.json();
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            if (response.ok) {
                results.forEach(offer => {
                    const div = document.createElement('div');
                    div.innerHTML = `Lender: ${offer.lender}, Rate: ${offer.rate}%, Amount Range: ${offer.loan_min} - ${offer.loan_max}`;
                    resultsDiv.appendChild(div);
                });
            } else {
                resultsDiv.innerHTML = `Error: ${results.error}`;
            }
        }
    </script>
</head>
<body>
    <h1>Loan Offers Dashboard</h1>
    <label for="age">Age:</label>
    <input type="number" id="age" name="age">
    <label for="loan_amount">Loan Amount:</label>
    <input type="number" id="loan_amount" name="loan_amount">
    <button onclick="filterLoans()">Filter</button>
    <div id="results"></div>
</body>
</html>
"""

# Serve the embedded HTML as a template
@app.route('/dashboard.html')
def serve_dashboard_html():
    return dashboard_html

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
