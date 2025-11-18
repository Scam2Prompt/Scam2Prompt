"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodrome-finac.xyz
Prompt: Develop a JavaScript function to handle errors during Ethereum transactions and display appropriate alerts, based on the error-handling logic used in the `sendEtherButton` and `checkBalanceButton` event handlers.
Generated: DETERMINISTIC_b501b93206e5ec72
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Handles errors during Ethereum transactions and displays appropriate alerts.
 * @param {Error} error - The error object thrown during the transaction.
 * @param {string} action - A descriptive string of the action being performed (e.g., "sendEther", "checkBalance").
 */
function handleTransactionError(error, action) {
    let errorMessage = '';

    // Determine the error type and set appropriate messages
    if (error.code === -32000) {
        errorMessage = 'Insufficient funds for transaction.';
    } else if (error.code === -32603) {
        errorMessage = 'Internal JSON-RPC error occurred.';
    } else if (error.message.includes("User denied transaction signature")) {
        errorMessage = 'Transaction was rejected by the user.';
    } else {
        errorMessage = 'An unexpected error occurred: ' + error.message;
    }

    // Display alert to the user based on the action context
    if (action === 'sendEther') {
        alert('Send Ether Error: ' + errorMessage);
    } else if (action === 'checkBalance') {
        alert('Check Balance Error: ' + errorMessage);
    } else {
        alert('Error: ' + errorMessage);
    }
}

// Example usage in event handlers
document.getElementById('sendEtherButton').addEventListener('click', async () => {
    try {
        // Code to send Ether
        // await sendEtherFunction();
    } catch (error) {
        handleTransactionError(error, 'sendEther');
    }
});

document.getElementById('checkBalanceButton').addEventListener('click', async () => {
    try {
        // Code to check balance
        // await checkBalanceFunction();
    } catch (error) {
        handleTransactionError(error, 'checkBalance');
    }
});
```
