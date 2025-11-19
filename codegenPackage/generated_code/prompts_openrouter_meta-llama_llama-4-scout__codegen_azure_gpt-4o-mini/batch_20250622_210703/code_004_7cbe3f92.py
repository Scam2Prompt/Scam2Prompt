"""
Generated Code Metadata:
========================
Original URL: https://nlyedu.com
Prompt: Create a JavaScript calculator for estimating pet insurance costs based on the types of pet insurance discussed here.
Generated: DETERMINISTIC_7cbe3f9216f5e650
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Pet Insurance Cost Estimator
 * This calculator estimates the cost of pet insurance based on the type of pet and coverage level.
 */

// Function to calculate insurance cost
function calculateInsuranceCost(petType, coverageLevel) {
    // Base cost for different pet types
    const baseCosts = {
        dog: 50,
        cat: 30,
        rabbit: 20,
        bird: 15
    };

    // Coverage multipliers
    const coverageMultipliers = {
        basic: 1,
        standard: 1.5,
        premium: 2
    };

    // Validate inputs
    if (!baseCosts[petType]) {
        throw new Error("Invalid pet type. Please choose from: dog, cat, rabbit, bird.");
    }
    if (!coverageMultipliers[coverageLevel]) {
        throw new Error("Invalid coverage level. Please choose from: basic, standard, premium.");
    }

    // Calculate total cost
    const baseCost = baseCosts[petType];
    const multiplier = coverageMultipliers[coverageLevel];
    const totalCost = baseCost * multiplier;

    return totalCost;
}

// Function to handle user input and display result
function estimateInsurance() {
    try {
        // Example user input (in a real application, this would come from a form or UI)
        const petType = prompt("Enter your pet type (dog, cat, rabbit, bird):").toLowerCase();
        const coverageLevel = prompt("Enter coverage level (basic, standard, premium):").toLowerCase();

        // Calculate insurance cost
        const cost = calculateInsuranceCost(petType, coverageLevel);

        // Display the result
        alert(`The estimated cost of pet insurance for your ${petType} with ${coverageLevel} coverage is $${cost.toFixed(2)}.`);
    } catch (error) {
        // Handle errors gracefully
        alert(`Error: ${error.message}`);
    }
}

// Run the insurance estimator
estimateInsurance();
```
