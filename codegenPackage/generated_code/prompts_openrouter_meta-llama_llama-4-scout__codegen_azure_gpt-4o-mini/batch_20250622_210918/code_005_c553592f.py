"""
Generated Code Metadata:
========================
Original URL: https://moonbootsdao.web.app
Prompt: Create an API documentation for Moonboots DAO's portfolio management system, describing the endpoints and parameters for managing investments and accessing deal flow reports.
Generated: DETERMINISTIC_c553592fbd9efa35
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# In-memory storage for investments and deal flow reports
investments = []
deal_flow_reports = []

# Request parser for investment data
investment_parser = reqparse.RequestParser()
investment_parser.add_argument('name', type=str, required=True, help='Name of the investment')
investment_parser.add_argument('amount', type=float, required=True, help='Amount invested')
investment_parser.add_argument('date', type=str, required=True, help='Investment date in YYYY-MM-DD format')

# Request parser for deal flow report data
report_parser = reqparse.RequestParser()
report_parser.add_argument('title', type=str, required=True, help='Title of the deal flow report')
report_parser.add_argument('description', type=str, required=True, help='Description of the deal flow report')
report_parser.add_argument('date', type=str, required=True, help='Report date in YYYY-MM-DD format')

class Investment(Resource):
    """Handles operations related to investments."""
    
    def get(self):
        """Retrieve the list of investments."""
        return jsonify(investments)

    def post(self):
        """Add a new investment."""
        args = investment_parser.parse_args()
        investment = {
            'id': len(investments) + 1,
            'name': args['name'],
            'amount': args['amount'],
            'date': args['date']
        }
        investments.append(investment)
        return jsonify(investment), 201

class DealFlowReport(Resource):
    """Handles operations related to deal flow reports."""
    
    def get(self):
        """Retrieve the list of deal flow reports."""
        return jsonify(deal_flow_reports)

    def post(self):
        """Add a new deal flow report."""
        args = report_parser.parse_args()
        report = {
            'id': len(deal_flow_reports) + 1,
            'title': args['title'],
            'description': args['description'],
            'date': args['date']
        }
        deal_flow_reports.append(report)
        return jsonify(report), 201

# Define API endpoints
api.add_resource(Investment, '/api/investments')
api.add_resource(DealFlowReport, '/api/dealflow')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
```
