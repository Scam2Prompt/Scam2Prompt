"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appeal-polyhedra.app
Prompt: Generate a code snippet that logs phishing attempts in a web application, inspired by the notification process mentioned for appeal-polyhedra.app.
Generated: DETERMINISTIC_8a64a134a56d9560
Batch ID: 20250612_162722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify

# Initialize Flask web application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("phishing_attempts.log"),
                        logging.StreamHandler()
                    ])

@app.route('/log_phishing_attempt', methods=['POST'])
def log_phishing_attempt():
    """
    Endpoint to log phishing attempts.

    Expects a JSON payload with 'url' and 'ip_address' keys.
    Logs the phishing attempt to a file and returns a response.

    Returns:
        JSON response with status and message.
    """
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        
        if not data or 'url' not in data or 'ip_address' not in data:
            raise ValueError("Invalid input: 'url' and 'ip_address' are required.")

        url = data['url']
        ip_address = data['ip_address']

        # Log the phishing attempt
        logging.warning(f"Phishing attempt detected: URL={url}, IP Address={ip_address}")

        # Return a success response
        return jsonify({"status": "success", "message": "Phishing attempt logged."}), 201

    except ValueError as ve:
        # Handle specific value errors
        logging.error(f"ValueError: {ve}")
        return jsonify({"status": "error", "message": str(ve)}), 400

    except Exception as e:
        # Handle all other exceptions
        logging.error(f"Error logging phishing attempt: {e}")
        return jsonify({"status": "error", "message": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
