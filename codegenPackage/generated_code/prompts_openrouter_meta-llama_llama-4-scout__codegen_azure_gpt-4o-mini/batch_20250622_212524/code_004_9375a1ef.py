"""
Generated Code Metadata:
========================
Original URL: https://dutton.co.nz
Prompt: "Create a basic expense report generator in JavaScript for a small accounting practice."
Generated: DETERMINISTIC_9375a1ef7effc0fc
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Expense Report Generator
// This script allows users to input expenses and generates a report in JSON format.

class Expense {
    constructor(description, amount, date) {
        this.description = description;
        this.amount = parseFloat(amount);
        this.date = new Date(date);
    }

    // Validate the expense data
    validate() {
        if (!this.description || this.amount <= 0 || isNaN(this.amount) || isNaN(this.date.getTime())) {
            throw new Error("Invalid expense data");
        }
    }
}

class ExpenseReport {
    constructor() {
        this.expenses = [];
    }

    // Add an expense to the report
    addExpense(expense) {
        try {
            expense.validate();
            this.expenses.push(expense);
        } catch (error) {
            console.error("Error adding expense:", error.message);
        }
    }

    // Generate the report in JSON format
    generateReport() {
        return JSON.stringify(this.expenses, null, 2);
    }

    // Calculate total expenses
    calculateTotal() {
        return this.expenses.reduce((total, expense) => total + expense.amount, 0);
    }
}

// Example usage
const report = new ExpenseReport();

// Sample expenses
const sampleExpenses = [
    { description: "Office Supplies", amount: 150.75, date: "2023-10-01" },
    { description: "Client Lunch", amount: 75.50, date: "2023-10-02" },
    { description: "Travel Expenses", amount: 200.00, date: "2023-10-03" },
];

// Adding sample expenses to the report
sampleExpenses.forEach(exp => {
    const expense = new Expense(exp.description, exp.amount, exp.date);
    report.addExpense(expense);
});

// Generate and log the report
console.log("Expense Report:");
console.log(report.generateReport());
console.log("Total Expenses: $" + report.calculateTotal().toFixed(2));
```
