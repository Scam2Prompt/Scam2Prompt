"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallett.creatorlink.net
Prompt: Explain how to use MetaMask with decentralized applications (dApps) and the benefits of this integration.
Generated: DETERMINISTIC_caef08e548653488
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMaskIntegration.js

/**
 * MetaMaskIntegration class to manage interactions with MetaMask and dApps.
 * This class provides methods to connect to MetaMask, check if it's installed,
 * and handle user account changes and network changes.
 */
class MetaMaskIntegration {
    constructor() {
        this.provider = null;
        this.accounts = [];
        this.networkId = null;

        // Bind event listeners for account and network changes
        this.handleAccountChange = this.handleAccountChange.bind(this);
        this.handleNetworkChange = this.handleNetworkChange.bind(this);
    }

    /**
     * Checks if MetaMask is installed in the browser.
     * @returns {boolean} True if MetaMask is installed, false otherwise.
     */
    isMetaMaskInstalled() {
        return typeof window.ethereum !== 'undefined';
    }

    /**
     * Connects to MetaMask and requests user accounts.
     * @returns {Promise<void>} Resolves when the connection is established.
     * @throws {Error} Throws an error if MetaMask is not installed or the user rejects the request.
     */
    async connectWallet() {
        if (!this.isMetaMaskInstalled()) {
            throw new Error('MetaMask is not installed. Please install it to use this dApp.');
        }

        try {
            // Request accounts from MetaMask
            this.accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.provider = window.ethereum;
            this.networkId = await this.provider.request({ method: 'net_version' });

            // Set up event listeners
            this.provider.on('accountsChanged', this.handleAccountChange);
            this.provider.on('chainChanged', this.handleNetworkChange);
        } catch (error) {
            console.error('Error connecting to MetaMask:', error);
            throw error;
        }
    }

    /**
     * Handles account change event from MetaMask.
     * @param {Array} newAccounts - The new list of accounts connected to MetaMask.
     */
    handleAccountChange(newAccounts) {
        // Update the accounts state
        this.accounts = newAccounts;
        console.log('Accounts changed:', this.accounts);
    }

    /**
     * Handles network change event from MetaMask.
     * @param {string} newNetworkId - The new network ID.
     */
    handleNetworkChange(newNetworkId) {
        this.networkId = newNetworkId;
        console.log('Network changed:', this.networkId);
    }

    /**
     * Retrieves the current connected accounts.
     * @returns {Array} The current connected accounts.
     */
    getAccounts() {
        return this.accounts;
    }

    /**
     * Retrieves the current network ID.
     * @returns {string} The current network ID.
     */
    getNetworkId() {
        return this.networkId;
    }
}

// Example usage
(async () => {
    const metaMaskIntegration = new MetaMaskIntegration();

    try {
        await metaMaskIntegration.connectWallet();
        console.log('Connected accounts:', metaMaskIntegration.getAccounts());
        console.log('Connected network ID:', metaMaskIntegration.getNetworkId());
    } catch (error) {
        console.error('Failed to connect to MetaMask:', error);
    }
})();
```
