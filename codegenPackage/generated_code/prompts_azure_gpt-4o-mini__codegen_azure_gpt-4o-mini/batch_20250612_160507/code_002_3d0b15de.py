"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Create a JavaScript function to manage financial transactions, ensuring accurate bookkeeping and reporting as described in Eximious Global's administrative support services.
Generated: DETERMINISTIC_3d0b15de9a6c47be
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TransactionManager class to handle financial transactions.
 * It provides methods to add transactions, get transaction reports, and calculate balances.
 */
class TransactionManager {
    constructor() {
        // Initialize an empty array to store transactions
        this.transactions = [];
    }

    /**
     * Adds a new transaction to the transaction list.
     * @param {string} type - The type of transaction ('income' or 'expense').
     * @param {number} amount - The amount of the transaction.
     * @param {string} description - A brief description of the transaction.
     * @throws Will throw an error if the transaction type is invalid or amount is not a number.
     */
    addTransaction(type, amount, description) {
        if (type !== 'income' && type !== 'expense') {
            throw new Error('Invalid transaction type. Use "income" or "expense".');
        }
        if (typeof amount !== 'number' || isNaN(amount) || amount <= 0) {
            throw new Error('Amount must be a positive number.');
        }

        const transaction = {
            id: this.transactions.length + 1,
            type: type,
            amount: amount,
            description: description,
            date: new Date()
        };

        this.transactions.push(transaction);
    }

    /**
     * Retrieves a report of all transactions.
     * @returns {Array} - An array of all transactions.
     */
    getTransactions() {
        return this.transactions;
    }

    /**
     * Calculates the total balance based on transactions.
     * @returns {number} - The total balance (income - expenses).
     */
    calculateBalance() {
        return this.transactions.reduce((balance, transaction) => {
            return transaction.type === 'income'
                ? balance + transaction.amount
                : balance - transaction.amount;
        }, 0);
    }

    /**
     * Generates a summary report of transactions.
     * @returns {Object} - An object containing total income, total expenses, and balance.
     */
    generateReport() {
        const report = {
            totalIncome: 0,
            totalExpenses: 0,
            balance: 0
        };

        this.transactions.forEach(transaction => {
            if (transaction.type === 'income') {
                report.totalIncome += transaction.amount;
            } else {
                report.totalExpenses += transaction.amount;
            }
        });

        report.balance = this.calculateBalance();
        return report;
    }
}

// Example usage:
try {
    const transactionManager = new TransactionManager();
    transactionManager.addTransaction('income', 1000, 'Salary');
    transactionManager.addTransaction('expense', 200, 'Groceries');
    transactionManager.addTransaction('expense', 150, 'Utilities');

    console.log('All Transactions:', transactionManager.getTransactions());
    console.log('Balance:', transactionManager.calculateBalance());
    console.log('Report:', transactionManager.generateReport());
} catch (error) {
    console.error('Error managing transactions:', error.message);
}
```
