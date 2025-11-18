"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venus-protocol-ipfs.4everland.app
Prompt: Generate code to integrate Venus Protocol's DeFi features into a wallet application for managing lending and borrowing on the BNB Chain.
Generated: DETERMINISTIC_96bfcb713f3af477
Batch ID: 20250612_145117
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.venus.io/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
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
// Import necessary libraries
const axios = require('axios');
const Web3 = require('web3');

// Constants for Venus Protocol API
const VENUS_API_URL = 'https://api.venus.io/v1';
const BNB_CHAIN_RPC_URL = 'https://bsc-dataseed.binance.org/';

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(BNB_CHAIN_RPC_URL));

// Wallet management class
class WalletManager {
    constructor(walletAddress, privateKey) {
        this.walletAddress = walletAddress;
        this.privateKey = privateKey;
        this.contracts = {};
    }

    // Fetch the current supply and borrow rates from Venus Protocol
    async fetchRates() {
        try {
            const response = await axios.get(`${VENUS_API_URL}/markets`);
            return response.data.markets;
        } catch (error) {
            console.error("Error fetching rates: ", error);
            throw new Error("Failed to fetch rates from Venus Protocol.");
        }
    }

    // Supply assets to Venus Protocol
    async supply(asset, amount) {
        try {
            // Assume `supplyToContract` is a method that interacts with the Venus Protocol contract
            const tx = await this.supplyToContract(asset, amount);
            return tx;
        } catch (error) {
            console.error("Error supplying asset: ", error);
            throw new Error("Failed to supply asset.");
        }
    }

    // Borrow assets from Venus Protocol
    async borrow(asset, amount) {
        try {
            // Assume `borrowFromContract` is a method that interacts with the Venus Protocol contract
            const tx = await this.borrowFromContract(asset, amount);
            return tx;
        } catch (error) {
            console.error("Error borrowing asset: ", error);
            throw new Error("Failed to borrow asset.");
        }
    }

    // Example method to supply to the contract (to be implemented)
    async supplyToContract(asset, amount) {
        // Implementation to interact with the smart contract would go here
        // For example purposes, we assume this function interacts with the Venus contract
        console.log(`Supplying ${amount} of ${asset} to Venus Protocol`);
        return 'Transaction Successful'; // Placeholder
    }

    // Example method to borrow from the contract (to be implemented)
    async borrowFromContract(asset, amount) {
        // Implementation to interact with the smart contract would go here
        // For example purposes, we assume this function interacts with the Venus contract
        console.log(`Borrowing ${amount} of ${asset} from Venus Protocol`);
        return 'Transaction Successful'; // Placeholder
    }
}

// Example usage of WalletManager
(async () => {
    try {
        const walletAddress = 'your_wallet_address_here';
        const privateKey = 'your_private_key_here';
        const walletManager = new WalletManager(walletAddress, privateKey);
        
        // Fetching rates
        const rates = await walletManager.fetchRates();
        console.log(rates);

        // Supply and borrow examples (amounts and assets would be based on real user input)
        const supplyTx = await walletManager.supply('BNB', 1);
        console.log(supplyTx);

        const borrowTx = await walletManager.borrow('BNB', 0.5);
        console.log(borrowTx);
    } catch (error) {
        console.error("An error occurred: ", error);
    }
})();
```

> **Note:** This code assumes that the methods for interacting with the actual Venus Protocol smart contracts (`supplyToContract` and `borrowFromContract`) would be defined with proper ABI and contract address references. The code also needs proper wallet handling and secure private key management for production readiness.
