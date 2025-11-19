"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Create a JavaScript function to manage financial transactions, ensuring accurate bookkeeping and reporting as described in Eximious Global's administrative support services.
Generated: DETERMINISTIC_3d0b15de9a6c47be
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * TransactionManager class to handle financial transactions with accurate bookkeeping and reporting.
 */
class TransactionManager {
    constructor() {
        // Initialize an empty array to hold transactions
        this.transactions = [];
    }

    /**
     * Adds a transaction to the ledger.
     * @param {string} description - Description of the transaction.
     * @param {number} amount - Amount of the transaction (can be negative for expenses).
     * @throws {Error} Will throw an error if amount is not a number or if it's not a finite value.
     */
    addTransaction(description, amount) {
        if (typeof amount !== 'number' || !isFinite(amount)) {
            throw new Error('Invalid amount: must be a finite number.');
        }
        
        const transaction = {
            id: this.transactions.length + 1, // Simple unique ID based on position
            description: description,
            amount: amount,
            date: new Date()
        };

        this.transactions.push(transaction);
    }

    /**
     * Calculates the total balance from all transactions.
     * @returns {number} The total balance.
     */
    getBalance() {
        return this.transactions.reduce((acc, transaction) => acc + transaction.amount, 0);
    }

    /**
     * Generates a report of all transactions.
     * @returns {Array<Object>} An array of transactions.
     */
    getTransactionReport() {
        return this.transactions.map(transaction => ({
            id: transaction.id,
            description: transaction.description,
            amount: transaction.amount,
            date: transaction.date.toISOString()
        }));
    }

    /**
     * Clears all transactions from the ledger.
     * @throws {Error} Will throw an error if there are no transactions to clear.
     */
    clearTransactions() {
        if (this.transactions.length === 0) {
            throw new Error('No transactions to clear.');
        }
        
        this.transactions = [];
    }
}

// Example usage:
const manager = new TransactionManager();

try {
    manager.addTransaction('Initial Deposit', 1000);
    manager.addTransaction('Grocery Shopping', -200);
    manager.addTransaction('Utility Bill', -150);

    console.log('Current Balance:', manager.getBalance()); // Output current balance
    console.log('Transaction Report:', manager.getTransactionReport()); // Output transaction report

    manager.clearTransactions(); // Clear all transactions
} catch (error) {
    console.error('Error:', error.message);
}
```
