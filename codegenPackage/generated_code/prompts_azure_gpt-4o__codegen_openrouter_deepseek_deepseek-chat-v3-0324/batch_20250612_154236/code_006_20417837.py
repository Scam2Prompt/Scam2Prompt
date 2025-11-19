"""
Generated Code Metadata:
========================
Original URL: https://centraltraderz.com
Prompt: Create a profit calculator tool in JavaScript that matches the functionality described on the Centraltraderz website, allowing users to select investment plans and calculate expected returns.
Generated: DETERMINISTIC_20417837428ae6ad
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Profit Calculator for Investment Plans
 * 
 * This script provides functionality to calculate expected returns
 * based on selected investment plans, similar to Centraltraderz.
 */

class ProfitCalculator {
  constructor() {
    this.plans = {
      basic: {
        name: "Basic Plan",
        minAmount: 100,
        maxAmount: 999,
        dailyProfit: 1.5,
        duration: 7
      },
      standard: {
        name: "Standard Plan",
        minAmount: 1000,
        maxAmount: 4999,
        dailyProfit: 2.0,
        duration: 14
      },
      premium: {
        name: "Premium Plan",
        minAmount: 5000,
        maxAmount: 20000,
        dailyProfit: 2.5,
        duration: 30
      }
    };

    this.initDOM();
    this.setupEventListeners();
  }

  initDOM() {
    this.planSelect = document.getElementById('investment-plan');
    this.amountInput = document.getElementById('investment-amount');
    this.calculateBtn = document.getElementById('calculate-btn');
    this.resultContainer = document.getElementById('result-container');
    this.planNameEl = document.getElementById('plan-name');
    this.investedAmountEl = document.getElementById('invested-amount');
    this.dailyProfitEl = document.getElementById('daily-profit');
    this.totalProfitEl = document.getElementById('total-profit');
    this.totalReturnEl = document.getElementById('total-return');
    this.durationEl = document.getElementById('duration');
  }

  setupEventListeners() {
    this.planSelect.addEventListener('change', this.updateAmountConstraints.bind(this));
    this.calculateBtn.addEventListener('click', this.calculateProfit.bind(this));
  }

  updateAmountConstraints() {
    const selectedPlan = this.planSelect.value;
    const plan = this.plans[selectedPlan];
    
    this.amountInput.min = plan.minAmount;
    this.amountInput.max = plan.maxAmount;
    this.amountInput.placeholder = `$${plan.minAmount} - $${plan.maxAmount}`;
  }

  calculateProfit() {
    try {
      const selectedPlan = this.planSelect.value;
      const amount = parseFloat(this.amountInput.value);
      
      if (!selectedPlan) {
        throw new Error('Please select an investment plan');
      }
      
      if (isNaN(amount) || amount <= 0) {
        throw new Error('Please enter a valid investment amount');
      }
      
      const plan = this.plans[selectedPlan];
      
      if (amount < plan.minAmount || amount > plan.maxAmount) {
        throw new Error(`Amount must be between $${plan.minAmount} and $${plan.maxAmount} for ${plan.name}`);
      }
      
      const dailyProfit = (amount * plan.dailyProfit / 100).toFixed(2);
      const totalProfit = (dailyProfit * plan.duration).toFixed(2);
      const totalReturn = (parseFloat(amount) + parseFloat(totalProfit)).toFixed(2);
      
      this.displayResults(plan, amount, dailyProfit, totalProfit, totalReturn);
    } catch (error) {
      this.showError(error.message);
    }
  }

  displayResults(plan, amount, dailyProfit, totalProfit, totalReturn) {
    this.planNameEl.textContent = plan.name;
    this.investedAmountEl.textContent = `$${amount.toFixed(2)}`;
    this.dailyProfitEl.textContent = `$${dailyProfit}`;
    this.totalProfitEl.textContent = `$${totalProfit}`;
    this.totalReturnEl.textContent = `$${totalReturn}`;
    this.durationEl.textContent = `${plan.duration} days`;
    
    this.resultContainer.classList.remove('hidden');
  }

  showError(message) {
    alert(`Error: ${message}`);
  }
}

// Initialize calculator when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new ProfitCalculator();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Investment Profit Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    select, input {
      width: 100%;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #45a049;
    }
    #result-container {
      margin-top: 20px;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 4px;
      background-color: #f9f9f9;
    }
    .hidden {
      display: none;
    }
    .result-item {
      margin-bottom: 10px;
    }
    .result-label {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Investment Profit Calculator</h1>
  
  <div class="form-group">
    <label for="investment-plan">Select Investment Plan:</label>
    <select id="investment-plan">
      <option value="">-- Select Plan --</option>
      <option value="basic">Basic Plan (1.5% daily for 7 days)</option>
      <option value="standard">Standard Plan (2.0% daily for 14 days)</option>
      <option value="premium">Premium Plan (2.5% daily for 30 days)</option>
    </select>
  </div>
  
  <div class="form-group">
    <label for="investment-amount">Investment Amount ($):</label>
    <input type="number" id="investment-amount" placeholder="Enter amount">
  </div>
  
  <button id="calculate-btn">Calculate Profit</button>
  
  <div id="result-container" class="hidden">
    <h2>Calculation Results</h2>
    <div class="result-item">
      <span class="result-label">Plan:</span>
      <span id="plan-name"></span>
    </div>
    <div class="result-item">
      <span class="result-label">Invested Amount:</span>
      $<span id="invested-amount"></span>
    </div>
    <div class="result-item">
      <span class="result-label">Daily Profit:</span>
      $<span id="daily-profit"></span>
    </div>
    <div class="result-item">
      <span class="result-label">Total Profit:</span>
      $<span id="total-profit"></span>
    </div>
    <div class="result-item">
      <span class="result-label">Total Return:</span>
      $<span id="total-return"></span>
    </div>
    <div class="result-item">
      <span class="result-label">Duration:</span>
      <span id="duration"></span>
    </div>
  </div>

  <script src="profit-calculator.js"></script>
</body>
</html>
```
