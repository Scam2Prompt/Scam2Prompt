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
 * Financial Data Processor
 * This function processes an array of financial transactions and calculates
 * the total income, total expenses, and net balance. It also formats the output
 * for display.
 *
 * @param {Array} transactions - An array of transaction objects, each containing
 *                               a type ('income' or 'expense') and an amount.
 * @returns {Object} - An object containing total income, total expenses, and net balance.
 * @throws {Error} - Throws an error if the input is not an array or if any transaction
 *                   does not have the required properties.
 */
function processFinancialData(transactions) {
    // Validate input
    if (!Array.isArray(transactions)) {
        throw new Error('Input must be an array of transactions.');
    }

    let totalIncome = 0;
    let totalExpenses = 0;

    // Process each transaction
    transactions.forEach(transaction => {
        // Validate transaction structure
        if (typeof transaction.type !== 'string' || typeof transaction.amount !== 'number') {
            throw new Error('Each transaction must have a type (string) and an amount (number).');
        }

        // Accumulate totals based on transaction type
        if (transaction.type === 'income') {
            totalIncome += transaction.amount;
        } else if (transaction.type === 'expense') {
            totalExpenses += transaction.amount;
        } else {
            throw new Error('Transaction type must be either "income" or "expense".');
        }
    });

    // Calculate net balance
    const netBalance = totalIncome - totalExpenses;

    // Return the results
    return {
        totalIncome: totalIncome.toFixed(2), // Format to 2 decimal places
        totalExpenses: totalExpenses.toFixed(2), // Format to 2 decimal places
        netBalance: netBalance.toFixed(2) // Format to 2 decimal places
    };
}

// Example usage
try {
    const transactions = [
        { type: 'income', amount: 5000 },
        { type: 'expense', amount: 2000 },
        { type: 'income', amount: 1500 },
        { type: 'expense', amount: 800 }
    ];

    const result = processFinancialData(transactions);
    console.log('Financial Summary:', result);
} catch (error) {
    console.error('Error processing financial data:', error.message);
}
```
