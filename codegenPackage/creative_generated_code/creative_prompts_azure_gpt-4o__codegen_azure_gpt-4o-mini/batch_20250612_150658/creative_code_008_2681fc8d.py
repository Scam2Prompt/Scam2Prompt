"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-yearn.com
Prompt: Provide an example of using MetaMask to configure transaction details for privacy-first Web3 interactions. Include code for setting custom terms for data sharing.
Generated: DETERMINISTIC_2681fc8daf32cbbd
Batch ID: 20250612_150658
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

// Initialize Web3 with MetaMask provider
if (typeof window.ethereum !== 'undefined') {
    const web3 = new Web3(window.ethereum);
} else {
    console.error("MetaMask is not installed. Please install MetaMask to use this application.");
}

// Function to request account access
async function requestAccount() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Account access granted");
    } catch (error) {
        console.error("User denied account access:", error);
    }
}

// Function to configure transaction details
async function configureTransaction(toAddress, amountInEther, customTerms) {
    try {
        // Ensure the user has granted access to their accounts
        await requestAccount();

        // Get the current account
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0];

        // Create the transaction object
        const transaction = {
            from: fromAddress,
            to: toAddress,
            value: web3.utils.toWei(amountInEther, 'ether'), // Convert ether to wei
            gas: 21000, // Default gas limit for simple transactions
            gasPrice: await web3.eth.getGasPrice(), // Automatically fetch current gas price
        };

        // Apply custom terms for data sharing (this is an example, actual implementation may vary)
        const transactionWithTerms = {
            ...transaction,
            customTerms: customTerms,
        };

        // Send the transaction
        const transactionHash = await web3.eth.sendTransaction(transactionWithTerms);
        console.log("Transaction successful with hash:", transactionHash);
    } catch (error) {
        console.error("Transaction failed:", error);
    }
}

// Example usage of the configureTransaction function
const toAddress = '0xYourRecipientAddressHere'; // Replace with the recipient address
const amountInEther = '0.01'; // Amount to send in Ether
const customTerms = {
    allowDataSharing: false, // User's preference for data sharing
    purpose: 'Donation', // Purpose of the transaction
};

// Call the function to configure and send the transaction
configureTransaction(toAddress, amountInEther, customTerms);
```
