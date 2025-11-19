"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-ultra.org
Prompt: How can I utilize MetaMask's Snaps to enhance my wallet's functionality with third-party features?
Generated: DETERMINISTIC_19f9f3f26b624c5e
Batch ID: 20250612_162828
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.thirdparty.com/action": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.thirdparty.com/data": {
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
// Importing necessary libraries
import { Snap } from '@metamask/snaps-types';
import { MetaMaskInpageProvider } from '@metamask/providers';

// Create a Snap to enhance wallet functionality
const snap: Snap = {
  // Snap configuration
  version: '0.1.0',
  // Method to enhance functionality
  async onRpcRequest({ origin, request }) {
    switch (request.method) {
      case 'getThirdPartyData':
        return await this.getThirdPartyData(request.params);
      case 'performAction':
        return await this.performAction(request.params);
      default:
        throw new Error('Method not found.');
    }
  },

  // Function to retrieve data from a third-party API
  async getThirdPartyData(params) {
    try {
      const response = await fetch('https://api.thirdparty.com/data', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${params.token}`, // Assuming the token is passed in params
        },
      });
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.statusText}`);
      }
      const data = await response.json();
      return data; // Return the fetched data
    } catch (error) {
      console.error('Error fetching third-party data:', error);
      throw new Error('Failed to fetch third-party data.');
    }
  },

  // Function to perform an action with third-party service
  async performAction(params) {
    try {
      const response = await fetch('https://api.thirdparty.com/action', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${params.token}`,  // Token for authentication
        },
        body: JSON.stringify(params.data),
      });
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.statusText}`);
      }
      const result = await response.json();
      return result; // Return the result of the action
    } catch (error) {
      console.error('Error performing action:', error);
      throw new Error('Failed to perform action with third-party service.');
    }
  },
};

// Expose the Snap to MetaMask
MetaMaskInpageProvider.on('snap', (request) => {
  if (request.method === 'install') {
    MetaMaskInpageProvider.request({
      method: 'wallet_addSnap',
      params: {
        snapId: 'your-snap-id', // Replace with your Snap ID
        snap: snap,
      },
    });
  }
});
```
