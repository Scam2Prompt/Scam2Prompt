"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendainforma.zya.me
Prompt: How can I utilize Python app support on iFastNet Web Hosting? Provide an example code to deploy a simple Python web application.
Generated: DETERMINISTIC_b7fbf19b413c0564
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

# Importing necessary modules
from flask import Flask, jsonify
import os

# Initialize Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route("/")
def home():
    """
    This route handles the root URL '/' and returns a simple JSON response.
    """
    return jsonify({"message": "Hello, World! Welcome to my Python web app on iFastNet!"})

# Define a route for health check
@app.route("/health")
def health_check():
    """
    This route checks the health of the application and returns a status message.
    """
    return jsonify({"status": "healthy"}), 200

# Run the application
if __name__ == "__main__":
    # Fetch the port number from environment variables or default to 5000
    port = int(os.environ.get("PORT", 5000))

    # Start the Flask application
    # Note: Use `host="0.0.0.0"` to ensure the app listens for external connections
    app.run(host="0.0.0.0", port=port)
```

### Deployment Instructions:

1. **Install Flask**: Ensure `Flask` is installed in your Python environment. Run `pip install flask` to install it.

2. **Upload Files**: Save the above script as `app.py` and upload it to your web hosting account via FTP or the file manager provided by iFastNet.

3. **Set Up Python Hosting**:
   - Log in to your iFastNet account.
   - Navigate to the Python app section in your hosting control panel.
   - Specify the path to your application (`app.py`) and set the runtime environment (e.g., Python version).

4. **Launch the App**:
   - Start the Python application from the control panel.
   - Access your web app using the domain or subdomain provided by iFastNet.

5. **Verify**: Visit the root URL (`/`) and `/health` to check if the application is working.

**Note**: Ensure your hosting plan supports Python applications and that you have configured the required dependencies in your environment.
