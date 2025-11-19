"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Design a basic data structure to store the transaction history, including date, event, amount, and address, and provide a sample implementation in JavaScript.
Generated: DETERMINISTIC_9daaf92ec06472d5
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Transaction History Data Structure and Implementation
 */

class Transaction {
    /**
     * Creates a new Transaction instance
     * @param {Date} date - The date of the transaction
     * @param {string} event - Description of the transaction event
     * @param {number} amount - Transaction amount (positive for credit, negative for debit)
     * @param {string} address - Associated wallet/account address
     */
    constructor(date, event, amount, address) {
        this.date = date;
        this.event = event;
        this.amount = amount;
        this.address = address;
    }

    /**
     * Returns transaction details as an object
     * @returns {Object} Transaction details
     */
    getDetails() {
        return {
            date: this.date,
            event: this.event,
            amount: this.amount,
            address: this.address
        };
    }
}

class TransactionHistory {
    constructor() {
        this.transactions = [];
    }

    /**
     * Adds a new transaction to the history
     * @param {Date} date - Transaction date
     * @param {string} event - Transaction event description
     * @param {number} amount - Transaction amount
     * @param {string} address - Associated address
     * @throws {Error} If any parameter is invalid
     */
    addTransaction(date, event, amount, address) {
        if (!(date instanceof Date) || isNaN(date.getTime())) {
            throw new Error('Invalid date provided');
        }
        if (typeof event !== 'string' || event.trim() === '') {
            throw new Error('Event description must be a non-empty string');
        }
        if (typeof amount !== 'number' || isNaN(amount)) {
            throw new Error('Amount must be a valid number');
        }
        if (typeof address !== 'string' || address.trim() === '') {
            throw new Error('Address must be a non-empty string');
        }

        const transaction = new Transaction(date, event, amount, address);
        this.transactions.push(transaction);
    }

    /**
     * Gets all transactions sorted by date (newest first)
     * @returns {Array<Transaction>} Array of transactions
     */
    getAllTransactions() {
        return [...this.transactions].sort((a, b) => b.date - a.date);
    }

    /**
     * Gets transactions filtered by address
     * @param {string} address - Address to filter by
     * @returns {Array<Transaction>} Filtered transactions
     */
    getTransactionsByAddress(address) {
        if (typeof address !== 'string' || address.trim() === '') {
            throw new Error('Address must be a non-empty string');
        }
        return this.transactions.filter(t => t.address === address);
    }

    /**
     * Gets the total balance across all transactions
     * @returns {number} Total balance
     */
    getBalance() {
        return this.transactions.reduce((sum, t) => sum + t.amount, 0);
    }
}

// Sample Implementation
const history = new TransactionHistory();

try {
    history.addTransaction(new Date('2023-01-15'), 'Deposit', 1000, '0x123abc');
    history.addTransaction(new Date('2023-01-16'), 'Withdrawal', -200, '0x123abc');
    history.addTransaction(new Date('2023-01-17'), 'Transfer', 500, '0x456def');
    
    console.log('All Transactions:', history.getAllTransactions());
    console.log('Transactions for 0x123abc:', history.getTransactionsByAddress('0x123abc'));
    console.log('Current Balance:', history.getBalance());
} catch (error) {
    console.error('Error:', error.message);
}
```
