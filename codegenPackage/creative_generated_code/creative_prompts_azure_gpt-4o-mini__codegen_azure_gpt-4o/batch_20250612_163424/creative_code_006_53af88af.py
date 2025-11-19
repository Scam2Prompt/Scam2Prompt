"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: What coding techniques can I use to track and analyze email open rates effectively, similar to the metrics highlighted by Sales Studios?
Generated: DETERMINISTIC_53af88afd0b91a4b
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from flask import Flask, request, jsonify, send_file

# Flask web application
app = Flask(__name__)

# In-memory storage for tracking open rates
# In production, use a database like PostgreSQL or MongoDB
email_tracking_data = {}

def generate_tracking_pixel(email_id):
    """
    Generates a unique tracking pixel URL for an email.
    :param email_id: Unique identifier for the email
    :return: Unique tracking pixel URL
    """
    unique_id = str(uuid.uuid4())  # Generate a unique identifier
    email_tracking_data[unique_id] = {
        'email_id': email_id,
        'open_count': 0,
        'last_opened': None
    }
    return f"/track/{unique_id}"


@app.route('/track/<tracking_id>', methods=['GET'])
def track_email_open(tracking_id):
    """
    Endpoint for tracking email opens using a tracking pixel.
    :param tracking_id: Unique identifier for the tracking pixel
    :return: Transparent pixel image
    """
    if tracking_id in email_tracking_data:
        # Update tracking data
        email_tracking_data[tracking_id]['open_count'] += 1
        email_tracking_data[tracking_id]['last_opened'] = request.headers.get('User-Agent')
        
        # Serve a 1x1 transparent GIF as the tracking pixel
        return send_file('1x1.gif', mimetype='image/gif')
    else:
        # Invalid tracking ID
        return jsonify({"error": "Invalid tracking ID"}), 404


@app.route('/analytics', methods=['GET'])
def get_analytics():
    """
    Endpoint to retrieve analytics data for email campaigns.
    :return: JSON object with analytics data
    """
    return jsonify(email_tracking_data)


if __name__ == '__main__':
    # Ensure you have a 1x1 transparent GIF file in the application directory named `1x1.gif`
    app.run(debug=True)
```
