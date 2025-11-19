"""
Generated Code Metadata:
========================
Original URL: https://crypto4rex360.com
Prompt: Create a JavaScript program to display a dynamic profit calculator for all investment plans on Crypto 4Rex 360, including user input for investment amounts and plan selection.
Generated: DETERMINISTIC_ab5120d6058a16bf
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Crypto 4Rex 360 Profit Calculator
 * A dynamic calculator to compute profits based on investment plans.
 */

// Investment plans data
const investmentPlans = [
  {
    id: 1,
    name: "Starter Plan",
    minAmount: 100,
    maxAmount: 999,
    dailyProfit: 0.05,
    duration: 7,
    features: ["5% daily profit", "7 days duration"]
  },
  {
    id: 2,
    name: "Premium Plan",
    minAmount: 1000,
    maxAmount: 4999,
    dailyProfit: 0.07,
    duration: 14,
    features: ["7% daily profit", "14 days duration"]
  },
  {
    id: 3,
    name: "Professional Plan",
    minAmount: 5000,
    maxAmount: 19999,
    dailyProfit: 0.09,
    duration: 21,
    features: ["9% daily profit", "21 days duration"]
  },
  {
    id: 4,
    name: "VIP Plan",
    minAmount: 20000,
    maxAmount: 100000,
    dailyProfit: 0.12,
    duration: 30,
    features: ["12% daily profit", "30 days duration"]
  }
];

// DOM elements
const planSelect = document.getElementById('plan-select');
const amountInput = document.getElementById('investment-amount');
const calculateBtn = document.getElementById('calculate-btn');
const resultsDiv = document.getElementById('results');
const planDetailsDiv = document.getElementById('plan-details');

// Initialize the calculator
function initCalculator() {
  // Populate plan select dropdown
  investmentPlans.forEach(plan => {
    const option = document.createElement('option');
    option.value = plan.id;
    option.textContent = plan.name;
    planSelect.appendChild(option);
  });

  // Set default plan details
  updatePlanDetails(investmentPlans[0]);
  
  // Add event listeners
  planSelect.addEventListener('change', handlePlanChange);
  amountInput.addEventListener('input', validateAmount);
  calculateBtn.addEventListener('click', calculateProfit);
}

// Update plan details display
function updatePlanDetails(plan) {
  planDetailsDiv.innerHTML = `
    <h3>${plan.name}</h3>
    <ul>
      ${plan.features.map(feature => `<li>${feature}</li>`).join('')}
    </ul>
    <p>Investment Range: $${plan.minAmount.toLocaleString()} - $${plan.maxAmount.toLocaleString()}</p>
  `;
}

// Handle plan selection change
function handlePlanChange() {
  const selectedPlanId = parseInt(planSelect.value);
  const selectedPlan = investmentPlans.find(plan => plan.id === selectedPlanId);
  updatePlanDetails(selectedPlan);
  validateAmount();
}

// Validate investment amount
function validateAmount() {
  const amount = parseFloat(amountInput.value) || 0;
  const selectedPlanId = parseInt(planSelect.value);
  const selectedPlan = investmentPlans.find(plan => plan.id === selectedPlanId);
  
  if (amount < selectedPlan.minAmount || amount > selectedPlan.maxAmount) {
    amountInput.classList.add('invalid');
    calculateBtn.disabled = true;
    return false;
  } else {
    amountInput.classList.remove('invalid');
    calculateBtn.disabled = false;
    return true;
  }
}

// Calculate and display profit
function calculateProfit() {
  if (!validateAmount()) return;

  const amount = parseFloat(amountInput.value);
  const selectedPlanId = parseInt(planSelect.value);
  const selectedPlan = investmentPlans.find(plan => plan.id === selectedPlanId);

  const dailyProfit = amount * selectedPlan.dailyProfit;
  const totalProfit = dailyProfit * selectedPlan.duration;
  const totalReturn = amount + totalProfit;

  resultsDiv.innerHTML = `
    <div class="result-item">
      <h3>Profit Calculation Results</h3>
      <p><strong>Plan:</strong> ${selectedPlan.name}</p>
      <p><strong>Investment Amount:</strong> $${amount.toLocaleString()}</p>
      <p><strong>Daily Profit:</strong> $${dailyProfit.toFixed(2)} (${(selectedPlan.dailyProfit * 100).toFixed(0)}%)</p>
      <p><strong>Total Profit (${selectedPlan.duration} days):</strong> $${totalProfit.toFixed(2)}</p>
      <p><strong>Total Return:</strong> $${totalReturn.toFixed(2)}</p>
    </div>
  `;
}

// Initialize calculator when DOM is loaded
document.addEventListener('DOMContentLoaded', initCalculator);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Crypto 4Rex 360 Profit Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      color: #333;
    }
    .calculator-container {
      background-color: #f9f9f9;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
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
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-size: 16px;
    }
    input.invalid {
      border-color: #ff4444;
    }
    button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 12px 20px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
      width: 100%;
    }
    button:disabled {
      background-color: #cccccc;
      cursor: not-allowed;
    }
    #plan-details, #results {
      margin-top: 20px;
      padding: 15px;
      background-color: #fff;
      border-radius: 4px;
      border: 1px solid #ddd;
    }
    .result-item p {
      margin: 8px 0;
    }
  </style>
</head>
<body>
  <div class="calculator-container">
    <h1>Crypto 4Rex 360 Profit Calculator</h1>
    
    <div class="form-group">
      <label for="plan-select">Select Investment Plan:</label>
      <select id="plan-select"></select>
    </div>
    
    <div id="plan-details"></div>
    
    <div class="form-group">
      <label for="investment-amount">Investment Amount ($):</label>
      <input type="number" id="investment-amount" min="0" step="1" placeholder="Enter amount">
    </div>
    
    <button id="calculate-btn" disabled>Calculate Profit</button>
    
    <div id="results"></div>
  </div>

  <script src="calculator.js"></script>
</body>
</html>
```
