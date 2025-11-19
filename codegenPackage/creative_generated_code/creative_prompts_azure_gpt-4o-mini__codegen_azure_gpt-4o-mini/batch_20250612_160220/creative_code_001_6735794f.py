"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seafirst-miners.com
Prompt: Write a JavaScript function that calculates potential returns based on the investment plans offered by SEAFIRST-MINERS, including the Starter, Moderate, Gold, and VIP packages.
Generated: DETERMINISTIC_6735794fa531c457
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential returns based on the investment plan.
 * 
 * @param {string} plan - The investment plan (Starter, Moderate, Gold, VIP).
 * @param {number} investmentAmount - The amount invested.
 * @returns {number} - The potential returns based on the investment plan.
 * @throws {Error} - Throws an error if the plan is invalid or if the investment amount is non-positive.
 */
function calculatePotentialReturns(plan, investmentAmount) {
    // Validate the investment amount
    if (typeof investmentAmount !== 'number' || investmentAmount <= 0) {
        throw new Error('Investment amount must be a positive number.');
    }

    // Define potential return rates for each investment plan
    const returnRates = {
        Starter: 0.05,   // 5% return
        Moderate: 0.1,    // 10% return
        Gold: 0.15,       // 15% return
        VIP: 0.2          // 20% return
    };

    // Check if the provided plan is valid
    if (!returnRates.hasOwnProperty(plan)) {
        throw new Error('Invalid investment plan. Please choose from Starter, Moderate, Gold, or VIP.');
    }

    // Calculate potential returns based on the selected plan
    const potentialReturns = investmentAmount * returnRates[plan];

    return potentialReturns; // Return the calculated potential returns
}

// Example usage:
try {
    const plan = 'Gold';
    const investment = 1000; // Investment amount in currency units
    const returns = calculatePotentialReturns(plan, investment);
    console.log(`Potential returns for the ${plan} plan with an investment of ${investment} is: ${returns}`);
} catch (error) {
    console.error('Error calculating potential returns:', error.message);
}
```
