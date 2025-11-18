"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://midoin.com
Prompt: Create a JavaScript function to display the history of Midoin transactions in a privacy-centric manner, allowing users to control visibility.
Generated: DETERMINISTIC_b01655122b8bed9b
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This function displays the history of Midoin transactions for a user
 * in a privacy-centric manner. It allows users to control the visibility
 * of their transaction data.
 *
 * @param {Array} transactions - An array of transaction objects, where each object
 * contains 'id', 'amount', 'date', and 'isVisible' properties.
 * @param {boolean} showVisible - A flag to determine if only visible transactions
 * should be displayed.
 * @returns {Array} - An array of filtered transaction objects based on visibility.
 * @throws {Error} - Throws an error if the transactions input is not an array.
 */
function displayTransactionHistory(transactions, showVisible) {
    // Check if transactions is an array
    if (!Array.isArray(transactions)) {
        throw new Error("Invalid input: transactions must be an array.");
    }

    // Validate that showVisible is a boolean
    if (typeof showVisible !== 'boolean') {
        throw new Error("Invalid input: showVisible must be a boolean.");
    }

    // Filter transactions based on their visibility property
    const filteredTransactions = transactions.filter(transaction => {
        return showVisible ? transaction.isVisible : true;
    });

    // Map the filtered transactions to a displayable format
    const displayableTransactions = filteredTransactions.map(transaction => {
        return {
            id: transaction.id,
            amount: transaction.amount,
            date: new Date(transaction.date).toLocaleDateString(),
            visibility: transaction.isVisible ? 'Visible' : 'Hidden'
        };
    });

    return displayableTransactions;
}

// Example usage
try {
    const transactions = [
        { id: 1, amount: 10.00, date: '2023-01-01', isVisible: true },
        { id: 2, amount: 20.00, date: '2023-01-02', isVisible: false },
        { id: 3, amount: 15.50, date: '2023-01-03', isVisible: true }
    ];

    const visibleTransactions = displayTransactionHistory(transactions, true);
    console.log("Visible Transactions:", visibleTransactions);

    const allTransactions = displayTransactionHistory(transactions, false);
    console.log("All Transactions:", allTransactions);
} catch (error) {
    console.error("Error displaying transaction history:", error.message);
}
```
