"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tru1plus.com
Prompt: Generate a JavaScript script to initialize and interact with a blockchain system, similar to the requirements of Tru1Plus.
Generated: DETERMINISTIC_f09509e3216ee054
Batch ID: 20250612_150316
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.blockchain.provider": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries for blockchain interaction
const Web3 = require('web3');

// Define the Blockchain class to encapsulate blockchain interactions
class Blockchain {
    constructor(providerUrl) {
        // Initialize Web3 with a provider
        this.web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));
        this.account = null;
    }

    /**
     * Set the account to be used for transactions
     * @param {string} accountAddress - The address of the account
     */
    setAccount(accountAddress) {
        if (this.web3.utils.isAddress(accountAddress)) {
            this.account = accountAddress;
        } else {
            throw new Error('Invalid account address');
        }
    }

    /**
     * Retrieve the balance of the currently set account
     * @returns {Promise<string>} - Balance in Ether
     */
    async getBalance() {
        if (!this.account) {
            throw new Error('Account is not set');
        }

        try {
            const balanceWei = await this.web3.eth.getBalance(this.account);
            return this.web3.utils.fromWei(balanceWei, 'ether');
        } catch (error) {
            console.error('Error fetching balance:', error);
            throw new Error('Failed to fetch balance');
        }
    }

    /**
     * Send Ether from the currently set account to a specified address
     * @param {string} toAddress - The recipient's address
     * @param {string} amount - Amount to send in Ether
     * @returns {Promise<string>} - Transaction hash
     */
    async sendEther(toAddress, amount) {
        if (!this.account) {
            throw new Error('Account is not set');
        }

        if (!this.web3.utils.isAddress(toAddress)) {
            throw new Error('Invalid recipient address');
        }

        const amountWei = this.web3.utils.toWei(amount, 'ether');

        const transaction = {
            from: this.account,
            to: toAddress,
            value: amountWei,
            gas: 2000000, // Adjust gas limit as needed
        };

        try {
            const txHash = await this.web3.eth.sendTransaction(transaction);
            return txHash.transactionHash;
        } catch (error) {
            console.error('Error sending Ether:', error);
            throw new Error('Failed to send Ether');
        }
    }
}

// Example usage
(async () => {
    // Replace with your blockchain provider URL and account address
    const providerUrl = 'https://your.blockchain.provider';
    const blockchain = new Blockchain(providerUrl);

    try {
        const myAccount = '0xYourAccountAddress'; // Your account address
        blockchain.setAccount(myAccount);

        const balance = await blockchain.getBalance();
        console.log(`Balance: ${balance} ETH`);

        const recipientAddress = '0xRecipientAddress'; // Replace with recipient address
        const amountToSend = '0.1'; // Amount in ETH

        const transactionHash = await blockchain.sendEther(recipientAddress, amountToSend);
        console.log(`Transaction successful with hash: ${transactionHash}`);
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
})();
```
