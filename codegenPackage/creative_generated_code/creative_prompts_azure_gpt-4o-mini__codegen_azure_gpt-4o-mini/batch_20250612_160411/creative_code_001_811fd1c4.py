"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenixglobaltrade.com
Prompt: Write a JavaScript function that calculates the potential ROI for different investment plans offered by ZenixGlobaltrade, including the Starter, Classic, Professional, and Premium plans.
Generated: DETERMINISTIC_811fd1c4cc55eb58
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
 * Calculates the potential Return on Investment (ROI) for different investment plans.
 * 
 * Investment Plans:
 * - Starter: 5% monthly return
 * - Classic: 10% monthly return
 * - Professional: 15% monthly return
 * - Premium: 20% monthly return
 * 
 * @param {string} plan - The investment plan name (Starter, Classic, Professional, Premium)
 * @param {number} principal - The initial amount of investment
 * @param {number} months - The duration of investment in months
 * @returns {number} - The total amount after the specified duration, or an error message if inputs are invalid
 */
function calculateROI(plan, principal, months) {
    // Validate input types
    if (typeof plan !== 'string' || typeof principal !== 'number' || typeof months !== 'number') {
        throw new Error('Invalid input types. Plan must be a string, principal and months must be numbers.');
    }
    
    // Validate input values
    if (principal <= 0 || months <= 0) {
        throw new Error('Principal and months must be greater than zero.');
    }

    // Define monthly return rates for each plan
    const rates = {
        Starter: 0.05,
        Classic: 0.10,
        Professional: 0.15,
        Premium: 0.20
    };

    // Get the monthly return rate based on the chosen plan
    const rate = rates[plan];
    
    // Validate the chosen plan
    if (rate === undefined) {
        throw new Error('Invalid investment plan. Please choose from Starter, Classic, Professional, or Premium.');
    }

    // Calculate total amount after the specified duration
    const totalAmount = principal * Math.pow((1 + rate), months);
    
    return totalAmount;
}

// Example usage (uncomment to run):
// try {
//     const result = calculateROI('Classic', 1000, 12);
//     console.log(`Total amount after 12 months: $${result.toFixed(2)}`);
// } catch (error) {
//     console.error(error.message);
// }
```
