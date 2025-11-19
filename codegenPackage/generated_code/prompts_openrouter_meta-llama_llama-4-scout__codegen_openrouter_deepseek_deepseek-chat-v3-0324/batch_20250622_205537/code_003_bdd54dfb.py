"""
Generated Code Metadata:
========================
Original URL: https://joinnow.info
Prompt: "Create a simple income calculator in JavaScript that demonstrates the potential earnings of Money Order Freedom subscribers based on the provided income examples."
Generated: DETERMINISTIC_bdd54dfbabb74b2d
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Money Order Freedom Income Calculator
 * Calculates potential earnings based on subscription tiers and example incomes.
 */

class IncomeCalculator {
  /**
   * Initialize the calculator with example income data
   */
  constructor() {
    this.exampleIncomes = {
      basic: {
        monthly: 500,
        yearly: 6000,
        description: "Basic subscriber earnings"
      },
      intermediate: {
        monthly: 1500,
        yearly: 18000,
        description: "Intermediate subscriber earnings"
      },
      advanced: {
        monthly: 3000,
        yearly: 36000,
        description: "Advanced subscriber earnings"
      },
      expert: {
        monthly: 7500,
        yearly: 90000,
        description: "Expert subscriber earnings"
      }
    };
  }

  /**
   * Calculate potential earnings based on subscription tier
   * @param {string} tier - Subscription tier (basic, intermediate, advanced, expert)
   * @param {number} months - Number of months to calculate
   * @returns {Object} - Calculated earnings with monthly and yearly projections
   * @throws {Error} - If invalid tier is provided
   */
  calculateEarnings(tier, months = 12) {
    if (!this.exampleIncomes[tier]) {
      throw new Error(`Invalid subscription tier: ${tier}`);
    }

    if (typeof months !== 'number' || months <= 0) {
      throw new Error('Months must be a positive number');
    }

    const baseIncome = this.exampleIncomes[tier];
    const calculatedYearly = baseIncome.yearly * (months / 12);

    return {
      monthly: baseIncome.monthly,
      projectedMonthly: baseIncome.monthly * months,
      yearly: baseIncome.yearly,
      projectedYearly: calculatedYearly,
      description: baseIncome.description,
      monthsCalculated: months
    };
  }

  /**
   * Get all available subscription tiers
   * @returns {Array} - List of available tiers
   */
  getAvailableTiers() {
    return Object.keys(this.exampleIncomes);
  }

  /**
   * Get example income for all tiers
   * @returns {Object} - All example incomes
   */
  getAllExampleIncomes() {
    return {...this.exampleIncomes};
  }
}

// UI Handler for the calculator
class CalculatorUI {
  constructor() {
    this.calculator = new IncomeCalculator();
    this.initializeUI();
  }

  initializeUI() {
    this.bindElements();
    this.populateTierDropdown();
    this.setupEventListeners();
  }

  bindElements() {
    this.tierSelect = document.getElementById('tier-select');
    this.monthsInput = document.getElementById('months-input');
    this.calculateBtn = document.getElementById('calculate-btn');
    this.resultsContainer = document.getElementById('results-container');
    this.exampleIncomesContainer = document.getElementById('example-incomes');
  }

  populateTierDropdown() {
    const tiers = this.calculator.getAvailableTiers();
    tiers.forEach(tier => {
      const option = document.createElement('option');
      option.value = tier;
      option.textContent = tier.charAt(0).toUpperCase() + tier.slice(1);
      this.tierSelect.appendChild(option);
    });
  }

  setupEventListeners() {
    this.calculateBtn.addEventListener('click', () => this.handleCalculate());
    this.displayExampleIncomes();
  }

  handleCalculate() {
    try {
      const tier = this.tierSelect.value;
      const months = parseInt(this.monthsInput.value) || 12;
      
      const results = this.calculator.calculateEarnings(tier, months);
      this.displayResults(results);
    } catch (error) {
      this.displayError(error.message);
    }
  }

  displayResults(results) {
    this.resultsContainer.innerHTML = `
      <div class="result-card">
        <h3>${results.description}</h3>
        <p><strong>Monthly Income:</strong> $${results.monthly.toLocaleString()}</p>
        <p><strong>Projected ${results.monthsCalculated}-month Income:</strong> $${results.projectedMonthly.toLocaleString()}</p>
        <p><strong>Yearly Income:</strong> $${results.yearly.toLocaleString()}</p>
        <p><strong>Projected Yearly Equivalent:</strong> $${results.projectedYearly.toLocaleString()}</p>
      </div>
    `;
  }

  displayError(message) {
    this.resultsContainer.innerHTML = `
      <div class="error-message">
        <p>Error: ${message}</p>
      </div>
    `;
  }

  displayExampleIncomes() {
    const incomes = this.calculator.getAllExampleIncomes();
    let html = '<h3>Example Incomes by Tier</h3><div class="income-grid">';
    
    for (const [tier, data] of Object.entries(incomes)) {
      html += `
        <div class="income-tier">
          <h4>${tier.charAt(0).toUpperCase() + tier.slice(1)}</h4>
          <p>Monthly: $${data.monthly.toLocaleString()}</p>
          <p>Yearly: $${data.yearly.toLocaleString()}</p>
        </div>
      `;
    }
    
    html += '</div>';
    this.exampleIncomesContainer.innerHTML = html;
  }
}

// Initialize the calculator UI when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new CalculatorUI();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Money Order Freedom Income Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      color: #333;
    }
    h1 {
      color: #2c3e50;
      text-align: center;
    }
    .calculator-container {
      background: #f9f9f9;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      margin-bottom: 20px;
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
      background: #3498db;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background: #2980b9;
    }
    .result-card, .error-message {
      background: white;
      padding: 15px;
      border-radius: 4px;
      margin-top: 20px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .error-message {
      background: #ffebee;
      color: #c62828;
    }
    .income-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 15px;
      margin-top: 15px;
    }
    .income-tier {
      background: white;
      padding: 15px;
      border-radius: 4px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .income-tier h4 {
      margin-top: 0;
      color: #2c3e50;
    }
  </style>
</head>
<body>
  <h1>Money Order Freedom Income Calculator</h1>
  
  <div class="calculator-container">
    <div class="form-group">
      <label for="tier-select">Subscription Tier:</label>
      <select id="tier-select"></select>
    </div>
    
    <div class="form-group">
      <label for="months-input">Number of Months:</label>
      <input type="number" id="months-input" value="12" min="1">
    </div>
    
    <button id="calculate-btn">Calculate Earnings</button>
    
    <div id="results-container"></div>
  </div>
  
  <div id="example-incomes"></div>

  <script src="calculator.js"></script>
</body>
</html>
```
