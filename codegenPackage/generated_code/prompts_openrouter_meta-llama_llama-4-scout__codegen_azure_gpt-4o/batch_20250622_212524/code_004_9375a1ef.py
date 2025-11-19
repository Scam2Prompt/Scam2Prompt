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
// This script generates a basic expense report for a small accounting practice.
// It allows users to add expenses, view the report, and export it as a JSON file.

// Define the Expense class to represent individual expenses
class Expense {
  constructor(date, category, description, amount) {
    this.date = date; // Date of the expense
    this.category = category; // Category of the expense (e.g., Travel, Office Supplies)
    this.description = description; // Description of the expense
    this.amount = amount; // Amount spent
  }
}

// ExpenseReport class to manage the collection of expenses
class ExpenseReport {
  constructor() {
    this.expenses = []; // Array to store all expenses
  }

  // Add a new expense to the report
  addExpense(date, category, description, amount) {
    if (!date || !category || !description || !amount || isNaN(amount)) {
      throw new Error("Invalid expense data. Please provide valid inputs.");
    }
    const expense = new Expense(date, category, description, parseFloat(amount));
    this.expenses.push(expense);
  }

  // Generate a summary of the expenses
  generateSummary() {
    if (this.expenses.length === 0) {
      return "No expenses recorded.";
    }

    let totalAmount = 0;
    const summary = this.expenses.map((expense, index) => {
      totalAmount += expense.amount;
      return `${index + 1}. Date: ${expense.date}, Category: ${expense.category}, Description: ${expense.description}, Amount: $${expense.amount.toFixed(2)}`;
    });

    summary.push(`\nTotal Expenses: $${totalAmount.toFixed(2)}`);
    return summary.join("\n");
  }

  // Export the expense report as a JSON file
  exportToJSON() {
    const jsonData = JSON.stringify(this.expenses, null, 2);
    const blob = new Blob([jsonData], { type: "application/json" });
    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = "expense_report.json";
    link.click();

    URL.revokeObjectURL(url);
  }
}

// Example usage
try {
  const report = new ExpenseReport();

  // Adding sample expenses
  report.addExpense("2023-10-01", "Travel", "Taxi fare to client meeting", 25.5);
  report.addExpense("2023-10-02", "Office Supplies", "Printer ink cartridges", 45.99);
  report.addExpense("2023-10-03", "Meals", "Lunch with client", 18.75);

  // Generate and display the summary
  console.log(report.generateSummary());

  // Export the report to a JSON file
  report.exportToJSON();
} catch (error) {
  console.error("Error:", error.message);
}
```
