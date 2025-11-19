"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recuperacionjc.com
Prompt: Create a JavaScript function that calculates potential savings on car insurance based on user input, inspired by the money-saving tips on recuperacionjc.com.
Generated: DETERMINISTIC_d4bb337d5946325c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential savings on car insurance based on user input.
 * 
 * @param {number} currentPremium - The current insurance premium amount.
 * @param {number} deductible - The chosen deductible amount.
 * @param {string} drivingRecord - The user's driving record ('good', 'average', 'bad').
 * @param {boolean} safetyFeatures - Indicates if the car has safety features.
 * @returns {number} - The estimated potential savings.
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculatePotentialSavings(currentPremium, deductible, drivingRecord, safetyFeatures) {
    // Validate inputs
    if (typeof currentPremium !== 'number' || currentPremium <= 0) {
        throw new Error('Invalid currentPremium: must be a positive number.');
    }
    if (typeof deductible !== 'number' || deductible < 0) {
        throw new Error('Invalid deductible: must be a non-negative number.');
    }
    if (!['good', 'average', 'bad'].includes(drivingRecord)) {
        throw new Error('Invalid drivingRecord: must be "good", "average", or "bad".');
    }
    if (typeof safetyFeatures !== 'boolean') {
        throw new Error('Invalid safetyFeatures: must be a boolean value.');
    }

    // Initialize potential savings variable
    let savings = 0;

    // Calculate savings based on driving record
    switch (drivingRecord) {
        case 'good':
            savings += currentPremium * 0.20; // 20% discount for good record
            break;
        case 'average':
            savings += currentPremium * 0.10; // 10% discount for average record
            break;
        case 'bad':
            savings += currentPremium * 0.05; // 5% discount for bad record
            break;
    }

    // Additional savings for having safety features
    if (safetyFeatures) {
        savings += currentPremium * 0.15; // 15% discount for safety features
    }

    // Adjust savings based on deductible choice
    if (deductible > 1000) {
        savings *= 1.10; // Increase savings by 10% for higher deductible
    } else if (deductible < 500) {
        savings *= 0.90; // Decrease savings by 10% for lower deductible
    }

    // Ensure savings do not exceed the current premium
    return Math.min(savings, currentPremium);
}

// Example usage (uncomment to test)
// try {
//     const potentialSavings = calculatePotentialSavings(1200, 750, 'good', true);
//     console.log(`Potential savings on car insurance: $${potentialSavings.toFixed(2)}`);
// } catch (error) {
//     console.error(error.message);
// }
```
