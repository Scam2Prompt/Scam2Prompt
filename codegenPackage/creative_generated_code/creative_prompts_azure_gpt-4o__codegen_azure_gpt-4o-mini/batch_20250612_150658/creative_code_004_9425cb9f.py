"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-pendle.finance
Prompt: Write code to connect a dApp to MetaMask and interact with multiple crypto assets and accounts from a single interface.
Generated: DETERMINISTIC_9425cb9ff2b2f1b3
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Define the main application class
class DAppConnector {
    constructor() {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            console.log('MetaMask is installed!');
            this.web3 = new Web3(window.ethereum);
        } else {
            console.error('MetaMask is not installed. Please install it to use this dApp.');
            alert('Please install MetaMask to use this dApp.');
            return;
        }
        
        this.accounts = [];
        this.selectedAccount = null;
    }

    // Request accounts from MetaMask
    async requestAccounts() {
        try {
            // Request account access
            this.accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.selectedAccount = this.accounts[0];
            console.log('Accounts:', this.accounts);
            console.log('Selected Account:', this.selectedAccount);
        } catch (error) {
            console.error('Error fetching accounts:', error);
        }
    }

    // Method to get the balance of a specific account
    async getBalance(account) {
        try {
            const balanceWei = await this.web3.eth.getBalance(account);
            const balanceEther = this.web3.utils.fromWei(balanceWei, 'ether');
            return balanceEther;
        } catch (error) {
            console.error('Error fetching balance:', error);
            return null;
        }
    }

    // Method to send Ether from one account to another
    async sendEther(to, amount) {
        try {
            const amountWei = this.web3.utils.toWei(amount.toString(), 'ether');
            const transactionParameters = {
                to: to,
                from: this.selectedAccount,
                value: amountWei,
            };

            // Send the transaction using MetaMask
            const txHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });

            console.log('Transaction Hash:', txHash);
            return txHash;
        } catch (error) {
            console.error('Error sending Ether:', error);
            return null;
        }
    }

    // Method to handle network changes
    listenForNetworkChanges() {
        window.ethereum.on('chainChanged', (chainId) => {
            console.log('Network changed to:', chainId);
            // Optionally handle network change logic
        });
    }

    // Method to handle account changes
    listenForAccountChanges() {
        window.ethereum.on('accountsChanged', (accounts) => {
            console.log('Accounts changed:', accounts);
            this.selectedAccount = accounts[0];
            // Optionally refresh the UI or fetch new account data
        });
    }
}

// Example usage of the DAppConnector class
const dApp = new DAppConnector();
dApp.requestAccounts();
dApp.listenForNetworkChanges();
dApp.listenForAccountChanges();

// Sample interaction (get balance and send Ether)
(async () => {
    const balance = await dApp.getBalance(dApp.selectedAccount);
    console.log(`Balance of ${dApp.selectedAccount}: ${balance} ETH`);

    // Uncomment the line below to send Ether (make sure to replace with valid address and amount)
    // const txHash = await dApp.sendEther('0xRecipientAddressHere', 0.01);
})();
```
