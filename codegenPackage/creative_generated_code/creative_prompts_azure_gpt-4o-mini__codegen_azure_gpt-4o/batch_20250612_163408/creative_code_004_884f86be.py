"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3334--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Explain how to configure NodeBalancers in Linode for improved application performance.
Generated: DETERMINISTIC_884f86be92853d84
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linode.com/v4": {
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
 * Script to configure NodeBalancers on Linode for improved application performance.
 * This script uses the Linode API to create and configure a NodeBalancer.
 * Ensure you have a valid Linode API Key before running this script.
 */

const axios = require('axios');

// Linode API base URL
const LINODE_API_BASE_URL = 'https://api.linode.com/v4';
// Replace with your Linode API Key
const LINODE_API_KEY = '<your-linode-api-key>';

/**
 * Function to create a NodeBalancer
 * @param {string} region - The region where the NodeBalancer will be created (e.g., "us-east").
 * @returns {Promise<object>} - Returns the created NodeBalancer object.
 */
async function createNodeBalancer(region) {
  try {
    const response = await axios.post(
      `${LINODE_API_BASE_URL}/nodebalancers`,
      {
        region: region,
      },
      {
        headers: {
          Authorization: `Bearer ${LINODE_API_KEY}`,
        },
      }
    );
    console.log('NodeBalancer created successfully:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error creating NodeBalancer:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Function to configure a NodeBalancer
 * @param {number} nodeBalancerId - The ID of the NodeBalancer to configure.
 * @param {number} port - The port to configure (e.g., 80 or 443).
 * @param {string} protocol - The protocol for the port (e.g., "http", "https").
 * @returns {Promise<object>} - Returns the configured NodeBalancer configuration object.
 */
async function configureNodeBalancer(nodeBalancerId, port, protocol) {
  try {
    const response = await axios.post(
      `${LINODE_API_BASE_URL}/nodebalancers/${nodeBalancerId}/configs`,
      {
        port: port,
        protocol: protocol,
        algorithm: 'roundrobin', // Load balancing algorithm: roundrobin, leastconn, etc.
        stickiness: 'none', // Session stickiness: none, table, etc.
        check: 'http', // Health check type: http, connection, etc.
        check_interval: 10, // Health check interval (in seconds).
        check_timeout: 5, // Health check timeout (in seconds).
        check_attempts: 3, // Number of health check attempts before marking a node down.
      },
      {
        headers: {
          Authorization: `Bearer ${LINODE_API_KEY}`,
        },
      }
    );
    console.log('NodeBalancer configured successfully:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error configuring NodeBalancer:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Main function to demonstrate creating and configuring a NodeBalancer.
 */
async function main() {
  try {
    const region = 'us-east'; // Replace with the desired region
    const nodeBalancer = await createNodeBalancer(region);

    const port = 80; // Replace with the desired port
    const protocol = 'http'; // Replace with the desired protocol
    await configureNodeBalancer(nodeBalancer.id, port, protocol);

    console.log('NodeBalancer setup completed successfully.');
  } catch (error) {
    console.error('Error in NodeBalancer setup:', error.message);
  }
}

// Execute the main function
main();
```

### Prerequisites:
- Install Axios: `npm install axios`
- Replace `<your-linode-api-key>` with your Linode API key.
- Ensure that the Linode account has sufficient permissions to create and configure NodeBalancers.
