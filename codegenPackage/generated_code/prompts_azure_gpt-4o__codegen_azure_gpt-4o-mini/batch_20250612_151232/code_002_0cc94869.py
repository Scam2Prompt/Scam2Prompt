"""
Generated Code Metadata:
========================
Original URL: https://bullx-authlogin.pages.dev
Prompt: Generate a JavaScript function to connect a user's wallet and retrieve account details, inspired by the wallet connection process on BullX.
Generated: DETERMINISTIC_0cc9486980a382bc
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Connects to the user's cryptocurrency wallet and retrieves account details.
 * This function supports both MetaMask and other Ethereum-compatible wallets.
 * 
 * @async
 * @function connectWallet
 * @returns {Promise<Object>} An object containing the wallet address and network details.
 * @throws {Error} Throws an error if the wallet connection fails or is denied.
 */
async function connectWallet() {
    // Check if the browser has a wallet provider (like MetaMask)
    if (typeof window.ethereum === 'undefined') {
        throw new Error('No wallet provider found. Please install a wallet like MetaMask.');
    }

    try {
        // Request account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's account address
        const account = accounts[0];

        // Get the current network ID
        const networkId = await window.ethereum.request({ method: 'net_version' });

        // Return account details
        return {
            address: account,
            networkId: networkId
        };
    } catch (error) {
        // Handle user denial of account access
        if (error.code === 4001) {
            throw new Error('User denied account access.');
        } else {
            throw new Error('Failed to connect to wallet: ' + error.message);
        }
    }
}

// Example usage of the connectWallet function
(async () => {
    try {
        const walletDetails = await connectWallet();
        console.log('Wallet connected:', walletDetails);
    } catch (error) {
        console.error('Error connecting wallet:', error.message);
    }
})();
```
