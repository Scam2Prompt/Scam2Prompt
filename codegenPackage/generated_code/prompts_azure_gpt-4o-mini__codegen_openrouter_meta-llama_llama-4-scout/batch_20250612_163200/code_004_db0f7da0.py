"""
Generated Code Metadata:
========================
Original URL: https://manta.zone
Prompt: Write a script that demonstrates how to authenticate with the Manta API.
Generated: DETERMINISTIC_db0f7da0acb6b86f
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Manta API Authentication Script

This script demonstrates how to authenticate with the Manta API using the
requests library and JSON Web Tokens (JWTs).

Usage:
    python manta_auth.py

Requirements:
    - requests
    - jwt
"""

import requests
import jwt
import argparse
import os

def load_config(config_file):
    """
    Load configuration from a JSON file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        dict: Configuration data.
    """
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse configuration file '{config_file}': {e}")
        exit(1)

def authenticate_manta_api(config):
    """
    Authenticate with the Manta API using a JSON Web Token.

    Args:
        config (dict): Configuration data.

    Returns:
        str: JSON Web Token.
    """
    try:
        # Set Manta API credentials
        manta_url = config['manta_url']
        client_id = config['client_id']
        client_secret = config['client_secret']
        username = config['username']
        password = config['password']

        # Obtain an access token
        auth_url = f"{manta_url}/auth/token"
        auth_response = requests.post(
            auth_url,
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data={
                'grant_type': 'password',
                'client_id': client_id,
                'client_secret': client_secret,
                'username': username,
                'password': password
            }
        )

        # Check if authentication was successful
        auth_response.raise_for_status()

        # Extract the access token
        access_token = auth_response.json()['access_token']

        # Create a JSON Web Token
        jwt_token = jwt.encode(
            {'access_token': access_token},
            client_secret,
            algorithm='HS256'
        )

        return jwt_token
    except requests.exceptions.HTTPError as e:
        print(f"Error: Authentication failed: {e}")
        exit(1)
    except jwt.ExpiredSignatureError:
        print("Error: JSON Web Token has expired.")
        exit(1)
    except jwt.InvalidTokenError:
        print("Error: Invalid JSON Web Token.")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='Manta API Authentication Script')
    parser.add_argument('-c', '--config', default='config.json', help='Path to the configuration file')
    args = parser.parse_args()

    import json
    config = load_config(args.config)
    jwt_token = authenticate_manta_api(config)

    print(f"JSON Web Token: {jwt_token}")

if __name__ == '__main__':
    main()
```
