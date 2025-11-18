"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Generate a function in JavaScript that recommends a Chevrolet Consórcio plan based on user input for budget, preferred vehicle model, and payment term, referencing the plan details from the Consórcio Chevrolet website.
Generated: DETERMINISTIC_ae0ab8a9bbd7ed31
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to recommend a Chevrolet Consórcio plan based on user input.
 *
 * @param {number} budget - The user's budget for the Consórcio plan.
 * @param {string} vehicleModel - The preferred Chevrolet vehicle model.
 * @param {number} paymentTerm - The desired payment term in months.
 * @returns {string} A recommendation message based on the input.
 */
function recommendConsorcioPlan(budget, vehicleModel, paymentTerm) {
    // Validate input parameters
    if (typeof budget !== 'number' || budget <= 0) {
        throw new Error("Invalid budget: Budget must be a positive number.");
    }
    if (typeof vehicleModel !== 'string' || vehicleModel.trim() === '') {
        throw new Error("Invalid vehicle model: Vehicle model must be a non-empty string.");
    }
    if (typeof paymentTerm !== 'number' || paymentTerm <= 0) {
        throw new Error("Invalid payment term: Payment term must be a positive number.");
    }

    // Sample Consórcio plan data (in a real scenario, this data would be fetched from the Chevrolet website)
    const consorcioPlans = [
        { model: 'Onix', minBudget: 20000, maxBudget: 30000, term: 60 },
        { model: 'Tracker', minBudget: 30000, maxBudget: 45000, term: 72 },
        { model: 'S10', minBudget: 45000, maxBudget: 60000, term: 84 },
    ];

    // Find a matching plan based on user input
    const matchingPlan = consorcioPlans.find(plan =>
        plan.model.toLowerCase() === vehicleModel.toLowerCase() &&
        budget >= plan.minBudget && budget <= plan.maxBudget &&
        paymentTerm <= plan.term
    );

    // Return recommendation or a message if no plan is found
    if (matchingPlan) {
        return `We recommend the Chevrolet Consórcio plan for the ${matchingPlan.model}. Your budget fits within the plan, and the payment term is acceptable.`;
    } else {
        return `Unfortunately, we couldn't find a suitable Chevrolet Consórcio plan for the ${vehicleModel} within your budget of ${budget} and payment term of ${paymentTerm} months.`;
    }
}

// Example usage
try {
    const recommendation = recommendConsorcioPlan(25000, 'Onix', 60);
    console.log(recommendation);
} catch (error) {
    console.error("Error:", error.message);
}
```
