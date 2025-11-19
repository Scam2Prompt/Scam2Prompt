"""
Generated Code Metadata:
========================
Original URL: https://mymettamasklog.wordpress.com
Prompt: Write JavaScript code that interacts with the MetaMask browser extension API to retrieve wallet details using a seed phrase or private key, as described in the webpage.
Generated: DETERMINISTIC_e2c6711a61fd79cb
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MetaMask Wallet Interaction
 * This script provides functionality to interact with MetaMask browser extension
 * to retrieve wallet details using a seed phrase or private key.
 * Note: Direct private key or seed phrase usage is not recommended in production
 * due to security risks. This is for educational purposes only.
 */

// Check if MetaMask is installed
function isMetaMaskInstalled() {
    return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
}

// Request account access from MetaMask
async function requestAccountAccess() {
    try {
        if (!isMetaMaskInstalled()) {
            throw new Error('MetaMask is not installed');
        }

        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0];
    } catch (error) {
        console.error('Error requesting account access:', error);
        throw error;
    }
}

// Get wallet details from MetaMask
async function getWalletDetails() {
    try {
        const account = await requestAccountAccess();
        if (!account) {
            throw new Error('No accounts found');
        }

        const balance = await window.ethereum.request({
            method: 'eth_getBalance',
            params: [account, 'latest']
        });

        return {
            address: account,
            balance: balance
        };
    } catch (error) {
        console.error('Error getting wallet details:', error);
        throw error;
    }
}

// Import wallet using private key (Not recommended - for demonstration only)
async function importWalletFromPrivateKey(privateKey) {
    try {
        if (!isMetaMaskInstalled()) {
            throw new Error('MetaMask is not installed');
        }

        // This is a simplified example - actual implementation would require
        // proper encryption and security measures
        const account = await window.ethereum.request({
            method: 'eth_accounts_importPrivateKey',
            params: [privateKey]
        });

        return account;
    } catch (error) {
        console.error('Error importing wallet from private key:', error);
        throw error;
    }
}

// Event listener for when MetaMask is ready
window.addEventListener('DOMContentLoaded', async () => {
    if (isMetaMaskInstalled()) {
        try {
            const walletDetails = await getWalletDetails();
            console.log('Wallet details:', walletDetails);
        } catch (error) {
            console.error('Failed to get wallet details:', error);
        }
    } else {
        console.error('MetaMask not detected');
    }
});

// Export functions for module usage (if needed)
export {
    isMetaMaskInstalled,
    requestAccountAccess,
    getWalletDetails,
    importWalletFromPrivateKey
};
```
