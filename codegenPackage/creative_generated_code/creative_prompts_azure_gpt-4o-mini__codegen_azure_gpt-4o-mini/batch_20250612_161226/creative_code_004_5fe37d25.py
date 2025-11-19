"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: What are the key features of the MetaMask SDK that I should consider when developing my application?
Generated: DETERMINISTIC_5fe37d2584c24384
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import { MetaMaskInpageProvider } from '@metamask/providers';

// Function to initialize MetaMask
async function initMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Create a provider instance
        const provider = window.ethereum;

        try {
            // Request account access if needed
            await provider.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask is connected');
            return provider;
        } catch (error) {
            // Handle error if user denies access
            console.error('User denied account access:', error);
            throw new Error('User denied account access');
        }
    } else {
        console.error('MetaMask is not installed');
        throw new Error('MetaMask is not installed');
    }
}

// Function to get the current connected account
async function getCurrentAccount(provider) {
    const accounts = await provider.request({ method: 'eth_accounts' });
    return accounts[0]; // Return the first account
}

// Function to send a transaction
async function sendTransaction(provider, transactionParameters) {
    try {
        const txHash = await provider.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        console.log('Transaction sent:', txHash);
        return txHash; // Return the transaction hash
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transaction failed');
    }
}

// Example usage of the MetaMask SDK functions
(async () => {
    try {
        const provider = await initMetaMask();
        const account = await getCurrentAccount(provider);
        console.log('Connected account:', account);

        const transactionParameters = {
            to: '0xRecipientAddress', // Replace with the recipient address
            from: account, // The connected account
            value: '0x29a2241af62c0000', // Amount in wei (1 ETH = 0x3b9aca00)
            gas: '0x5208', // Optional, gas limit
            gasPrice: '0x3b9aca00', // Optional, gas price
        };

        // Send the transaction
        const txHash = await sendTransaction(provider, transactionParameters);
        console.log('Transaction successful with hash:', txHash);
    } catch (error) {
        console.error('Error:', error);
    }
})();
```
