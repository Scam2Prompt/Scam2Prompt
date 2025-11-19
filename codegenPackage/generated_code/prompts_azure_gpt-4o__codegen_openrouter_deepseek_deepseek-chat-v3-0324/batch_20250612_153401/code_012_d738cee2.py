"""
Generated Code Metadata:
========================
Original URL: https://mileimoneda.pages.dev
Prompt: Create a tutorial for integrating a wallet connection feature into a cryptocurrency platform using JavaScript and web3.js, inspired by the MetaMask integration described on Milei Moneda.
Generated: DETERMINISTIC_d738cee27b6b20db
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');

// Check if Web3 is injected by MetaMask or other wallet
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
} else {
    console.error('Please install MetaMask or another Web3 provider!');
}

// Wallet connection class
class WalletConnector {
    constructor() {
        this.web3 = null;
        this.account = null;
        this.chainId = null;
    }

    /**
     * Initialize Web3 and set up event listeners
     */
    async init() {
        try {
            // Request account access if needed
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            
            // Create Web3 instance
            this.web3 = new Web3(window.ethereum);
            
            // Get current account
            this.account = accounts[0];
            
            // Get current chain ID
            this.chainId = await this.web3.eth.getChainId();
            
            // Set up event listeners
            this.setupEventListeners();
            
            console.log('Wallet connected successfully!', {
                account: this.account,
                chainId: this.chainId
            });
            
            return {
                success: true,
                account: this.account,
                chainId: this.chainId
            };
        } catch (error) {
            console.error('Error connecting wallet:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Set up event listeners for account and chain changes
     */
    setupEventListeners() {
        // Handle account changes
        window.ethereum.on('accountsChanged', (accounts) => {
            if (accounts.length === 0) {
                console.log('Please connect to MetaMask.');
                this.account = null;
            } else {
                this.account = accounts[0];
                console.log('Account changed:', this.account);
            }
        });

        // Handle chain changes
        window.ethereum.on('chainChanged', (chainId) => {
            this.chainId = parseInt(chainId, 16);
            console.log('Chain changed:', this.chainId);
            // Recommended to reload the page to avoid any issues
            window.location.reload();
        });
    }

    /**
     * Get the current account balance
     * @returns {Promise<Object>} Balance information
     */
    async getBalance() {
        try {
            if (!this.web3 || !this.account) {
                throw new Error('Wallet not connected');
            }
            
            const balance = await this.web3.eth.getBalance(this.account);
            const formattedBalance = this.web3.utils.fromWei(balance, 'ether');
            
            return {
                success: true,
                balance: formattedBalance,
                rawBalance: balance
            };
        } catch (error) {
            console.error('Error getting balance:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Send a transaction
     * @param {string} toAddress - Recipient address
     * @param {string} amount - Amount in ETH
     * @returns {Promise<Object>} Transaction result
     */
    async sendTransaction(toAddress, amount) {
        try {
            if (!this.web3 || !this.account) {
                throw new Error('Wallet not connected');
            }
            
            const value = this.web3.utils.toWei(amount, 'ether');
            const tx = {
                from: this.account,
                to: toAddress,
                value: value
            };
            
            const txHash = await this.web3.eth.sendTransaction(tx);
            
            return {
                success: true,
                transactionHash: txHash.transactionHash
            };
        } catch (error) {
            console.error('Error sending transaction:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Disconnect wallet
     */
    disconnect() {
        this.web3 = null;
        this.account = null;
        this.chainId = null;
        console.log('Wallet disconnected');
    }
}

// Example usage
document.addEventListener('DOMContentLoaded', async () => {
    const walletConnector = new WalletConnector();
    
    // Connect button click handler
    document.getElementById('connectButton').addEventListener('click', async () => {
        const result = await walletConnector.init();
        if (result.success) {
            document.getElementById('walletAddress').textContent = result.account;
            document.getElementById('networkId').textContent = result.chainId;
            
            // Get and display balance
            const balanceResult = await walletConnector.getBalance();
            if (balanceResult.success) {
                document.getElementById('balance').textContent = balanceResult.balance;
            }
        } else {
            alert(`Error: ${result.error}`);
        }
    });
    
    // Send transaction button click handler
    document.getElementById('sendButton').addEventListener('click', async () => {
        const toAddress = document.getElementById('recipientAddress').value;
        const amount = document.getElementById('sendAmount').value;
        
        if (!toAddress || !amount) {
            alert('Please enter recipient address and amount');
            return;
        }
        
        const result = await walletConnector.sendTransaction(toAddress, amount);
        if (result.success) {
            alert(`Transaction sent! Hash: ${result.transactionHash}`);
        } else {
            alert(`Error: ${result.error}`);
        }
    });
    
    // Disconnect button click handler
    document.getElementById('disconnectButton').addEventListener('click', () => {
        walletConnector.disconnect();
        document.getElementById('walletAddress').textContent = 'Not connected';
        document.getElementById('networkId').textContent = 'Not connected';
        document.getElementById('balance').textContent = '0';
    });
});
```
