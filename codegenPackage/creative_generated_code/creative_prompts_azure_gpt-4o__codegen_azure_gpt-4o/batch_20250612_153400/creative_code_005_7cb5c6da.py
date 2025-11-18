"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://f-money.pages.dev
Prompt: Write code to implement a budgeting tool in JavaScript, inspired by the features of the fMoney app.
Generated: DETERMINISTIC_7cb5c6da6d1d989a
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Budgeting Tool inspired by fMoney
 * Features:
 * - Add income and expenses
 * - View summary of total income, total expenses, and balance
 * - Optional categorization for income and expenses
 * - Error handling for invalid inputs
 * 
 * Author: Professional Developer
 * Date: YYYY-MM-DD
 */

class BudgetingTool {
  constructor() {
    this.transactions = []; // Array to store all transactions (income and expenses)
  }

  /**
   * Adds an income or expense transaction.
   * @param {string} type - 'income' or 'expense'.
   * @param {number} amount - Positive numeric value for the transaction amount.
   * @param {string} [category] - Optional category for the transaction.
   * @throws Will throw an error if type or amount is invalid.
   */
  addTransaction(type, amount, category = null) {
    if (type !== 'income' && type !== 'expense') {
      throw new Error("Invalid transaction type. Must be 'income' or 'expense'.");
    }
    if (typeof amount !== 'number' || amount <= 0) {
      throw new Error('Transaction amount must be a positive number.');
    }

    const transaction = {
      id: this.#generateID(),
      type,
      amount,
      category,
      date: new Date()
    };
    this.transactions.push(transaction);
  }

  /**
   * Generates a summary of the budget.
   * @returns {object} Summary containing total income, total expenses, and balance.
   */
  getSummary() {
    const totalIncome = this.transactions
      .filter(txn => txn.type === 'income')
      .reduce((sum, txn) => sum + txn.amount, 0);

    const totalExpenses = this.transactions
      .filter(txn => txn.type === 'expense')
      .reduce((sum, txn) => sum + txn.amount, 0);

    return {
      totalIncome,
      totalExpenses,
      balance: totalIncome - totalExpenses
    };
  }

  /**
   * Lists all transactions.
   * @returns {Array} Array of all transactions.
   */
  listTransactions() {
    return this.transactions;
  }

  /**
   * Deletes a transaction by ID.
   * @param {string} transactionID - The ID of the transaction to delete.
   * @returns {boolean} True if deletion was successful, false otherwise.
   */
  deleteTransaction(transactionID) {
    const initialLength = this.transactions.length;
    this.transactions = this.transactions.filter(txn => txn.id !== transactionID);
    return this.transactions.length < initialLength; // True if a transaction was deleted
  }

  /**
   * Generates a unique ID for each transaction.
   * @returns {string} A unique transaction ID.
   */
  #generateID() {
    return (
      Date.now().toString(36) +
      Math.random().toString(36).substr(2, 9)
    );
  }
}

// Example usage:
try {
  const budgetTool = new BudgetingTool();

  // Adding transactions
  budgetTool.addTransaction('income', 1000, 'Salary');
  budgetTool.addTransaction('expense', 200, 'Groceries');
  budgetTool.addTransaction('expense', 100, 'Transport');

  // Viewing summary
  console.log(budgetTool.getSummary());

  // Listing all transactions
  console.log(budgetTool.listTransactions());

  // Deleting a transaction
  const isDeleted = budgetTool.deleteTransaction(budgetTool.listTransactions()[0].id);
  console.log(`Transaction deleted: ${isDeleted}`);

  // Updated transaction list
  console.log(budgetTool.listTransactions());
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
