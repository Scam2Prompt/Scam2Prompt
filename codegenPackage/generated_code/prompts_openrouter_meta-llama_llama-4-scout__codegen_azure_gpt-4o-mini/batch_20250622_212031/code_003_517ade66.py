"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Create a JavaScript function to calculate the cost of installation for a Gree Versati III heat pump based on the provided pricing on frigoterm.ro."
Generated: DETERMINISTIC_517ade66122aa961
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the installation cost for a Gree Versati III heat pump.
 * 
 * @param {number} unitPrice - The price of the heat pump unit.
 * @param {number} installationRate - The hourly rate for installation.
 * @param {number} hours - The estimated number of hours for installation.
 * @returns {number} - The total cost of installation including the unit price.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateInstallationCost(unitPrice, installationRate, hours) {
    // Validate inputs
    if (typeof unitPrice !== 'number' || unitPrice < 0) {
        throw new Error('Invalid unit price. It must be a non-negative number.');
    }
    if (typeof installationRate !== 'number' || installationRate < 0) {
        throw new Error('Invalid installation rate. It must be a non-negative number.');
    }
    if (typeof hours !== 'number' || hours < 0) {
        throw new Error('Invalid hours. It must be a non-negative number.');
    }

    // Calculate installation cost
    const installationCost = installationRate * hours;

    // Calculate total cost
    const totalCost = unitPrice + installationCost;

    return totalCost;
}

// Example usage
try {
    const unitPrice = 1500; // Example unit price in currency
    const installationRate = 50; // Example installation rate per hour
    const hours = 5; // Example estimated hours for installation

    const totalCost = calculateInstallationCost(unitPrice, installationRate, hours);
    console.log(`The total installation cost is: ${totalCost}`);
} catch (error) {
    console.error(`Error calculating installation cost: ${error.message}`);
}
```
