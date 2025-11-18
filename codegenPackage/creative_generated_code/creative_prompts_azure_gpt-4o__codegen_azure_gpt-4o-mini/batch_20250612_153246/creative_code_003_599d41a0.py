"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mywanderloop.com
Prompt: Create a function in JavaScript to implement promotional bonuses for online casinos, using examples from the innovations described on myWanderLoop.
Generated: DETERMINISTIC_599d41a07e0699e4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate promotional bonuses for online casinos.
 * 
 * @param {number} baseAmount - The base amount to calculate the bonus on.
 * @param {string} bonusType - The type of bonus ('welcome', 'reload', 'loyalty').
 * @returns {number} - The total amount including the promotional bonus.
 * @throws {Error} - Throws an error if an invalid bonus type is provided.
 */
function calculatePromotionalBonus(baseAmount, bonusType) {
    // Validate input
    if (typeof baseAmount !== 'number' || baseAmount <= 0) {
        throw new Error('Base amount must be a positive number.');
    }

    const bonusRates = {
        welcome: 0.100, // 10% bonus for welcome
        reload: 0.050,   // 5% bonus for reload
        loyalty: 0.025   // 2.5% bonus for loyalty
    };

    // Check if the provided bonus type is valid
    if (!(bonusType in bonusRates)) {
        throw new Error('Invalid bonus type. Valid types are: welcome, reload, loyalty.');
    }

    // Calculate the bonus based on the bonus type
    const bonus = baseAmount * bonusRates[bonusType];

    // Return the total amount including the promotional bonus
    return baseAmount + bonus;
}

// Example Usage
try {
    const baseAmount = 100; // Example base amount
    const bonusType = 'welcome'; // Choose the type of bonus
    const totalAmount = calculatePromotionalBonus(baseAmount, bonusType);
    console.log(`Total amount after applying ${bonusType} bonus: $${totalAmount.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
