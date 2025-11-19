"""
Generated Code Metadata:
========================
Original URL: https://open-sea-web3-app.vercel.app
Prompt: Generate code to handle wallet disconnection and display a message to the user in a Web3 app using ethers.js.
Generated: DETERMINISTIC_3abc697249f5a9d1
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the ethers library
import { ethers } from 'ethers';

// Function to initialize the Web3 provider and handle wallet connection
async function initWeb3() {
    // Check if the browser has a wallet provider (like MetaMask)
    if (typeof window.ethereum !== 'undefined') {
        // Create a new provider instance
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Request account access if needed
        try {
            await provider.send("eth_requestAccounts", []);
            console.log("Wallet connected successfully.");
        } catch (error) {
            console.error("User denied account access:", error);
            return;
        }

        // Set up event listener for wallet disconnection
        window.ethereum.on('disconnect', handleDisconnect);
    } else {
        console.error("No wallet provider found. Please install a wallet like MetaMask.");
        alert("No wallet provider found. Please install a wallet like MetaMask.");
    }
}

// Function to handle wallet disconnection
function handleDisconnect(error) {
    // Log the error for debugging purposes
    console.error("Wallet disconnected:", error);

    // Display a message to the user
    alert("Your wallet has been disconnected. Please reconnect to continue using the app.");
}

// Call the initWeb3 function to set everything up
initWeb3().catch((error) => {
    console.error("Error initializing Web3:", error);
});
```
