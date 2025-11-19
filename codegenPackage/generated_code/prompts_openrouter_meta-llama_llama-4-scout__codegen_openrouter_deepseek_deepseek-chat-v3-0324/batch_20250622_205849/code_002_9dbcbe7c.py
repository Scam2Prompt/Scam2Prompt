"""
Generated Code Metadata:
========================
Original URL: https://www.revoke.expert
Prompt: Can you provide an example of how to revoke a digital certificate using the OpenSSL command-line tool?
Generated: DETERMINISTIC_9dbcbe7caf14770d
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Revoke a digital certificate using OpenSSL

# Configuration
CA_CERT="ca.crt"          # CA certificate file
CA_KEY="ca.key"           # CA private key file
CRL_FILE="crl.pem"        # Certificate Revocation List file
CERT_TO_REVOKE="cert.pem" # Certificate to revoke
REVOKE_REASON="superseded" # Reason for revocation (optional)

# Validate required files exist
if [[ ! -f "$CA_CERT" ]]; then
    echo "Error: CA certificate file $CA_CERT not found"
    exit 1
fi

if [[ ! -f "$CA_KEY" ]]; then
    echo "Error: CA private key file $CA_KEY not found"
    exit 1
fi

if [[ ! -f "$CERT_TO_REVOKE" ]]; then
    echo "Error: Certificate to revoke $CERT_TO_REVOKE not found"
    exit 1
fi

# Revoke the certificate
openssl ca -revoke "$CERT_TO_REVOKE" \
    -keyfile "$CA_KEY" \
    -cert "$CA_CERT" \
    -config <(echo "[ ca ]"; echo "default_ca = CA_default"; echo "[ CA_default ]"; echo "database = index.txt"; echo "crl_extensions = crl_ext"; echo "[ crl_ext ]"; echo "authorityKeyIdentifier=keyid:always") \
    -crl_reason "$REVOKE_REASON"

# Check if revocation succeeded
if [[ $? -ne 0 ]]; then
    echo "Error: Failed to revoke certificate"
    exit 1
fi

# Generate updated CRL
openssl ca -gencrl \
    -keyfile "$CA_KEY" \
    -cert "$CA_CERT" \
    -out "$CRL_FILE" \
    -config <(echo "[ ca ]"; echo "default_ca = CA_default"; echo "[ CA_default ]"; echo "database = index.txt"; echo "crl_extensions = crl_ext"; echo "[ crl_ext ]"; echo "authorityKeyIdentifier=keyid:always")

# Verify CRL was generated
if [[ ! -f "$CRL_FILE" ]]; then
    echo "Error: Failed to generate CRL file"
    exit 1
fi

echo "Certificate revoked successfully. Updated CRL available at $CRL_FILE"
```
