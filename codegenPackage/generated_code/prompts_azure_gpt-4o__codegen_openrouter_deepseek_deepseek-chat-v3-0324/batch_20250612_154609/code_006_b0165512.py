"""
Generated Code Metadata:
========================
Original URL: https://midoin.com
Prompt: Create a JavaScript function to display the history of Midoin transactions in a privacy-centric manner, allowing users to control visibility.
Generated: DETERMINISTIC_b01655122b8bed9b
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays Midoin transaction history with privacy controls.
 * @param {Array} transactions - Array of transaction objects.
 * @param {Object} privacySettings - User's privacy preferences.
 * @param {boolean} privacySettings.showAmounts - Whether to display transaction amounts.
 * @param {boolean} privacySettings.showTimestamps - Whether to display transaction timestamps.
 * @param {boolean} privacySettings.showCounterparties - Whether to display counterparty information.
 * @returns {Array} Formatted transactions based on privacy settings.
 */
function displayTransactionHistory(transactions, privacySettings) {
    // Validate inputs
    if (!Array.isArray(transactions)) {
        throw new Error('Transactions must be an array');
    }
    
    if (!privacySettings || typeof privacySettings !== 'object') {
        throw new Error('Privacy settings must be an object');
    }

    // Default privacy settings if not provided
    const defaultPrivacySettings = {
        showAmounts: true,
        showTimestamps: true,
        showCounterparties: true
    };

    // Merge user settings with defaults
    const effectiveSettings = {
        ...defaultPrivacySettings,
        ...privacySettings
    };

    // Process each transaction according to privacy settings
    return transactions.map(transaction => {
        // Validate transaction structure
        if (!transaction || typeof transaction !== 'object') {
            console.warn('Invalid transaction encountered, skipping');
            return null;
        }

        const formattedTransaction = {
            id: transaction.id || 'unknown',
            type: transaction.type || 'unknown'
        };

        // Apply privacy settings
        if (effectiveSettings.showAmounts && transaction.amount !== undefined) {
            formattedTransaction.amount = transaction.amount;
        }

        if (effectiveSettings.showTimestamps && transaction.timestamp) {
            formattedTransaction.timestamp = transaction.timestamp;
        }

        if (effectiveSettings.showCounterparties && transaction.counterparty) {
            formattedTransaction.counterparty = transaction.counterparty;
        }

        // Add metadata if present
        if (transaction.metadata) {
            formattedTransaction.metadata = transaction.metadata;
        }

        return formattedTransaction;
    }).filter(transaction => transaction !== null); // Remove any invalid transactions
}

// Example usage:
/*
const transactions = [
    {
        id: 'txn_123',
        type: 'transfer',
        amount: 100,
        timestamp: '2023-01-01T12:00:00Z',
        counterparty: 'user_456',
        metadata: { note: 'Payment for services' }
    },
    {
        id: 'txn_124',
        type: 'deposit',
        amount: 500,
        timestamp: '2023-01-02T09:30:00Z'
    }
];

const privacySettings = {
    showAmounts: false,
    showCounterparties: true
};

const filteredTransactions = displayTransactionHistory(transactions, privacySettings);
console.log(filteredTransactions);
*/
```
