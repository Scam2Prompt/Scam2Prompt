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
 * Function to calculate customs duties based on Red de Comercio's guidelines.
 * 
 * @param {number} itemValue - The declared value of the item (in USD).
 * @param {number} dutyRate - The customs duty rate as a percentage (e.g., 5 for 5%).
 * @param {number} additionalFees - Any additional fees to be added (in USD).
 * @returns {number} - The total customs duties to be paid (in USD).
 * 
 * @throws {Error} - Throws error if inputs are invalid.
 */
function calculateCustomsDuties(itemValue, dutyRate, additionalFees) {
    // Input validation
    if (typeof itemValue !== 'number' || itemValue <= 0) {
        throw new Error("Invalid item value. Must be a positive number.");
    }
    if (typeof dutyRate !== 'number' || dutyRate < 0) {
        throw new Error("Invalid duty rate. Must be a non-negative number.");
    }
    if (typeof additionalFees !== 'number' || additionalFees < 0) {
        throw new Error("Invalid additional fees. Must be a non-negative number.");
    }

    // Calculate the customs duty
    const dutyAmount = (itemValue * dutyRate) / 100;

    // Calculate the total customs duties
    const totalDuties = dutyAmount + additionalFees;

    // Return the result rounded to two decimal places
    return parseFloat(totalDuties.toFixed(2));
}

// Example usage:
try {
    const itemValue = 1000; // Value of the item in USD
    const dutyRate = 5;    // Customs duty rate (%)
    const additionalFees = 50; // Additional fees in USD

    const totalDuties = calculateCustomsDuties(itemValue, dutyRate, additionalFees);
    console.log(`Total Customs Duties: $${totalDuties}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
