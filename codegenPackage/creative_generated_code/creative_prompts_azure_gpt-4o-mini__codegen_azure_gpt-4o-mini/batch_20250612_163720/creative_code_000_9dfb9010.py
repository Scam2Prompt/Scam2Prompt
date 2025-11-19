"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binairop.com
Prompt: How can I implement a shared IP configuration for multiple domains in my web application?
Generated: DETERMINISTIC_9dfb901005e90d5f
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration for shared IPs
SHARED_IPS = {
    'domain1.com': '192.168.1.1',
    'domain2.com': '192.168.1.1',
    'domain3.com': '192.168.1.2',
}

@app.route('/get_ip', methods=['GET'])
def get_ip():
    """
    Retrieve the shared IP configuration based on the request domain.

    Returns:
        JSON response with the domain and its corresponding IP address.
    """
    # Get the host from the request
    host = request.host.split(':')[0]  # Handle port if present
    
    # Check if the domain exists in shared IPs
    if host in SHARED_IPS:
        ip_address = SHARED_IPS[host]
        return jsonify({'domain': host, 'ip_address': ip_address}), 200
    else:
        # Handle the case where the domain is not found
        return jsonify({'error': 'Domain not found'}), 404

if __name__ == '__main__':
    try:
        # Running the Flask application
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        # Catch and log any exceptions during application startup
        print(f"An error occurred while starting the server: {e}")
```
