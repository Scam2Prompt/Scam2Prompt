"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Create a JavaScript function to integrate a wallet connection feature for a crypto-based platform, supporting Metamask and Trust Wallet, as described in the "How to Buy $SCORP" section of Scorpion Casino.
Generated: DETERMINISTIC_daa6090142e83159
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * WalletConnect class to facilitate connection with crypto wallets
 */
class WalletConnect {
    constructor() {
        // Check if Ethereum provider is available (MetaMask or Trust Wallet)
        this.provider = window.ethereum || window.web3?.currentProvider;
        this.account = null;
        this.chainId = null;

        // Ensure the provider is available
        if (!this.provider) {
            throw new Error("No wallet provider found. Please install MetaMask or Trust Wallet.");
        }
    }

    /**
     * Initiates connection to the crypto wallet
     * @returns {Promise<string>} The connected wallet address
     * @throws Will throw an error if the connection fails
     */
    async connect() {
        try {
            // Request account access
            const accounts = await this.provider.request({ method: 'eth_requestAccounts' });
            this.account = accounts[0];

            // Get the current chain ID
            this.chainId = await this.provider.request({ method: 'eth_chainId' });

            // Return the connected account
            return this.account;
        } catch (error) {
            throw new Error(`Failed to connect to wallet: ${error.message}`);
        }
    }

    /**
     * Checks if the wallet is connected
     * @returns {boolean} True if connected, otherwise false
     */
    isConnected() {
        return this.account !== null;
    }

    /**
     * Disconnects the wallet (clears the account info)
     */
    disconnect() {
        this.account = null;
        this.chainId = null;
    }

    /**
     * Retrieves the connected account address
     * @returns {string|null} The connected wallet address or null if not connected
     */
    getAccount() {
        return this.account;
    }

    /**
     * Retrieves the current chain ID
     * @returns {string|null} The current chain ID or null if not connected
     */
    getChainId() {
        return this.chainId;
    }
}

/**
 * Usage
 */
(async () => {
    const walletConnect = new WalletConnect();

    document.getElementById('connect-button').addEventListener('click', async () => {
        try {
            const account = await walletConnect.connect();
            console.log(`Connected account: ${account}`);
            alert(`Connected to wallet: ${account}`);
        } catch (error) {
            console.error(error);
            alert(error.message);
        }
    });
})();
```

Make sure to create an HTML element with the id `connect-button` for this script to work properly.
