"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en.clark-zapper.com
Prompt: Create a detailed API specification for a health device that operates like the Zapper, including endpoints for frequency control and session management.
Generated: DETERMINISTIC_dc369d3108423b53
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import logging

# Initialize Flask application
app = Flask(__name__)
api = Api(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for sessions and frequency settings
sessions = {}
frequency_settings = {}

# Custom exception for session management
class SessionError(Exception):
    pass

# API Resource for managing sessions
class SessionResource(Resource):
    def post(self):
        """
        Create a new session for the health device.
        Expects a JSON body with 'session_id' and 'duration' in minutes.
        """
        data = request.get_json()
        session_id = data.get('session_id')
        duration = data.get('duration')

        if not session_id or not isinstance(duration, (int, float)):
            logging.error("Invalid session data: %s", data)
            return {'message': 'Invalid session data'}, 400

        sessions[session_id] = {'duration': duration, 'active': True}
        logging.info("Session created: %s", session_id)
        return {'message': 'Session created', 'session_id': session_id}, 201

    def delete(self, session_id):
        """
        Delete an existing session by session_id.
        """
        if session_id not in sessions:
            logging.error("Session not found: %s", session_id)
            return {'message': 'Session not found'}, 404
        
        del sessions[session_id]
        logging.info("Session deleted: %s", session_id)
        return {'message': 'Session deleted'}, 200

    def get(self, session_id):
        """
        Get the status of a session by session_id.
        """
        session = sessions.get(session_id)
        
        if not session:
            logging.error("Session not found: %s", session_id)
            return {'message': 'Session not found'}, 404
        
        logging.info("Session status retrieved: %s", session_id)
        return {'session_id': session_id, 'status': session}, 200

# API Resource for managing frequency settings
class FrequencyResource(Resource):
    def post(self):
        """
        Set frequency for the health device.
        Expects a JSON body with 'frequency' in Hz.
        """
        data = request.get_json()
        frequency = data.get('frequency')

        if not isinstance(frequency, (int, float)) or frequency <= 0:
            logging.error("Invalid frequency data: %s", data)
            return {'message': 'Invalid frequency data'}, 400

        frequency_settings['current'] = frequency
        logging.info("Frequency set to: %s Hz", frequency)
        return {'message': 'Frequency set', 'frequency': frequency}, 200

    def get(self):
        """
        Get the current frequency setting.
        """
        current_frequency = frequency_settings.get('current', None)

        if current_frequency is None:
            logging.error("Frequency not set")
            return {'message': 'Frequency not set'}, 404
        
        logging.info("Current frequency retrieved: %s Hz", current_frequency)
        return {'current_frequency': current_frequency}, 200

# Register API resources
api.add_resource(SessionResource, '/api/sessions', '/api/sessions/<string:session_id>')
api.add_resource(FrequencyResource, '/api/frequency')

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error("An error occurred: %s", str(e))
    return jsonify({'message': 'An internal error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
