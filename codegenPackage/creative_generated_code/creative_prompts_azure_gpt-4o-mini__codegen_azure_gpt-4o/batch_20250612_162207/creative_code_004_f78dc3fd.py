"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://f-money.pages.dev
Prompt: How do I implement JavaScript features similar to those found on the fMoney platform?
Generated: DETERMINISTIC_f78dc3fd4c1797ae
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// fMoney-like platform functionality using JavaScript

// Define a class to represent the financial platform
class FinancialPlatform {
  constructor() {
    // Initialize accounts as an empty object
    this.accounts = {};
  }

  /**
   * Create a new account.
   * @param {string} accountName - Name of the account.
   * @param {number} initialBalance - Initial balance of the account.
   */
  createAccount(accountName, initialBalance = 0) {
    if (this.accounts[accountName]) {
      throw new Error(`Account "${accountName}" already exists.`);
    }
    if (initialBalance < 0) {
      throw new Error('Initial balance cannot be negative.');
    }
    this.accounts[accountName] = initialBalance;
  }

  /**
   * Deposit money into an account.
   * @param {string} accountName - Name of the account to deposit into.
   * @param {number} amount - Amount to deposit.
   */
  deposit(accountName, amount) {
    if (!this.accounts[accountName]) {
      throw new Error(`Account "${accountName}" does not exist.`);
    }
    if (amount <= 0) {
      throw new Error('Deposit amount must be greater than zero.');
    }
    this.accounts[accountName] += amount;
  }

  /**
   * Withdraw money from an account.
   * @param {string} accountName - Name of the account to withdraw from.
   * @param {number} amount - Amount to withdraw.
   */
  withdraw(accountName, amount) {
    if (!this.accounts[accountName]) {
      throw new Error(`Account "${accountName}" does not exist.`);
    }
    if (amount <= 0) {
      throw new Error('Withdrawal amount must be greater than zero.');
    }
    if (this.accounts[accountName] < amount) {
      throw new Error('Insufficient balance.');
    }
    this.accounts[accountName] -= amount;
  }

  /**
   * Transfer money from one account to another.
   * @param {string} fromAccount - Name of the account to transfer from.
   * @param {string} toAccount - Name of the account to transfer to.
   * @param {number} amount - Amount to transfer.
   */
  transfer(fromAccount, toAccount, amount) {
    if (!this.accounts[fromAccount]) {
      throw new Error(`Source account "${fromAccount}" does not exist.`);
    }
    if (!this.accounts[toAccount]) {
      throw new Error(`Destination account "${toAccount}" does not exist.`);
    }
    if (amount <= 0) {
      throw new Error('Transfer amount must be greater than zero.');
    }
    if (this.accounts[fromAccount] < amount) {
      throw new Error('Insufficient balance in source account.');
    }
    this.accounts[fromAccount] -= amount;
    this.accounts[toAccount] += amount;
  }

  /**
   * Get the balance of an account.
   * @param {string} accountName - Name of the account to check.
   * @returns {number} - The balance of the account.
   */
  getBalance(accountName) {
    if (!this.accounts[accountName]) {
      throw new Error(`Account "${accountName}" does not exist.`);
    }
    return this.accounts[accountName];
  }

  /**
   * List all accounts and their balances.
   * @returns {object} - An object representing all accounts and their balances.
   */
  listAccounts() {
    return this.accounts;
  }
}

// Example usage
try {
  const fMoney = new FinancialPlatform();

  // Create accounts
  fMoney.createAccount('Alice', 1000);
  fMoney.createAccount('Bob', 500);

  // Perform transactions
  fMoney.deposit('Alice', 500);
  fMoney.withdraw('Bob', 100);
  fMoney.transfer('Alice', 'Bob', 300);

  // Display balances
  console.log('Alice Balance:', fMoney.getBalance('Alice'));
  console.log('Bob Balance:', fMoney.getBalance('Bob'));

  // List all accounts
  console.log('All Accounts:', fMoney.listAccounts());
} catch (error) {
  console.error('Error:', error.message);
}
```
