"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-metmschrxtnsg.gitbook.io
Prompt: Create a step-by-step guide for using MetaMask's API to send Ethereum from one wallet to another within a web application.
Generated: DETERMINISTIC_d2666de0547d7d86
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary packages
import Web3 from 'web3';

// Function to initialize Web3 with MetaMask
async function initWeb3() {
    if (window.ethereum) {
        // Create a new instance of Web3 using MetaMask's provider
        const web3 = new Web3(window.ethereum);
        try {
            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("MetaMask account connected");
            return web3;
        } catch (error) {
            // Handle user denial of account access
            console.error("User denied account access:", error);
            throw new Error("User denied account access");
        }
    } else {
        // Handle the case where MetaMask is not installed
        console.error("MetaMask is not installed");
        throw new Error("MetaMask is not installed");
    }
}

// Function to send Ethereum from one wallet to another
async function sendEthereum(web3, fromAddress, toAddress, amountInEther) {
    try {
        // Convert the amount to Wei (1 Ether = 10^18 Wei)
        const amountInWei = web3.utils.toWei(amountInEther, 'ether');

        // Create the transaction object
        const transactionObject = {
            from: fromAddress,
            to: toAddress,
            value: amountInWei,
            gas: 21000, // Set a gas limit (recommended for a simple transfer)
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transactionObject);
        console.log("Transaction successful with hash:", txHash.transactionHash);
        return txHash.transactionHash;
    } catch (error) {
        // Handle errors during the transaction
        console.error("Transaction failed:", error);
        throw new Error("Transaction failed");
    }
}

// Main function to execute the transfer
async function main() {
    try {
        const web3 = await initWeb3();
        
        // Get the accounts from MetaMask
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0]; // Using the first account
        
        // Specify the recipient address and amount to send
        const toAddress = '0xRecipientAddressHere'; // Replace with the recipient address
        const amountInEther = '0.01'; // Amount to send in Ether
        
        // Call the sendEthereum function
        const transactionHash = await sendEthereum(web3, fromAddress, toAddress, amountInEther);
        
        // Log the transaction hash
        console.log("Transaction Hash:", transactionHash);
    } catch (error) {
        // Handle any errors in the main function
        console.error("An error occurred in the main function:", error);
    }
}

// Execute the main function when the script loads
main();
```

Make sure to replace `'0xRecipientAddressHere'` with the actual recipient wallet address before running the code.
