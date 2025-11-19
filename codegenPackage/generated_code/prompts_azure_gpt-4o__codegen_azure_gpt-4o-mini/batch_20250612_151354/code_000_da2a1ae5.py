"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Write JavaScript code to integrate a "Connect Wallet" feature for a blockchain-based FPS game, referencing the functionality described on ev.io, including wallet conversion history and crypto earning mechanisms.
Generated: DETERMINISTIC_da2a1ae5d8330251
Batch ID: 20250612_151354
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
import { ethers } from 'ethers';

// Define the ConnectWallet class
class ConnectWallet {
    constructor() {
        this.web3 = null;
        this.provider = null;
        this.account = null;
        this.networkId = null;
    }

    // Initialize the wallet connection
    async init() {
        if (window.ethereum) {
            this.provider = new ethers.providers.Web3Provider(window.ethereum);
            this.web3 = new Web3(window.ethereum);
            await this.requestAccount();
            this.networkId = await this.getNetworkId();
        } else {
            console.error("Please install MetaMask!");
            alert("Please install MetaMask!");
        }
    }

    // Request account access
    async requestAccount() {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.account = accounts[0];
            console.log(`Connected account: ${this.account}`);
        } catch (error) {
            console.error("Error requesting account:", error);
            alert("Failed to connect wallet. Please try again.");
        }
    }

    // Get the current network ID
    async getNetworkId() {
        try {
            const networkId = await this.web3.eth.net.getId();
            console.log(`Connected to network ID: ${networkId}`);
            return networkId;
        } catch (error) {
            console.error("Error fetching network ID:", error);
            throw new Error("Failed to fetch network ID.");
        }
    }

    // Fetch wallet conversion history
    async fetchConversionHistory() {
        try {
            // Placeholder for fetching conversion history from a backend API
            const response = await fetch(`/api/conversion-history?account=${this.account}`);
            if (!response.ok) {
                throw new Error("Failed to fetch conversion history.");
            }
            const history = await response.json();
            console.log("Conversion History:", history);
            return history;
        } catch (error) {
            console.error("Error fetching conversion history:", error);
            alert("Failed to fetch conversion history. Please try again later.");
        }
    }

    // Fetch crypto earnings
    async fetchCryptoEarnings() {
        try {
            // Placeholder for fetching crypto earnings from a backend API
            const response = await fetch(`/api/crypto-earnings?account=${this.account}`);
            if (!response.ok) {
                throw new Error("Failed to fetch crypto earnings.");
            }
            const earnings = await response.json();
            console.log("Crypto Earnings:", earnings);
            return earnings;
        } catch (error) {
            console.error("Error fetching crypto earnings:", error);
            alert("Failed to fetch crypto earnings. Please try again later.");
        }
    }
}

// Instantiate and initialize the ConnectWallet class
const walletConnector = new ConnectWallet();
walletConnector.init();

// Example usage of fetching conversion history and crypto earnings
document.getElementById('fetchHistoryButton').addEventListener('click', async () => {
    await walletConnector.fetchConversionHistory();
});

document.getElementById('fetchEarningsButton').addEventListener('click', async () => {
    await walletConnector.fetchCryptoEarnings();
});
```

### Notes:
- Ensure that you have the necessary libraries (`web3` and `ethers`) installed in your project.
- The API endpoints for fetching conversion history and crypto earnings are placeholders and should be replaced with actual endpoints from your backend service.
- The code includes error handling and user notifications for better user experience.
