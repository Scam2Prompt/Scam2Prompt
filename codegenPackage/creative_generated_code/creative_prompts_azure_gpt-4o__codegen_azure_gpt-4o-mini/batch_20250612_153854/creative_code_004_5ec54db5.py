"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Suggest tools or frameworks for building a fintech solution that supports private equity investment lifecycle management, inspired by Alghanim Capital's expertise in this domain.
Generated: DETERMINISTIC_5ec54db5ef0e5187
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a FinTech solution
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import logging

# Initialize logging for error tracking
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# Database configuration (replace with your own configurations)
DATABASE_URI = 'sqlite:///fintech.db'  # Change to your actual database URI
engine = create_engine(DATABASE_URI)

# Initialize DataFrame for private equity investments
investments_df = pd.DataFrame(columns=['investment_id', 'amount', 'date', 'fund', 'status'])

@app.route('/add_investment', methods=['POST'])
def add_investment():
    """
    Add a new investment to the investments DataFrame.
    Expects JSON data with investment details.
    """
    try:
        data = request.json
        investment_id = data['investment_id']
        amount = data['amount']
        date = data['date']
        fund = data['fund']
        status = data['status']

        # Create a new investment record
        global investments_df
        investments_df = investments_df.append({
            'investment_id': investment_id,
            'amount': amount,
            'date': date,
            'fund': fund,
            'status': status
        }, ignore_index=True)

        return jsonify({"message": "Investment added successfully!"}), 201

    except KeyError as e:
        logging.error(f"KeyError: Missing key in request data: {e}")
        return jsonify({"error": "Missing key in request data"}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/list_investments', methods=['GET'])
def list_investments():
    """
    Retrieve a list of all investments.
    """
    try:
        return jsonify(investments_df.to_dict(orient='records')), 200
    except Exception as e:
        logging.error(f"Unexpected error while listing investments: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/delete_investment/<investment_id>', methods=['DELETE'])
def delete_investment(investment_id):
    """
    Delete an investment by investment_id.
    """
    try:
        global investments_df
        investments_df = investments_df[investments_df['investment_id'] != investment_id]
        return jsonify({"message": "Investment deleted successfully!"}), 200
    except Exception as e:
        logging.error(f"Unexpected error while deleting investment: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Start the Flask web server
    app.run(debug=True)
```
