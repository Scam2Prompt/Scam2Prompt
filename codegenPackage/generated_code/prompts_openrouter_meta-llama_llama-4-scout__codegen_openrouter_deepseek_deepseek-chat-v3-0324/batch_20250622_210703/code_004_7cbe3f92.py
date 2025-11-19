"""
Generated Code Metadata:
========================
Original URL: https://nlyedu.com
Prompt: Create a JavaScript calculator for estimating pet insurance costs based on the types of pet insurance discussed here.
Generated: DETERMINISTIC_7cbe3f9216f5e650
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Pet Insurance Calculator
 * Estimates insurance costs based on pet type, age, breed, and coverage level
 */

class PetInsuranceCalculator {
  constructor() {
    // Base rates per pet type (per month)
    this.baseRates = {
      dog: 30,
      cat: 20,
      bird: 15,
      rabbit: 12,
      reptile: 18,
      exotic: 25
    };

    // Age multipliers
    this.ageFactors = {
      '0-2': 1.0,
      '3-5': 1.2,
      '6-8': 1.5,
      '9+': 2.0
    };

    // Breed risk factors
    this.breedFactors = {
      low: 1.0,
      medium: 1.3,
      high: 1.7
    };

    // Coverage level multipliers
    this.coverageLevels = {
      basic: 1.0,
      standard: 1.5,
      premium: 2.0
    };
  }

  /**
   * Calculate monthly insurance cost
   * @param {string} petType - Type of pet (dog, cat, etc.)
   * @param {number} age - Age of pet in years
   * @param {string} breedRisk - Breed risk level (low, medium, high)
   * @param {string} coverage - Coverage level (basic, standard, premium)
   * @returns {number} Monthly insurance cost
   */
  calculateCost(petType, age, breedRisk, coverage) {
    try {
      // Validate inputs
      if (!this.baseRates[petType.toLowerCase()]) {
        throw new Error('Invalid pet type');
      }
      if (typeof age !== 'number' || age < 0) {
        throw new Error('Age must be a positive number');
      }
      if (!this.breedFactors[breedRisk.toLowerCase()]) {
        throw new Error('Invalid breed risk level');
      }
      if (!this.coverageLevels[coverage.toLowerCase()]) {
        throw new Error('Invalid coverage level');
      }

      // Get base rate
      const baseRate = this.baseRates[petType.toLowerCase()];

      // Determine age factor
      let ageFactor;
      if (age <= 2) ageFactor = this.ageFactors['0-2'];
      else if (age <= 5) ageFactor = this.ageFactors['3-5'];
      else if (age <= 8) ageFactor = this.ageFactors['6-8'];
      else ageFactor = this.ageFactors['9+'];

      // Get breed factor
      const breedFactor = this.breedFactors[breedRisk.toLowerCase()];

      // Get coverage factor
      const coverageFactor = this.coverageLevels[coverage.toLowerCase()];

      // Calculate final cost
      return baseRate * ageFactor * breedFactor * coverageFactor;
    } catch (error) {
      console.error('Calculation error:', error.message);
      return null;
    }
  }
}

// UI Handler Class
class PetInsuranceUI {
  constructor() {
    this.calculator = new PetInsuranceCalculator();
    this.initDOM();
    this.bindEvents();
  }

  initDOM() {
    this.petTypeSelect = document.getElementById('pet-type');
    this.ageInput = document.getElementById('pet-age');
    this.breedRiskSelect = document.getElementById('breed-risk');
    this.coverageSelect = document.getElementById('coverage-level');
    this.calculateBtn = document.getElementById('calculate-btn');
    this.resultDiv = document.getElementById('result');
    this.errorDiv = document.getElementById('error');
  }

  bindEvents() {
    this.calculateBtn.addEventListener('click', () => this.handleCalculate());
  }

  handleCalculate() {
    this.errorDiv.textContent = '';
    this.resultDiv.textContent = '';

    try {
      const petType = this.petTypeSelect.value;
      const age = parseInt(this.ageInput.value);
      const breedRisk = this.breedRiskSelect.value;
      const coverage = this.coverageSelect.value;

      if (!petType || !age || !breedRisk || !coverage) {
        throw new Error('All fields are required');
      }

      const cost = this.calculator.calculateCost(petType, age, breedRisk, coverage);
      
      if (cost === null) {
        throw new Error('Invalid calculation parameters');
      }

      this.resultDiv.textContent = `Estimated Monthly Cost: $${cost.toFixed(2)}`;
    } catch (error) {
      this.errorDiv.textContent = error.message;
    }
  }
}

// Initialize UI when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new PetInsuranceUI();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pet Insurance Calculator</title>
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
      box-sizing: border-box;
    }
    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 15px;
      border: none;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #45a049;
    }
    #result {
      margin-top: 20px;
      font-size: 18px;
      font-weight: bold;
    }
    #error {
      color: red;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <h1>Pet Insurance Calculator</h1>
  
  <div class="form-group">
    <label for="pet-type">Pet Type:</label>
    <select id="pet-type">
      <option value="">Select Pet Type</option>
      <option value="dog">Dog</option>
      <option value="cat">Cat</option>
      <option value="bird">Bird</option>
      <option value="rabbit">Rabbit</option>
      <option value="reptile">Reptile</option>
      <option value="exotic">Exotic</option>
    </select>
  </div>
  
  <div class="form-group">
    <label for="pet-age">Pet Age (years):</label>
    <input type="number" id="pet-age" min="0" step="1">
  </div>
  
  <div class="form-group">
    <label for="breed-risk">Breed Risk Level:</label>
    <select id="breed-risk">
      <option value="">Select Risk Level</option>
      <option value="low">Low</option>
      <option value="medium">Medium</option>
      <option value="high">High</option>
    </select>
  </div>
  
  <div class="form-group">
    <label for="coverage-level">Coverage Level:</label>
    <select id="coverage-level">
      <option value="">Select Coverage</option>
      <option value="basic">Basic</option>
      <option value="standard">Standard</option>
      <option value="premium">Premium</option>
    </select>
  </div>
  
  <button id="calculate-btn">Calculate</button>
  
  <div id="result"></div>
  <div id="error"></div>

  <script src="calculator.js"></script>
</body>
</html>
```
