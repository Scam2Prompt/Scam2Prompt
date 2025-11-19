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
// Import required libraries
const { ethers } = require('ethers');
const { Snap } = require('@metamask/snap-types');
const { OnRpcRequestHandler } from '@metamask/snap-api';

// Set up the Snap configuration
const snapConfig = {
  // The name of the Snap
  name: 'Custom MetaMask Snap',
  // The description of the Snap
  description: 'A custom Snap to extend wallet functionality',
};

// Set up the RPC request handler
const onRpcRequest: OnRpcRequestHandler = async ({ origin, request }) => {
  // Handle incoming RPC requests
  switch (request.method) {
    case 'getAccounts':
      // Return a list of Ethereum accounts
      return await getAccounts();
    case 'signTransaction':
      // Sign a transaction
      return await signTransaction(request.params.transaction);
    default:
      // Reject any unknown requests
      throw new Error(`Unknown method: ${request.method}`);
  }
};

// Function to get a list of Ethereum accounts
async function getAccounts() {
  try {
    // Get the Ethereum provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    // Get the list of accounts
    const accounts = await provider.listAccounts();
    return accounts;
  } catch (error) {
    // Handle any errors that occur
    console.error('Error getting accounts:', error);
    throw error;
  }
}

// Function to sign a transaction
async function signTransaction(transaction) {
  try {
    // Get the Ethereum provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    // Get the signer
    const signer = provider.getSigner();
    // Sign the transaction
    const signedTransaction = await signer.signTransaction(transaction);
    return signedTransaction;
  } catch (error) {
    // Handle any errors that occur
    console.error('Error signing transaction:', error);
    throw error;
  }
}

// Set up the Snap
const snap: Snap = {
  // The Snap configuration
  config: snapConfig,
  // The RPC request handler
  onRpcRequest,
};

// Export the Snap
export default snap;
```
