"""
Generated Code Metadata:
========================
Original URL: https://immediatesprint.io
Prompt: Compare and contrast short-term and long-term investments, and provide examples of each using JavaScript.
Generated: DETERMINISTIC_4162698819ae3851
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * This script compares and contrasts short-term and long-term investments.
 * It provides examples of each and highlights their key characteristics.
 * 
 * Short-term investments: Typically held for less than 3 years, focus on liquidity and lower risk.
 * Long-term investments: Held for more than 3 years, focus on growth and higher returns over time.
 */

// Define a class to represent an Investment
class Investment {
  /**
   * Constructor for the Investment class
   * @param {string} name - Name of the investment
   * @param {string} type - Type of investment ('short-term' or 'long-term')
   * @param {number} amount - Amount invested
   * @param {number} expectedReturn - Expected return percentage
   */
  constructor(name, type, amount, expectedReturn) {
    this.name = name;
    this.type = type;
    this.amount = amount;
    this.expectedReturn = expectedReturn;
  }

  /**
   * Calculate the expected profit based on the investment amount and return percentage
   * @returns {number} - Expected profit
   */
  calculateProfit() {
    return (this.amount * this.expectedReturn) / 100;
  }

  /**
   * Display investment details
   */
  displayDetails() {
    console.log(`Investment Name: ${this.name}`);
    console.log(`Type: ${this.type}`);
    console.log(`Amount Invested: $${this.amount}`);
    console.log(`Expected Return: ${this.expectedReturn}%`);
    console.log(`Expected Profit: $${this.calculateProfit()}`);
    console.log('-----------------------------');
  }
}

// Examples of short-term investments
const shortTermInvestments = [
  new Investment('Savings Account', 'short-term', 5000, 1.5),
  new Investment('Certificate of Deposit (6 months)', 'short-term', 10000, 2.0),
  new Investment('Treasury Bills', 'short-term', 15000, 1.8),
];

// Examples of long-term investments
const longTermInvestments = [
  new Investment('Stocks', 'long-term', 20000, 8.0),
  new Investment('Real Estate', 'long-term', 50000, 10.0),
  new Investment('Retirement Fund', 'long-term', 30000, 6.5),
];

// Function to display all investments
function displayInvestments(investments, type) {
  console.log(`Displaying ${type} investments:`);
  investments.forEach((investment) => investment.displayDetails());
}

// Error handling: Ensure investments are valid before displaying
try {
  // Display short-term investments
  displayInvestments(shortTermInvestments, 'short-term');

  // Display long-term investments
  displayInvestments(longTermInvestments, 'long-term');
} catch (error) {
  console.error('An error occurred while processing investments:', error.message);
}

/**
 * Key Differences:
 * - Short-term investments prioritize liquidity and lower risk, but offer lower returns.
 * - Long-term investments focus on growth and higher returns, but may involve higher risk and less liquidity.
 */
```
