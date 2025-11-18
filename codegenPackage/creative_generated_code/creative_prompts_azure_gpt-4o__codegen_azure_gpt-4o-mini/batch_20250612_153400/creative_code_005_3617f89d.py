"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmoney.pages.dev
Prompt: Provide an example of using fMoney with JavaScript to manage expense categories in a web application.
Generated: DETERMINISTIC_3617f89d22776f7c
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the fMoney library for managing financial data
import fMoney from 'fmoney';

// Expense category management class
class ExpenseManager {
    constructor() {
        // Initialize an empty array to hold expense categories
        this.categories = [];
    }

    /**
     * Adds a new expense category
     * @param {string} categoryName - The name of the expense category
     * @param {number} budget - The budget allocated for this category
     * @throws Will throw an error if the category name is empty or budget is negative
     */
    addCategory(categoryName, budget) {
        if (!categoryName || typeof categoryName !== 'string') {
            throw new Error('Category name must be a non-empty string');
        }
        if (budget < 0) {
            throw new Error('Budget must be a non-negative number');
        }

        const category = {
            name: categoryName,
            budget: budget,
            expenses: []
        };
        this.categories.push(category);
    }

    /**
     * Adds an expense to a specified category
     * @param {string} categoryName - The name of the category where the expense will be added
     * @param {number} amount - The amount of the expense
     * @throws Will throw an error if the category is not found or amount is negative
     */
    addExpense(categoryName, amount) {
        if (amount < 0) {
            throw new Error('Expense amount must be a non-negative number');
        }

        const category = this.categories.find(cat => cat.name === categoryName);
        if (!category) {
            throw new Error(`Category "${categoryName}" not found`);
        }

        category.expenses.push(amount);
    }

    /**
     * Calculates the total expenses for a specified category
     * @param {string} categoryName - The name of the category
     * @returns {number} - The total expenses for the category
     * @throws Will throw an error if the category is not found
     */
    getTotalExpenses(categoryName) {
        const category = this.categories.find(cat => cat.name === categoryName);
        if (!category) {
            throw new Error(`Category "${categoryName}" not found`);
        }

        return fMoney.sum(category.expenses);
    }

    /**
     * Gets the remaining budget for a specified category
     * @param {string} categoryName - The name of the category
     * @returns {number} - The remaining budget for the category
     * @throws Will throw an error if the category is not found
     */
    getRemainingBudget(categoryName) {
        const category = this.categories.find(cat => cat.name === categoryName);
        if (!category) {
            throw new Error(`Category "${categoryName}" not found`);
        }

        const totalExpenses = this.getTotalExpenses(categoryName);
        return fMoney.subtract(category.budget, totalExpenses);
    }
}

// Example usage
try {
    const expenseManager = new ExpenseManager();

    // Adding categories
    expenseManager.addCategory('Groceries', 500);
    expenseManager.addCategory('Utilities', 300);

    // Adding expenses
    expenseManager.addExpense('Groceries', 150);
    expenseManager.addExpense('Utilities', 100);

    // Getting total expenses and remaining budget
    const totalGroceries = expenseManager.getTotalExpenses('Groceries');
    const remainingGroceries = expenseManager.getRemainingBudget('Groceries');

    console.log(`Total Groceries Expenses: ${totalGroceries}`);
    console.log(`Remaining Groceries Budget: ${remainingGroceries}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
