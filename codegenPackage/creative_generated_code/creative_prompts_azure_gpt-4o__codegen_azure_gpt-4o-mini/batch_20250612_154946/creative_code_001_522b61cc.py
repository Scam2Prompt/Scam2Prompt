"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.marketmaking.pro
Prompt: Provide an example of how to use JavaScript to enable functionality for a financial app like MMPRO Finance.
Generated: DETERMINISTIC_522b61cc98a4b180
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// FinancialApp class to handle basic financial functionalities for MMPRO Finance
class FinancialApp {
    constructor() {
        this.transactions = [];
    }

    /**
     * Adds a new transaction to the transaction list
     * @param {string} type - The type of transaction ('income' or 'expense')
     * @param {number} amount - The amount of the transaction
     * @param {string} description - A brief description of the transaction
     * @throws Will throw an error if the transaction type is invalid
     */
    addTransaction(type, amount, description) {
        if (type !== 'income' && type !== 'expense') {
            throw new Error("Invalid transaction type. Use 'income' or 'expense'.");
        }
        if (typeof amount !== 'number' || amount <= 0) {
            throw new Error("Amount must be a positive number.");
        }
        if (typeof description !== 'string' || description.trim() === '') {
            throw new Error("Description must be a non-empty string.");
        }

        const transaction = {
            id: this.transactions.length + 1,
            type,
            amount,
            description,
            date: new Date().toISOString(),
        };

        this.transactions.push(transaction);
        console.log("Transaction added:", transaction);
    }

    /**
     * Calculates the total income
     * @returns {number} The total income amount
     */
    calculateTotalIncome() {
        return this.transactions
            .filter(tx => tx.type === 'income')
            .reduce((total, tx) => total + tx.amount, 0);
    }

    /**
     * Calculates the total expense
     * @returns {number} The total expense amount
     */
    calculateTotalExpense() {
        return this.transactions
            .filter(tx => tx.type === 'expense')
            .reduce((total, tx) => total + tx.amount, 0);
    }

    /**
     * Calculates the net balance (income - expenses)
     * @returns {number} The net balance
     */
    calculateNetBalance() {
        return this.calculateTotalIncome() - this.calculateTotalExpense();
    }

    /**
     * Displays all transactions
     */
    displayTransactions() {
        if (this.transactions.length === 0) {
            console.log("No transactions available.");
            return;
        }
        console.table(this.transactions);
    }
}

// Example usage of FinancialApp
try {
    const financeApp = new FinancialApp();

    // Adding some transactions
    financeApp.addTransaction('income', 5000, 'Salary for the month');
    financeApp.addTransaction('expense', 1500, 'Groceries');
    financeApp.addTransaction('expense', 200, 'Utilities');
    financeApp.addTransaction('income', 1200, 'Freelance project');

    // Display transactions
    financeApp.displayTransactions();

    // Calculate and display totals
    console.log("Total Income: $", financeApp.calculateTotalIncome());
    console.log("Total Expense: $", financeApp.calculateTotalExpense());
    console.log("Net Balance: $", financeApp.calculateNetBalance());
} catch (error) {
    console.error("Error occurred:", error.message);
}
```
