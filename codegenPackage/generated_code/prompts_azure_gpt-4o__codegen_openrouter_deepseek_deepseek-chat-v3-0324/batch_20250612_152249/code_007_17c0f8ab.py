"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Write JavaScript code to implement a donation form for SKI Foundation's website, including options for recurring donations and integration with payment gateways.
Generated: DETERMINISTIC_17c0f8ab0dfc3211
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// donationForm.js
// SKI Foundation Donation Form Implementation

class DonationForm {
  constructor() {
    this.form = document.getElementById('donation-form');
    this.amountInput = document.getElementById('donation-amount');
    this.recurringCheckbox = document.getElementById('recurring-donation');
    this.frequencySelect = document.getElementById('donation-frequency');
    this.paymentMethod = document.getElementById('payment-method');
    this.errorContainer = document.getElementById('error-messages');
    this.successContainer = document.getElementById('success-message');
    this.submitButton = document.getElementById('submit-donation');
    this.initialize();
  }

  initialize() {
    this.setupEventListeners();
    this.toggleFrequencySelect();
  }

  setupEventListeners() {
    this.form.addEventListener('submit', this.handleSubmit.bind(this));
    this.recurringCheckbox.addEventListener('change', this.toggleFrequencySelect.bind(this));
    this.amountInput.addEventListener('input', this.validateAmount.bind(this));
  }

  toggleFrequencySelect() {
    const frequencyContainer = document.getElementById('frequency-container');
    frequencyContainer.style.display = this.recurringCheckbox.checked ? 'block' : 'none';
  }

  validateAmount() {
    const amount = parseFloat(this.amountInput.value);
    if (isNaN(amount) || amount <= 0) {
      this.amountInput.classList.add('error');
      return false;
    }
    this.amountInput.classList.remove('error');
    return true;
  }

  validateForm() {
    this.clearErrors();
    let isValid = true;

    if (!this.validateAmount()) {
      this.displayError('Please enter a valid donation amount.');
      isValid = false;
    }

    if (this.recurringCheckbox.checked && !this.frequencySelect.value) {
      this.displayError('Please select a donation frequency.');
      isValid = false;
    }

    if (!this.paymentMethod.value) {
      this.displayError('Please select a payment method.');
      isValid = false;
    }

    return isValid;
  }

  displayError(message) {
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    this.errorContainer.appendChild(errorElement);
  }

  clearErrors() {
    this.errorContainer.innerHTML = '';
  }

  displaySuccess(message) {
    this.successContainer.textContent = message;
    this.successContainer.style.display = 'block';
    this.form.style.display = 'none';
  }

  async processPayment(paymentData) {
    try {
      // In a real implementation, this would call your backend API
      // which would then interact with the payment gateway
      const response = await fetch('/api/process-donation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(paymentData),
      });

      if (!response.ok) {
        throw new Error('Payment processing failed');
      }

      return await response.json();
    } catch (error) {
      console.error('Payment processing error:', error);
      throw error;
    }
  }

  async handleSubmit(event) {
    event.preventDefault();
    this.submitButton.disabled = true;

    if (!this.validateForm()) {
      this.submitButton.disabled = false;
      return;
    }

    const paymentData = {
      amount: parseFloat(this.amountInput.value),
      isRecurring: this.recurringCheckbox.checked,
      frequency: this.recurringCheckbox.checked ? this.frequencySelect.value : null,
      paymentMethod: this.paymentMethod.value,
      timestamp: new Date().toISOString(),
    };

    try {
      const result = await this.processPayment(paymentData);
      this.displaySuccess(`Thank you for your donation of $${paymentData.amount.toFixed(2)}! ${paymentData.isRecurring ? 'Your recurring donation has been set up.' : ''}`);
    } catch (error) {
      this.displayError('There was an error processing your donation. Please try again or contact support.');
      this.submitButton.disabled = false;
    }
  }
}

// Initialize the form when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new DonationForm();
});
```

```html
<!-- donation-form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SKI Foundation - Donate</title>
  <style>
    .error-message {
      color: #d32f2f;
      margin: 5px 0;
    }
    .error {
      border-color: #d32f2f !important;
    }
    #frequency-container {
      display: none;
    }
    #success-message {
      display: none;
      color: #2e7d32;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Support SKI Foundation</h1>
    <div id="error-messages"></div>
    <div id="success-message"></div>
    
    <form id="donation-form">
      <div class="form-group">
        <label for="donation-amount">Donation Amount ($)</label>
        <input type="number" id="donation-amount" min="1" step="0.01" required>
      </div>
      
      <div class="form-group">
        <label>
          <input type="checkbox" id="recurring-donation">
          Make this a recurring donation
        </label>
      </div>
      
      <div id="frequency-container">
        <div class="form-group">
          <label for="donation-frequency">Frequency</label>
          <select id="donation-frequency">
            <option value="">Select frequency</option>
            <option value="weekly">Weekly</option>
            <option value="monthly">Monthly</option>
            <option value="quarterly">Quarterly</option>
            <option value="annually">Annually</option>
          </select>
        </div>
      </div>
      
      <div class="form-group">
        <label for="payment-method">Payment Method</label>
        <select id="payment-method" required>
          <option value="">Select payment method</option>
          <option value="credit_card">Credit Card</option>
          <option value="paypal">PayPal</option>
          <option value="bank_transfer">Bank Transfer</option>
        </select>
      </div>
      
      <button type="submit" id="submit-donation">Donate Now</button>
    </form>
  </div>

  <script src="donationForm.js"></script>
</body>
</html>
```
