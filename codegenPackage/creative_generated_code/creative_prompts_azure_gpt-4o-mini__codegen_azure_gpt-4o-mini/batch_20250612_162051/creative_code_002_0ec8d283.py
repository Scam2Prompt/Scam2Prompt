"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Create a JavaScript function that calculates the estimated cost of a residential interior design project using Nyiku Design's pricing plans.
Generated: DETERMINISTIC_0ec8d283d91fb771
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost of a residential interior design project
 * based on Nyiku Design's pricing plans.
 *
 * @param {number} squareFeet - The total square footage of the space to be designed.
 * @param {string} designLevel - The level of design service required. It can be 'basic', 'standard', or 'premium'.
 * @returns {number} - The estimated cost of the project.
 * @throws {Error} - Throws an error if the square footage is negative or if the design level is invalid.
 */
function calculateDesignCost(squareFeet, designLevel) {
    // Pricing plans per square foot
    const pricingPlans = {
        basic: 5,    // Basic plan cost per square foot
        standard: 10, // Standard plan cost per square foot
        premium: 15   // Premium plan cost per square foot
    };

    // Validate input parameters
    if (squareFeet < 0) {
        throw new Error("Square footage cannot be negative.");
    }
    if (!pricingPlans.hasOwnProperty(designLevel)) {
        throw new Error("Invalid design level. Options are 'basic', 'standard', or 'premium'.");
    }

    // Calculate the estimated cost
    const costPerSquareFoot = pricingPlans[designLevel];
    const estimatedCost = squareFeet * costPerSquareFoot;

    return estimatedCost;
}

// Example usage
try {
    const totalCost = calculateDesignCost(1500, 'standard');
    console.log(`The estimated cost of the project is $${totalCost}.`);
} catch (error) {
    console.error(`Error calculating design cost: ${error.message}`);
}
```
