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
/**
 * Represents a single transaction in the transaction history.
 */
class Transaction {
  /**
   * Creates a new Transaction instance.
   * 
   * @param {Date} date - The date of the transaction.
   * @param {string} event - The event type of the transaction.
   * @param {number} amount - The amount of the transaction.
   * @param {string} address - The address associated with the transaction.
   */
  constructor(date, event, amount, address) {
    if (!(date instanceof Date)) {
      throw new Error('Date must be a Date object');
    }
    if (typeof event !== 'string') {
      throw new Error('Event must be a string');
    }
    if (typeof amount !== 'number') {
      throw new Error('Amount must be a number');
    }
    if (typeof address !== 'string') {
      throw new Error('Address must be a string');
    }

    this.date = date;
    this.event = event;
    this.amount = amount;
    this.address = address;
  }

  /**
   * Returns a string representation of the transaction.
   * 
   * @returns {string}
   */
  toString() {
    return `Date: ${this.date.toISOString()}, Event: ${this.event}, Amount: ${this.amount}, Address: ${this.address}`;
  }
}

/**
 * Represents a collection of transactions.
 */
class TransactionHistory {
  /**
   * Creates a new TransactionHistory instance.
   */
  constructor() {
    this.transactions = [];
  }

  /**
   * Adds a new transaction to the transaction history.
   * 
   * @param {Transaction} transaction - The transaction to add.
   */
  addTransaction(transaction) {
    if (!(transaction instanceof Transaction)) {
      throw new Error('Transaction must be a Transaction object');
    }
    this.transactions.push(transaction);
  }

  /**
   * Returns the transaction history as an array of transactions.
   * 
   * @returns {Transaction[]}
   */
  getTransactions() {
    return this.transactions;
  }

  /**
   * Returns a string representation of the transaction history.
   * 
   * @returns {string}
   */
  toString() {
    return this.transactions.map(transaction => transaction.toString()).join('\n');
  }
}

// Sample implementation
function main() {
  try {
    const transactionHistory = new TransactionHistory();

    const transaction1 = new Transaction(new Date('2022-01-01'), 'Deposit', 100.0, '123 Main St');
    const transaction2 = new Transaction(new Date('2022-01-15'), 'Withdrawal', -50.0, '456 Elm St');
    const transaction3 = new Transaction(new Date('2022-02-01'), 'Deposit', 200.0, '789 Oak St');

    transactionHistory.addTransaction(transaction1);
    transactionHistory.addTransaction(transaction2);
    transactionHistory.addTransaction(transaction3);

    console.log(transactionHistory.toString());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
