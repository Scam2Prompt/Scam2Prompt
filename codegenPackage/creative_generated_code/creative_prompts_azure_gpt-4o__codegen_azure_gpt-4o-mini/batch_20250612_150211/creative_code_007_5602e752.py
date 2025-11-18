"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ye-8lg.pages.dev
Prompt: Generate code to handle a signature request for wallet ownership verification, ensuring compatibility with MetaMask, as described in the $YE Token presale process.
Generated: DETERMINISTIC_5602e7527c4f58e0
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletOwnershipVerification.js

// Import necessary libraries
import Web3 from 'web3';

// Initialize Web3 with MetaMask provider
const web3 = new Web3(window.ethereum);

// Function to request signature for wallet ownership verification
async function requestWalletOwnershipSignature() {
    try {
        // Check if MetaMask is installed
        if (!window.ethereum) {
            throw new Error('MetaMask is not installed. Please install it to proceed.');
        }

        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's current account address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Define the message to be signed (you can customize this as needed)
        const message = `Verify ownership of wallet: ${userAddress} at ${new Date().toISOString()}`;

        // Request signature from the user
        const signature = await web3.eth.personal.sign(message, userAddress);

        // Return the signed message and signature
        return {
            address: userAddress,
            message: message,
            signature: signature
        };
    } catch (error) {
        // Handle errors gracefully
        console.error("Error requesting wallet ownership signature:", error);
        throw new Error('Failed to request wallet ownership verification signature.');
    }
}

// Function to validate the signature (Optional: for backend verification)
function validateSignature({ address, message, signature }) {
    // Recover the signer address from the signature
    const signerAddress = web3.eth.accounts.recover(message, signature);

    // Check if the recovered address matches the original wallet address
    return signerAddress.toLowerCase() === address.toLowerCase();
}

// Example usage of the requestWalletOwnershipSignature function
(async () => {
    try {
        const result = await requestWalletOwnershipSignature();
        console.log('Signature Request Result:', result);

        // Optionally validate the signature
        const isValid = validateSignature(result);
        console.log('Is the signature valid?', isValid);
    } catch (error) {
        console.error(error);
    }
})();
```
