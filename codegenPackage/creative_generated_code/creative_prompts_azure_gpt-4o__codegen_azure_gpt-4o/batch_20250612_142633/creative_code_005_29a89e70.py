"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-2.vip
Prompt: Provide an example of JavaScript code for signing and sending Ethereum transactions in a DeFi application using ethers.js.
Generated: DETERMINISTIC_29a89e70e9a4a557
Batch ID: 20250612_142633
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import the ethers.js library
const { ethers } = require('ethers');

// Configuration for Ethereum provider and wallet
const providerUrl = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const privateKey = 'YOUR_PRIVATE_KEY'; // Replace with your wallet's private key

// Initialize provider and wallet
const provider = new ethers.JsonRpcProvider(providerUrl);
const wallet = new ethers.Wallet(privateKey, provider);

// Example function to sign and send a transaction
async function sendTransaction(toAddress, amountInEther) {
    try {
        // Validate input
        if (!ethers.isAddress(toAddress)) {
            throw new Error('Invalid recipient address');
        }
        
        // Convert Ether amount to Wei
        const amountInWei = ethers.parseEther(amountInEther);

        // Create a transaction object
        const tx = {
            to: toAddress,
            value: amountInWei,
            gasLimit: 21000, // Typical gas limit for ETH transfers
            gasPrice: await provider.getGasPrice(), // Get current gas price
        };

        // Sign and send the transaction
        const sentTx = await wallet.sendTransaction(tx);

        console.log('Transaction sent! Hash:', sentTx.hash);

        // Wait for the transaction to be mined
        const receipt = await sentTx.wait();
        console.log('Transaction confirmed! Receipt:', receipt);

        return receipt; // Return the transaction receipt
    } catch (error) {
        console.error('Error sending transaction:', error);
    }
}

// Example usage
(async () => {
    const recipientAddress = '0xReceiverAddressHere'; // Replace with the recipient's address
    const amountToSend = '0.01'; // Amount in Ether

    const receipt = await sendTransaction(recipientAddress, amountToSend);

    if (receipt) {
        console.log('Transaction successful!');
    }
})();
```
