"""
Generated Code Metadata:
========================
Original URL: https://washingtonpost.earnwithliquid.com
Prompt: Generate JavaScript code to create a simple cashback calculator for Amazon purchases with a 2% cashback rate, similar to The Washington Post's offer.
Generated: DETERMINISTIC_f65e13c16e2334d3
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Amazon Cashback Calculator
 * Calculates cashback based on Amazon purchase amount with a 2% cashback rate.
 */

class CashbackCalculator {
  /**
   * Initialize the calculator with cashback rate
   * @param {number} cashbackRate - Cashback percentage (e.g., 2 for 2%)
   */
  constructor(cashbackRate = 2) {
    this.cashbackRate = cashbackRate;
  }

  /**
   * Calculate cashback amount
   * @param {number} purchaseAmount - Total purchase amount in USD
   * @returns {number} Calculated cashback amount
   * @throws {Error} If purchaseAmount is not a positive number
   */
  calculateCashback(purchaseAmount) {
    if (typeof purchaseAmount !== 'number' || purchaseAmount <= 0) {
      throw new Error('Purchase amount must be a positive number');
    }

    return (purchaseAmount * this.cashbackRate) / 100;
  }
}

// DOM Elements
const form = document.getElementById('cashback-form');
const amountInput = document.getElementById('purchase-amount');
const resultDiv = document.getElementById('result');

// Initialize calculator with 2% cashback rate
const calculator = new CashbackCalculator(2);

/**
 * Handle form submission
 * @param {Event} e - Form submit event
 */
function handleSubmit(e) {
  e.preventDefault();
  
  try {
    const purchaseAmount = parseFloat(amountInput.value);
    const cashback = calculator.calculateCashback(purchaseAmount);
    
    resultDiv.innerHTML = `
      <p>Purchase Amount: $${purchaseAmount.toFixed(2)}</p>
      <p>Cashback Rate: ${calculator.cashbackRate}%</p>
      <p class="highlight">You Earn: $${cashback.toFixed(2)}</p>
    `;
    resultDiv.style.display = 'block';
  } catch (error) {
    resultDiv.innerHTML = `<p class="error">${error.message}</p>`;
    resultDiv.style.display = 'block';
  }
}

// Event Listeners
if (form) {
  form.addEventListener('submit', handleSubmit);
}

// HTML Structure Example (for reference, not part of JS code)
/*
<form id="cashback-form">
  <label for="purchase-amount">Amazon Purchase Amount ($):</label>
  <input type="number" id="purchase-amount" step="0.01" min="0.01" required>
  <button type="submit">Calculate Cashback</button>
</form>
<div id="result" style="display: none;"></div>
*/
```
