"""
Generated Code Metadata:
========================
Original URL: https://presale-humanizedai.web.app
Prompt: Develop a feature that allows users to select staking percentages (e.g., 25%, 50%, 75%, MAX) and update the calculated earnings accordingly, as seen on the HumanizedAi staking page.
Generated: DETERMINISTIC_49ba4546cda5961a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// StakingCalculator.js

/**
 * Calculates earnings based on selected staking percentage.
 */
class StakingCalculator {
  /**
   * @param {number} principal - Initial investment amount.
   * @param {number} rate - Interest rate (in decimal form, e.g., 5% = 0.05).
   * @param {number} time - Time period (in years).
   */
  constructor(principal, rate, time) {
    this.principal = principal;
    this.rate = rate;
    this.time = time;
  }

  /**
   * Calculates earnings based on staking percentage.
   * @param {string} stakingPercentage - Selected staking percentage (e.g., 25%, 50%, 75%, MAX).
   * @returns {number} Calculated earnings.
   */
  calculateEarnings(stakingPercentage) {
    let percentageValue;

    switch (stakingPercentage) {
      case 'MAX':
        percentageValue = 1; // Assuming MAX is 100%
        break;
      default:
        const percentageMatch = stakingPercentage.match(/^(\d+)%$/);
        if (!percentageMatch) {
          throw new Error(`Invalid staking percentage: ${stakingPercentage}`);
        }
        percentageValue = parseInt(percentageMatch[1], 10) / 100;
    }

    const earnings = this.principal * (1 + this.rate) ** this.time * percentageValue;
    return earnings;
  }
}

// StakingPage.js

class StakingPage {
  constructor(calculator) {
    this.calculator = calculator;
    this.stakingPercentages = ['25%', '50%', '75%', 'MAX'];
  }

  /**
   * Updates calculated earnings based on selected staking percentage.
   * @param {string} selectedPercentage - Selected staking percentage.
   */
  updateEarnings(selectedPercentage) {
    try {
      const earnings = this.calculator.calculateEarnings(selectedPercentage);
      this.displayEarnings(earnings);
    } catch (error) {
      this.displayError(error.message);
    }
  }

  /**
   * Displays calculated earnings.
   * @param {number} earnings - Calculated earnings.
   */
  displayEarnings(earnings) {
    console.log(`Calculated earnings: ${earnings.toFixed(2)}`);
    // Update UI component with calculated earnings
  }

  /**
   * Displays error message.
   * @param {string} errorMessage - Error message.
   */
  displayError(errorMessage) {
    console.error(`Error: ${errorMessage}`);
    // Update UI component with error message
  }

  /**
   * Renders staking percentage selection options.
   */
  renderStakingPercentages() {
    console.log('Staking Percentages:');
    this.stakingPercentages.forEach((percentage) => {
      console.log(`- ${percentage}`);
    });
  }
}

// Example usage:

const calculator = new StakingCalculator(1000, 0.05, 1);
const stakingPage = new StakingPage(calculator);

stakingPage.renderStakingPercentages();

const selectedPercentage = '50%';
stakingPage.updateEarnings(selectedPercentage);
```
