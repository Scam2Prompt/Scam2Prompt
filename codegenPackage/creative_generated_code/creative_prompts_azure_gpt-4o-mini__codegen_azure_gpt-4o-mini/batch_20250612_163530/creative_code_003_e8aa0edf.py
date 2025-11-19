"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-audius.com
Prompt: Provide an example of how to implement security features like Wallet Guard using MetaMask.
Generated: DETERMINISTIC_e8aa0edf6dc3bccc
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';

// Define a WalletGuard class for managing wallet security features
class WalletGuard {
    constructor() {
        this.web3 = null;
        this.provider = null;
    }

    // Initializes the wallet and detects MetaMask
    async init() {
        try {
            // Detecting Ethereum provider (MetaMask)
            this.provider = await detectEthereumProvider();

            if (!this.provider) {
                throw new Error('Please install MetaMask!');
            }

            // Create a new Web3 instance using the detected provider
            this.web3 = new Web3(this.provider);

            // Request account access if needed
            await this.requestAccountAccess();
            console.log('WalletGuard initialized and MetaMask is connected.');
        } catch (error) {
            console.error('Error initializing WalletGuard:', error.message);
        }
    }

    // Requests the user to connect their MetaMask account
    async requestAccountAccess() {
        try {
            // Request account access
            const accounts = await this.provider.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error('Unable to access accounts:', error.message);
            throw error;
        }
    }

    // Method to send a transaction securely
    async sendTransaction(toAddress, amount) {
        try {
            const accounts = await this.web3.eth.getAccounts();

            if (accounts.length === 0) {
                throw new Error('No accounts found. Please connect your wallet.');
            }

            const transactionParameters = {
                to: toAddress, // Required except during contract publications.
                from: accounts[0], // Must match user's active address.
                value: this.web3.utils.toHex(this.web3.utils.toWei(amount, 'ether')), // Converted to hex.
            };

            // Send the transaction
            const txHash = await this.provider.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });

            console.log('Transaction sent with hash:', txHash);
            return txHash;
        } catch (error) {
            console.error('Error sending transaction:', error.message);
            throw error;
        }
    }
}

// Example usage of WalletGuard
(async () => {
    const walletGuard = new WalletGuard();
    await walletGuard.init();

    // Sending a transaction as an example
    try {
        const hash = await walletGuard.sendTransaction('0xRecipientAddressHere', '0.01');
        console.log('Transaction successful with hash:', hash);
    } catch (error) {
        console.error('Transaction failed:', error.message);
    }
})();
```

In this code, we implement a `WalletGuard` class to manage wallet security features using MetaMask. The code includes wallet initialization, account access request, and secure transaction sending, with appropriate error handling and comments.
