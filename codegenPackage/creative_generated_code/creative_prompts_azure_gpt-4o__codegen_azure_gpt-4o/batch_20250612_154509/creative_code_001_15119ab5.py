"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gonetwork.eu
Prompt: Recommend a JavaScript library or API for retrieving domain information, referencing tools like those found on https://gonetwork.eu.
Generated: DETERMINISTIC_15119ab5609d759f
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A script to retrieve domain information using the `whois-json` library.
 * This library provides simple WHOIS lookups for domain names.
 * 
 * Usage:
 * 1. Ensure Node.js is installed on your system.
 * 2. Install the `whois-json` package by running: npm install whois-json
 * 3. Run this script with Node.js.
 */

const whois = require('whois-json');

/**
 * Function to fetch domain information.
 * @param {string} domain - The domain name to look up.
 * @returns {Promise<Object>} - A promise that resolves to the domain information.
 */
async function fetchDomainInfo(domain) {
    try {
        console.log(`Fetching domain information for: ${domain}`);
        
        // Perform WHOIS lookup
        const domainInfo = await whois(domain);
        
        // Log or process the domain information
        console.log('Domain information:', domainInfo);
        
        return domainInfo;
    } catch (error) {
        // Handle errors gracefully
        console.error('Error fetching domain information:', error.message);
        throw error;
    }
}

/**
 * Example Usage
 * Replace 'example.com' with the domain you want to look up.
 */
const domainToLookup = 'example.com';

fetchDomainInfo(domainToLookup)
    .then(domainInfo => {
        console.log('Domain lookup successful!');
    })
    .catch(error => {
        console.error('Domain lookup failed.');
    });
```

Note: Make sure to install the `whois-json` package before running the script by executing `npm install whois-json`. This script fetches WHOIS information for a given domain name and includes proper error handling for production readiness.
