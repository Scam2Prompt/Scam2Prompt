"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqed.com
Prompt: Generate code to enable JavaScript-based wallet integration for an Ethereum DeFi application, ensuring seamless user interaction.
Generated: DETERMINISTIC_2b439b271e897c6d
Batch ID: 20250612_154002
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

// Define a class for the Ethereum wallet integration
class EthereumWallet {
    constructor() {
        // Initialize web3 instance
        this.web3 = null;
        this.account = null;
        this.init();
    }

    // Initialize the wallet connection
    async init() {
        if (window.ethereum) {
            // Use MetaMask's provider
            this.web3 = new Web3(window.ethereum);
            try {
                // Request account access if needed
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                // Get the user's account address
                const accounts = await this.web3.eth.getAccounts();
                this.account = accounts[0];
                console.log(`Connected account: ${this.account}`);
            } catch (error) {
                // Handle user rejection of account access
                console.error("User denied account access", error);
            }
        } else {
            console.error("No Ethereum provider found. Please install MetaMask.");
        }
    }

    // Function to get account balance
    async getBalance() {
        if (!this.account) {
            throw new Error("No account connected");
        }

        try {
            // Fetch the balance of the connected account
            const balanceWei = await this.web3.eth.getBalance(this.account);
            // Convert balance from Wei to Ether
            const balanceEther = this.web3.utils.fromWei(balanceWei, 'ether');
            return balanceEther;
        } catch (error) {
            console.error("Error fetching balance", error);
            throw error;
        }
    }

    // Function to send Ether to another account
    async sendEther(toAddress, amount) {
        if (!this.account) {
            throw new Error("No account connected");
        }

        try {
            // Convert amount to Wei
            const amountWei = this.web3.utils.toWei(amount.toString(), 'ether');

            // Create transaction object
            const transactionParameters = {
                to: toAddress, // Required except during contract publications.
                from: this.account, // Must match user's active account.
                value: amountWei, // Only required to send ether to the recipient from the initiating external account.
                gas: '21000', // Optional. The amount of gas to use for the transaction.
            };

            // Send the transaction
            const txHash = await this.web3.eth.sendTransaction(transactionParameters);
            console.log(`Transaction successful with hash: ${txHash.transactionHash}`);
            return txHash.transactionHash;
        } catch (error) {
            console.error("Error sending Ether", error);
            throw error;
        }
    }
}

// Create an instance of the EthereumWallet class
const wallet = new EthereumWallet();

// Example usage
(async () => {
    try {
        // Fetch account balance
        const balance = await wallet.getBalance();
        console.log(`Account balance: ${balance} ETH`);

        // Uncomment the following line to send Ether (ensure to replace with a valid address and amount)
        // const txHash = await wallet.sendEther('0xRecipientAddress', 0.01);
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
})();
```
