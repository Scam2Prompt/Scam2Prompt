"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reddecomercio.com
Prompt: Create a function in JavaScript that calculates customs duties based on the guidelines from Red de Comercio's consulting services.
Generated: DETERMINISTIC_31ec13dbd74eea1f
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates customs duties based on the specified guidelines.
 * 
 * @param {number} itemValue - The declared value of the item in the local currency.
 * @param {number} customsRate - The applicable customs duty rate (percentage).
 * @param {number} taxRate - The applicable tax rate (percentage).
 * @returns {number} - The total customs duties including taxes.
 * @throws {Error} - Throws an error if itemValue, customsRate, or taxRate are invalid.
 */
function calculateCustomsDuties(itemValue, customsRate, taxRate) {
    // Validate input parameters
    if (typeof itemValue !== 'number' || itemValue < 0) {
        throw new Error('Invalid item value. It must be a non-negative number.');
    }
    if (typeof customsRate !== 'number' || customsRate < 0) {
        throw new Error('Invalid customs rate. It must be a non-negative number.');
    }
    if (typeof taxRate !== 'number' || taxRate < 0) {
        throw new Error('Invalid tax rate. It must be a non-negative number.');
    }

    // Calculate customs duty
    const customsDuty = (itemValue * customsRate) / 100;

    // Calculate total tax on customs duty
    const totalTax = (customsDuty * taxRate) / 100;

    // Calculate total customs duties including taxes
    const totalCustomsDuties = customsDuty + totalTax;

    return totalCustomsDuties;
}

// Example usage
try {
    const itemValue = 1000; // Example item value in local currency
    const customsRate = 5; // Example customs rate in percentage
    const taxRate = 10; // Example tax rate in percentage

    const duties = calculateCustomsDuties(itemValue, customsRate, taxRate);
    console.log(`Total customs duties: ${duties.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating customs duties: ${error.message}`);
}
```
