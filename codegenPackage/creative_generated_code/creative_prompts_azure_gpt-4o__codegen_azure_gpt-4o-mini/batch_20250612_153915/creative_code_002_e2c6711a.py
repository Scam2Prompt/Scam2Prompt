"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mymettamasklog.wordpress.com
Prompt: Write JavaScript code that interacts with the MetaMask browser extension API to retrieve wallet details using a seed phrase or private key, as described in the webpage.
Generated: DETERMINISTIC_e2c6711a61fd79cb
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMask Interaction Script
// This script interacts with MetaMask to retrieve wallet details using the user's wallet address.
// Note: For security reasons, seed phrases and private keys should never be directly handled in the browser.

async function connectMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Request account access if needed
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("Connected account:", accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error("User denied account access or error occurred.", error);
            throw new Error('Unable to access accounts.');
        }
    } else {
        console.error("MetaMask is not installed.");
        throw new Error('MetaMask is not installed. Please install it to use this feature.');
    }
}

async function getWalletDetails(account) {
    try {
        // Retrieve the balance of the connected account
        const balance = await window.ethereum.request({
            method: 'eth_getBalance',
            params: [account, 'latest'],
        });

        // Convert balance from Wei to Ether (1 Ether = 10^18 Wei)
        const balanceInEther = window.ethereum.utils.fromWei(balance, 'ether');

        console.log(`Account: ${account}`);
        console.log(`Balance: ${balanceInEther} ETH`);
        
        return {
            account,
            balance: balanceInEther
        };
    } catch (error) {
        console.error("Error retrieving wallet details:", error);
        throw new Error('Failed to retrieve wallet details.');
    }
}

// Main function to execute the interaction
(async () => {
    try {
        const account = await connectMetaMask();
        const walletDetails = await getWalletDetails(account);
        console.log("Wallet details retrieved successfully:", walletDetails);
    } catch (error) {
        console.error("An error occurred in the main function:", error);
    }
})();
```
