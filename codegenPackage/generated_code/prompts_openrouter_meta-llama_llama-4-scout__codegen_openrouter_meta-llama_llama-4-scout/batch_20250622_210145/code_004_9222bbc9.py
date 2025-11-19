"""
Generated Code Metadata:
========================
Original URL: https://rexaslive.pages.dev
Prompt: Create a simple JavaScript function to handle financial data processing and display.
Generated: DETERMINISTIC_9222bbc9d38ba8c9
Batch ID: 20250622_210145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * FinancialDataProcessor class to handle financial data processing and display.
 */
class FinancialDataProcessor {
  /**
   * Constructor to initialize the financial data processor.
   * @param {Array<Object>} financialData - Array of financial data objects.
   */
  constructor(financialData) {
    this.financialData = financialData;
  }

  /**
   * Calculate the total income from the financial data.
   * @returns {number} The total income.
   */
  calculateTotalIncome() {
    return this.financialData.reduce((acc, current) => acc + current.income, 0);
  }

  /**
   * Calculate the total expense from the financial data.
   * @returns {number} The total expense.
   */
  calculateTotalExpense() {
    return this.financialData.reduce((acc, current) => acc + current.expense, 0);
  }

  /**
   * Calculate the net profit from the financial data.
   * @returns {number} The net profit.
   */
  calculateNetProfit() {
    return this.calculateTotalIncome() - this.calculateTotalExpense();
  }

  /**
   * Display the financial data in a tabular format.
   */
  displayFinancialData() {
    try {
      console.log("Financial Data:");
      console.log(`| ${"Date".padEnd(10)} | ${"Income".padEnd(10)} | ${"Expense".padEnd(10)} | ${"Net Profit".padEnd(10)} |`);
      console.log("-".repeat(50));
      this.financialData.forEach((data) => {
        const netProfit = data.income - data.expense;
        console.log(`| ${data.date.toLocaleDateString().padEnd(10)} | ${data.income.toFixed(2).padEnd(10)} | ${data.expense.toFixed(2).padEnd(10)} | ${netProfit.toFixed(2).padEnd(10)} |`);
      });
      console.log("-".repeat(50));
      console.log(`Total Income: ${this.calculateTotalIncome().toFixed(2)}`);
      console.log(`Total Expense: ${this.calculateTotalExpense().toFixed(2)}`);
      console.log(`Net Profit: ${this.calculateNetProfit().toFixed(2)}`);
    } catch (error) {
      console.error("Error displaying financial data:", error);
    }
  }
}

// Example usage:
const financialData = [
  { date: new Date("2022-01-01"), income: 1000, expense: 500 },
  { date: new Date("2022-01-02"), income: 1200, expense: 600 },
  { date: new Date("2022-01-03"), income: 1500, expense: 700 },
];

const processor = new FinancialDataProcessor(financialData);
processor.displayFinancialData();
```
