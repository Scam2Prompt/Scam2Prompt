"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cur.ve.fi
Prompt: What libraries can I use to enhance JavaScript functionality for domain information retrieval like on cur.ve.fi?
Generated: DETERMINISTIC_75390c8fb041f738
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for domain information retrieval
const axios = require('axios'); // For making HTTP requests
const dns = require('dns'); // Built-in module for DNS queries
const whois = require('whois-json'); // For WHOIS lookup

/**
 * Retrieves domain information such as DNS records and WHOIS data.
 * @param {string} domain - The domain to retrieve information for.
 * @returns {Promise<Object>} - A promise that resolves to an object containing domain information.
 * @throws {Error} - Throws an error if the domain is invalid or retrieval fails.
 */
async function getDomainInfo(domain) {
    try {
        // Validate the domain input
        if (!isValidDomain(domain)) {
            throw new Error('Invalid domain format.');
        }

        // Retrieve DNS records
        const dnsRecords = await lookupDNS(domain);

        // Retrieve WHOIS data
        const whoisData = await lookupWHOIS(domain);

        // Combine results
        return {
            domain,
            dns: dnsRecords,
            whois: whoisData,
        };
    } catch (error) {
        console.error(`Error retrieving information for ${domain}:`, error);
        throw new Error('Unable to retrieve domain information.');
    }
}

/**
 * Validates the format of the domain name.
 * @param {string} domain - The domain to validate.
 * @returns {boolean} - Returns true if the domain is valid, otherwise false.
 */
function isValidDomain(domain) {
    const domainRegex = /^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$/;
    return domainRegex.test(domain);
}

/**
 * Looks up DNS records for a given domain.
 * @param {string} domain - The domain to look up.
 * @returns {Promise<Object>} - A promise that resolves to the DNS records.
 */
function lookupDNS(domain) {
    return new Promise((resolve, reject) => {
        dns.resolve(domain, (err, addresses) => {
            if (err) {
                return reject(err);
            }
            resolve(addresses);
        });
    });
}

/**
 * Performs a WHOIS lookup for a given domain.
 * @param {string} domain - The domain to look up.
 * @returns {Promise<Object>} - A promise that resolves to the WHOIS data.
 */
function lookupWHOIS(domain) {
    return whois(domain).catch((error) => {
        console.error(`WHOIS lookup error for ${domain}:`, error);
        throw error; // Rethrow the error for further handling
    });
}

// Example usage
(async () => {
    const domain = 'example.com';
    try {
        const domainInfo = await getDomainInfo(domain);
        console.log('Domain Information:', domainInfo);
    } catch (error) {
        console.error(error.message);
    }
})();

```

### Required Libraries
Make sure to install the necessary libraries using npm:

```bash
npm install axios whois-json
```
