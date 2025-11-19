"""
Generated Code Metadata:
========================
Original URL: https://activefusionnet.vercel.app
Prompt: Provide an example of a JavaScript implementation for connecting multiple wallets (e.g., Metamask, Coinbase Wallet) in a single decentralized application.
Generated: DETERMINISTIC_0e61c51112a5eb58
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Define a class for WalletConnector
class WalletConnector {
    constructor() {
        // Initialize web3 instance
        this.web3 = null;
        this.currentAccount = null;
    }

    // Method to connect to a wallet
    async connectWallet(walletType) {
        try {
            if (walletType === 'metamask') {
                // Check if MetaMask is installed
                if (window.ethereum) {
                    this.web3 = new Web3(window.ethereum);
                    // Request account access
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    this.currentAccount = await this.getCurrentAccount();
                    console.log(`Connected to MetaMask: ${this.currentAccount}`);
                } else {
                    throw new Error('MetaMask is not installed. Please install it to use this feature.');
                }
            } else if (walletType === 'coinbase') {
                // Check if Coinbase Wallet is installed
                if (window.coinbaseWallet) {
                    this.web3 = new Web3(window.coinbaseWallet);
                    const accounts = await window.coinbaseWallet.enable();
                    this.currentAccount = accounts[0];
                    console.log(`Connected to Coinbase Wallet: ${this.currentAccount}`);
                } else {
                    throw new Error('Coinbase Wallet is not installed. Please install it to use this feature.');
                }
            } else {
                throw new Error('Unsupported wallet type. Please choose either "metamask" or "coinbase".');
            }
        } catch (error) {
            console.error('Error connecting to wallet:', error.message);
        }
    }

    // Method to get the current account
    async getCurrentAccount() {
        if (this.web3) {
            const accounts = await this.web3.eth.getAccounts();
            return accounts[0];
        }
        throw new Error('Web3 instance is not initialized.');
    }

    // Method to disconnect the wallet
    disconnectWallet() {
        this.web3 = null;
        this.currentAccount = null;
        console.log('Disconnected from wallet.');
    }
}

// Example usage
const walletConnector = new WalletConnector();

// Connect to MetaMask
document.getElementById('connect-metamask').addEventListener('click', () => {
    walletConnector.connectWallet('metamask');
});

// Connect to Coinbase Wallet
document.getElementById('connect-coinbase').addEventListener('click', () => {
    walletConnector.connectWallet('coinbase');
});

// Disconnect wallet
document.getElementById('disconnect').addEventListener('click', () => {
    walletConnector.disconnectWallet();
});
```

```html
<!-- HTML structure for wallet connection buttons -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallet Connector</title>
</head>
<body>
    <h1>Connect Your Wallet</h1>
    <button id="connect-metamask">Connect MetaMask</button>
    <button id="connect-coinbase">Connect Coinbase Wallet</button>
    <button id="disconnect">Disconnect Wallet</button>

    <script src="path/to/web3.min.js"></script>
    <script src="path/to/your-script.js"></script>
</body>
</html>
```
