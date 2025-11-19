"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Develop a code snippet that demonstrates how to configure NodeBalancers in Linode for load balancing web applications.
Generated: DETERMINISTIC_5977835b00eea9aa
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
// Import required libraries
const axios = require('axios');

// Linode API Token (Replace with your actual API token)
const API_TOKEN = 'YOUR_LINODE_API_TOKEN';

// Linode API Base URL
const BASE_URL = 'https://api.linode.com/v4';

// Function to create a NodeBalancer
async function createNodeBalancer(region) {
  try {
    const response = await axios.post(
      `${BASE_URL}/nodebalancers`,
      { region: region },
      {
        headers: {
          Authorization: `Bearer ${API_TOKEN}`,
          'Content-Type': 'application/json',
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

// Function to configure a NodeBalancer's port for HTTP load balancing
async function configureNodeBalancerPort(nodeBalancerId, portConfig) {
  try {
    const response = await axios.post(
      `${BASE_URL}/nodebalancers/${nodeBalancerId}/configs`,
      portConfig,
      {
        headers: {
          Authorization: `Bearer ${API_TOKEN}`,
          'Content-Type': 'application/json',
        },
      }
    );

    console.log('NodeBalancer port configured successfully:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error configuring NodeBalancer port:', error.response?.data || error.message);
    throw error;
  }
}

// Function to add a backend node to the NodeBalancer
async function addBackendNode(nodeBalancerId, configId, backendNodeConfig) {
  try {
    const response = await axios.post(
      `${BASE_URL}/nodebalancers/${nodeBalancerId}/configs/${configId}/nodes`,
      backendNodeConfig,
      {
        headers: {
          Authorization: `Bearer ${API_TOKEN}`,
          'Content-Type': 'application/json',
        },
      }
    );

    console.log('Backend node added successfully:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error adding backend node:', error.response?.data || error.message);
    throw error;
  }
}

// Usage example
(async () => {
  try {
    // Step 1: Create a NodeBalancer in the desired region
    const region = 'us-east'; // Replace with your region
    const nodeBalancer = await createNodeBalancer(region);

    // Step 2: Configure the NodeBalancer's port for HTTP load balancing
    const portConfig = {
      port: 80,
      protocol: 'http',
      algorithm: 'roundrobin',
      check: 'http',
      check_path: '/',
    };
    const config = await configureNodeBalancerPort(nodeBalancer.id, portConfig);

    // Step 3: Add backend nodes to the NodeBalancer
    const backendNodeConfig = [
      { address: '192.168.1.1', label: 'web-server-1' },
      { address: '192.168.1.2', label: 'web-server-2' },
    ];

    for (const node of backendNodeConfig) {
      await addBackendNode(nodeBalancer.id, config.id, node);
    }

    console.log('NodeBalancer setup completed successfully.');
  } catch (error) {
    console.error('Error during NodeBalancer setup:', error.message);
  }
})();
```

Replace the placeholders (`YOUR_LINODE_API_TOKEN`, region, and backend node details) with actual values relevant to your setup. Ensure you have the `axios` package installed in your project by running `npm install axios` before running this script.
