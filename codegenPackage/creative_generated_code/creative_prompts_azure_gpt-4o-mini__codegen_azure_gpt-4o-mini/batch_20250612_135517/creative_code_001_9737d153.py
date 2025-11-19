"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livinglargfx.com
Prompt: Write a JavaScript function that calculates potential earnings based on the Bronze and Gold pricing plans offered by livinglargfx, given a specific investment amount.
Generated: DETERMINISTIC_9737d153e1bd9519
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential earnings based on the investment amount and pricing plans.
 * @param {number} investment - The amount of money to invest.
 * @param {string} plan - The pricing plan ("Bronze" or "Gold").
 * @returns {number} - The potential earnings based on the selected plan.
 * @throws {Error} - Throws an error if the investment is not a positive number or if an invalid plan is provided.
 */
function calculatePotentialEarnings(investment, plan) {
    // Validate the investment amount
    if (typeof investment !== 'number' || investment <= 0) {
        throw new Error('Investment must be a positive number.');
    }

    // Define earnings multipliers for the pricing plans
    const pricingPlans = {
        Bronze: 1.2, // 20% return
        Gold: 1.5 // 50% return
    };

    // Validate the pricing plan
    if (!pricingPlans.hasOwnProperty(plan)) {
        throw new Error('Invalid plan. Please choose "Bronze" or "Gold".');
    }

    // Calculate potential earnings
    const earningsMultiplier = pricingPlans[plan];
    const potentialEarnings = investment * earningsMultiplier;

    return potentialEarnings;
}

// Example Usage
try {
    const investmentAmount = 1000; // Example investment amount
    const chosenPlan = 'Gold'; // Example chosen plan
    const earnings = calculatePotentialEarnings(investmentAmount, chosenPlan);
    console.log(`Potential earnings for ${chosenPlan} plan: $${earnings.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
