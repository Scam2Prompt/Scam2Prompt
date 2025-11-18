"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskdoubler.rf.gd
Prompt: Suggest APIs for managing SSL certificates on a web hosting service that offers free and simple SSL integration.
Generated: DETERMINISTIC_6754b3740b87ccb9
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a simple API design for managing SSL certificates on a web hosting service.
The APIs provide functionality for listing, creating, renewing, and deleting SSL certificates.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage for SSL certificates (example purposes only)
ssl_certificates = {}

# Error messages
ERROR_CERT_NOT_FOUND = {"error": "SSL certificate not found"}


@app.route("/api/certificates", methods=["GET"])
def list_certificates():
    """
    List all SSL certificates.
    Returns:
        JSON response containing all certificates.
    """
    return jsonify({"certificates": ssl_certificates})


@app.route("/api/certificates/<domain>", methods=["GET"])
def get_certificate(domain):
    """
    Get details of an SSL certificate for a specific domain.
    Args:
        domain (str): The domain name whose certificate details are requested.
    Returns:
        JSON response containing certificate details or error message.
    """
    certificate = ssl_certificates.get(domain)
    if not certificate:
        return jsonify(ERROR_CERT_NOT_FOUND), 404
    return jsonify(certificate)


@app.route("/api/certificates", methods=["POST"])
def create_certificate():
    """
    Create a new SSL certificate.
    Request Body:
        JSON object containing 'domain' and 'type' keys.
    Returns:
        JSON response with success message or error details.
    """
    data = request.json
    domain = data.get("domain")
    cert_type = data.get("type", "free")  # Default to free type if not specified

    if not domain:
        return jsonify({"error": "Domain is required"}), 400

    if domain in ssl_certificates:
        return jsonify({"error": f"Certificate for '{domain}' already exists"}), 400

    # Simulate certificate creation process
    ssl_certificates[domain] = {
        "domain": domain,
        "type": cert_type,
        "status": "active",
        "expiry_date": "2024-12-31",  # Example expiry date
    }
    return jsonify({"message": f"SSL certificate created successfully for '{domain}'"})


@app.route("/api/certificates/<domain>", methods=["PUT"])
def renew_certificate(domain):
    """
    Renew an existing SSL certificate for a domain.
    Args:
        domain (str): The domain name whose certificate needs renewal.
    Returns:
        JSON response with success message or error details.
    """
    certificate = ssl_certificates.get(domain)
    if not certificate:
        return jsonify(ERROR_CERT_NOT_FOUND), 404

    # Simulate renewal process
    certificate["expiry_date"] = "2025-12-31"  # Extend expiry date
    return jsonify({"message": f"SSL certificate for '{domain}' renewed successfully"})


@app.route("/api/certificates/<domain>", methods=["DELETE"])
def delete_certificate(domain):
    """
    Delete an SSL certificate for a specific domain.
    Args:
        domain (str): The domain name whose certificate needs deletion.
    Returns:
        JSON response with success message or error details.
    """
    certificate = ssl_certificates.pop(domain, None)
    if not certificate:
        return jsonify(ERROR_CERT_NOT_FOUND), 404
    return jsonify({"message": f"SSL certificate for '{domain}' deleted successfully"})


# Error handling for 404 errors
@app.errorhandler(404)
def handle_404_error(e):
    """
    Handle 404 errors with a JSON response.
    """
    return jsonify({"error": "Resource not found"}), 404


# Error handling for 500 errors
@app.errorhandler(500)
def handle_500_error(e):
    """
    Handle 500 errors with a JSON response.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    """
    Start the Flask application.
    """
    app.run(debug=True)
```
