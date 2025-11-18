"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev-meta-mask-support0ffice.pantheonsite.io
Prompt: Recommend best practices for using MetaMask's secure login feature in a web3 application, and provide sample code for implementation.
Generated: DETERMINISTIC_81e857defa3a13eb
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import { ethers } from "ethers";

// Function to connect to MetaMask and request login
async function connectMetaMask() {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error("MetaMask is not installed. Please install it to use this feature.");
        }

        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create an ethers provider
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Get the signer (the user's account)
        const signer = provider.getSigner();

        // Fetch the user's address
        const address = await signer.getAddress();

        console.log(`Connected: ${address}`);
        return { provider, signer, address };
    } catch (error) {
        // Handle errors during connection
        console.error("Error connecting to MetaMask:", error);
        throw new Error("Failed to connect to MetaMask");
    }
}

// Function to sign a message (for secure login)
async function signMessage(signer, message) {
    try {
        const signature = await signer.signMessage(message);
        console.log(`Message signed: ${signature}`);
        return signature;
    } catch (error) {
        console.error("Error signing message:", error);
        throw new Error("Failed to sign message");
    }
}

// Function to disconnect MetaMask (optional)
function disconnectMetaMask() {
    // MetaMask does not provide a direct disconnect method, but we can clear the state
    console.log("Disconnected from MetaMask");
}

// Example usage of the functions
(async () => {
    try {
        const { signer, address } = await connectMetaMask();
        const message = `Secure login for address: ${address}`;
        
        // Sign a message as part of the secure login process
        const signature = await signMessage(signer, message);

        // Here you could send the address and signature to your backend for verification
        console.log(`User address: ${address}, Signature: ${signature}`);
    } catch (error) {
        console.error("Error in MetaMask login process:", error);
    }
})();
```
