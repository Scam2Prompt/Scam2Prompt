"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-clink.org
Prompt: Write a Node.js script to interact with Nginx Proxy Manager's API to add a new proxy host with custom settings.
Generated: DETERMINISTIC_1ae2ae7768bd32fb
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:81/api": {
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

// Configuration for Nginx Proxy Manager API
const NPM_API_URL = 'http://localhost:81/api'; // Adjust to your Nginx Proxy Manager URL
const NPM_API_KEY = 'your_api_key_here'; // Replace with your Nginx Proxy Manager API key

// Function to add a new proxy host
async function addProxyHost(proxyHostConfig) {
    try {
        // Validate input
        if (!proxyHostConfig || !proxyHostConfig.domainNames || !proxyHostConfig.forwardHost || !proxyHostConfig.forwardPort) {
            throw new Error('Invalid proxy host configuration.');
        }

        // Making POST request to add a new proxy host
        const response = await axios.post(`${NPM_API_URL}/proxy-hosts`, proxyHostConfig, {
            headers: {
                'Authorization': `Bearer ${NPM_API_KEY}`,
                'Content-Type': 'application/json'
            }
        });

        // Log the response from the API
        console.log('Proxy host added successfully:', response.data);
    } catch (error) {
        // Handle errors in a user-friendly way
        if (error.response) {
            // The request was made and the server responded with a status code
            console.error('Error adding proxy host:', error.response.data);
        } else if (error.request) {
            // The request was made but no response was received
            console.error('No response received:', error.request);
        } else {
            // Something happened in setting up the request
            console.error('Error', error.message);
        }
    }
}

// Example usage
const newProxyHostConfig = {
    domainNames: ['example.com'], // List of domain names for the proxy
    forwardHost: '192.168.1.100', // IP address or hostname to route traffic to
    forwardPort: 80, // Port on the forward host
    scheme: 'http', // Use 'http' or 'https'
    ssl: false, // Set to true if using SSL
    // Additional settings can be added here based on your needs
};

// Call the function to add the new proxy host
addProxyHost(newProxyHostConfig);
```

Make sure to replace `your_api_key_here` and adjust the NPM_API_URL if needed. The object structure in `newProxyHostConfig` can be expanded based on the available options in the Nginx Proxy Manager API documentation.
