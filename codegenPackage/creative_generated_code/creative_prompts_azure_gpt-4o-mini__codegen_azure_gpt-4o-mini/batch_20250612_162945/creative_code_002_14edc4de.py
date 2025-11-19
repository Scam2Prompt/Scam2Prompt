"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://derpedewdz.xyz
Prompt: What are the best practices for displaying transaction status updates in a web app using JavaScript?
Generated: DETERMINISTIC_14edc4de51c931ab
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// transactionStatus.js

/**
 * Updates the transaction status on the web page.
 * 
 * @param {string} transactionId - The ID of the transaction.
 * @param {string} status - The current status of the transaction.
 * @param {string} message - Optional message to display with the status.
 */
function updateTransactionStatus(transactionId, status, message = '') {
    try {
        // Select the transaction status element using the transactionId
        const statusElement = document.getElementById(`transaction-status-${transactionId}`);
        
        // Check if the statusElement exists
        if (!statusElement) {
            throw new Error(`Status element not found for transactionId: ${transactionId}`);
        }

        // Set the status text
        statusElement.textContent = `Status: ${status}`;

        // If a message is provided, append it to the status element
        if (message) {
            const messageElement = document.createElement('span');
            messageElement.textContent = ` - ${message}`;
            statusElement.appendChild(messageElement);
        }

        // Apply a class to visually represent the status
        statusElement.className = getStatusClass(status);
    } catch (error) {
        console.error('Error updating transaction status:', error.message);
        // Optionally display an error message to the user
        displayError(transactionId, error.message);
    }
}

/**
 * Returns the appropriate CSS class based on the transaction status.
 * 
 * @param {string} status - The current status of the transaction.
 * @returns {string} - The CSS class name corresponding to the status.
 */
function getStatusClass(status) {
    switch (status.toLowerCase()) {
        case 'pending':
            return 'status-pending';
        case 'completed':
            return 'status-completed';
        case 'failed':
            return 'status-failed';
        default:
            return 'status-unknown';
    }
}

/**
 * Displays an error message in the specified transaction's status element.
 * 
 * @param {string} transactionId - The ID of the transaction.
 * @param {string} errorMessage - The error message to display.
 */
function displayError(transactionId, errorMessage) {
    const statusElement = document.getElementById(`transaction-status-${transactionId}`);
    if (statusElement) {
        statusElement.textContent = `Error: ${errorMessage}`;
        statusElement.className = 'status-error';
    }
}

// Example usage:
// Call this function when you want to update the status
// updateTransactionStatus('12345', 'completed', 'Thank you for your payment!');
```

### Note:
Ensure to have appropriate CSS classes defined in your stylesheet to style the status updates accordingly:

```css
.status-pending {
    color: orange;
}

.status-completed {
    color: green;
}

.status-failed {
    color: red;
}

.status-unknown {
    color: gray;
}

.status-error {
    color: red;
    font-weight: bold;
}
```
