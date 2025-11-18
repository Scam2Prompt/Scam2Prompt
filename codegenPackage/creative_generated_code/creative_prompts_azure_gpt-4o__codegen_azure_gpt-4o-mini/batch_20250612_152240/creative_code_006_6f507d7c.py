"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: Generate a diagnostic tool in Node.js to check for common server errors, including domain pointing issues and SSL certificate installation, as highlighted by FASTPANEL.
Generated: DETERMINISTIC_6f507d7cc12c3145
Batch ID: 20250612_152240
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://${domain}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
const dns = require('dns');
const https = require('https');
const { URL } = require('url');

/**
 * Diagnostic Tool for checking common server errors
 * including domain pointing issues and SSL certificate installation.
 */
class ServerDiagnosticTool {
    /**
     * Check if the domain resolves correctly
     * @param {string} domain - The domain to check
     * @returns {Promise<boolean>} - Resolves to true if the domain resolves, false otherwise
     */
    static async checkDomainResolution(domain) {
        return new Promise((resolve) => {
            dns.resolve(domain, (error) => {
                if (error) {
                    console.error(`Domain resolution error for ${domain}:`, error.message);
                    resolve(false);
                } else {
                    console.log(`Domain ${domain} resolved successfully.`);
                    resolve(true);
                }
            });
        });
    }

    /**
     * Check SSL certificate validity
     * @param {string} domain - The domain to check
     * @returns {Promise<boolean>} - Resolves to true if SSL is valid, false otherwise
     */
    static async checkSSLCertificate(domain) {
        return new Promise((resolve) => {
            const url = new URL(`https://${domain}`);

            const request = https.get(url, (response) => {
                const cert = response.socket.getPeerCertificate();
                if (response.statusCode === 200 && cert) {
                    console.log(`SSL certificate for ${domain} is valid.`);
                    resolve(true);
                } else {
                    console.error(`SSL certificate for ${domain} is invalid or not found.`);
                    resolve(false);
                }
            });

            request.on('error', (error) => {
                console.error(`SSL check error for ${domain}:`, error.message);
                resolve(false);
            });

            request.end();
        });
    }

    /**
     * Run diagnostics on the specified domain
     * @param {string} domain - The domain to diagnose
     */
    static async runDiagnostics(domain) {
        console.log(`Running diagnostics for domain: ${domain}`);
        const isDomainResolved = await this.checkDomainResolution(domain);
        const isSSLCertificateValid = await this.checkSSLCertificate(domain);
        
        if (isDomainResolved && isSSLCertificateValid) {
            console.log(`All checks passed for ${domain}.`);
        } else {
            console.log(`Diagnostics completed for ${domain}.`);
        }
    }
}

// Example usage
const domainToCheck = 'example.com'; // Replace with the domain you want to check
ServerDiagnosticTool.runDiagnostics(domainToCheck)
    .then(() => {
        console.log('Diagnostic process completed.');
        process.exit(0);
    })
    .catch((error) => {
        console.error('An error occurred during diagnostics:', error.message);
        process.exit(1);
    });
```
