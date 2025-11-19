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
 * Calculates the total cost of a membership plan for Batıkent Tofaş Spor Klübü.
 * 
 * @param {string} plan - The chosen membership plan ('basic', 'premium', 'vip').
 * @param {string} frequency - The billing frequency ('monthly', 'yearly').
 * @returns {number} - The total cost for the selected plan and frequency.
 * @throws {Error} - Throws an error if the plan or frequency is invalid.
 */
function calculateMembershipCost(plan, frequency) {
    // Define the cost structure for each plan
    const pricing = {
        basic: { monthly: 50, yearly: 500 },
        premium: { monthly: 80, yearly: 800 },
        vip: { monthly: 120, yearly: 1200 }
    };

    // Validate the input parameters
    if (!pricing[plan]) {
        throw new Error(`Invalid plan selected: ${plan}. Valid options are: ${Object.keys(pricing).join(', ')}`);
    }
    if (!pricing[plan][frequency]) {
        throw new Error(`Invalid frequency selected: ${frequency}. Valid options are: monthly, yearly`);
    }

    // Calculate the total cost based on the selected plan and frequency
    const totalCost = pricing[plan][frequency];

    return totalCost;
}

// Example usage:
try {
    const plan = 'premium'; // Example plan
    const frequency = 'yearly'; // Example frequency
    const totalCost = calculateMembershipCost(plan, frequency);
    console.log(`The total cost for the ${plan} plan on a ${frequency} basis is: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
