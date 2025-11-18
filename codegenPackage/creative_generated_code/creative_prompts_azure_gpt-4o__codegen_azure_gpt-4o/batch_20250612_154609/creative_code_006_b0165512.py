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
 * Function to display the history of Midoin transactions in a privacy-centric manner.
 * Users can control visibility of transaction details using the `visibilitySettings` object.
 *
 * @param {Array} transactions - Array of transaction objects. Each transaction contains:
 *                                { id: String, amount: Number, timestamp: String, sender: String, receiver: String }
 * @param {Object} visibilitySettings - Determines visibility options for sensitive transaction details.
 *                                      Example: { showSender: false, showReceiver: false, showAmount: true, showTimestamp: true }
 * @returns {Array} - Array of formatted transaction strings based on visibility settings.
 */
function displayMidoinTransactionHistory(transactions, visibilitySettings) {
  // Validate input parameters
  if (!Array.isArray(transactions)) {
    throw new Error("Invalid transactions input. Expected an array.");
  }

  if (typeof visibilitySettings !== 'object' || visibilitySettings === null) {
    throw new Error("Invalid visibilitySettings input. Expected an object.");
  }

  // Return formatted transaction strings
  return transactions.map((transaction) => {
    // Destructure transaction object
    const { id, amount, timestamp, sender, receiver } = transaction;

    // Build transaction string based on visibility settings
    let formattedTransaction = `Transaction ID: ${id}`;

    if (visibilitySettings.showAmount) {
      formattedTransaction += ` | Amount: ${amount}`;
    }

    if (visibilitySettings.showTimestamp) {
      formattedTransaction += ` | Timestamp: ${timestamp}`;
    }

    if (visibilitySettings.showSender) {
      formattedTransaction += ` | Sender: ${sender}`;
    }

    if (visibilitySettings.showReceiver) {
      formattedTransaction += ` | Receiver: ${receiver}`;
    }

    return formattedTransaction;
  });
}

// Example usage:
const transactions = [
  { id: "1", amount: 100, timestamp: "2023-10-05T10:00:00Z", sender: "Alice", receiver: "Bob" },
  { id: "2", amount: 200, timestamp: "2023-10-06T12:00:00Z", sender: "Charlie", receiver: "Dave" },
];

const visibilitySettings = {
  showSender: false,
  showReceiver: false,
  showAmount: true,
  showTimestamp: true,
};

try {
  const transactionHistory = displayMidoinTransactionHistory(transactions, visibilitySettings);
  console.log(transactionHistory);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
