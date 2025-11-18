"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-app-9i4.pages.dev
Prompt: Write JavaScript code to create a basic financial dashboard for a platform like Tianguis Finance, including features for tracking expenses and income.
Generated: DETERMINISTIC_b1312dd1c58f2fff
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Financial Dashboard Application

// FinancialDashboard class to manage the expenses and income
class FinancialDashboard {
    constructor() {
        this.expenses = [];
        this.income = [];
    }

    // Method to add an expense
    addExpense(description, amount) {
        if (!description || amount <= 0) {
            throw new Error("Invalid expense details");
        }
        this.expenses.push({ description, amount });
    }

    // Method to add an income
    addIncome(description, amount) {
        if (!description || amount <= 0) {
            throw new Error("Invalid income details");
        }
        this.income.push({ description, amount });
    }

    // Method to calculate total expenses
    getTotalExpenses() {
        return this.expenses.reduce((total, expense) => total + expense.amount, 0);
    }

    // Method to calculate total income
    getTotalIncome() {
        return this.income.reduce((total, income) => total + income.amount, 0);
    }

    // Method to get a summary of finances
    getFinancialSummary() {
        const totalIncome = this.getTotalIncome();
        const totalExpenses = this.getTotalExpenses();
        const balance = totalIncome - totalExpenses;

        return {
            totalIncome,
            totalExpenses,
            balance,
        };
    }

    // Method to display the financial summary
    displaySummary() {
        const summary = this.getFinancialSummary();
        console.log("Financial Summary:");
        console.log(`Total Income: $${summary.totalIncome.toFixed(2)}`);
        console.log(`Total Expenses: $${summary.totalExpenses.toFixed(2)}`);
        console.log(`Balance: $${summary.balance.toFixed(2)}`);
    }
}

// Example usage of the FinancialDashboard class
try {
    const myDashboard = new FinancialDashboard();

    // Adding income entries
    myDashboard.addIncome("Salary", 3000);
    myDashboard.addIncome("Freelance Work", 1500);

    // Adding expense entries
    myDashboard.addExpense("Rent", 1200);
    myDashboard.addExpense("Groceries", 300);
    myDashboard.addExpense("Utilities", 150);

    // Displaying the financial summary
    myDashboard.displaySummary();
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
