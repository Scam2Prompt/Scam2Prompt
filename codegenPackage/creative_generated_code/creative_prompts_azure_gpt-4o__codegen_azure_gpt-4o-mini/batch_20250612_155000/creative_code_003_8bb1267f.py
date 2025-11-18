"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercgc.com
Prompt: Provide an example of JavaScript code that integrates ETH 2.0 functionality into a web application.
Generated: DETERMINISTIC_8bb1267fd84fe0e5
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

/**
 * EthereumService class to handle Ethereum interactions
 */
class EthereumService {
    constructor() {
        // Initialize web3 with a provider
        this.web3 = new Web3(window.ethereum); // Assumes MetaMask is installed
        this.account = null;
    }

    /**
     * Request account access if needed
     * @returns {Promise<void>}
     */
    async requestAccount() {
        try {
            // Request account access from the user
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.account = accounts[0];
            console.log('Account connected:', this.account);
        } catch (error) {
            console.error('User rejected the request:', error);
            throw error; // Rethrow the error after logging
        }
    }

    /**
     * Get the balance of the connected account
     * @returns {Promise<string>} The balance in Ether
     */
    async getBalance() {
        if (!this.account) {
            throw new Error('Account not connected. Please request account access first.');
        }
        try {
            const balanceWei = await this.web3.eth.getBalance(this.account);
            return this.web3.utils.fromWei(balanceWei, 'ether'); // Convert Wei to Ether
        } catch (error) {
            console.error('Error fetching balance:', error);
            throw error; // Rethrow the error after logging
        }
    }

    /**
     * Send Ether to another address
     * @param {string} to - The recipient address
     * @param {string} amount - The amount in Ether to send
     * @returns {Promise<string>} Transaction hash
     */
    async sendEther(to, amount) {
        if (!this.account) {
            throw new Error('Account not connected. Please request account access first.');
        }
        try {
            const valueWei = this.web3.utils.toWei(amount, 'ether');
            const transactionParameters = {
                to: to,
                from: this.account,
                value: valueWei,
            };

            // Send transaction
            const txHash = await this.web3.eth.sendTransaction(transactionParameters);
            console.log('Transaction successful with hash:', txHash.transactionHash);
            return txHash.transactionHash;
        } catch (error) {
            console.error('Error sending Ether:', error);
            throw error; // Rethrow the error after logging
        }
    }
}

// Example usage of the EthereumService class
(async () => {
    const ethService = new EthereumService();

    try {
        // Request user account access
        await ethService.requestAccount();

        // Get the balance of the connected account
        const balance = await ethService.getBalance();
        console.log('Current balance:', balance, 'ETH');

        // Example of sending Ether (replace with a real recipient address and amount)
        // const recipientAddress = '0xRecipientAddressHere';
        // const amountToSend = '0.01'; // Amount in Ether
        // const txHash = await ethService.sendEther(recipientAddress, amountToSend);
        // console.log('Transaction hash:', txHash);
    } catch (error) {
        console.error('Ethereum service error:', error);
    }
})();
```

**Note:** Before running this code, ensure that you have MetaMask installed and set up in your browser. Replace `0xRecipientAddressHere` and `0.01` with actual values when sending Ether.
