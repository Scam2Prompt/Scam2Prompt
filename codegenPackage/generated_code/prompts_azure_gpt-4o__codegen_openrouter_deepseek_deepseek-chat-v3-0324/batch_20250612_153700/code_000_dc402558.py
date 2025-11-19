"""
Generated Code Metadata:
========================
Original URL: https://ponet.pro
Prompt: Write JavaScript code to create a presale platform interface that dynamically updates based on user input, similar to platforms requiring JavaScript to function.
Generated: DETERMINISTIC_dc402558ce95d977
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Presale Platform Interface
 * Dynamically updates based on user input with real-time calculations
 */

class PresalePlatform {
  constructor() {
    this.tokenPrice = 0.10; // Initial token price in USD
    this.minPurchase = 50; // Minimum purchase amount in USD
    this.maxPurchase = 5000; // Maximum purchase amount in USD
    this.tokensSold = 0;
    this.totalRaised = 0;
    this.presaleTarget = 100000; // Presale target in USD
    this.initElements();
    this.setupEventListeners();
    this.updateUI();
  }

  initElements() {
    this.amountInput = document.getElementById('presale-amount');
    this.tokenAmountDisplay = document.getElementById('token-amount');
    this.totalRaisedDisplay = document.getElementById('total-raised');
    this.progressBar = document.getElementById('progress-bar');
    this.buyButton = document.getElementById('buy-button');
    this.errorDisplay = document.getElementById('error-message');
    this.successDisplay = document.getElementById('success-message');
  }

  setupEventListeners() {
    this.amountInput.addEventListener('input', () => this.handleAmountChange());
    this.buyButton.addEventListener('click', () => this.handlePurchase());
  }

  handleAmountChange() {
    this.clearMessages();
    const amount = parseFloat(this.amountInput.value) || 0;
    
    if (amount > 0) {
      const tokens = amount / this.tokenPrice;
      this.tokenAmountDisplay.textContent = tokens.toFixed(2);
    } else {
      this.tokenAmountDisplay.textContent = '0.00';
    }
  }

  handlePurchase() {
    this.clearMessages();
    const amount = parseFloat(this.amountInput.value) || 0;

    try {
      this.validatePurchase(amount);
      this.processPurchase(amount);
      this.showSuccess(`Successfully purchased ${(amount / this.tokenPrice).toFixed(2)} tokens!`);
      this.amountInput.value = '';
      this.tokenAmountDisplay.textContent = '0.00';
    } catch (error) {
      this.showError(error.message);
    }
  }

  validatePurchase(amount) {
    if (isNaN(amount) || amount <= 0) {
      throw new Error('Please enter a valid amount');
    }

    if (amount < this.minPurchase) {
      throw new Error(`Minimum purchase is $${this.minPurchase}`);
    }

    if (amount > this.maxPurchase) {
      throw new Error(`Maximum purchase is $${this.maxPurchase}`);
    }
  }

  processPurchase(amount) {
    this.tokensSold += amount / this.tokenPrice;
    this.totalRaised += amount;
    this.updateUI();
  }

  updateUI() {
    this.totalRaisedDisplay.textContent = this.totalRaised.toFixed(2);
    const progressPercentage = Math.min((this.totalRaised / this.presaleTarget) * 100, 100);
    this.progressBar.style.width = `${progressPercentage}%`;
  }

  showError(message) {
    this.errorDisplay.textContent = message;
    this.errorDisplay.style.display = 'block';
  }

  showSuccess(message) {
    this.successDisplay.textContent = message;
    this.successDisplay.style.display = 'block';
    setTimeout(() => {
      this.successDisplay.style.display = 'none';
    }, 5000);
  }

  clearMessages() {
    this.errorDisplay.style.display = 'none';
    this.successDisplay.style.display = 'none';
  }
}

// Initialize the presale platform when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new PresalePlatform();
});
```
