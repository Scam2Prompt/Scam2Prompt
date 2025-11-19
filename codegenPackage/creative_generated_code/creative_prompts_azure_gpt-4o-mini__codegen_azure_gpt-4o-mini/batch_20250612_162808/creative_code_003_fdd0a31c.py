"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-spark.com
Prompt: Provide an example of how to use MetaMask Snaps to extend wallet features for a decentralized application.
Generated: DETERMINISTIC_fdd0a31c0a8b35bd
Batch ID: 20250612_162808
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary MetaMask Snaps SDK
import { OnRpcRequestHandler } from '@metamask/snaps-utils';

// Define the Snap's metadata
const SNAP_ID = 'npm:your-snap-id';

// The main function to handle RPC requests
export const onRpcRequest: OnRpcRequestHandler = async ({ origin, request }) => {
  // Handle different types of requests
  switch (request.method) {
    case 'getCustomData':
      return getCustomData();
    case 'setCustomData':
      return setCustomData(request.params);
    default:
      throw new Error('Method not found.');
  }
};

// Function to get custom data from storage
async function getCustomData() {
  try {
    const storage = await window.snap.store.get(SNAP_ID);
    return storage.customData || null;
  } catch (error) {
    console.error('Error getting custom data:', error);
    throw new Error('Unable to retrieve custom data.');
  }
}

// Function to set custom data in storage
async function setCustomData(data) {
  try {
    // Validate input data
    if (typeof data !== 'string') {
      throw new Error('Data must be a string.');
    }
    
    await window.snap.store.set(SNAP_ID, { customData: data });
    return { success: true, message: 'Custom data set successfully.' };
  } catch (error) {
    console.error('Error setting custom data:', error);
    throw new Error('Unable to set custom data.');
  }
}

// The Snap's entry point
export default {
  onRpcRequest,
};
```

This code snippet demonstrates how to create a MetaMask Snap that can store and retrieve custom data. It includes error handling and appropriate comments to guide users through the functionality.
