"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-crystaldashsss.pages.dev
Prompt: Generate JavaScript code to implement wallet scanning functionality for connecting to dApps, as outlined in the CrystalDash portal documentation.
Generated: DETERMINISTIC_249670ce202e72b6
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// WalletScanner.js

/**
 * WalletScanner class to handle wallet connection and dApp interactions
 */
class WalletScanner {
    constructor() {
        this.provider = null;
    }

    /**
     * Initialize the wallet connection
     * @returns {Promise<void>}
     */
    async init() {
        // Check if the browser has a wallet provider
        if (typeof window.ethereum !== 'undefined') {
            this.provider = window.ethereum;
            console.log('Ethereum wallet found');
        } else {
            console.error('No Ethereum wallet found. Please install a wallet like MetaMask.');
            throw new Error('No wallet provider found');
        }
    }

    /**
     * Request connection to the wallet
     * @returns {Promise<string>} - The connected account address
     */
    async connectWallet() {
        try {
            // Request account access
            const accounts = await this.provider.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error('Failed to connect wallet:', error);
            throw new Error('Failed to connect wallet');
        }
    }

    /**
     * Check if the wallet is connected
     * @returns {Promise<boolean>}
     */
    async isConnected() {
        try {
            const accounts = await this.provider.request({ method: 'eth_accounts' });
            return accounts.length > 0;
        } catch (error) {
            console.error('Failed to check wallet connection:', error);
            return false;
        }
    }

    /**
     * Listen for account changes
     * @param {function} callback - Function to call when account changes
     */
    onAccountChange(callback) {
        if (this.provider) {
            this.provider.on('accountsChanged', (accounts) => {
                console.log('Account changed:', accounts[0]);
                callback(accounts[0]);
            });
        } else {
            console.error('Provider not initialized. Please call init() first.');
        }
    }

    /**
     * Listen for network changes
     * @param {function} callback - Function to call when network changes
     */
    onNetworkChange(callback) {
        if (this.provider) {
            this.provider.on('chainChanged', (chainId) => {
                console.log('Network changed to:', chainId);
                callback(chainId);
            });
        } else {
            console.error('Provider not initialized. Please call init() first.');
        }
    }
}

// Usage example
(async () => {
    const walletScanner = new WalletScanner();
    try {
        await walletScanner.init();
        const account = await walletScanner.connectWallet();
        console.log('Successfully connected to account:', account);

        walletScanner.onAccountChange((newAccount) => {
            console.log('New account:', newAccount);
        });

        walletScanner.onNetworkChange((newChainId) => {
            console.log('Network changed to:', newChainId);
        });
    } catch (error) {
        console.error('Error occurred:', error);
    }
})();
```
