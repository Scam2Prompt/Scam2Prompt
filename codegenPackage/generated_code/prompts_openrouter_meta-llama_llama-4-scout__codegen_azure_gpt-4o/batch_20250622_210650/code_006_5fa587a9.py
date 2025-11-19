"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Write a JavaScript function to calculate the total cost of a membership plan for Batıkent Tofaş Spor Klübü based on the chosen plan and billing frequency.
Generated: DETERMINISTIC_5fa587a938fdb204
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculate the total cost of a membership plan for Batıkent Tofaş Spor Klübü.
 * 
 * @param {string} plan - The membership plan chosen. Options: "basic", "standard", "premium".
 * @param {string} frequency - The billing frequency. Options: "monthly", "quarterly", "yearly".
 * @returns {number} - The total cost of the membership plan.
 * @throws {Error} - Throws an error if the plan or frequency is invalid.
 */
function calculateMembershipCost(plan, frequency) {
    // Define the base prices for each plan
    const planPrices = {
        basic: 50,      // $50 per month
        standard: 100,  // $100 per month
        premium: 150    // $150 per month
    };

    // Define the discount multipliers for each billing frequency
    const frequencyMultipliers = {
        monthly: 1,          // No discount
        quarterly: 3 * 0.95, // 5% discount for quarterly billing
        yearly: 12 * 0.90    // 10% discount for yearly billing
    };

    // Validate the plan
    if (!planPrices.hasOwnProperty(plan)) {
        throw new Error(`Invalid plan: ${plan}. Valid options are "basic", "standard", "premium".`);
    }

    // Validate the frequency
    if (!frequencyMultipliers.hasOwnProperty(frequency)) {
        throw new Error(`Invalid frequency: ${frequency}. Valid options are "monthly", "quarterly", "yearly".`);
    }

    // Calculate the total cost
    const basePrice = planPrices[plan];
    const multiplier = frequencyMultipliers[frequency];
    const totalCost = basePrice * multiplier;

    // Return the total cost rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
    const plan = "premium";
    const frequency = "yearly";
    const cost = calculateMembershipCost(plan, frequency);
    console.log(`The total cost for the ${plan} plan with ${frequency} billing is $${cost}.`);
} catch (error) {
    console.error(error.message);
}
```
