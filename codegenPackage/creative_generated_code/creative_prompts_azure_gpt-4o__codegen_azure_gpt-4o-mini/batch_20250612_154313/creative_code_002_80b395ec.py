"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Develop a function in JavaScript that calculates unnecessary expenses from a list of transactions, inspired by Cashflow Routine's advice on optimizing spending.
Generated: DETERMINISTIC_80b395ec75906883
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates unnecessary expenses from a list of transactions based on predefined criteria.
 *
 * @param {Array} transactions - An array of transaction objects, each containing a 'description' and 'amount'.
 * @returns {Object} - An object containing the total unnecessary expenses and a detailed list of such expenses.
 * @throws {Error} - Throws an error if the input is not an array or if any transaction is missing required properties.
 */
function calculateUnnecessaryExpenses(transactions) {
    // Validate input
    if (!Array.isArray(transactions)) {
        throw new Error("Invalid input: transactions must be an array.");
    }

    // Initialize variables to hold unnecessary expenses details
    let totalUnnecessaryExpenses = 0;
    const unnecessaryExpensesList = [];

    // Define criteria for unnecessary expenses
    const unnecessaryKeywords = ['coffee', 'dining', 'subscription', 'gaming', 'snacks'];

    // Process each transaction
    transactions.forEach(transaction => {
        // Validate transaction structure
        if (typeof transaction !== 'object' || transaction === null ||
            !transaction.hasOwnProperty('description') || 
            !transaction.hasOwnProperty('amount')) {
            throw new Error("Invalid transaction format. Each transaction must contain 'description' and 'amount'.");
        }

        // Check if the transaction is considered unnecessary
        const isUnnecessary = unnecessaryKeywords.some(keyword => 
            transaction.description.toLowerCase().includes(keyword)
        );

        // If unnecessary, update totals
        if (isUnnecessary) {
            totalUnnecessaryExpenses += transaction.amount;
            unnecessaryExpensesList.push(transaction);
        }
    });

    // Return the total and details of unnecessary expenses
    return {
        totalUnnecessaryExpenses,
        unnecessaryExpensesList
    };
}

// Example usage:
try {
    const transactions = [
        { description: 'Coffee at cafe', amount: 5 },
        { description: 'Grocery shopping', amount: 50 },
        { description: 'Monthly subscription', amount: 12 },
        { description: 'Snacks', amount: 8 }
    ];

    const result = calculateUnnecessaryExpenses(transactions);
    console.log("Total Unnecessary Expenses: $", result.totalUnnecessaryExpenses);
    console.log("Details of Unnecessary Expenses:", result.unnecessaryExpensesList);
} catch (error) {
    console.error("Error:", error.message);
}
```
