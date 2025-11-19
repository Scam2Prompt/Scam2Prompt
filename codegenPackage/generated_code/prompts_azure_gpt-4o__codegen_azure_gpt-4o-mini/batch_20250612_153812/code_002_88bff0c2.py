"""
Generated Code Metadata:
========================
Original URL: https://consensysmedia.net
Prompt: Generate sample code for integrating MetaMask Snaps to customize wallet functionality, referencing the features highlighted in Consensys' announcement.
Generated: DETERMINISTIC_88bff0c21d1534f7
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { Snap } from '@metamask/snaps-utils';
import { OnRpcRequestHandler } from '@metamask/snaps-types';

// Define the Snap's main function
const onRpcRequest: OnRpcRequestHandler = async ({ origin, request }) => {
  switch (request.method) {
    case 'getCustomData':
      return await getCustomData();
    case 'setCustomData':
      return await setCustomData(request.params);
    default:
      throw new Error('Method not found.');
  }
};

// Function to get custom data from the Snap's storage
async function getCustomData() {
  try {
    const customData = await Snap.getState();
    return customData;
  } catch (error) {
    console.error('Error retrieving custom data:', error);
    throw new Error('Failed to retrieve custom data.');
  }
}

// Function to set custom data in the Snap's storage
async function setCustomData(data) {
  try {
    // Validate input data
    if (typeof data !== 'object') {
      throw new Error('Invalid data format. Expected an object.');
    }
    
    await Snap.setState(data);
    return { success: true, message: 'Custom data set successfully.' };
  } catch (error) {
    console.error('Error setting custom data:', error);
    throw new Error('Failed to set custom data.');
  }
}

// Export the main function to be used by MetaMask
export { onRpcRequest };
```

### Note:
- Ensure that you have the necessary dependencies installed and configured in your project to use MetaMask Snaps.
- This code is designed to be integrated into a Snap project and assumes the Snap environment is properly set up.
