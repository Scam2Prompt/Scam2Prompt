"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3346--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of using Linode's NodeBalancers to distribute traffic across multiple web servers, including API calls for configuration.
Generated: DETERMINISTIC_d1a4f0c6c556c4fc
Batch ID: 20250612_151018
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
// Import the required libraries
const axios = require('axios');

// Constants for Linode API authentication
const LINODE_API_URL = 'https://api.linode.com/v4';
const API_TOKEN = 'YOUR_API_TOKEN'; // Replace with your Linode API token

/**
 * Sets up a NodeBalancer to distribute traffic across multiple web servers.
 * This script assumes that the servers are already created and their IPs are known.
 */
async function setupNodeBalancer() {
  try {
    // Step 1: Create a NodeBalancer
    const nodeBalancerResponse = await axios.post(
      `${LINODE_API_URL}/nodebalancers`,
      {
        region: 'us-east', // Change region as needed
      },
      {
        headers: {
          Authorization: `Bearer ${API_TOKEN}`,
        },
      }
    );

    const nodeBalancerId = nodeBalancerResponse.data.id;
    console.log(`NodeBalancer created successfully. ID: ${nodeBalancerId}`);

    // Step 2: Create a configuration for the NodeBalancer
    const configResponse = await axios.post(
      `${LINODE_API_URL}/nodebalancers/${nodeBalancerId}/configs`,
      {
        protocol: 'http', // Protocol can be 'http', 'https', or 'tcp'
        port: 80, // Port for traffic
        algorithm: 'roundrobin', // Load balancing algorithm ('roundrobin', 'leastconn', etc.)
        stickiness: 'table', // Session stickiness ('table', 'none', etc.)
      },
      {
        headers: {
          Authorization: `Bearer ${API_TOKEN}`,
        },
      }
    );

    const configId = configResponse.data.id;
    console.log(`NodeBalancer configuration created successfully. Config ID: ${configId}`);

    // Step 3: Add web server nodes to the NodeBalancer configuration
    const webServers = [
      { address: '192.168.1.101' }, // Replace with your web servers' IP addresses
      { address: '192.168.1.102' },
      { address: '192.168.1.103' },
    ];

    for (const server of webServers) {
      const nodeResponse = await axios.post(
        `${LINODE_API_URL}/nodebalancers/${nodeBalancerId}/configs/${configId}/nodes`,
        {
          address: server.address,
          label: `Node-${server.address}`, // Label for the node
          weight: 100, // Weight for load balancing (higher means more traffic)
        },
        {
          headers: {
            Authorization: `Bearer ${API_TOKEN}`,
          },
        }
      );

      console.log(`Node added successfully. Node ID: ${nodeResponse.data.id}`);
    }

    console.log('NodeBalancer setup complete.');
  } catch (error) {
    console.error('Error occurred while setting up the NodeBalancer:', error.response?.data || error.message);
  }
}

// Execute the function to set up the NodeBalancer
setupNodeBalancer();
```

### Notes:
- Replace `YOUR_API_TOKEN` with your actual Linode API token.
- Update the `region` and `webServers` array to match your requirements.
- This code uses `axios` for API calls, so ensure you install it via `npm install axios` before running the script.
