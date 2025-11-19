"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passiveinvestincome.com
Prompt: Create a JavaScript function that calculates potential earnings based on the investment plans offered by PassiveInvestIncome, including different deposit amounts and durations.
Generated: DETERMINISTIC_52cddae91fd9455b
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential earnings based on investment plans.
 * @param {number} depositAmount - The amount to be invested.
 * @param {number} durationMonths - The duration of the investment in months.
 * @param {string} planType - The type of investment plan ('basic', 'premium', 'vip').
 * @returns {number} - The potential earnings from the investment.
 * @throws {Error} - Throws an error for invalid inputs.
 */
function calculatePotentialEarnings(depositAmount, durationMonths, planType) {
    // Validate inputs
    if (typeof depositAmount !== 'number' || depositAmount <= 0) {
        throw new Error('Invalid deposit amount. It must be a positive number.');
    }
    if (typeof durationMonths !== 'number' || durationMonths <= 0) {
        throw new Error('Invalid duration. It must be a positive integer representing months.');
    }
    if (typeof planType !== 'string' || !['basic', 'premium', 'vip'].includes(planType.toLowerCase())) {
        throw new Error('Invalid plan type. It must be one of: basic, premium, or vip.');
    }

    // Define interest rates based on plan types
    const interestRates = {
        basic: 0.05,   // 5% interest for basic plan
        premium: 0.07, // 7% interest for premium plan
        vip: 0.10      // 10% interest for VIP plan
    };

    // Calculate the total earnings
    const interestRate = interestRates[planType.toLowerCase()];
    const earnings = depositAmount * (1 + interestRate) ** durationMonths;

    return parseFloat(earnings.toFixed(2)); // Return earnings rounded to 2 decimal places
}

// Example usage
try {
    const deposit = 1000; // Amount to invest
    const duration = 12; // Duration in months
    const plan = 'premium'; // Chosen investment plan

    const potentialEarnings = calculatePotentialEarnings(deposit, duration, plan);
    console.log(`Potential earnings: $${potentialEarnings}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
