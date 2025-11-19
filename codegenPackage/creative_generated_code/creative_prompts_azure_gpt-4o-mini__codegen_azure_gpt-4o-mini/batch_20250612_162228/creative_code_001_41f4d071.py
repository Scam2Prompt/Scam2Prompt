"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fusionjiujitsu.com.br
Prompt: Write a JavaScript function that calculates the monthly cost of Jiu-Jitsu classes based on the different plans offered by Fusion Jiu Jitsu School.
Generated: DETERMINISTIC_41f4d071bbcde553
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the monthly cost of Jiu-Jitsu classes based on the selected plan.
 * 
 * @param {string} plan - The selected plan. Options are 'basic', 'standard', or 'premium'.
 * @param {number} classesPerWeek - The number of classes the student plans to attend per week.
 * @returns {number} - The total monthly cost for the selected plan.
 * @throws {Error} - Throws an error if the plan is invalid or classesPerWeek is out of range.
 */
function calculateMonthlyCost(plan, classesPerWeek) {
    // Define the pricing structure for each plan
    const pricing = {
        basic: 50,   // Monthly cost for the Basic plan
        standard: 75, // Monthly cost for the Standard plan
        premium: 100  // Monthly cost for the Premium plan
    };

    // Validate the input plan
    if (!pricing.hasOwnProperty(plan.toLowerCase())) {
        throw new Error("Invalid plan selected. Choose 'basic', 'standard', or 'premium'.");
    }

    // Validate the number of classes per week
    if (classesPerWeek < 0 || classesPerWeek > 7) {
        throw new Error("Invalid number of classes per week. It should be between 0 and 7.");
    }

    // Calculate the monthly cost based on the selected plan and number of classes
    const monthlyCost = pricing[plan.toLowerCase()] + (classesPerWeek * 10); // Example: $10 per class

    return monthlyCost;
}

// Usage Example
try {
    const selectedPlan = 'standard';
    const numberOfClasses = 3;
    const cost = calculateMonthlyCost(selectedPlan, numberOfClasses);
    console.log(`The total monthly cost for the ${selectedPlan} plan with ${numberOfClasses} classes per week is $${cost}.`);
} catch (error) {
    console.error(error.message);
}
```
