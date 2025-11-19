"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-defi.xyz
Prompt: Suggest a library for handling network connectivity issues in a DeFi application that uses MetaMask.
Generated: DETERMINISTIC_3b54fd0b44bb4265
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

class DeFiApp {
    constructor() {
        // Initialize web3 and provider variables
        this.web3 = null;
        this.provider = null;
    }

    /**
     * Initializes the web3 instance with MetaMask provider
     */
    async init() {
        try {
            // Check if the user has MetaMask installed
            if (typeof window.ethereum !== 'undefined') {
                this.provider = window.ethereum;
                this.web3 = new Web3(this.provider);
                console.log('MetaMask is installed!');
                
                // Request account access if needed
                await this.requestAccount();
            } else {
                console.error('MetaMask is not installed. Please install it to use this app.');
            }
        } catch (error) {
            console.error('Error initializing web3:', error);
        }
    }

    /**
     * Requests account access from MetaMask
     */
    async requestAccount() {
        try {
            // Request account access
            const accounts = await this.provider.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
        } catch (error) {
            console.error('Error requesting account access:', error);
            // Handle user rejection of account access
            if (error.code === 4001) {
                console.error('User denied account access');
            }
        }
    }

    /**
     * Checks the network connectivity and returns the current network ID
     * @returns {Promise<string|null>} The network ID or null if there is an error
     */
    async checkNetworkConnectivity() {
        try {
            const networkId = await this.web3.eth.net.getId();
            console.log('Connected to network ID:', networkId);
            return networkId;
        } catch (error) {
            console.error('Network connectivity issue:', error);
            return null;
        }
    }

    /**
     * Checks if the MetaMask is connected and handles network changes
     */
    setupEventListeners() {
        this.provider.on('accountsChanged', (accounts) => {
            console.log('Accounts changed:', accounts);
            // Handle account change logic here
        });

        this.provider.on('chainChanged', (chainId) => {
            console.log('Network changed:', chainId);
            // Handle network change logic here
            window.location.reload(); // Reload the page to update the network state
        });
    }

    /**
     * Starts the application
     */
    async start() {
        await this.init();
        const networkId = await this.checkNetworkConnectivity();
        if (networkId) {
            this.setupEventListeners();
        }
    }
}

// Initialize and start the DeFi application
const defiApp = new DeFiApp();
defiApp.start();
```
