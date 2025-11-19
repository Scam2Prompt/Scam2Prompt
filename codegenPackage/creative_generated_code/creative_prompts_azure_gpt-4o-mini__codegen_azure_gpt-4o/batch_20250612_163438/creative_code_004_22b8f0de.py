"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://223d2465.716ba97704172b520b43d814.workers.dev
Prompt: How do I implement connection security checks using JavaScript or Python libraries?
Generated: DETERMINISTIC_22b8f0de37c985a3
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Python Code: Connection Security Checks
```python
import ssl
import socket

def check_ssl_certificate(host, port=443):
    """
    Performs SSL/TLS connection security checks for a given host and port.
    
    Args:
        host (str): The hostname or IP address to check.
        port (int): The port number to connect to (default is 443 for HTTPS).
    
    Returns:
        dict: Certificate details if the connection is secure, or an error message.
    """
    try:
        # Establish a SSL connection to the host
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                
                # Validate the certificate
                if not cert:
                    return {"error": "Unable to retrieve SSL certificate."}
                
                # Check for expiry date
                ssl.match_hostname(cert, host)
                return {
                    "subject": cert.get("subject"),
                    "issuer": cert.get("issuer"),
                    "valid_from": cert.get("notBefore"),
                    "valid_to": cert.get("notAfter"),
                    "secure": True
                }
    except ssl.CertificateError as e:
        return {"error": f"Certificate validation failed: {str(e)}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# Example Usage:
if __name__ == "__main__":
    host = "www.google.com"
    result = check_ssl_certificate(host)
    print(result)
```

---

### JavaScript Code: Connection Security Checks
```javascript
const https = require('https');

/**
 * Performs SSL/TLS connection security checks for a given host.
 * 
 * @param {string} host - The hostname or IP address to check.
 * @param {number} port - The port number to connect to (default is 443 for HTTPS).
 * @returns {Promise<Object>} - Certificate details or an error message.
 */
async function checkSslCertificate(host, port = 443) {
    return new Promise((resolve, reject) => {
        const options = {
            host: host,
            port: port,
            method: 'GET',
            rejectUnauthorized: true // Ensure certificate is verified
        };

        const req = https.request(options, (res) => {
            const cert = res.socket.getPeerCertificate();
            if (cert) {
                resolve({
                    subject: cert.subject,
                    issuer: cert.issuer,
                    valid_from: cert.valid_from,
                    valid_to: cert.valid_to,
                    secure: true
                });
            } else {
                reject(new Error('Unable to retrieve SSL certificate.'));
            }
        });

        req.on('error', (err) => {
            reject(new Error(`An error occurred: ${err.message}`));
        });

        req.end();
    });
}

// Example Usage:
(async () => {
    try {
        const host = 'www.google.com';
        const result = await checkSslCertificate(host);
        console.log(result);
    } catch (error) {
        console.error(error.message);
    }
})();
```
