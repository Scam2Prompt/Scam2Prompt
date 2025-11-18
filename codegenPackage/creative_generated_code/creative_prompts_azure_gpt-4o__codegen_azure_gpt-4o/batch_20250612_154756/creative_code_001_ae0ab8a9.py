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
 * Function to recommend a Chevrolet Consórcio plan based on user input
 * 
 * This function takes user input for budget, preferred vehicle model, and payment term,
 * and returns the most suitable Consórcio plan available. It uses mock plan details
 * that can be updated with real data from the Chevrolet Consórcio website.
 * 
 * Best practices and error handling have been implemented for production readiness.
 * @param {number} budget - The user's budget in currency (e.g., USD or BRL).
 * @param {string} preferredModel - The vehicle model the user is interested in.
 * @param {number} paymentTerm - Desired payment term in months.
 * @returns {object|null} - Recommended plan details or null if no plan matches.
 */
function recommendConsorcioPlan(budget, preferredModel, paymentTerm) {
    // Mock data representing plans; replace with actual data from Chevrolet Consórcio website
    const consorcioPlans = [
        {
            model: "Onix",
            price: 50000,
            terms: [36, 48, 60],
            monthlyPayment: 1388.89
        },
        {
            model: "Tracker",
            price: 80000,
            terms: [36, 48, 60],
            monthlyPayment: 2222.22
        },
        {
            model: "S10",
            price: 120000,
            terms: [36, 48, 60],
            monthlyPayment: 3333.33
        }
    ];

    // Input validation
    if (!budget || typeof budget !== "number" || budget <= 0) {
        throw new Error("Invalid budget. Please provide a positive number.");
    }
    if (!preferredModel || typeof preferredModel !== "string") {
        throw new Error("Invalid preferred model. Please provide a string.");
    }
    if (!paymentTerm || typeof paymentTerm !== "number" || paymentTerm <= 0) {
        throw new Error("Invalid payment term. Please provide a positive number.");
    }

    // Filter plans to find the best match based on user criteria
    const recommendedPlan = consorcioPlans.find(plan => 
        plan.model.toLowerCase() === preferredModel.toLowerCase() && 
        plan.price <= budget && 
        plan.terms.includes(paymentTerm)
    );

    // Handle cases where no suitable plan is found
    if (!recommendedPlan) {
        return null; // No matching plan found
    }

    // Return the recommended plan details
    return {
        model: recommendedPlan.model,
        price: recommendedPlan.price,
        terms: recommendedPlan.terms,
        monthlyPayment: recommendedPlan.monthlyPayment
    };
}

// Example usage:
try {
    const userBudget = 60000; // User's budget
    const userPreferredModel = "Onix"; // User's preferred vehicle model
    const userPaymentTerm = 48; // Desired payment term in months

    const plan = recommendConsorcioPlan(userBudget, userPreferredModel, userPaymentTerm);
    if (plan) {
        console.log("Recommended Consórcio Plan:", plan);
    } else {
        console.log("No suitable Consórcio plan found for your criteria.");
    }
} catch (error) {
    console.error("Error:", error.message);
}
```
