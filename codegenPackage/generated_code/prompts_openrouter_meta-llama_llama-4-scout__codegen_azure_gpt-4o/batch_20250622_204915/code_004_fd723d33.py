"""
Generated Code Metadata:
========================
Original URL: https://howtosuecslplasma.org
Prompt: Create a JavaScript function to calculate the potential compensation for a plaintiff in a CSL Plasma lawsuit based on factors like medical expenses and lost wages.
Generated: DETERMINISTIC_fd723d3355c486f4
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate potential compensation for a plaintiff in a CSL Plasma lawsuit.
 * 
 * @param {Object} factors - An object containing the relevant factors for compensation calculation.
 * @param {number} factors.medicalExpenses - Total medical expenses incurred by the plaintiff.
 * @param {number} factors.lostWages - Total lost wages due to inability to work.
 * @param {number} factors.painAndSufferingMultiplier - Multiplier for pain and suffering (typically between 1 and 5).
 * @returns {number} - The calculated potential compensation amount.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateCompensation(factors) {
    // Validate input
    if (!factors || typeof factors !== 'object') {
        throw new Error("Invalid input: factors must be an object.");
    }

    const { medicalExpenses, lostWages, painAndSufferingMultiplier } = factors;

    if (typeof medicalExpenses !== 'number' || medicalExpenses < 0) {
        throw new Error("Invalid input: medicalExpenses must be a non-negative number.");
    }

    if (typeof lostWages !== 'number' || lostWages < 0) {
        throw new Error("Invalid input: lostWages must be a non-negative number.");
    }

    if (typeof painAndSufferingMultiplier !== 'number' || painAndSufferingMultiplier < 1 || painAndSufferingMultiplier > 5) {
        throw new Error("Invalid input: painAndSufferingMultiplier must be a number between 1 and 5.");
    }

    // Calculate compensation
    const painAndSuffering = (medicalExpenses + lostWages) * painAndSufferingMultiplier;
    const totalCompensation = medicalExpenses + lostWages + painAndSuffering;

    return totalCompensation;
}

// Example usage:
try {
    const factors = {
        medicalExpenses: 5000,
        lostWages: 2000,
        painAndSufferingMultiplier: 3
    };

    const compensation = calculateCompensation(factors);
    console.log(`Potential compensation: $${compensation.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating compensation: ${error.message}`);
}
```
