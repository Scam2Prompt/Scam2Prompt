"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.network
Prompt: Can you provide an example of how to use the WalletConnect API for connecting to multiple wallets in a web3 application?
Generated: DETERMINISTIC_5fbe00fe92e6cc7d
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
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Define a class to manage WalletConnect connections
class WalletConnectManager {
    constructor() {
        // Initialize an array to hold active connectors
        this.connectors = [];
        this.web3Instances = [];
    }

    // Function to create a new WalletConnect provider
    async createProvider() {
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
        });

        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Return the provider instance
        return provider;
    }

    // Function to connect to a new wallet
    async connectWallet() {
        try {
            const provider = await this.createProvider();
            // Initialize Web3 instance with the provider
            const web3 = new Web3(provider);

            // Store the provider and Web3 instance
            this.connectors.push(provider);
            this.web3Instances.push(web3);

            console.log("Wallet connected successfully!");

            // Listen for session disconnection
            provider.on("disconnect", (error) => {
                this.disconnectWallet(provider);
            });

            return web3;
        } catch (error) {
            console.error("Failed to connect wallet:", error);
        }
    }

    // Function to disconnect a wallet
    disconnectWallet(provider) {
        // Remove the provider and corresponding Web3 instance
        const index = this.connectors.indexOf(provider);
        if (index > -1) {
            this.connectors.splice(index, 1);
            this.web3Instances.splice(index, 1);
        }

        console.log("Wallet disconnected successfully!");
    }

    // Function to get the connected Web3 instances
    getConnectedWeb3Instances() {
        return this.web3Instances;
    }
}

// Example usage of WalletConnectManager
(async () => {
    const walletManager = new WalletConnectManager();

    // Connect to multiple wallets
    await walletManager.connectWallet();
    await walletManager.connectWallet();

    // Retrieve and log the connected Web3 instances
    const web3s = walletManager.getConnectedWeb3Instances();
    console.log("Connected Web3 instances:", web3s);
})();
```
