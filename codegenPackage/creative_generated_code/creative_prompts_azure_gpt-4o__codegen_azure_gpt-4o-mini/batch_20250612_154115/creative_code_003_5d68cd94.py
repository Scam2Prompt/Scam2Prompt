"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: Write code to send Ethereum tokens from a MetaMask wallet, allowing users to customize gas fees and transaction speeds.
Generated: DETERMINISTIC_5d68cd947e78b354
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';

// Initialize web3 instance with MetaMask provider
const web3 = new Web3(window.ethereum);

// Function to send Ethereum tokens
async function sendEthereumTokens(toAddress, amount, gasPrice, gasLimit) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's active Ethereum account
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0];

        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Prepare the transaction object
        const transactionObject = {
            from: fromAddress,
            to: toAddress,
            value: amountInWei,
            gas: gasLimit || 21000, // Default gas limit for simple ETH transfers
            gasPrice: gasPrice || await web3.eth.getGasPrice(), // Default to current gas price
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transactionObject);
        
        console.log('Transaction successful with hash:', txHash.transactionHash);
        return txHash.transactionHash; // Return the transaction hash

    } catch (error) {
        // Handle errors gracefully
        console.error('Error sending transaction:', error.message);
        throw new Error('Transaction failed: ' + error.message);
    }
}

// Example usage of the sendEthereumTokens function
(async () => {
    const toAddress = '0xRecipientAddressHere'; // Replace with recipient address
    const amount = 0.1; // Amount in Ether
    const gasPrice = '20000000000'; // Custom gas price in Wei (e.g., 20 Gwei)
    const gasLimit = 21000; // Optional custom gas limit

    try {
        const transactionHash = await sendEthereumTokens(toAddress, amount, gasPrice, gasLimit);
        console.log('Transaction sent! Hash:', transactionHash);
    } catch (error) {
        console.error('Failed to send tokens:', error);
    }
})();
```

**Note**: Make sure to replace `'0xRecipientAddressHere'` with the actual recipient's Ethereum address before running the code. Additionally, users must have MetaMask installed and connected to interact with this code.
