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
 * FinancialTransactionManager - A class to manage financial transactions with bookkeeping and reporting capabilities.
 */
class FinancialTransactionManager {
    /**
     * Initializes the FinancialTransactionManager with an empty ledger.
     */
    constructor() {
        this.ledger = [];
        this.categories = new Set();
    }

    /**
     * Adds a new transaction to the ledger.
     * @param {string} id - Unique identifier for the transaction.
     * @param {string} description - Description of the transaction.
     * @param {number} amount - Transaction amount (positive for income, negative for expense).
     * @param {string} category - Transaction category.
     * @param {Date} date - Date of the transaction.
     * @throws {Error} If required fields are missing or invalid.
     */
    addTransaction(id, description, amount, category, date = new Date()) {
        if (!id || !description || amount === undefined || !category) {
            throw new Error('Missing required transaction fields');
        }

        if (typeof amount !== 'number' || isNaN(amount)) {
            throw new Error('Amount must be a valid number');
        }

        if (this.ledger.some(t => t.id === id)) {
            throw new Error('Transaction ID must be unique');
        }

        const transaction = {
            id,
            description,
            amount,
            category,
            date: date instanceof Date ? date : new Date(date),
            timestamp: new Date()
        };

        this.ledger.push(transaction);
        this.categories.add(category);
    }

    /**
     * Gets all transactions in the ledger.
     * @returns {Array} Array of all transactions.
     */
    getAllTransactions() {
        return [...this.ledger];
    }

    /**
     * Gets transactions filtered by category.
     * @param {string} category - Category to filter by.
     * @returns {Array} Array of filtered transactions.
     */
    getTransactionsByCategory(category) {
        if (!this.categories.has(category)) {
            return [];
        }
        return this.ledger.filter(t => t.category === category);
    }

    /**
     * Gets transactions within a date range.
     * @param {Date} startDate - Start date of range.
     * @param {Date} endDate - End date of range.
     * @returns {Array} Array of filtered transactions.
     */
    getTransactionsByDateRange(startDate, endDate) {
        const start = new Date(startDate);
        const end = new Date(endDate);
        return this.ledger.filter(t => {
            const transactionDate = new Date(t.date);
            return transactionDate >= start && transactionDate <= end;
        });
    }

    /**
     * Calculates the total balance.
     * @returns {number} Sum of all transaction amounts.
     */
    getBalance() {
        return this.ledger.reduce((sum, t) => sum + t.amount, 0);
    }

    /**
     * Generates a financial report.
     * @param {Date} startDate - Optional start date for report period.
     * @param {Date} endDate - Optional end date for report period.
     * @returns {Object} Financial report containing summary and categorized data.
     */
    generateReport(startDate, endDate) {
        const transactions = startDate && endDate 
            ? this.getTransactionsByDateRange(startDate, endDate) 
            : this.getAllTransactions();

        const totalIncome = transactions
            .filter(t => t.amount > 0)
            .reduce((sum, t) => sum + t.amount, 0);

        const totalExpenses = transactions
            .filter(t => t.amount < 0)
            .reduce((sum, t) => sum + Math.abs(t.amount), 0);

        const netBalance = totalIncome - totalExpenses;

        const categories = {};
        this.categories.forEach(category => {
            const categoryTransactions = transactions.filter(t => t.category === category);
            const categoryTotal = categoryTransactions.reduce((sum, t) => sum + t.amount, 0);
            categories[category] = {
                count: categoryTransactions.length,
                total: categoryTotal,
                percentage: (Math.abs(categoryTotal) / (totalIncome + totalExpenses)) * 100 || 0
            };
        });

        return {
            period: {
                start: startDate || new Date(Math.min(...this.ledger.map(t => new Date(t.date)))),
                end: endDate || new Date(Math.max(...this.ledger.map(t => new Date(t.date))))
            },
            summary: {
                totalTransactions: transactions.length,
                totalIncome,
                totalExpenses,
                netBalance
            },
            categories
        };
    }

    /**
     * Exports ledger data to CSV format.
     * @returns {string} CSV formatted string of all transactions.
     */
    exportToCSV() {
        const headers = ['ID', 'Date', 'Description', 'Amount', 'Category'];
        const rows = this.ledger.map(t => [
            t.id,
            t.date.toISOString().split('T')[0],
            `"${t.description.replace(/"/g, '""')}"`,
            t.amount,
            t.category
        ]);

        return [headers, ...rows]
            .map(row => row.join(','))
            .join('\n');
    }
}

// Example usage:
// const ftm = new FinancialTransactionManager();
// ftm.addTransaction('t1', 'Client Payment', 1000, 'Income');
// ftm.addTransaction('t2', 'Office Supplies', -50, 'Expenses');
// console.log(ftm.generateReport());
```
