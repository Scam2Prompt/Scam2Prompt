"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Write a Python script to query the SUNAT API for tax compliance checks, inspired by the "Principales trámites ante la SUNAT y tribunal fiscal" course on AulaContable.
Generated: DETERMINISTIC_5d5d45fe8641fd34
Batch ID: 20250612_154523
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sunat.gob.pe/api/ruc/v1.0/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

# SUNAT API Configuration
SUNAT_API_URL = "https://api.sunat.gob.pe/api/ruc/v1.0/"
SUNAT_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your SUNAT API key
COMPANY_RUC = "YOUR_COMPANY_RUC_HERE"  # Replace with the company RUC to query

def get_sunat_token(api_key):
    """
    Obtain a token to authenticate with the SUNAT API.

    Args:
        api_key (str): The SUNAT API key.

    Returns:
        str: The obtained token.
    """
    try:
        response = requests.post(
            f"{SUNAT_API_URL}generarToken",
            headers={"Content-Type": "application/json"},
            json={"apiKey": api_key},
        )
        response.raise_for_status()
        return response.json()["token"]
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining token: {e}")
        return None

def query_sunat_ruc(token, ruc):
    """
    Query the SUNAT API for tax compliance checks.

    Args:
        token (str): The obtained token.
        ruc (str): The company RUC to query.

    Returns:
        dict: The query result.
    """
    try:
        response = requests.get(
            f"{SUNAT_API_URL}consultaRUC/{ruc}",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying SUNAT API: {e}")
        return None

def main():
    # Obtain a token to authenticate with the SUNAT API
    token = get_sunat_token(SUNAT_API_KEY)
    if token is None:
        return

    # Query the SUNAT API for tax compliance checks
    result = query_sunat_ruc(token, COMPANY_RUC)
    if result is not None:
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
```
