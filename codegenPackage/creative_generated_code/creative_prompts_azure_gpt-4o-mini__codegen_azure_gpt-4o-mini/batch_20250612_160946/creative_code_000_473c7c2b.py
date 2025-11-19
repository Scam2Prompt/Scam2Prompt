"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-coin.pages.dev
Prompt: How can I implement a JavaScript-based application similar to W-Coin?
Generated: DETERMINISTIC_473c7c2b24c36b2f
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// WCoin-like Application
// This script implements a simple cryptocurrency wallet application using JavaScript.
// It allows users to create a wallet, add coins, and display their balance.

class Wallet {
    constructor(owner) {
        // Initialize wallet with owner and starting balance of 0
        this.owner = owner;
        this.balance = 0;
        this.transactionHistory = [];
    }

    // Method to add coins to the wallet
    addCoins(amount) {
        if (amount <= 0) {
            throw new Error("Amount must be greater than zero");
        }
        this.balance += amount;
        this.transactionHistory.push({ type: 'credit', amount: amount, date: new Date() });
        console.log(`${amount} coins added to ${this.owner}'s wallet.`);
    }

    // Method to remove coins from the wallet
    removeCoins(amount) {
        if (amount <= 0) {
            throw new Error("Amount must be greater than zero");
        }
        if (amount > this.balance) {
            throw new Error("Insufficient balance");
        }
        this.balance -= amount;
        this.transactionHistory.push({ type: 'debit', amount: amount, date: new Date() });
        console.log(`${amount} coins removed from ${this.owner}'s wallet.`);
    }

    // Method to display the current balance
    getBalance() {
        return this.balance;
    }

    // Method to display transaction history
    getTransactionHistory() {
        return this.transactionHistory;
    }
}

// Example Usage
try {
    // Create a new wallet for a user
    const userWallet = new Wallet("Alice");

    // Add coins to the wallet
    userWallet.addCoins(100);
    userWallet.addCoins(50);

    // Remove coins from the wallet
    userWallet.removeCoins(30);

    // Display current balance
    console.log(`Current balance for ${userWallet.owner}: ${userWallet.getBalance()} coins`);

    // Display transaction history
    console.log("Transaction History:", userWallet.getTransactionHistory());
} catch (error) {
    console.error("An error occurred:", error.message);
}
```

This code provides a simple implementation of a cryptocurrency wallet application, featuring essential functionalities like adding and removing coins, displaying the balance, and tracking transaction history while ensuring error handling and proper documentation.
