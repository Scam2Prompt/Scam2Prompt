"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milt-os.com
Prompt: Can you provide a code example for setting up Cloudflare Access with Google authentication?
Generated: DETERMINISTIC_bc6dd87304eb1772
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# This is a configuration file for setting up Cloudflare Access with Google authentication.
# Add this YAML content to your Cloudflare Access application policy in the Cloudflare dashboard.

# Application Configuration
applications:
  - name: "My Secure App" # Provide a name for the application
    domain: "secure.myapp.com" # Replace with your application's custom domain
    session_duration: "24h" # Define how long the session will last before re-authentication is required
    type: "self_hosted" # Indicates a self-hosted application

# Authentication Method
identity_providers:
  - name: "Google" # Name of the identity provider
    type: "google" # Set Google as the authentication provider
    config:
      client_id: "YOUR_GOOGLE_CLIENT_ID" # Replace with your Google OAuth Client ID
      client_secret: "YOUR_GOOGLE_CLIENT_SECRET" # Replace with your Google OAuth Client Secret

# Access Policy
policies:
  - name: "Default Policy" # Provide a name for your access policy
    decision: "allow" # Set to "allow" to grant access
    include:
      - email:
          - "admin@myapp.com" # Replace with the allowed email addresses
          - "user@myapp.com"  # Add additional emails as needed
    identity_provider_ids:
      - "Google" # Reference the identity provider used in the authentication step
```
