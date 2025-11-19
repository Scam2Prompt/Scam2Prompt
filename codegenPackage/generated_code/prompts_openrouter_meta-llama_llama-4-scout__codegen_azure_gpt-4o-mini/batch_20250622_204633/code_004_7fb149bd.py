"""
Generated Code Metadata:
========================
Original URL: https://metamaskchromee.blogspot.com
Prompt: Generate code snippets in JavaScript for interacting with the Ethereum blockchain using MetaMask Chrome, including functions for sending and receiving Ether.
Generated: DETERMINISTIC_7fb149bd6b4ce022
Batch ID: 20250622_204633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the required libraries
const Web3 = require('web3');

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to use this application.');
}

// Create a new instance of Web3 using MetaMask's provider
const web3 = new Web3(window.ethereum);

// Function to request account access
async function requestAccount() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Account access granted');
    } catch (error) {
        console.error('User denied account access:', error);
    }
}

// Function to send Ether from one account to another
async function sendEther(toAddress, amountInEther) {
    try {
        // Ensure the user has connected their account
        await requestAccount();

        // Get the user's current account
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0];

        // Convert Ether amount to Wei
        const amountInWei = web3.utils.toWei(amountInEther, 'ether');

        // Create the transaction object
        const transactionParameters = {
            to: toAddress,
            from: fromAddress,
            value: amountInWei,
            gas: '21000', // Standard gas limit for Ether transfer
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transactionParameters);
        console.log('Transaction successful with hash:', txHash.transactionHash);
    } catch (error) {
        console.error('Error sending Ether:', error);
    }
}

// Function to get the balance of an account
async function getBalance(address) {
    try {
        // Get the balance in Wei
        const balanceInWei = await web3.eth.getBalance(address);
        
        // Convert the balance to Ether
        const balanceInEther = web3.utils.fromWei(balanceInWei, 'ether');
        console.log(`Balance of ${address}: ${balanceInEther} ETH`);
        return balanceInEther;
    } catch (error) {
        console.error('Error fetching balance:', error);
    }
}

// Example usage
(async () => {
    // Request account access
    await requestAccount();

    // Replace with a valid Ethereum address
    const recipientAddress = '0xRecipientAddressHere';
    
    // Send 0.1 Ether to the recipient
    await sendEther(recipientAddress, '0.1');

    // Get the balance of the recipient
    await getBalance(recipientAddress);
})();
```
