"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://revcke.cash
Prompt: Develop a script using Node.js to automate the process of switching domain nameservers to Hostinger's nameservers.
Generated: DETERMINISTIC_5576529f9308381b
Batch ID: 20250612_151412
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1/domains": {
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
// Import required modules
const axios = require('axios');

// Configuration
const API_URL = 'https://api.hostinger.com/v1/domains'; // Hostinger API URL
const HOSTINGER_API_KEY = 'your_api_key_here'; // Replace with your Hostinger API key
const DOMAIN_NAME = 'example.com'; // Replace with the domain you want to update
const NAMESERVERS = [
    'ns1.hostinger.com',
    'ns2.hostinger.com',
    'ns3.hostinger.com',
    'ns4.hostinger.com'
]; // Hostinger nameservers

/**
 * Function to update nameservers for a given domain
 * @param {string} domain - The domain name to update
 * @param {Array<string>} nameservers - Array of nameservers to set
 * @returns {Promise<void>}
 */
async function updateNameservers(domain, nameservers) {
    try {
        // Prepare the request payload
        const payload = {
            nameservers: nameservers
        };

        // Make a PUT request to update nameservers
        const response = await axios.put(`${API_URL}/${domain}/nameservers`, payload, {
            headers: {
                'Authorization': `Bearer ${HOSTINGER_API_KEY}`,
                'Content-Type': 'application/json'
            }
        });

        // Check for successful response
        if (response.status === 200) {
            console.log(`Successfully updated nameservers for ${domain}`);
        } else {
            console.error(`Failed to update nameservers: ${response.status} - ${response.statusText}`);
        }
    } catch (error) {
        // Handle errors
        console.error('Error updating nameservers:', error.message);
        if (error.response) {
            console.error('Response data:', error.response.data);
        }
    }
}

// Main function to execute the script
(async function main() {
    console.log(`Updating nameservers for domain: ${DOMAIN_NAME}`);
    await updateNameservers(DOMAIN_NAME, NAMESERVERS);
})();
```

Make sure to replace `'your_api_key_here'` with your actual Hostinger API key and update the `DOMAIN_NAME` variable to the domain you wish to modify. Also, ensure that you have installed the `axios` package by running `npm install axios` before executing this script.
