"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherfi.us
Prompt: Generate a sample configuration for integrating Tetherfi with Active Directory for secure single sign-on (SSO) access.
Generated: DETERMINISTIC_b0726988f5f527ab
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ldap
import ssl
from flask import Flask, request, jsonify
from ldap3 import Server, Connection, ALL, NTLM, Tls

# Flask application to handle SSO integration
app = Flask(__name__)

# Configuration for Active Directory
AD_SERVER = "ldap://your-ad-server.domain.com"
AD_USERNAME = "your-domain\\service-account"
AD_PASSWORD = "your-service-account-password"
BASE_DN = "dc=your-domain,dc=com"

# SSL/TLS context for secure communication with Active Directory
tls_configuration = Tls(validate=ssl.CERT_REQUIRED, version=ssl.PROTOCOL_TLSv1_2)

# Connect to Active Directory server
def connect_to_ad(username, password):
    try:
        # Create the server object with Active Directory server details
        server = Server(AD_SERVER, use_ssl=True, get_info=ALL, tls=tls_configuration)
        
        # Create a connection using NTLM authentication
        connection = Connection(
            server,
            user=username,
            password=password,
            authentication=NTLM,
            auto_bind=True
        )
        return connection
    except Exception as e:
        # Log and handle connection errors
        print(f"Error connecting to Active Directory: {str(e)}")
        return None

# Route to handle SSO login
@app.route("/sso-login", methods=["POST"])
def sso_login():
    try:
        # Extract the credentials from the request (e.g., username and password)
        data = request.json
        ad_username = data.get("username")
        ad_password = data.get("password")

        # Validate input data
        if not ad_username or not ad_password:
            return jsonify({"error": "Username and password are required"}), 400
        
        # Attempt to connect to Active Directory
        connection = connect_to_ad(ad_username, ad_password)
        if connection and connection.bind():
            # Successful authentication
            return jsonify({"message": "Login successful"}), 200
        else:
            # Authentication failed
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route for health check
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK"}), 200

# Main entry point
if __name__ == "__main__":
    # Start the Flask application
    app.run(host="0.0.0.0", port=5000, debug=False)
```
