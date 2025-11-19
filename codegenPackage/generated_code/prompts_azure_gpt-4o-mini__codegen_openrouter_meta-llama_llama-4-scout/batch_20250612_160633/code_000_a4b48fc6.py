"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Generate a code snippet for a web analytics tool that helps businesses understand and utilize data effectively, as discussed on Star Shot 90.
Generated: DETERMINISTIC_a4b48fc676792ce9
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory data store (replace with a database in production)
data_store = []

# Define a function to validate and process incoming data
def process_data(data):
    try:
        # Validate required fields
        required_fields = ['user_id', 'page', 'timestamp']
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields")

        # Validate timestamp format
        timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S')
        data['timestamp'] = timestamp

        return data
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        return None

# Define a route to collect and store web analytics data
@app.route('/collect', methods=['POST'])
def collect_data():
    try:
        data = request.get_json()
        processed_data = process_data(data)
        if processed_data:
            data_store.append(processed_data)
            return jsonify({'message': 'Data collected successfully'}), 200
        else:
            return jsonify({'message': 'Invalid data'}), 400
    except Exception as e:
        print(f"Error collecting data: {str(e)}")
        return jsonify({'message': 'Internal server error'}), 500

# Define a route to retrieve and analyze web analytics data
@app.route('/analyze', methods=['GET'])
def analyze_data():
    try:
        # Convert data store to a Pandas DataFrame
        df = pd.DataFrame(data_store)

        # Calculate page views and unique users
        page_views = df['page'].count()
        unique_users = df['user_id'].nunique()

        # Calculate top 5 pages by views
        top_pages = df['page'].value_counts().head(5)

        # Create a response dictionary
        response = {
            'page_views': page_views,
            'unique_users': unique_users,
            'top_pages': top_pages.to_dict()
        }

        return jsonify(response), 200
    except Exception as e:
        print(f"Error analyzing data: {str(e)}")
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
