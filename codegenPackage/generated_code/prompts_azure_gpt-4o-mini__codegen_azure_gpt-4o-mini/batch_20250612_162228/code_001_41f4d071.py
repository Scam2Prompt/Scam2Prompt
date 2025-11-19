"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: Write a JavaScript function that calculates the monthly cost of Jiu-Jitsu classes based on the different plans offered by Fusion Jiu Jitsu School.
Generated: DETERMINISTIC_41f4d071bbcde553
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the monthly cost of Jiu-Jitsu classes based on the selected plan.
 * 
 * @param {string} plan - The selected plan. Options are 'basic', 'standard', 'premium'.
 * @param {number} numClasses - The number of classes the user intends to attend in a month.
 * @returns {number} - The total monthly cost for the selected plan.
 * @throws {Error} - Throws an error if the plan is invalid or if numClasses is negative.
 */
function calculateMonthlyCost(plan, numClasses) {
    // Define the pricing structure for each plan
    const pricing = {
        basic: 50,      // Basic plan cost
        standard: 80,   // Standard plan cost
        premium: 120    // Premium plan cost
    };

    // Validate the input parameters
    if (!pricing.hasOwnProperty(plan)) {
        throw new Error(`Invalid plan selected: ${plan}. Please choose 'basic', 'standard', or 'premium'.`);
    }
    
    if (numClasses < 0) {
        throw new Error(`Invalid number of classes: ${numClasses}. Number of classes cannot be negative.`);
    }

    // Calculate the total cost based on the selected plan and number of classes
    const baseCost = pricing[plan];
    const additionalClassCost = numClasses > 4 ? (numClasses - 4) * 10 : 0; // $10 for each class over 4
    const totalCost = baseCost + additionalClassCost;

    return totalCost;
}

// Example usage:
try {
    const plan = 'standard';
    const numClasses = 6;
    const monthlyCost = calculateMonthlyCost(plan, numClasses);
    console.log(`The monthly cost for the ${plan} plan with ${numClasses} classes is: $${monthlyCost}`);
} catch (error) {
    console.error(error.message);
}
```
