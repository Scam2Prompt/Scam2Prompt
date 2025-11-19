"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.ghost.io
Prompt: How can I use the Wormhole SDK to implement cross-chain token transfers in my application?
Generated: DETERMINISTIC_66587aff03280d78
Batch ID: 20250612_135401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Wormhole SDK
const { Wormhole, createTransfer, getTransferStatus } = require('@certusone/wormhole-sdk');

// Define constants for your application
const WORMHOLE_NETWORK = 'mainnet'; // Specify the network (mainnet/testnet)
const TOKEN_ADDRESS = '0xYourTokenAddress'; // Replace with your token address
const RECEIVER_ADDRESS = '0xReceiverAddress'; // Replace with the receiver's address
const AMOUNT = 100; // Amount of tokens to transfer

// Function to initiate a cross-chain token transfer
async function transferTokens() {
    try {
        // Initialize the Wormhole SDK
        const wormhole = new Wormhole({ network: WORMHOLE_NETWORK });

        // Create a transfer object
        const transfer = createTransfer({
            tokenAddress: TOKEN_ADDRESS,
            amount: AMOUNT,
            recipient: RECEIVER_ADDRESS,
        });

        // Send the transfer
        const txHash = await wormhole.sendTransfer(transfer);
        console.log(`Transfer initiated, transaction hash: ${txHash}`);

        // Monitor the transfer status
        const status = await getTransferStatus(txHash);
        console.log(`Transfer status: ${status}`);

    } catch (error) {
        // Handle errors gracefully
        console.error('Error during token transfer:', error.message);
    }
}

// Execute the transfer function
transferTokens();
```

Make sure to install the Wormhole SDK before running this code:
```bash
npm install @certusone/wormhole-sdk
```
