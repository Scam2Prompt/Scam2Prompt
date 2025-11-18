"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-lnds.pages.dev
Prompt: Create a function in JavaScript to connect a dApp with a Coinbase Wallet using the wallet's browser extension, as outlined on the webpage.
Generated: DETERMINISTIC_66f461be5dcb7849
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connects a decentralized application (dApp) to the Coinbase Wallet using the wallet's browser extension.
 * 
 * @async
 * @function connectCoinbaseWallet
 * @returns {Promise<void>} - Returns a promise that resolves if the connection is successful, or rejects with an error.
 * 
 * @throws {Error} - Throws an error if the Coinbase Wallet extension is not installed or connection fails.
 */
async function connectCoinbaseWallet() {
    try {
        // Check if Coinbase Wallet is installed
        if (typeof window.coinbase !== 'undefined') {
            // Request account access
            const accounts = await window.coinbase.request({ method: 'eth_requestAccounts' });

            // Check if accounts were returned
            if (accounts.length === 0) {
                throw new Error('No accounts found. Please ensure you have connected your Coinbase Wallet.');
            }

            // Log the connected account
            console.log('Connected to Coinbase Wallet account:', accounts[0]);
            
            // Optionally, you can set up a listener for account changes
            window.coinbase.on('accountsChanged', (newAccounts) => {
                console.log('Accounts changed:', newAccounts);
            });

            // Optionally, you can set up a listener for network changes
            window.coinbase.on('chainChanged', (chainId) => {
                console.log('Chain changed to:', chainId);
            });
        } else {
            throw new Error('Coinbase Wallet extension is not installed. Please install it to connect.');
        }
    } catch (error) {
        // Handle errors gracefully
        console.error('Failed to connect to Coinbase Wallet:', error.message);
        throw error; // Re-throw the error for further handling if needed
    }
}
```
