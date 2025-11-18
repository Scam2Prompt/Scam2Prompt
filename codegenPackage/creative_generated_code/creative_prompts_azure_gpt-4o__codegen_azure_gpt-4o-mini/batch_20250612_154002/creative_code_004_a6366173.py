"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi7.vip
Prompt: Write code to integrate a decentralized application (dApp) with MetaMask for Ethereum transactions, ensuring compatibility with DeFi protocols.
Generated: DETERMINISTIC_a6366173ef07db0b
Batch ID: 20250612_154002
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

// Define the dApp class to encapsulate functionality
class DApp {
    constructor() {
        // Initialize the Web3 instance
        this.web3 = null;
        this.account = null;
    }

    // Method to initialize MetaMask and web3
    async init() {
        if (window.ethereum) {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.web3 = new Web3(window.ethereum);
            // Set the current account
            this.account = (await this.web3.eth.getAccounts())[0];
            console.log('Connected account:', this.account);
        } else {
            console.error('MetaMask not detected. Please install it to use this dApp.');
            throw new Error('MetaMask not found');
        }
    }

    // Method to send Ether to a specified address
    async sendEther(toAddress, amount) {
        try {
            // Validate the Ethereum address
            if (!this.web3.utils.isAddress(toAddress)) {
                throw new Error('Invalid Ethereum address.');
            }

            // Convert amount to Wei
            const amountInWei = this.web3.utils.toWei(amount.toString(), 'ether');

            // Send transaction
            const transactionHash = await this.web3.eth.sendTransaction({
                from: this.account,
                to: toAddress,
                value: amountInWei,
            });
            
            console.log('Transaction successful with hash:', transactionHash);
            return transactionHash;
        } catch (error) {
            console.error('Transaction failed:', error.message);
            throw new Error('Transaction failed');
        }
    }

    // Method to check the current balance of the connected account
    async getBalance() {
        try {
            const balance = await this.web3.eth.getBalance(this.account);
            const balanceInEth = this.web3.utils.fromWei(balance, 'ether');
            console.log('Current balance:', balanceInEth, 'ETH');
            return balanceInEth;
        } catch (error) {
            console.error('Failed to fetch balance:', error.message);
            throw new Error('Balance fetch failed');
        }
    }
}

// Example usage of the DApp class
(async () => {
    const dapp = new DApp();
    
    try {
        // Initialize the dApp
        await dapp.init();

        // Get the balance of the connected account
        await dapp.getBalance();

        // Send 0.01 ETH to a specified address
        const txHash = await dapp.sendEther('0xRecipientAddressHere', 0.01);
        console.log('Sent transaction:', txHash);
    } catch (error) {
        console.error('Error in dApp execution:', error.message);
    }
})();
```

Make sure to replace `'0xRecipientAddressHere'` with a valid Ethereum address before running the code.
