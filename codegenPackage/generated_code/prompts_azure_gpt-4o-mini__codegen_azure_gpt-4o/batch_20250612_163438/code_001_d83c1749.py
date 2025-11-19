"""
Generated Code Metadata:
========================
Original URL: https://haciendodestinos.com
Prompt: Write a code snippet for an API that analyzes tourism data to identify potential growth areas in Argentina, inspired by the insights from Haciendo Destinos.
Generated: DETERMINISTIC_d83c1749f481e113
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# Mock data for demonstration purposes
# In production, this would be replaced with a database or external data source
TOURISM_DATA = pd.DataFrame({
    'region': ['Buenos Aires', 'Patagonia', 'Cuyo', 'Northwest', 'Northeast'],
    'visitor_count': [500000, 300000, 200000, 150000, 100000],
    'average_spend_per_visitor': [1000, 1200, 800, 700, 600],
    'infrastructure_score': [8.5, 7.0, 6.5, 5.0, 4.5],
    'growth_potential_score': [7.5, 8.0, 6.0, 7.0, 5.5]
})

@app.route('/analyze-tourism', methods=['POST'])
def analyze_tourism():
    """
    API endpoint to analyze tourism data and identify potential growth areas in Argentina.
    Accepts optional filters via JSON payload.
    """
    try:
        # Parse request payload
        filters = request.json if request.is_json else {}
        
        # Apply filters if provided
        filtered_data = TOURISM_DATA.copy()
        if 'min_visitor_count' in filters:
            filtered_data = filtered_data[filtered_data['visitor_count'] >= filters['min_visitor_count']]
        if 'min_infrastructure_score' in filters:
            filtered_data = filtered_data[filtered_data['infrastructure_score'] >= filters['min_infrastructure_score']]
        
        # Calculate growth potential based on weighted factors
        filtered_data['growth_index'] = (
            filtered_data['growth_potential_score'] * 0.5 +
            filtered_data['infrastructure_score'] * 0.3 +
            (filtered_data['average_spend_per_visitor'] / 1000) * 0.2
        )
        
        # Sort by growth index in descending order
        sorted_data = filtered_data.sort_values(by='growth_index', ascending=False)
        
        # Convert to JSON-friendly format
        result = sorted_data[['region', 'growth_index']].to_dict(orient='records')
        
        return jsonify({
            'status': 'success',
            'data': result
        }), 200
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
