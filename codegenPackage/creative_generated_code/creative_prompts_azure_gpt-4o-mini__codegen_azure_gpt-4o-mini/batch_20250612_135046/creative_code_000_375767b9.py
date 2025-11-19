"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.network
Prompt: How can I implement WalletConnect in my dApp to enhance user experience and facilitate wallet connections?
Generated: DETERMINISTIC_375767b9526a25c1
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider
import Web3 from "web3"; // Web3.js library

// Initialize variables
let provider; // WalletConnect provider instance
let web3; // Web3 instance

// Function to initialize WalletConnect
async function initWalletConnect() {
    try {
        // Create a new WalletConnect provider
        provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID", // Replace with your Infura project ID
        });

        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Create a Web3 instance with the WalletConnect provider
        web3 = new Web3(provider);

        console.log("WalletConnect initialized successfully");
    } catch (error) {
        console.error("Error initializing WalletConnect:", error);
        // Handle initialization error (e.g., notify the user)
    }
}

// Function to get the connected account
async function getAccount() {
    try {
        // Get the accounts from the provider
        const accounts = await web3.eth.getAccounts();
        if (accounts.length > 0) {
            console.log("Connected account:", accounts[0]);
            return accounts[0];
        } else {
            console.warn("No accounts found");
            return null;
        }
    } catch (error) {
        console.error("Error fetching account:", error);
        // Handle account fetching error (e.g., notify the user)
    }
}

// Function to disconnect the wallet
async function disconnectWallet() {
    try {
        // Close the provider connection
        await provider.disconnect();
        console.log("Wallet disconnected successfully");
    } catch (error) {
        console.error("Error disconnecting wallet:", error);
        // Handle disconnection error (e.g., notify the user)
    }
}

// Event listener for account change
provider.on("accountsChanged", (accounts) => {
    console.log("Accounts changed:", accounts);
});

// Event listener for chain change
provider.on("chainChanged", (chainId) => {
    console.log("Chain changed:", chainId);
});

// Event listener for session disconnection
provider.on("disconnect", (code, reason) => {
    console.log("Wallet disconnected:", code, reason);
});

// Export functions for use in your application
export { initWalletConnect, getAccount, disconnectWallet };
```
