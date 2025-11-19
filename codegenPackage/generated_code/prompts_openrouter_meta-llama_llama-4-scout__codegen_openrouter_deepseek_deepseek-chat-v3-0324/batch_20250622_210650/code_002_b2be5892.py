"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Generate a code snippet in JavaScript to implement a simple calculator for calculating labor law compensation, taking into account factors such as salary, years of service, and type of dismissal.
Generated: DETERMINISTIC_b2be58927d0cfdd2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Labor Law Compensation Calculator
 * Calculates compensation based on salary, years of service, and dismissal type
 */

class LaborLawCalculator {
  /**
   * @param {number} monthlySalary - Monthly salary in local currency
   * @param {number} yearsOfService - Total years of service
   * @param {string} dismissalType - Type of dismissal ('unjustified', 'justified', 'resignation')
   */
  constructor(monthlySalary, yearsOfService, dismissalType) {
    this.validateInput(monthlySalary, yearsOfService, dismissalType);
    
    this.monthlySalary = monthlySalary;
    this.yearsOfService = yearsOfService;
    this.dismissalType = dismissalType.toLowerCase();
  }

  /**
   * Validates input parameters
   * @throws {Error} If input is invalid
   */
  validateInput(monthlySalary, yearsOfService, dismissalType) {
    if (typeof monthlySalary !== 'number' || monthlySalary <= 0) {
      throw new Error('Monthly salary must be a positive number');
    }
    
    if (typeof yearsOfService !== 'number' || yearsOfService < 0) {
      throw new Error('Years of service must be a non-negative number');
    }
    
    const validDismissalTypes = ['unjustified', 'justified', 'resignation'];
    if (!validDismissalTypes.includes(dismissalType.toLowerCase())) {
      throw new Error(`Dismissal type must be one of: ${validDismissalTypes.join(', ')}`);
    }
  }

  /**
   * Calculates compensation based on labor law rules
   * @returns {number} Compensation amount in local currency
   */
  calculateCompensation() {
    let compensation = 0;
    
    // Base compensation rules
    if (this.dismissalType === 'unjustified') {
      // 1 month per year of service for unjustified dismissal
      compensation = this.monthlySalary * this.yearsOfService;
      
      // Minimum of 3 months salary if less than 1 year of service
      if (this.yearsOfService < 1) {
        compensation = Math.max(compensation, this.monthlySalary * 3);
      }
    } 
    else if (this.dismissalType === 'justified') {
      // 0.5 month per year of service for justified dismissal
      compensation = this.monthlySalary * this.yearsOfService * 0.5;
      
      // Minimum of 1 month salary if less than 1 year of service
      if (this.yearsOfService < 1) {
        compensation = Math.max(compensation, this.monthlySalary);
      }
    }
    // No compensation for resignation
    
    return Math.round(compensation * 100) / 100; // Round to 2 decimal places
  }
}

// Example usage:
try {
  const calculator = new LaborLawCalculator(3000, 5, 'unjustified');
  const compensation = calculator.calculateCompensation();
  console.log(`Compensation amount: ${compensation}`);
} catch (error) {
  console.error(`Error calculating compensation: ${error.message}`);
}
```
