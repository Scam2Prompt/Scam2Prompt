"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Design an API for integrating agricultural data from various sources, including mobile apps and web platforms, for analytics and reporting, like Azagros.
Generated: DETERMINISTIC_daced5d6dc712740
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory storage for agricultural data (replace with a database in production)
agricultural_data = []

# Error messages
ERROR_INVALID_DATA = "Invalid data format. Please provide valid JSON."
ERROR_SOURCE_NOT_FOUND = "Source not found."

# API Endpoints

@app.route('/api/data', methods=['POST'])
def add_data():
    """
    Endpoint to add agricultural data from various sources.
    Expects JSON payload with 'source', 'data', and 'timestamp'.
    """
    try:
        # Parse JSON payload
        payload = request.get_json()
        if not payload or 'source' not in payload or 'data' not in payload or 'timestamp' not in payload:
            return jsonify({'error': ERROR_INVALID_DATA}), 400
        
        # Add data to in-memory storage
        agricultural_data.append(payload)
        logging.info(f"Data added from source: {payload['source']}")
        return jsonify({'message': 'Data added successfully'}), 201
    except Exception as e:
        logging.error(f"Error adding data: {str(e)}")
        return jsonify({'error': 'An error occurred while adding data'}), 500

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    Endpoint to retrieve all agricultural data.
    """
    try:
        return jsonify({'data': agricultural_data}), 200
    except Exception as e:
        logging.error(f"Error retrieving data: {str(e)}")
        return jsonify({'error': 'An error occurred while retrieving data'}), 500

@app.route('/api/data/<source>', methods=['GET'])
def get_data_by_source(source):
    """
    Endpoint to retrieve agricultural data by source.
    """
    try:
        # Filter data by source
        filtered_data = [entry for entry in agricultural_data if entry['source'] == source]
        if not filtered_data:
            return jsonify({'error': ERROR_SOURCE_NOT_FOUND}), 404
        
        return jsonify({'data': filtered_data}), 200
    except Exception as e:
        logging.error(f"Error retrieving data for source {source}: {str(e)}")
        return jsonify({'error': 'An error occurred while retrieving data'}), 500

@app.route('/api/data/<source>', methods=['DELETE'])
def delete_data_by_source(source):
    """
    Endpoint to delete agricultural data by source.
    """
    try:
        global agricultural_data
        # Filter out data from the specified source
        original_length = len(agricultural_data)
        agricultural_data = [entry for entry in agricultural_data if entry['source'] != source]
        
        if len(agricultural_data) == original_length:
            return jsonify({'error': ERROR_SOURCE_NOT_FOUND}), 404
        
        logging.info(f"Data deleted for source: {source}")
        return jsonify({'message': f'Data deleted for source: {source}'}), 200
    except Exception as e:
        logging.error(f"Error deleting data for source {source}: {str(e)}")
        return jsonify({'error': 'An error occurred while deleting data'}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Endpoint to check the health of the API.
    """
    return jsonify({'status': 'API is running'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
