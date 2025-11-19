"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-axelar.com
Prompt: Provide an example of how to use the Axelar Interchain Token Service in a JavaScript application to facilitate cross-chain transactions.
Generated: DETERMINISTIC_d30d13f3b8ba0a2e
Batch ID: 20250612_160413
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-ethereum-node-url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://gateway.axelar.network": {
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
// Import necessary libraries
const { AxelarSigners, AxelarGateway } = require('@axelar-network/axelar-gateway-sdk');
const { ethers } = require('ethers');

// Define configuration parameters
const axelarGatewayUrl = 'https://gateway.axelar.network';
const chainId = 'your-chain-id'; // Replace with the desired chain ID
const privateKey = 'your-private-key'; // Replace with your wallet's private key
const destinationChain = 'destination-chain-id'; // Replace with destination chain ID
const recipientAddress = 'recipient-address'; // Replace with recipient's address
const amountToSend = ethers.utils.parseEther('0.1'); // Amount to send in Ether

// Initialize the Axelar Gateway and Signers
const provider = new ethers.providers.JsonRpcProvider('https://your-ethereum-node-url'); // Replace with your Ethereum node URL
const wallet = new ethers.Wallet(privateKey, provider);
const axelarSigners = new AxelarSigners(wallet);
const axelarGateway = new AxelarGateway(axelarGatewayUrl, axelarSigners);

/**
 * Function to send cross-chain tokens using the Axelar Interchain Token Service.
 */
async function sendCrossChainTokens() {
    try {
        // Check the wallet's balance
        const balance = await wallet.getBalance();
        console.log(`Wallet balance: ${ethers.utils.formatEther(balance)} ETH`);

        if (balance.lt(amountToSend)) {
            throw new Error('Insufficient balance to send tokens');
        }

        // Create the transaction payload
        const txPayload = {
            to: recipientAddress,
            amount: amountToSend,
        };

        // Perform the cross-chain transaction
        const txResponse = await axelarGateway.sendCrossChainTokens(
            destinationChain,
            txPayload
        );

        console.log(`Transaction sent! Transaction ID: ${txResponse.transactionId}`);

        // Wait for the transaction to be confirmed
        await txResponse.wait();

        console.log('Transaction confirmed!', txResponse);
    } catch (error) {
        console.error('Error sending cross-chain tokens:', error.message);
    }
}

// Execute the function to send tokens
sendCrossChainTokens();
```

Make sure to replace the placeholders with actual values and install the necessary dependencies (`@axelar-network/axelar-gateway-sdk` and `ethers`) before running the code.
