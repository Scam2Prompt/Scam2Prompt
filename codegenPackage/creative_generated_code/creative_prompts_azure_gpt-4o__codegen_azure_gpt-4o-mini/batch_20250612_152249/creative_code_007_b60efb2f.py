"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portalhub.tistory.com
Prompt: Recommend best practices for implementing a secure wallet connection feature in a web application, inspired by the content on https://portalhub.tistory.com.
Generated: DETERMINISTIC_b60efb2fedf5a4b0
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletConnection.js

/**
 * WalletConnection class for managing secure wallet connections in a web application.
 */
class WalletConnection {
    constructor() {
        this.provider = null; // Stores the wallet provider
    }

    /**
     * Initializes the wallet connection
     * @throws Will throw an error if the user does not have a wallet installed
     */
    async init() {
        if (typeof window.ethereum === 'undefined') {
            throw new Error('No crypto wallet found. Please install Metamask.');
        }
        this.provider = window.ethereum;
        await this.requestAccount();
    }

    /**
     * Requests account access if needed and sets up event listeners.
     * @throws Will throw an error if account access is denied
     */
    async requestAccount() {
        try {
            const accounts = await this.provider.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
        } catch (error) {
            throw new Error('User denied account access');
        }
    }

    /**
     * Listens for account changes and handles them.
     */
    listenForAccountChange() {
        this.provider.on('accountsChanged', (accounts) => {
            if (accounts.length === 0) {
                console.error('Please connect to MetaMask.');
            } else {
                console.log('Account changed to:', accounts[0]);
            }
        });
    }

    /**
     * Listens for network changes and handles them.
     */
    listenForNetworkChange() {
        this.provider.on('chainChanged', (chainId) => {
            console.log('Network changed to:', chainId);
            // Optionally, reload the page or update state based on the new network
        });
    }

    /**
     * Disconnects the wallet connection.
     */
    disconnect() {
        this.provider = null;
        console.log('Wallet disconnected.');
    }
}

// Usage example
(async () => {
    const walletConnection = new WalletConnection();

    try {
        await walletConnection.init();
        walletConnection.listenForAccountChange();
        walletConnection.listenForNetworkChange();
    } catch (error) {
        console.error('Error connecting to wallet:', error.message);
    }
})();
```

### Notes:
- This code implements a simple wallet connection feature, specifically for Ethereum-based wallets like MetaMask.
- It includes proper error handling and ensures that the user is informed of any issues during the connection process.
- The class design encapsulates the functionality, promoting reusability and separation of concerns.
