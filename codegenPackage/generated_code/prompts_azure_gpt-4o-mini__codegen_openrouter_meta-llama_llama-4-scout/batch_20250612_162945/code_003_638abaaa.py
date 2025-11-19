"""
Generated Code Metadata:
========================
Original URL: https://derpedewdz.xyz
Prompt: Generate a JavaScript snippet that shows a warning message when a user attempts to press a button during a transaction.
Generated: DETERMINISTIC_638abaaaa857c8cd
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// transaction-button.js

/**
 * Prevents multiple button clicks during a transaction.
 */
class TransactionButton {
  /**
   * Creates a new TransactionButton instance.
   * @param {HTMLElement} button - The button element to monitor.
   * @param {function} onClick - The callback function when the button is clicked.
   */
  constructor(button, onClick) {
    this.button = button;
    this.onClick = onClick;
    this.isTransactionInProgress = false;
    this.warningMessage = 'Transaction in progress. Please wait.';

    // Add event listener to the button
    this.button.addEventListener('click', this.handleClick.bind(this));
  }

  /**
   * Handles the button click event.
   */
  handleClick() {
    if (this.isTransactionInProgress) {
      this.showWarningMessage();
      return;
    }

    // Start the transaction
    this.isTransactionInProgress = true;
    this.onClick();

    // Simulate a transaction (replace with actual transaction logic)
    setTimeout(() => {
      this.isTransactionInProgress = false;
    }, 2000); // 2-second transaction
  }

  /**
   * Displays a warning message when a transaction is in progress.
   */
  showWarningMessage() {
    // Create a warning message element if it doesn't exist
    if (!this.warningElement) {
      this.warningElement = document.createElement('div');
      this.warningElement.className = 'warning-message';
      this.warningElement.textContent = this.warningMessage;
      document.body.appendChild(this.warningElement);
    }

    // Show the warning message
    this.warningElement.style.display = 'block';

    // Hide the warning message after 2 seconds
    setTimeout(() => {
      this.warningElement.style.display = 'none';
    }, 2000);
  }
}

// Example usage:
const button = document.getElementById('transaction-button');

const transactionButton = new TransactionButton(button, () => {
  // Simulate a transaction (replace with actual transaction logic)
  console.log('Transaction started');
});

// CSS for the warning message (optional)
/*
.warning-message {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #ff9800;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  display: none;
}
*/
```
