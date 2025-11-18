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
// Budgeting Tool in JavaScript

class Budget {
    constructor(name, initialAmount = 0) {
        this.name = name; // Name of the budget
        this.initialAmount = initialAmount; // Initial budget amount
        this.remainingAmount = initialAmount; // Amount remaining in the budget
        this.expenses = []; // Array to store expenses
    }

    // Method to add an expense
    addExpense(description, amount) {
        if (amount <= 0) {
            throw new Error("Expense amount must be greater than zero.");
        }
        if (this.remainingAmount - amount < 0) {
            throw new Error("Expense exceeds remaining budget.");
        }
        const expense = {
            description,
            amount,
            date: new Date().toISOString().split('T')[0] // Current date in YYYY-MM-DD format
        };
        this.expenses.push(expense); // Add expense to expenses array
        this.remainingAmount -= amount; // Deduct from remaining amount
    }

    // Method to remove an expense by index
    removeExpense(index) {
        if (index < 0 || index >= this.expenses.length) {
            throw new Error("Invalid expense index.");
        }
        const removedExpense = this.expenses.splice(index, 1)[0]; // Remove expense
        this.remainingAmount += removedExpense.amount; // Add back to remaining amount
    }

    // Method to get the budget summary
    getSummary() {
        return {
            name: this.name,
            initialAmount: this.initialAmount,
            remainingAmount: this.remainingAmount,
            totalExpenses: this.expenses.reduce((total, expense) => total + expense.amount, 0),
            expenses: this.expenses
        };
    }
}

// Usage Example

try {
    const monthlyBudget = new Budget("Monthly Expenses", 1000); // Create a new budget
    monthlyBudget.addExpense("Groceries", 200); // Add expense
    monthlyBudget.addExpense("Utilities", 150); // Add expense
    console.log(monthlyBudget.getSummary()); // Display budget summary

    monthlyBudget.removeExpense(0); // Remove first expense
    console.log(monthlyBudget.getSummary()); // Display updated budget summary
} catch (error) {
    console.error("Error:", error.message); // Handle errors gracefully
}
```
