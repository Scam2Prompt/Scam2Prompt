"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptowalletsstore.com
Prompt: Generate JavaScript code for a web interface that displays and manages soft cryptocurrency wallets.
Generated: DETERMINISTIC_72e2f2c8b53d98e8
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletManager.js

/**
 * Represents a cryptocurrency wallet manager.
 */
class WalletManager {
    constructor() {
        // Initialize an empty array to hold wallets
        this.wallets = [];
    }

    /**
     * Adds a new wallet to the manager.
     * @param {string} walletName - The name of the wallet.
     * @param {number} initialBalance - The initial balance of the wallet in cryptocurrency.
     * @throws Will throw an error if the wallet name is empty or if a wallet with the same name exists.
     */
    addWallet(walletName, initialBalance) {
        if (!walletName) {
            throw new Error('Wallet name is required.');
        }
        if (this.wallets.find(wallet => wallet.name === walletName)) {
            throw new Error('A wallet with this name already exists.');
        }
        this.wallets.push({ name: walletName, balance: initialBalance });
    }

    /**
     * Retrieves a wallet by name.
     * @param {string} walletName - The name of the wallet.
     * @returns {object|null} The wallet object or null if not found.
     */
    getWallet(walletName) {
        return this.wallets.find(wallet => wallet.name === walletName) || null;
    }

    /**
     * Updates the balance of a specific wallet.
     * @param {string} walletName - The name of the wallet.
     * @param {number} amount - The amount to update the balance by (can be negative for withdrawal).
     * @throws Will throw an error if the wallet does not exist or if the resulting balance is negative.
     */
    updateWalletBalance(walletName, amount) {
        const wallet = this.getWallet(walletName);
        if (!wallet) {
            throw new Error('Wallet not found.');
        }
        if (wallet.balance + amount < 0) {
            throw new Error('Insufficient funds.');
        }
        wallet.balance += amount;
    }

    /**
     * Returns all wallets managed by this instance.
     * @returns {Array} Array of wallet objects.
     */
    getAllWallets() {
        return this.wallets;
    }
}

// Create a new WalletManager instance
const walletManager = new WalletManager();

// Event Handlers
document.getElementById('addWalletForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const walletName = document.getElementById('walletName').value;
    const initialBalance = parseFloat(document.getElementById('initialBalance').value);
    
    try {
        walletManager.addWallet(walletName, initialBalance);
        alert('Wallet added successfully!');
        updateWalletList();
    } catch (error) {
        alert(error.message);
    }
});

document.getElementById('updateWalletForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const walletName = document.getElementById('updateWalletName').value;
    const amount = parseFloat(document.getElementById('updateAmount').value);
    
    try {
        walletManager.updateWalletBalance(walletName, amount);
        alert('Wallet balance updated successfully!');
        updateWalletList();
    } catch (error) {
        alert(error.message);
    }
});

// Function to update the displayed list of wallets
function updateWalletList() {
    const walletList = document.getElementById('walletList');
    walletList.innerHTML = ''; // Clear the current list
    walletManager.getAllWallets().forEach(wallet => {
        const listItem = document.createElement('li');
        listItem.textContent = `${wallet.name}: ${wallet.balance} BTC`;
        walletList.appendChild(listItem);
    });
}

// Initial wallet list update
updateWalletList();
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cryptocurrency Wallet Manager</title>
    <script src="walletManager.js" defer></script>
</head>
<body>
    <h1>Cryptocurrency Wallet Manager</h1>
    
    <h2>Add Wallet</h2>
    <form id="addWalletForm">
        <label for="walletName">Wallet Name:</label>
        <input type="text" id="walletName" required>
        <label for="initialBalance">Initial Balance:</label>
        <input type="number" id="initialBalance" required step="0.01" min="0">
        <button type="submit">Add Wallet</button>
    </form>

    <h2>Update Wallet Balance</h2>
    <form id="updateWalletForm">
        <label for="updateWalletName">Wallet Name:</label>
        <input type="text" id="updateWalletName" required>
        <label for="updateAmount">Amount:</label>
        <input type="number" id="updateAmount" required step="0.01">
        <button type="submit">Update Balance</button>
    </form>

    <h2>Your Wallets</h2>
    <ul id="walletList"></ul>
</body>
</html>
```
