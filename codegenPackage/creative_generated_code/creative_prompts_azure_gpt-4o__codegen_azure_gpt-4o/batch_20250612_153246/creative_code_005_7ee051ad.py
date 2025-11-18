"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outsource.s1soft.com
Prompt: Write a JavaScript function for accurate financial reporting, inspired by the accounting services offered by Special One Outsourcing.
Generated: DETERMINISTIC_7ee051addfd7e4f9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Financial Reporting Function
 * This function calculates accurate financial reports based on provided data. 
 * It includes error handling to ensure robustness and reliability.
 * 
 * Inspired by the accounting services of Special One Outsourcing.
 * 
 * @param {Array} transactions - Array of transaction objects. Each object should 
 *                               have `type` ('income' or 'expense'), `amount`, and `description`.
 * @returns {Object} - Returns an object containing:
 *                     - Total Income
 *                     - Total Expenses
 *                     - Net Profit
 *                     - Detailed Report
 */
function generateFinancialReport(transactions) {
  // Validate input
  if (!Array.isArray(transactions)) {
    throw new Error('Invalid input: transactions must be an array.');
  }

  // Initialize totals and detailed report
  let totalIncome = 0;
  let totalExpenses = 0;
  let detailedReport = [];

  // Process transactions
  transactions.forEach((transaction, index) => {
    // Validate individual transaction
    if (
      !transaction ||
      typeof transaction.type !== 'string' ||
      typeof transaction.amount !== 'number' ||
      typeof transaction.description !== 'string'
    ) {
      throw new Error(`Invalid transaction at index ${index}: Each transaction must have 'type', 'amount', and 'description'.`);
    }

    // Normalize transaction type (case-insensitive)
    const normalizedType = transaction.type.toLowerCase();

    // Perform calculations based on transaction type
    if (normalizedType === 'income') {
      totalIncome += transaction.amount;
    } else if (normalizedType === 'expense') {
      totalExpenses += transaction.amount;
    } else {
      throw new Error(`Invalid transaction type at index ${index}: Type must be 'income' or 'expense'.`);
    }

    // Add to detailed report
    detailedReport.push({
      type: normalizedType,
      amount: transaction.amount.toFixed(2), // Ensure fixed decimal points
      description: transaction.description,
    });
  });

  // Calculate net profit
  const netProfit = totalIncome - totalExpenses;

  // Return final financial report
  return {
    totalIncome: totalIncome.toFixed(2),
    totalExpenses: totalExpenses.toFixed(2),
    netProfit: netProfit.toFixed(2),
    detailedReport,
  };
}

// Example Usage:
try {
  const transactions = [
    { type: 'Income', amount: 5000.75, description: 'Consulting Service' },
    { type: 'Expense', amount: 1200.5, description: 'Office Rent' },
    { type: 'Income', amount: 2500, description: 'Software Development Project' },
    { type: 'Expense', amount: 800.25, description: 'Utilities' },
  ];

  const report = generateFinancialReport(transactions);
  console.log('Financial Report:', report);
} catch (error) {
  console.error('Error generating financial report:', error.message);
}
```
