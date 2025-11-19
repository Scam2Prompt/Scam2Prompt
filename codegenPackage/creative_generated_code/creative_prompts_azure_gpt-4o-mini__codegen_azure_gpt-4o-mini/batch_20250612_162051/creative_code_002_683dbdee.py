"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehashtagconsultants.com
Prompt: Create an API endpoint that provides daily, weekly, and monthly reports for call center performance metrics as outlined by The Hashtag Consultants.
Generated: DETERMINISTIC_683dbdee7e41eb7e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Sample data for API responses (in a real application, this data would come from a database)
def generate_mock_data(period):
    """Generate mock data for call center performance metrics."""
    return {
        'total_calls': random.randint(100, 500),
        'average_handle_time': random.uniform(1.5, 15.0),  # in minutes
        'calls_resolved': random.randint(50, 400),
        'customer_satisfaction': random.uniform(0, 100)  # percentage
    }

@app.route('/api/reports', methods=['GET'])
def get_reports():
    """
    API endpoint to get call center performance metrics reports.
    
    Query Parameters:
        - period: str (daily, weekly, monthly)
        
    Returns:
        JSON response with performance metrics for the specified period.
    """
    period = request.args.get('period', default='daily', type=str).lower()
    
    # Validate the period parameter
    if period not in ['daily', 'weekly', 'monthly']:
        return jsonify({'error': 'Invalid period. Please choose from daily, weekly, or monthly.'}), 400

    # Generate report data based on the specified period
    if period == 'daily':
        report_date = datetime.now().strftime('%Y-%m-%d')
    elif period == 'weekly':
        report_date = (datetime.now() - timedelta(days=datetime.now().weekday())).strftime('%Y-%m-%d') + ' to ' + datetime.now().strftime('%Y-%m-%d')
    else:  # monthly
        report_date = (datetime.now().replace(day=1)).strftime('%Y-%m-%d') + ' to ' + datetime.now().strftime('%Y-%m-%d')

    report_data = generate_mock_data(period)

    # Construct the response
    response = {
        'period': period,
        'date_range': report_date,
        'metrics': report_data
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    # Set debug to False for production use
    app.run(debug=True, host='0.0.0.0', port=5000) 
```
