"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-node-82f.pages.dev
Prompt: Write a code snippet to connect a mobile wallet to decentralized applications (Dapps) using the features described on the site.
Generated: DETERMINISTIC_458cb4a229ce7c02
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider';

// Function to initialize the connection to the mobile wallet
async function connectWallet() {
    // Create WalletConnect Provider
    const provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_ID", // Replace with your Infura project ID
    });

    // Check if the provider is already connected
    if (!provider.connected) {
        // Enable session (triggers QR Code modal)
        await provider.enable();
    }

    // Create a Web3 instance using the provider
    const web3 = new Web3(provider);

    // Get the user's accounts
    const accounts = await web3.eth.getAccounts();

    // Handle case where no accounts are found
    if (accounts.length === 0) {
        console.error("No accounts found. Please connect your wallet.");
        return;
    }

    // Log the connected account
    console.log("Connected account:", accounts[0]);

    // Add error handling for potential issues
    provider.on("disconnect", (error) => {
        console.error("Disconnected:", error);
    });

    provider.on("accountsChanged", (accounts) => {
        console.log("Accounts changed:", accounts);
    });

    provider.on("chainChanged", (chainId) => {
        console.log("Chain changed:", chainId);
    });

    // Return the web3 instance for further use
    return web3;
}

// Execute the connection process (to be called on a user action, like button click)
connectWallet().catch((error) => {
    console.error("Failed to connect wallet:", error);
});
```
