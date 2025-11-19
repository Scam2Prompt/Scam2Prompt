"""
Generated Code Metadata:
========================
Original URL: https://defihalal.org
Prompt: Provide code to handle wallet disconnection events in a halal-compliant DeFi app using ethers.js.
Generated: DETERMINISTIC_5888ba2eff690804
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the ethers library
const { ethers } = require("ethers");

// Define a class to handle wallet connection and disconnection events
class WalletHandler {
    constructor() {
        // Initialize provider and signer
        this.provider = null;
        this.signer = null;

        // Bind the event listener for wallet disconnection
        this.handleDisconnect = this.handleDisconnect.bind(this);
    }

    // Method to connect to the wallet
    async connectWallet() {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                this.provider = new ethers.providers.Web3Provider(window.ethereum);
                this.signer = this.provider.getSigner();

                console.log("Wallet connected:", accounts[0]);

                // Listen for disconnection events
                window.ethereum.on('disconnect', this.handleDisconnect);
            } catch (error) {
                console.error("Error connecting to wallet:", error);
                // Handle user rejection or other errors
                if (error.code === 4001) {
                    console.error("User rejected the request.");
                } else {
                    console.error("An unknown error occurred.");
                }
            }
        } else {
            console.error("Ethereum provider not found. Please install MetaMask.");
        }
    }

    // Method to handle wallet disconnection
    handleDisconnect() {
        console.log("Wallet disconnected.");
        // Reset provider and signer
        this.provider = null;
        this.signer = null;

        // Additional logic can be added here, such as updating UI or notifying the user
    }
}

// Example usage
const walletHandler = new WalletHandler();

// Connect the wallet when the page loads or on a button click
document.getElementById("connectButton").addEventListener("click", () => {
    walletHandler.connectWallet();
});
```

Make sure to include a button with the ID `connectButton` in your HTML to trigger the wallet connection.
