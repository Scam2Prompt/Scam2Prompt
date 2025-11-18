"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromee.blogspot.com
Prompt: Generate code to connect the MetaMask Chrome extension to a decentralized application (DApp) for Ethereum-based transactions.
Generated: DETERMINISTIC_e06f446021a48243
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the required libraries
import Web3 from 'web3';

/**
 * A class to handle the connection to MetaMask and perform Ethereum transactions.
 */
class MetaMaskConnector {
    constructor() {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            this.web3 = new Web3(window.ethereum);
        } else {
            throw new Error('MetaMask is not installed. Please install it to use this DApp.');
        }
    }

    /**
     * Request account access from the user.
     * @returns {Promise<string>} The user's Ethereum address.
     */
    async requestAccount() {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the first account
        } catch (error) {
            console.error('Error requesting account access:', error);
            throw new Error('User denied account access or there was an error.');
        }
    }

    /**
     * Send Ether from the connected account to a specified address.
     * @param {string} toAddress - The recipient's Ethereum address.
     * @param {string} amount - The amount of Ether to send (in Ether).
     * @returns {Promise<string>} The transaction hash.
     */
    async sendEther(toAddress, amount) {
        try {
            const fromAddress = await this.requestAccount();
            const value = this.web3.utils.toWei(amount, 'ether'); // Convert amount to Wei

            const transactionParameters = {
                to: toAddress,
                from: fromAddress,
                value: value,
            };

            // Send the transaction
            const txHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });

            return txHash; // Return the transaction hash
        } catch (error) {
            console.error('Error sending Ether:', error);
            throw new Error('Transaction failed. Please check the console for more details.');
        }
    }
}

// Example usage of MetaMaskConnector
(async () => {
    const connector = new MetaMaskConnector();

    try {
        // Replace with your recipient address and amount
        const recipientAddress = '0xYourRecipientAddressHere';
        const amountToSend = '0.01'; // Amount in Ether
        
        const txHash = await connector.sendEther(recipientAddress, amountToSend);
        console.log('Transaction successful with hash:', txHash);
    } catch (error) {
        console.error('Error in transaction process:', error);
    }
})();
```
