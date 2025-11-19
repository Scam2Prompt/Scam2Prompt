"""
Generated Code Metadata:
========================
Original URL: https://hop-protocol.pages.dev
Prompt: Create a code example that demonstrates how to customize the recipient and options for a transaction using the Hop Protocol's SDK.
Generated: DETERMINISTIC_c2033d198b6bbee7
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the Hop SDK
const { Hop } = require('@hop-protocol/sdk');

// Initialize the Hop SDK
const hop = new Hop({
  network: 'mainnet', // Use 'mainnet' or 'goerli' depending on your environment
});

// Function to customize recipient and options for a transaction
async function customizeTransaction() {
  try {
    // Define the transaction parameters
    const sourceChain = 'ethereum'; // Source chain (e.g., 'ethereum', 'polygon', etc.)
    const destinationChain = 'polygon'; // Destination chain
    const token = 'USDC'; // Token to transfer (e.g., 'USDC', 'DAI', etc.)
    const amount = '100'; // Amount to transfer (in token units)
    const recipient = '0xRecipientAddressHere'; // Recipient address

    // Define custom options for the transaction
    const options = {
      deadline: Math.floor(Date.now() / 1000) + 60 * 30, // Transaction deadline (30 minutes from now)
      slippageTolerance: 0.01, // Slippage tolerance (1%)
      bonderFee: '0.01', // Optional bonder fee (in token units)
    };

    // Perform the transfer using the Hop SDK
    const tx = await hop.transfer.send({
      sourceChain,
      destinationChain,
      token,
      amount,
      recipient,
      options,
    });

    console.log('Transaction sent successfully:', tx);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error while sending transaction:', error.message);
  }
}

// Execute the function
customizeTransaction();
```
