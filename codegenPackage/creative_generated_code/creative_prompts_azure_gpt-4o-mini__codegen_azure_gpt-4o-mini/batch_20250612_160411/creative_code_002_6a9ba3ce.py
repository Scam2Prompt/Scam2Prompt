"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Create a function in JavaScript that calculates potential ROI for different investment plans (Basic, Silver, Gold) offered by Welstrade.
Generated: DETERMINISTIC_6a9ba3ce337d93bf
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential Return on Investment (ROI) based on the investment plan chosen.
 * 
 * Investment Plans:
 * - Basic: 5% annual return
 * - Silver: 10% annual return
 * - Gold: 15% annual return
 * 
 * @param {number} principal - The initial amount of money invested.
 * @param {number} years - The number of years the money is invested for.
 * @param {string} plan - The investment plan ('Basic', 'Silver', or 'Gold').
 * @returns {number} - The total amount after the investment period.
 * @throws {Error} - Throws an error if the principal is less than or equal to 0,
 *                   years is less than or equal to 0, or an invalid plan is provided.
 */
function calculateROI(principal, years, plan) {
    // Validate inputs
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal must be a positive number.');
    }
    if (typeof years !== 'number' || years <= 0) {
        throw new Error('Years must be a positive number.');
    }
    if (typeof plan !== 'string' || !['Basic', 'Silver', 'Gold'].includes(plan)) {
        throw new Error('Invalid plan. Must be "Basic", "Silver", or "Gold".');
    }

    // Define the annual return rates for each plan
    const rates = {
        Basic: 0.05,
        Silver: 0.10,
        Gold: 0.15
    };

    // Calculate total amount after the investment period
    const rate = rates[plan];
    const totalAmount = principal * Math.pow((1 + rate), years);
    
    return totalAmount;
}

// Example usage:
try {
    const initialInvestment = 1000; // Initial investment amount
    const investmentYears = 5;       // Investment duration in years
    const selectedPlan = 'Gold';      // Selected investment plan

    const totalReturn = calculateROI(initialInvestment, investmentYears, selectedPlan);
    console.log(`Total amount after ${investmentYears} years in the ${selectedPlan} plan: $${totalReturn.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
