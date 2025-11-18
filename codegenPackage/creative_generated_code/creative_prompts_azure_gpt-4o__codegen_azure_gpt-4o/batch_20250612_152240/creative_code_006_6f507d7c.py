"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: Generate a diagnostic tool in Node.js to check for common server errors, including domain pointing issues and SSL certificate installation, as highlighted by FASTPANEL.
Generated: DETERMINISTIC_6f507d7cc12c3145
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Diagnostic Tool for Server Health Check
 * This tool checks common server errors including:
 * - Domain pointing issues
 * - SSL certificate installation
 * 
 * Author: Expert Programmer
 * Language: Node.js
 * Best practices and production standards applied
 */

const https = require('https');
const http = require('http');
const dns = require('dns');

/**
 * Check if a domain is properly pointed to the server's IP address
 * @param {string} domain - The domain name to check
 * @param {string} serverIP - The server's expected IP address
 * @returns {Promise<string>} - Diagnostic result
 */
async function checkDomainPointing(domain, serverIP) {
    return new Promise((resolve, reject) => {
        dns.lookup(domain, (err, address) => {
            if (err) {
                reject(`DNS Lookup failed for domain '${domain}': ${err.message}`);
            } else if (address !== serverIP) {
                resolve(`Domain '${domain}' is not pointed correctly. Expected: ${serverIP}, Found: ${address}`);
            } else {
                resolve(`Domain '${domain}' is pointed correctly to ${serverIP}.`);
            }
        });
    });
}

/**
 * Check if SSL certificate is properly installed for a domain
 * @param {string} domain - The domain name to check
 * @returns {Promise<string>} - Diagnostic result
 */
async function checkSSLCertificate(domain) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: domain,
            method: 'GET',
            port: 443,
        };

        const req = https.request(options, (res) => {
            const cert = res.socket.getPeerCertificate();
            if (!cert || Object.keys(cert).length === 0) {
                resolve(`SSL certificate is not installed for '${domain}'.`);
            } else {
                resolve(`SSL certificate is installed for '${domain}'. Subject: ${cert.subject.CN}`);
            }
        });

        req.on('error', (err) => {
            if (err.code === 'ECONNREFUSED') {
                resolve(`SSL certificate check failed for '${domain}'. HTTPS connection refused.`);
            } else {
                reject(`Error checking SSL certificate for '${domain}': ${err.message}`);
            }
        });

        req.end();
    });
}

/**
 * Run diagnostics on the server
 * @param {string} domain - The domain name to check
 * @param {string} serverIP - The server's expected IP address
 */
async function runDiagnostics(domain, serverIP) {
    console.log(`Starting diagnostics for domain '${domain}' with expected server IP '${serverIP}'...\n`);

    try {
        const domainResult = await checkDomainPointing(domain, serverIP);
        console.log(domainResult);
    } catch (error) {
        console.error(`Domain Pointing Check Error: ${error}`);
    }

    try {
        const sslResult = await checkSSLCertificate(domain);
        console.log(sslResult);
    } catch (error) {
        console.error(`SSL Certificate Check Error: ${error}`);
    }

    console.log("\nDiagnostics Complete.");
}

// Example Usage:
// Replace 'example.com' and '127.0.0.1' with your domain and server IP address.
const domain = 'example.com';
const serverIP = '127.0.0.1';

runDiagnostics(domain, serverIP);
```

This code provides a diagnostic tool in Node.js to check for domain pointing issues and SSL certificate installation. It uses DNS lookup and HTTPS connection to verify configurations and includes error handling for potential failures.
