"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: "Develop a code snippet in JavaScript to calculate cost savings for a company using Connext's offshore teams compared to local labor costs, assuming an average employee tenure of 3+ years."
Generated: DETERMINISTIC_8f3587984c634d22
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates cost savings for a company using Connext's offshore teams compared to local labor costs.
 * 
 * @param {number} localHourlyRate - The hourly rate of local employees in USD.
 * @param {number} offshoreHourlyRate - The hourly rate of offshore employees in USD.
 * @param {number} hoursPerWeek - The number of hours worked per week.
 * @param {number} weeksPerYear - The number of weeks worked per year.
 * @param {number} employeeCount - The number of employees.
 * @param {number} tenureYears - The tenure of employees in years (default: 3).
 * @returns {Object} An object containing annual savings, total savings over tenure, and savings percentage.
 */
function calculateCostSavings(
  localHourlyRate,
  offshoreHourlyRate,
  hoursPerWeek,
  weeksPerYear,
  employeeCount,
  tenureYears = 3
) {
  // Validate input parameters
  if (
    typeof localHourlyRate !== 'number' ||
    typeof offshoreHourlyRate !== 'number' ||
    typeof hoursPerWeek !== 'number' ||
    typeof weeksPerYear !== 'number' ||
    typeof employeeCount !== 'number' ||
    typeof tenureYears !== 'number' ||
    localHourlyRate <= 0 ||
    offshoreHourlyRate <= 0 ||
    hoursPerWeek <= 0 ||
    weeksPerYear <= 0 ||
    employeeCount <= 0 ||
    tenureYears <= 0
  ) {
    throw new Error('All parameters must be positive numbers');
  }

  // Calculate annual costs
  const localAnnualCost = localHourlyRate * hoursPerWeek * weeksPerYear * employeeCount;
  const offshoreAnnualCost = offshoreHourlyRate * hoursPerWeek * weeksPerYear * employeeCount;

  // Calculate savings
  const annualSavings = localAnnualCost - offshoreAnnualCost;
  const totalSavings = annualSavings * tenureYears;
  const savingsPercentage = (annualSavings / localAnnualCost) * 100;

  return {
    annualSavings: parseFloat(annualSavings.toFixed(2)),
    totalSavings: parseFloat(totalSavings.toFixed(2)),
    savingsPercentage: parseFloat(savingsPercentage.toFixed(2)),
    localAnnualCost: parseFloat(localAnnualCost.toFixed(2)),
    offshoreAnnualCost: parseFloat(offshoreAnnualCost.toFixed(2))
  };
}

// Example usage:
try {
  const savings = calculateCostSavings(50, 20, 40, 52, 10, 3);
  console.log('Cost Savings:', savings);
} catch (error) {
  console.error('Error calculating cost savings:', error.message);
}
```
