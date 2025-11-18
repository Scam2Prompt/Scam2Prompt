"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activefusionnet.vercel.app
Prompt: Write JavaScript code to integrate Metamask wallet connection functionality into a decentralized application, referencing multichain support features.
Generated: DETERMINISTIC_256328f7d491916b
Batch ID: 20250612_152321
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

// Metamask connection functionality
class MetamaskConnector {
    constructor() {
        // Initialize Web3 instance
        this.web3 = null;
        this.currentAccount = null;
        this.networkId = null;
    }

    // Check if Metamask is installed
    async checkMetamaskInstallation() {
        if (typeof window.ethereum === 'undefined') {
            throw new Error('Metamask is not installed. Please install it to use this application.');
        }
    }

    // Connect to Metamask wallet
    async connect() {
        try {
            await this.checkMetamaskInstallation();
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.currentAccount = accounts[0];
            this.web3 = new Web3(window.ethereum);
            this.networkId = await this.web3.eth.net.getId();
            console.log(`Connected to account: ${this.currentAccount} on network id: ${this.networkId}`);
        } catch (error) {
            console.error('Failed to connect to Metamask:', error);
            throw new Error('Connection to Metamask failed. Please try again.');
        }
    }

    // Get the current account
    getCurrentAccount() {
        if (!this.currentAccount) {
            throw new Error('No account connected. Please connect to Metamask first.');
        }
        return this.currentAccount;
    }

    // Switch to a different network (multichain support)
    async switchNetwork(chainId) {
        try {
            await window.ethereum.request({
                method: 'wallet_switchEthereumChain',
                params: [{ chainId: Web3.utils.toHex(chainId) }],
            });
            this.networkId = chainId; // Update the current network id
            console.log(`Switched to network id: ${this.networkId}`);
        } catch (error) {
            console.error('Failed to switch network:', error);
            if (error.code === 4902) {
                // This error code indicates the chain is not added to Metamask
                throw new Error('This network is not available in your Metamask. Please add it first.');
            }
            throw new Error('Network switch failed. Please try again.');
        }
    }
}

// Example usage
(async () => {
    const metamaskConnector = new MetamaskConnector();

    try {
        // Connecting to Metamask
        await metamaskConnector.connect();

        // Fetch and log the current account
        const account = metamaskConnector.getCurrentAccount();
        console.log(`Current account: ${account}`);

        // Switch to an example network (e.g., Binance Smart Chain Mainnet)
        await metamaskConnector.switchNetwork(56); // BSC Mainnet ID
    } catch (error) {
        console.error('Error:', error.message);
    }
})();
```
