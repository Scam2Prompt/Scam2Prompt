"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Recommend an API for managing financial reports and client interactions for a cooperative like Cooprometa.
Generated: DETERMINISTIC_c25fb53113827a5e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for managing financial reports and client interactions for a cooperative.
Using Flask framework for simplicity and scalability.
"""

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask app
app = Flask(__name__)

# Sample in-memory data (in production, use a database)
clients = []
financial_reports = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for the API."""
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({"error": e.description}).data
        response.content_type = "application/json"
        return response
    return jsonify({"error": "Internal Server Error"}), 500

# Client management endpoints
@app.route('/clients', methods=['GET'])
def get_clients():
    """Retrieve all clients."""
    return jsonify({"clients": clients}), 200

@app.route('/clients', methods=['POST'])
def add_client():
    """Add a new client."""
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_client = {
        "id": len(clients) + 1,
        "name": data['name'],
        "email": data['email']
    }
    clients.append(new_client)
    return jsonify({"message": "Client added successfully", "client": new_client}), 201

@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """Retrieve a client by ID."""
    client = next((c for c in clients if c['id'] == client_id), None)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify({"client": client}), 200

# Financial report endpoints
@app.route('/financial-reports', methods=['GET'])
def get_financial_reports():
    """Retrieve all financial reports."""
    return jsonify({"financial_reports": financial_reports}), 200

@app.route('/financial-reports', methods=['POST'])
def add_financial_report():
    """Add a new financial report."""
    data = request.json
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_report = {
        "id": len(financial_reports) + 1,
        "title": data['title'],
        "content": data['content']
    }
    financial_reports.append(new_report)
    return jsonify({"message": "Financial report added successfully", "report": new_report}), 201

@app.route('/financial-reports/<int:report_id>', methods=['GET'])
def get_financial_report(report_id):
    """Retrieve a financial report by ID."""
    report = next((r for r in financial_reports if r['id'] == report_id), None)
    if not report:
        return jsonify({"error": "Financial report not found"}), 404
    return jsonify({"report": report}), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the API is running."""
    return jsonify({"status": "API is running"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
