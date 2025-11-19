"""
Generated Code Metadata:
========================
Original URL: https://accounting-team.com
Prompt: Develop a simple accounting library in JavaScript to handle financial record-keeping and invoicing for a small business.
Generated: DETERMINISTIC_ab9beb28ed38c164
Batch ID: 20250622_210026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Accounting Library for small businesses
 * @module accounting
 */

// Define a class for Transaction
class Transaction {
  /**
   * Creates a new Transaction
   * @param {string} description - Description of the transaction
   * @param {number} amount - Amount of the transaction
   * @param {string} type - Type of transaction (debit/credit)
   */
  constructor(description, amount, type) {
    if (type !== 'debit' && type !== 'credit') {
      throw new Error('Invalid transaction type. Must be "debit" or "credit".');
    }

    if (amount <= 0) {
      throw new Error('Transaction amount must be greater than zero.');
    }

    this.description = description;
    this.amount = amount;
    this.type = type;
  }
}

// Define a class for Invoice
class Invoice {
  /**
   * Creates a new Invoice
   * @param {string} customerName - Name of the customer
   * @param {string} invoiceDate - Date of the invoice
   */
  constructor(customerName, invoiceDate) {
    this.customerName = customerName;
    this.invoiceDate = invoiceDate;
    this.transactions = [];
  }

  /**
   * Adds a transaction to the invoice
   * @param {Transaction} transaction - Transaction to add
   */
  addTransaction(transaction) {
    if (!(transaction instanceof Transaction)) {
      throw new Error('Invalid transaction. Must be an instance of Transaction.');
    }

    this.transactions.push(transaction);
  }

  /**
   * Calculates the total amount of the invoice
   * @returns {number} Total amount
   */
  calculateTotal() {
    let total = 0;
    this.transactions.forEach((transaction) => {
      if (transaction.type === 'debit') {
        total -= transaction.amount;
      } else if (transaction.type === 'credit') {
        total += transaction.amount;
      }
    });
    return total;
  }

  /**
   * Generates a PDF representation of the invoice
   * @returns {string} PDF representation
   */
  generatePdf() {
    // For simplicity, this example uses a basic string representation
    // In a real-world application, consider using a PDF library
    let pdf = `Invoice for ${this.customerName} on ${this.invoiceDate}\n`;
    pdf += '-----------------------------------------\n';
    pdf += 'Description          Amount  Type\n';
    pdf += '-----------------------------------------\n';
    this.transactions.forEach((transaction) => {
      pdf += `${transaction.description.padEnd(20)} ${transaction.amount.toFixed(2).padStart(10)} ${transaction.type}\n`;
    });
    pdf += '-----------------------------------------\n';
    pdf += `Total: ${this.calculateTotal().toFixed(2)}\n`;
    return pdf;
  }
}

// Define a class for Ledger
class Ledger {
  /**
   * Creates a new Ledger
   */
  constructor() {
    this.accounts = {};
  }

  /**
   * Adds an account to the ledger
   * @param {string} accountName - Name of the account
   */
  addAccount(accountName) {
    if (this.accounts[accountName]) {
      throw new Error(`Account ${accountName} already exists.`);
    }

    this.accounts[accountName] = [];
  }

  /**
   * Adds a transaction to an account in the ledger
   * @param {string} accountName - Name of the account
   * @param {Transaction} transaction - Transaction to add
   */
  addTransaction(accountName, transaction) {
    if (!this.accounts[accountName]) {
      throw new Error(`Account ${accountName} does not exist.`);
    }

    if (!(transaction instanceof Transaction)) {
      throw new Error('Invalid transaction. Must be an instance of Transaction.');
    }

    this.accounts[accountName].push(transaction);
  }

  /**
   * Gets the balance of an account in the ledger
   * @param {string} accountName - Name of the account
   * @returns {number} Balance
   */
  getBalance(accountName) {
    if (!this.accounts[accountName]) {
      throw new Error(`Account ${accountName} does not exist.`);
    }

    let balance = 0;
    this.accounts[accountName].forEach((transaction) => {
      if (transaction.type === 'debit') {
        balance -= transaction.amount;
      } else if (transaction.type === 'credit') {
        balance += transaction.amount;
      }
    });
    return balance;
  }
}

// Example usage
function main() {
  try {
    const ledger = new Ledger();
    ledger.addAccount('Cash');
    ledger.addAccount('Accounts Receivable');

    const invoice = new Invoice('John Doe', '2022-01-01');
    const transaction1 = new Transaction('Sale', 100, 'credit');
    const transaction2 = new Transaction('Payment', 50, 'debit');
    invoice.addTransaction(transaction1);
    invoice.addTransaction(transaction2);

    ledger.addTransaction('Cash', transaction2);
    ledger.addTransaction('Accounts Receivable', transaction1);

    console.log(invoice.generatePdf());
    console.log(`Cash balance: ${ledger.getBalance('Cash')}`);
    console.log(`Accounts Receivable balance: ${ledger.getBalance('Accounts Receivable')}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
