"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: Create a JavaScript function that calculates potential savings on car insurance based on user input, inspired by the money-saving tips on recuperacionjc.com.
Generated: DETERMINISTIC_d4bb337d5946325c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential savings on car insurance based on user input.
 * 
 * @param {number} currentPremium - The current car insurance premium amount.
 * @param {number} newPremium - The proposed new car insurance premium amount.
 * @param {number} deductibleDifference - The difference in deductibles between current and new policies.
 * @returns {object} An object containing potential savings and a message.
 * @throws {Error} Throws an error if inputs are not valid numbers.
 */
function calculateInsuranceSavings(currentPremium, newPremium, deductibleDifference) {
    // Validate input types
    if (typeof currentPremium !== 'number' || typeof newPremium !== 'number' || typeof deductibleDifference !== 'number') {
        throw new Error('All inputs must be valid numbers.');
    }

    // Validate input values
    if (currentPremium < 0 || newPremium < 0 || deductibleDifference < 0) {
        throw new Error('Premiums and deductible differences must be non-negative.');
    }

    // Calculate potential savings
    const savings = currentPremium - newPremium - deductibleDifference;

    // Prepare the result message
    let message;
    if (savings > 0) {
        message = `You could save $${savings.toFixed(2)} on your car insurance!`;
    } else if (savings < 0) {
        message = `Your new premium is higher by $${Math.abs(savings).toFixed(2)}.`;
    } else {
        message = 'Your new premium is the same as your current premium.';
    }

    // Return the result as an object
    return {
        savings: savings,
        message: message
    };
}

// Example usage:
try {
    const result = calculateInsuranceSavings(1200, 1000, 200);
    console.log(result.message); // Output the savings message
} catch (error) {
    console.error('Error calculating savings:', error.message);
}
```
