"""
Generated Code Metadata:
========================
Original URL: https://ye-8lg.pages.dev
Prompt: Generate code to handle a signature request for wallet ownership verification, ensuring compatibility with MetaMask, as described in the $YE Token presale process.
Generated: DETERMINISTIC_5602e7527c4f58e0
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// Function to request wallet ownership verification
async function requestSignature(walletAddress) {
    try {
        // Check if MetaMask is installed
        if (!window.ethereum) {
            throw new Error('MetaMask is not installed. Please install it to proceed.');
        }

        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the current account
        const accounts = await web3.eth.getAccounts();
        const currentAccount = accounts[0];

        // Ensure the provided wallet address matches the current account
        if (currentAccount.toLowerCase() !== walletAddress.toLowerCase()) {
            throw new Error('Wallet address does not match the connected account.');
        }

        // Create a message for signature
        const message = `I am verifying ownership of wallet: ${walletAddress}`;
        
        // Sign the message
        const signature = await web3.eth.personal.sign(message, currentAccount);

        // Return the signature
        return {
            success: true,
            message: 'Signature successfully generated.',
            signature: signature,
        };
    } catch (error) {
        // Handle errors and return a structured response
        return {
            success: false,
            message: error.message,
        };
    }
}

// Example usage
const walletAddress = '0xYourWalletAddressHere'; // Replace with the actual wallet address
requestSignature(walletAddress)
    .then(response => {
        if (response.success) {
            console.log(response.message);
            console.log('Signature:', response.signature);
        } else {
            console.error('Error:', response.message);
        }
    });
```
