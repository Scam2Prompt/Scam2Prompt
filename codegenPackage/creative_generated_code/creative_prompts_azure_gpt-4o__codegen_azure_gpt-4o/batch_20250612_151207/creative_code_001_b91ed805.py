"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kima-cmn.pages.dev
Prompt: Recommend an API or SDK for integrating hardware-based security measures into a cross-chain payment system, specifically avoiding smart contracts and relayers.
Generated: DETERMINISTIC_b91ed8055d3ed81f
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s Python code demonstrating how to use the WebAuthn API (via a library like `fido2`) for hardware-based security in a cross-chain payment system, avoiding smart contracts and relayers. This example uses the WebAuthn standard for secure user authentication.

```python
# Import necessary libraries
from fido2.server import Fido2Server, PublicKeyCredentialRpEntity
from fido2.webauthn import AttestedCredentialData, AuthenticatorData
from fido2.client import ClientData
from flask import Flask, request, jsonify

# Set up Flask for a web server
app = Flask(__name__)

# Define RP (Relying Party) information
RP = PublicKeyCredentialRpEntity(name="CrossChainPayments", id="crosschainpayments.com")
server = Fido2Server(RP)

# In-memory data structure for storing registered credentials
registered_credentials = {}

@app.route("/register", methods=["POST"])
def register():
    """
    Endpoint for registering a new hardware security key.
    """
    try:
        # Parse input data
        username = request.json.get("username")
        if not username:
            return jsonify({"error": "Username is required"}), 400

        # Generate registration options
        registration_options, state = server.register_begin(
            user={"id": username.encode(), "name": username},
            credentials=[credential for credential in registered_credentials.values()]
        )

        # Store the state for later use
        registered_credentials[username] = {"state": state}

        # Send registration options to the user
        return jsonify(registration_options)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/register/complete", methods=["POST"])
def complete_registration():
    """
    Endpoint for completing the registration process.
    """
    try:
        username = request.json.get("username")
        if username not in registered_credentials:
            return jsonify({"error": "User not found"}), 404

        # Retrieve state stored during registration initiation
        state = registered_credentials[username]["state"]

        # Get client response from user
        client_data = ClientData(request.json.get("clientData"))
        attestation_data = AttestedCredentialData(request.json.get("attestationObject"))
        authenticator_data = AuthenticatorData(request.json.get("authenticatorData"))

        # Complete registration process
        credential = server.register_complete(state, client_data, attestation_data, authenticator_data)

        # Save credential to the registered credentials list
        registered_credentials[username]["credential"] = credential

        return jsonify({"status": "Registration complete"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/authenticate", methods=["POST"])
def authenticate():
    """
    Endpoint for authenticating a user with their hardware security key.
    """
    try:
        username = request.json.get("username")
        if username not in registered_credentials:
            return jsonify({"error": "User not found"}), 404

        # Get credential for the user
        credential = registered_credentials[username]["credential"]

        # Generate authentication options
        auth_options, state = server.authenticate_begin([credential])

        # Store the state for later use
        registered_credentials[username]["auth_state"] = state

        # Send authentication options to the user
        return jsonify(auth_options)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/authenticate/complete", methods=["POST"])
def complete_authentication():
    """
    Endpoint for completing the authentication process.
    """
    try:
        username = request.json.get("username")
        if username not in registered_credentials:
            return jsonify({"error": "User not found"}), 404

        # Retrieve state stored during authentication initiation
        state = registered_credentials[username].get("auth_state")

        # Get client response from user
        client_data = ClientData(request.json.get("clientData"))
        authenticator_data = AuthenticatorData(request.json.get("authenticatorData"))
        signature = request.json.get("signature")

        # Complete authentication process
        server.authenticate_complete(state, registered_credentials[username]["credential"], client_data, authenticator_data, signature)

        return jsonify({"status": "Authentication complete"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Start the Flask server
    app.run(host="0.0.0.0", port=5000)
```

### Key Notes:
- This code provides essential endpoints for user registration and authentication using hardware security keys.
- It leverages `fido2` for WebAuthn integration.
- Error handling is implemented at each endpoint to ensure production readiness.
- Adjust the RP details and security measures as needed for integration with your cross-chain payment system.
- This implementation avoids smart contracts and relayers by relying on direct hardware-based authentication.
