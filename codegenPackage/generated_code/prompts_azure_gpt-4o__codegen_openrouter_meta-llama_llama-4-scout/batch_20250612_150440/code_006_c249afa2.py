"""
Generated Code Metadata:
========================
Original URL: https://metamask-snap-polkadot.pages.dev
Prompt: Create a dApp example that uses the Polkadot Wallet Snap functionality, based on the Metamask Snap Polkadot documentation.
Generated: DETERMINISTIC_c249afa2ae6ec242
Batch ID: 20250612_150440
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
const { OnRpcRequestHandler } = require('@metamask/snap-api');

// Set up Polkadot Wallet Snap
const polkadotSnapId = 'npm:polkadot-wallet-snap';
const polkadotSnapName = 'Polkadot Wallet Snap';

// Set up RPC request handler
const onRpcRequest: OnRpcRequestHandler = async ({ origin, request }) => {
  // Handle incoming RPC requests
  switch (request.method) {
    case 'getAccounts':
      // Get Polkadot accounts
      return getAccounts();
    case 'signTransaction':
      // Sign Polkadot transaction
      return signTransaction(request.params);
    default:
      // Handle unknown RPC methods
      throw new Error(`Unknown method: ${request.method}`);
  }
};

// Get Polkadot accounts
const getAccounts = async () => {
  try {
    // Request accounts from Polkadot Wallet Snap
    const accounts = await ethereum.request({
      method: 'snap_getAccounts',
      params: [polkadotSnapId],
    });
    return accounts;
  } catch (error) {
    // Handle errors
    console.error('Error getting accounts:', error);
    throw error;
  }
};

// Sign Polkadot transaction
const signTransaction = async (params) => {
  try {
    // Request transaction signing from Polkadot Wallet Snap
    const signedTransaction = await ethereum.request({
      method: 'snap_signTransaction',
      params: [polkadotSnapId, params],
    });
    return signedTransaction;
  } catch (error) {
    // Handle errors
    console.error('Error signing transaction:', error);
    throw error;
  }
};

// Set up Snap
const snap: Snap = {
  // Snap metadata
  name: polkadotSnapName,
  version: '1.0.0',
  // RPC request handler
  onRpcRequest,
};

// Export Snap
export default snap;
```

```javascript
// index.js
import { installSnap } from '@metamask/snap-ui';
import snap from './snap.js';

const init = async () => {
  try {
    // Install Snap
    const installedSnap = await installSnap({
      snapId: 'npm:polkadot-wallet-snap',
      version: '1.0.0',
    });
    // Enable Snap
    await installedSnap.enable();
  } catch (error) {
    console.error('Error initializing Snap:', error);
  }
};

init();
```
