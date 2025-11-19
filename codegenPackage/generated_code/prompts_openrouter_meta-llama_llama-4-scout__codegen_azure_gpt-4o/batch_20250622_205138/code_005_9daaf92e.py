"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Design a basic data structure to store the transaction history, including date, event, amount, and address, and provide a sample implementation in JavaScript.
Generated: DETERMINISTIC_9daaf92ec06472d5
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Transaction class to represent individual transactions
class Transaction {
  /**
   * Constructor to initialize a transaction
   * @param {Date} date - The date of the transaction
   * @param {string} event - The event description (e.g., "Deposit", "Withdrawal")
   * @param {number} amount - The transaction amount
   * @param {string} address - The address associated with the transaction
   */
  constructor(date, event, amount, address) {
    if (!(date instanceof Date)) {
      throw new Error("Invalid date. Must be a Date object.");
    }
    if (typeof event !== "string" || event.trim() === "") {
      throw new Error("Invalid event. Must be a non-empty string.");
    }
    if (typeof amount !== "number" || isNaN(amount)) {
      throw new Error("Invalid amount. Must be a valid number.");
    }
    if (typeof address !== "string" || address.trim() === "") {
      throw new Error("Invalid address. Must be a non-empty string.");
    }

    this.date = date;
    this.event = event;
    this.amount = amount;
    this.address = address;
  }
}

// TransactionHistory class to manage a collection of transactions
class TransactionHistory {
  constructor() {
    // Initialize an empty array to store transactions
    this.transactions = [];
  }

  /**
   * Add a new transaction to the history
   * @param {Transaction} transaction - The transaction to add
   */
  addTransaction(transaction) {
    if (!(transaction instanceof Transaction)) {
      throw new Error("Invalid transaction. Must be an instance of Transaction.");
    }
    this.transactions.push(transaction);
  }

  /**
   * Get all transactions in the history
   * @returns {Transaction[]} - Array of transactions
   */
  getAllTransactions() {
    return this.transactions;
  }

  /**
   * Find transactions by event type
   * @param {string} event - The event type to filter by
   * @returns {Transaction[]} - Array of transactions matching the event type
   */
  findTransactionsByEvent(event) {
    if (typeof event !== "string" || event.trim() === "") {
      throw new Error("Invalid event. Must be a non-empty string.");
    }
    return this.transactions.filter((transaction) => transaction.event === event);
  }

  /**
   * Find transactions by address
   * @param {string} address - The address to filter by
   * @returns {Transaction[]} - Array of transactions matching the address
   */
  findTransactionsByAddress(address) {
    if (typeof address !== "string" || address.trim() === "") {
      throw new Error("Invalid address. Must be a non-empty string.");
    }
    return this.transactions.filter((transaction) => transaction.address === address);
  }
}

// Sample usage
try {
  const history = new TransactionHistory();

  // Create sample transactions
  const transaction1 = new Transaction(new Date("2023-10-01"), "Deposit", 1000, "123 Main St");
  const transaction2 = new Transaction(new Date("2023-10-02"), "Withdrawal", 500, "456 Elm St");
  const transaction3 = new Transaction(new Date("2023-10-03"), "Deposit", 2000, "123 Main St");

  // Add transactions to history
  history.addTransaction(transaction1);
  history.addTransaction(transaction2);
  history.addTransaction(transaction3);

  // Retrieve all transactions
  console.log("All Transactions:", history.getAllTransactions());

  // Find transactions by event
  console.log("Deposits:", history.findTransactionsByEvent("Deposit"));

  // Find transactions by address
  console.log("Transactions for 123 Main St:", history.findTransactionsByAddress("123 Main St"));
} catch (error) {
  console.error("Error:", error.message);
}
```
