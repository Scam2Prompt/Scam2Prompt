"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-audius.com
Prompt: Generate a code example for connecting a dapp to MetaMask for handling ETH transactions.
Generated: DETERMINISTIC_f15134bd26c485df
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
import Web3 from 'web3';

class EthTransactionHandler {
    constructor() {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            this.web3 = new Web3(window.ethereum);
        } else {
            console.error('MetaMask is not installed. Please install it to use this application.');
            return;
        }
    }

    // Request account access
    async requestAccount() {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.account = accounts[0]; // Set the first account
            console.log('Connected account:', this.account);
        } catch (error) {
            console.error('Error requesting account:', error);
        }
    }

    // Send ETH to a specified address
    async sendEth(toAddress, amount) {
        if (!this.account) {
            console.error('No account found. Please connect to MetaMask first.');
            return;
        }

        // Validate amount
        const amountInWei = this.web3.utils.toWei(amount.toString(), 'ether');
        if (isNaN(amountInWei) || amountInWei <= 0) {
            console.error('Invalid amount. Please enter a positive number.');
            return;
        }

        const transactionParameters = {
            to: toAddress, // Required
            from: this.account, // Must match user's active wallet address.
            value: amountInWei, // Converted amount in wei
        };

        // Send the transaction
        try {
            const txHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });
            console.log('Transaction sent! Transaction Hash:', txHash);
        } catch (error) {
            console.error('Error sending transaction:', error);
        }
    }
}

// Example usage
(async () => {
    const ethHandler = new EthTransactionHandler();
    await ethHandler.requestAccount();

    // Replace '0xRecipientAddress' with the actual recipient address and '0.01' with the amount in ETH
    await ethHandler.sendEth('0xRecipientAddress', 0.01);
})();
```
