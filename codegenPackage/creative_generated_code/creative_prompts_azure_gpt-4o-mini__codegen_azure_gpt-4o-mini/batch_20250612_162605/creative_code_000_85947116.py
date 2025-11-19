"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapptoolkit.com
Prompt: How can I use the Web3Modal SDK to connect users' wallets to my decentralized application?
Generated: DETERMINISTIC_85947116f18dbb56
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

// Define the main application class
class DApp {
    constructor() {
        // Initialize Web3Modal
        this.provider = null;
        this.web3Modal = new Web3Modal({
            network: "mainnet", // Specify the network (e.g., mainnet, rinkeby)
            cacheProvider: true, // Optional, to cache the provider
            providerOptions: {} // Optional, specify provider options for additional wallets
        });
    }

    // Function to connect wallet
    async connectWallet() {
        try {
            // Open the modal to connect wallet
            this.provider = await this.web3Modal.connect();
            // Create an ethers provider from the connected wallet
            const ethersProvider = new ethers.providers.Web3Provider(this.provider);
            // Get the signer for transaction signing
            this.signer = ethersProvider.getSigner();

            // Fetch the user's account address
            const address = await this.signer.getAddress();
            console.log(`Wallet connected: ${address}`);
            return address;
        } catch (error) {
            console.error("Failed to connect wallet:", error);
            throw new Error("Unable to connect to wallet. Please try again.");
        }
    }

    // Function to disconnect wallet
    async disconnectWallet() {
        if (this.provider) {
            await this.web3Modal.clearCachedProvider();
            this.provider = null;
            console.log("Wallet disconnected");
        }
    }
}

// Example of how to use the DApp class
(async () => {
    const dApp = new DApp();

    // Connect wallet
    try {
        const userAddress = await dApp.connectWallet();
        // You can now use userAddress for further interactions
    } catch (error) {
        console.error(error.message);
    }

    // To disconnect the wallet (called based on user action, e.g., button click)
    // await dApp.disconnectWallet();
})();
```
