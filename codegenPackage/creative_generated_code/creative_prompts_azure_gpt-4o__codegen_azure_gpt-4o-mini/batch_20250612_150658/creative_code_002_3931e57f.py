"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-metis.net
Prompt: Generate a code example demonstrating how to use MetaMask Snaps to extend wallet functionality with third-party features.
Generated: DETERMINISTIC_3931e57fdcba001c
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { OnRpcRequestHandler, Snap } from '@metamask/snaps-types';

// Define a Snap object
const snap: Snap = {
  // The onRpcRequest method is invoked when the Snap receives an RPC request
  onRpcRequest: async ({ origin, request }) => {
    switch (request.method) {
      case 'getAccountBalances':
        return await getAccountBalances(origin, request.params);
      case 'sendTransaction':
        return await sendTransaction(origin, request.params);
      default:
        throw new Error('Method not found.');
    }
  },
};

// Function to get account balances
async function getAccountBalances(origin, params) {
  try {
    // Replace with actual logic to fetch balances
    const balances = {}; // Mocked balances
    return balances;
  } catch (error) {
    // Handle any errors that occur during the fetching of account balances
    console.error(`Error fetching account balances from ${origin}:`, error);
    throw new Error('Failed to fetch account balances.');
  }
}

// Function to send a transaction
async function sendTransaction(origin, params) {
  // Validate input parameters
  if (!params || !params.to || !params.amount) {
    throw new Error('Invalid parameters for sending transaction.');
  }

  try {
    // Replace with actual logic to send a transaction
    const transactionHash = '0xabc...'; // Mocked transaction hash
    return transactionHash;
  } catch (error) {
    // Handle any errors that occur during transaction sending
    console.error(`Error sending transaction from ${origin}:`, error);
    throw new Error('Transaction failed.');
  }
}

// Export the Snap as a module
export default snap;
```

This code snippet provides a basic structure for a MetaMask Snap, including two example methods: `getAccountBalances` and `sendTransaction`. It includes proper error handling, input validation, and follows best coding practices.
