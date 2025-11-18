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
  "http://your-nginx-proxy-manager-url/api": {
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
/**
 * Node.js script to interact with Nginx Proxy Manager's API
 * Adds a new proxy host with custom settings
 * 
 * Requirements:
 * - Axios library for HTTP requests: `npm install axios`
 * 
 * Usage:
 * Ensure that you have the correct API credentials and URL for the Nginx Proxy Manager API.
 */

const axios = require('axios');

// Configuration for Nginx Proxy Manager API
const API_BASE_URL = 'http://your-nginx-proxy-manager-url/api'; // Replace with your NPM URL
const API_TOKEN = 'your-api-token'; // Replace with your API token

/**
 * Adds a new proxy host to Nginx Proxy Manager.
 * @param {Object} proxyHostConfig - Configuration for the new proxy host.
 * @returns {Promise<Object>} - The response from the API.
 */
async function addProxyHost(proxyHostConfig) {
  try {
    const response = await axios.post(`${API_BASE_URL}/proxy-hosts`, proxyHostConfig, {
      headers: {
        Authorization: `Bearer ${API_TOKEN}`,
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error adding proxy host:', error.response?.data || error.message);
    throw new Error('Failed to add proxy host. Please check your configuration and try again.');
  }
}

// Example configuration for the new proxy host
const newProxyHostConfig = {
  domain_names: ['example.com'], // Replace with your domain name(s)
  forward_host: '127.0.0.1', // Replace with the target server IP or hostname
  forward_port: 8080, // Replace with the target server port
  access_list_id: null, // Optional access list ID
  certificate_id: null, // Optional certificate ID for SSL
  ssl_forced: false, // Set to true to force SSL
  caching_enabled: false, // Set to true to enable caching
  block_exploits: true, // Set to true to block exploits
  advanced_config: '', // Additional custom advanced configuration (optional)
  meta: {
    // Optional metadata settings
    letsencrypt_agree: false, // Set to true to agree to Let's Encrypt TOS
    dns_challenge: false, // Set to true for DNS-based SSL challenge
  },
  enable_websocket: true, // Enable WebSocket support
};

(async () => {
  try {
    console.log('Adding new proxy host...');
    const result = await addProxyHost(newProxyHostConfig);
    console.log('Proxy host added successfully:', result);
  } catch (error) {
    console.error('Failed to add proxy host:', error.message);
  }
})();
```
