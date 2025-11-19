"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: Generate code snippets demonstrating how to adjust gas fees and customize transaction settings in MetaMask.
Generated: DETERMINISTIC_b77dc34ad82463c6
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const ethers = require('ethers');

// Function to adjust gas fees and customize transaction settings in MetaMask
async function sendTransaction(toAddress, amount, customGasPrice, customGasLimit) {
    try {
        // Ensure MetaMask is available
        if (typeof window.ethereum === 'undefined') {
            throw new Error("MetaMask is not installed. Please install it to proceed.");
        }

        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create a provider using MetaMask's provider
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Get the signer (account that will send the transaction)
        const signer = provider.getSigner();

        // Prepare the transaction object
        const transaction = {
            to: toAddress,
            value: ethers.utils.parseEther(amount.toString()), // Convert amount to wei
            gasLimit: customGasLimit || ethers.utils.hexlify(21000), // Default gas limit if not provided
            gasPrice: customGasPrice || await provider.getGasPrice() // Default gas price if not provided
        };

        // Send the transaction
        const txResponse = await signer.sendTransaction(transaction);

        // Await transaction confirmation
        const txReceipt = await txResponse.wait();

        console.log("Transaction successful with hash:", txReceipt.transactionHash);
    } catch (error) {
        // Handle errors gracefully
        console.error("Transaction failed:", error.message);
    }
}

// Example usage:
// Adjust these values as necessary
const recipientAddress = "0xYourRecipientAddressHere";
const amountToSend = 0.01; // Amount in Ether
const customGasPrice = ethers.utils.parseUnits('50', 'gwei'); // Custom gas price in gwei
const customGasLimit = ethers.utils.hexlify(21000); // Custom gas limit

// Call the function to send the transaction
sendTransaction(recipientAddress, amountToSend, customGasPrice, customGasLimit);
```
