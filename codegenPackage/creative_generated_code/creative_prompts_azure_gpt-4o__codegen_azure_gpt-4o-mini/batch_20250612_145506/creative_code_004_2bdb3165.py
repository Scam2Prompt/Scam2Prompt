"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.ro
Prompt: Provide an example of how to implement EIP-1559 transaction support in a blockchain application using MetaMask.
Generated: DETERMINISTIC_2bdb31658a2616f3
Batch ID: 20250612_145506
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

// Initialize Web3 with the provider from MetaMask
const web3 = new Web3(window.ethereum);

// Function to send an EIP-1559 transaction
async function sendEIP1559Transaction() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the current account from MetaMask
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0];

        // Define the transaction parameters
        const transactionParameters = {
            from: fromAddress, // sender's address
            to: '0xRecipientAddressHere', // recipient's address
            value: web3.utils.toHex(web3.utils.toWei('0.01', 'ether')), // amount to send in Wei
            maxFeePerGas: web3.utils.toHex(web3.utils.toWei('100', 'gwei')), // max fee per gas
            maxPriorityFeePerGas: web3.utils.toHex(web3.utils.toWei('2', 'gwei')), // max priority fee per gas
            gas: '21000', // gas limit
        };

        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log('Transaction sent successfully with hash:', txHash);
    } catch (error) {
        // Handle errors during transaction
        console.error('Transaction failed:', error.message);
    }
}

// Call the function to send the transaction
sendEIP1559Transaction();
```
