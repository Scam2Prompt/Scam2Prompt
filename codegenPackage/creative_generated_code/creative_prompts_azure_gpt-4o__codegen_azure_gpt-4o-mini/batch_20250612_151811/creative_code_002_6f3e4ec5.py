"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-live.org
Prompt: Generate code to configure a branded streaming platform with custom RTMP endpoints, white-label solutions, and advanced analytics for enterprise-grade live streaming.
Generated: DETERMINISTIC_6f3e4ec51fe07396
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///streaming_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for RTMP endpoints
class RTMPEndpoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<RTMPEndpoint {self.name} at {self.url}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/rtmp-endpoints', methods=['POST'])
def create_rtmp_endpoint():
    """
    Create a new RTMP endpoint.
    Expects JSON data with 'name' and 'url'.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'url' not in data:
            raise BadRequest("Missing 'name' or 'url' in request data")
        
        new_endpoint = RTMPEndpoint(name=data['name'], url=data['url'])
        db.session.add(new_endpoint)
        db.session.commit()
        
        logging.info(f'Created RTMP endpoint: {new_endpoint}')
        return jsonify({'id': new_endpoint.id, 'name': new_endpoint.name, 'url': new_endpoint.url}), 201
        
    except BadRequest as e:
        logging.error(f'BadRequest: {str(e)}')
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error(f'Error creating RTMP endpoint: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/rtmp-endpoints', methods=['GET'])
def get_rtmp_endpoints():
    """
    Retrieve all RTMP endpoints.
    """
    try:
        endpoints = RTMPEndpoint.query.all()
        return jsonify([{'id': ep.id, 'name': ep.name, 'url': ep.url} for ep in endpoints]), 200
    except Exception as e:
        logging.error(f'Error retrieving RTMP endpoints: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/analytics', methods=['POST'])
def track_analytics():
    """
    Track analytics for a live stream.
    Expects JSON data with 'endpoint_id', 'viewer_count', and 'duration'.
    """
    try:
        data = request.get_json()
        if not data or 'endpoint_id' not in data or 'viewer_count' not in data or 'duration' not in data:
            raise BadRequest("Missing 'endpoint_id', 'viewer_count', or 'duration' in request data")

        # Here you would typically save the analytics data to a database
        logging.info(f'Tracked analytics for endpoint {data["endpoint_id"]}: {data["viewer_count"]} viewers for {data["duration"]} seconds.')
        
        return jsonify({'status': 'success', 'message': 'Analytics tracked successfully.'}), 200
        
    except BadRequest as e:
        logging.error(f'BadRequest: {str(e)}')
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error(f'Error tracking analytics: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

# Main entry point of the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```
