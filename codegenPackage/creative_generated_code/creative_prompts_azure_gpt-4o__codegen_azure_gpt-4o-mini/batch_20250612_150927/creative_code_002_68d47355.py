"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://982e0a97.web3-site.pages.dev
Prompt: Recommend a library for managing Web3 transactions and demonstrate its usage in code, as outlined by freeCodeCamp.
Generated: DETERMINISTIC_68d47355463b6987
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
const { ethers } = require('ethers');

// Setting up provider with Infura (or another Ethereum node provider)
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');

// Define the wallet using a private key
const privateKey = 'YOUR_PRIVATE_KEY';
const wallet = new ethers.Wallet(privateKey, provider);

/**
 * Function to send Ether from one wallet to another
 * @param {string} toAddress - The address of the recipient
 * @param {string} amountInEther - The amount of Ether to send
 */
async function sendEther(toAddress, amountInEther) {
    try {
        // Convert Ether amount to Wei
        const amountInWei = ethers.utils.parseEther(amountInEther);

        // Create a transaction object
        const tx = {
            to: toAddress,
            value: amountInWei,
            gasLimit: ethers.utils.hexlify(21000), // Set gas limit for a standard transaction
            gasPrice: await provider.getGasPrice(), // Get current gas price
        };

        // Send the transaction
        const transactionResponse = await wallet.sendTransaction(tx);
        console.log(`Transaction sent! Hash: ${transactionResponse.hash}`);

        // Wait for the transaction to be mined
        const receipt = await transactionResponse.wait();
        console.log(`Transaction mined! Block Number: ${receipt.blockNumber}`);
    } catch (error) {
        console.error('Error sending transaction:', error);
    }
}

// Example usage
const recipientAddress = '0xRecipientAddressHere'; // Replace with the recipient's address
const amountToSend = '0.01'; // Amount in Ether

// Call the function to send Ether
sendEther(recipientAddress, amountToSend);
```

Make sure to replace `'YOUR_INFURA_PROJECT_ID'`, `'YOUR_PRIVATE_KEY'`, and `'0xRecipientAddressHere'` with your actual parameters. Also, ensure you handle private keys securely and never expose them in production code.
