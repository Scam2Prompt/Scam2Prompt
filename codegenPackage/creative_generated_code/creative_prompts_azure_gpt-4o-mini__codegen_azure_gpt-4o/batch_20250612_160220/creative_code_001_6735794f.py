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
 * Calculates potential returns for an investment plan.
 * 
 * SEAFIRST-MINERS offers the following packages:
 * Starter: 5% return
 * Moderate: 10% return
 * Gold: 15% return
 * VIP: 20% return
 * 
 * @param {string} plan - The investment plan (Starter, Moderate, Gold, VIP).
 * @param {number} amount - The investment amount.
 * @returns {number} - The potential return on investment.
 * @throws {Error} - Throws error if invalid plan or amount is provided.
 */
function calculatePotentialReturns(plan, amount) {
    // Validate input
    if (typeof plan !== 'string' || typeof amount !== 'number' || amount <= 0) {
        throw new Error('Invalid input: Plan must be a string and amount must be a positive number.');
    }

    // Define the percentage returns for each plan
    const plans = {
        Starter: 0.05,   // 5% return
        Moderate: 0.10,  // 10% return
        Gold: 0.15,      // 15% return
        VIP: 0.20        // 20% return
    };

    // Check if the plan exists
    if (!plans[plan]) {
        throw new Error(`Invalid plan: '${plan}' is not a recognized investment plan.`);
    }

    // Calculate and return the potential return
    const percentageReturn = plans[plan];
    return amount * percentageReturn;
}

// Example usage:
try {
    const plan = 'Gold';
    const investmentAmount = 1000;
    const returns = calculatePotentialReturns(plan, investmentAmount);
    console.log(`Potential returns for the ${plan} plan: $${returns.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
