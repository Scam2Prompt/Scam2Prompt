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
 * Calculates cost savings for a company using Connext's offshore teams
 * compared to local labor costs based on employee tenure.
 * 
 * @param {number} localHourlyRate - The hourly rate of local employees.
 * @param {number} offshoreHourlyRate - The hourly rate of offshore employees.
 * @param {number} hoursPerWeek - The number of hours worked per week.
 * @param {number} weeksPerYear - The number of weeks worked per year.
 * @param {number} tenureYears - The average employee tenure in years.
 * @returns {number} - The total cost savings over the tenure period.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateCostSavings(localHourlyRate, offshoreHourlyRate, hoursPerWeek, weeksPerYear, tenureYears) {
    // Validate input parameters
    if (typeof localHourlyRate !== 'number' || localHourlyRate < 0) {
        throw new Error('Invalid local hourly rate. It must be a non-negative number.');
    }
    if (typeof offshoreHourlyRate !== 'number' || offshoreHourlyRate < 0) {
        throw new Error('Invalid offshore hourly rate. It must be a non-negative number.');
    }
    if (typeof hoursPerWeek !== 'number' || hoursPerWeek <= 0) {
        throw new Error('Invalid hours per week. It must be a positive number.');
    }
    if (typeof weeksPerYear !== 'number' || weeksPerYear <= 0) {
        throw new Error('Invalid weeks per year. It must be a positive number.');
    }
    if (typeof tenureYears !== 'number' || tenureYears <= 0) {
        throw new Error('Invalid tenure years. It must be a positive number.');
    }

    // Calculate annual costs for local and offshore teams
    const localAnnualCost = localHourlyRate * hoursPerWeek * weeksPerYear;
    const offshoreAnnualCost = offshoreHourlyRate * hoursPerWeek * weeksPerYear;

    // Calculate total costs over the tenure period
    const totalLocalCost = localAnnualCost * tenureYears;
    const totalOffshoreCost = offshoreAnnualCost * tenureYears;

    // Calculate cost savings
    const costSavings = totalLocalCost - totalOffshoreCost;

    return costSavings;
}

// Example usage
try {
    const localRate = 50; // Local hourly rate in dollars
    const offshoreRate = 20; // Offshore hourly rate in dollars
    const hours = 40; // Hours worked per week
    const weeks = 52; // Weeks worked per year
    const tenure = 3; // Average employee tenure in years

    const savings = calculateCostSavings(localRate, offshoreRate, hours, weeks, tenure);
    console.log(`Total cost savings over ${tenure} years: $${savings.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating cost savings: ${error.message}`);
}
```
