"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: "Design an API for a business accelerator platform that connects early-stage technology-enabled companies with investors and financial advisors in Africa, including API documentation and sandbox testing."
Generated: DETERMINISTIC_d074d096ab260fc8
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database simulation
companies = []
investors = []
financial_advisors = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# API Documentation
@app.route('/api/docs', methods=['GET'])
def api_docs():
    """
    API Documentation Endpoint
    Returns a JSON object describing the available endpoints.
    """
    docs = {
        "endpoints": {
            "/api/companies": {
                "GET": "List all companies",
                "POST": "Add a new company"
            },
            "/api/investors": {
                "GET": "List all investors",
                "POST": "Add a new investor"
            },
            "/api/financial-advisors": {
                "GET": "List all financial advisors",
                "POST": "Add a new financial advisor"
            },
            "/api/docs": {
                "GET": "Get API documentation"
            }
        }
    }
    return jsonify(docs)

# Companies Endpoints
@app.route('/api/companies', methods=['GET', 'POST'])
def manage_companies():
    """
    GET: Retrieve all companies
    POST: Add a new company
    """
    if request.method == 'GET':
        return jsonify(companies)
    elif request.method == 'POST':
        data = request.json
        if not data or 'name' not in data or 'sector' not in data:
            return jsonify({"error": "Invalid data"}), 400
        company = {
            "id": len(companies) + 1,
            "name": data['name'],
            "sector": data['sector'],
            "location": data.get('location', 'Unknown')
        }
        companies.append(company)
        return jsonify(company), 201

# Investors Endpoints
@app.route('/api/investors', methods=['GET', 'POST'])
def manage_investors():
    """
    GET: Retrieve all investors
    POST: Add a new investor
    """
    if request.method == 'GET':
        return jsonify(investors)
    elif request.method == 'POST':
        data = request.json
        if not data or 'name' not in data or 'investment_focus' not in data:
            return jsonify({"error": "Invalid data"}), 400
        investor = {
            "id": len(investors) + 1,
            "name": data['name'],
            "investment_focus": data['investment_focus'],
            "location": data.get('location', 'Unknown')
        }
        investors.append(investor)
        return jsonify(investor), 201

# Financial Advisors Endpoints
@app.route('/api/financial-advisors', methods=['GET', 'POST'])
def manage_financial_advisors():
    """
    GET: Retrieve all financial advisors
    POST: Add a new financial advisor
    """
    if request.method == 'GET':
        return jsonify(financial_advisors)
    elif request.method == 'POST':
        data = request.json
        if not data or 'name' not in data or 'expertise' not in data:
            return jsonify({"error": "Invalid data"}), 400
        advisor = {
            "id": len(financial_advisors) + 1,
            "name": data['name'],
            "expertise": data['expertise'],
            "location": data.get('location', 'Unknown')
        }
        financial_advisors.append(advisor)
        return jsonify(advisor), 201

# Sandbox Testing Endpoint
@app.route('/api/sandbox', methods=['POST'])
def sandbox_testing():
    """
    POST: Simulate API interactions for testing purposes
    """
    data = request.json
    if not data or 'test_case' not in data:
        return jsonify({"error": "Invalid data"}), 400
    test_case = data['test_case']
    if test_case == "add_company":
        return jsonify({"message": "Company added successfully in sandbox"}), 200
    elif test_case == "add_investor":
        return jsonify({"message": "Investor added successfully in sandbox"}), 200
    elif test_case == "add_financial_advisor":
        return jsonify({"message": "Financial advisor added successfully in sandbox"}), 200
    else:
        return jsonify({"error": "Unknown test case"}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
