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
 * Pricing Plan:
 * - Basic Plan: $50 per square meter
 * - Premium Plan: $100 per square meter
 * - Luxury Plan: $200 per square meter
 * 
 * Additional Fees:
 * - Custom Furniture: +$500 per item
 * - Special Wall Treatments: +$300 per wall
 * 
 * @param {number} area - Area of the residential space in square meters.
 * @param {string} plan - Pricing plan ('basic', 'premium', 'luxury').
 * @param {number} customFurnitureCount - Number of custom furniture items required.
 * @param {number} specialWallTreatmentCount - Number of walls requiring special treatment.
 * @returns {number} - The total estimated cost of the project.
 * @throws Will throw an error if invalid input is provided.
 */
function calculateInteriorDesignCost(area, plan, customFurnitureCount, specialWallTreatmentCount) {
    // Validate input
    if (typeof area !== 'number' || area <= 0) {
        throw new Error("Invalid area. It must be a positive number.");
    }
    if (!['basic', 'premium', 'luxury'].includes(plan)) {
        throw new Error("Invalid plan. Choose 'basic', 'premium', or 'luxury'.");
    }
    if (typeof customFurnitureCount !== 'number' || customFurnitureCount < 0) {
        throw new Error("Invalid custom furniture count. It must be a non-negative number.");
    }
    if (typeof specialWallTreatmentCount !== 'number' || specialWallTreatmentCount < 0) {
        throw new Error("Invalid special wall treatment count. It must be a non-negative number.");
    }

    // Pricing details
    const pricingPlans = {
        basic: 50,
        premium: 100,
        luxury: 200
    };
    const customFurnitureFee = 500; // Fee per custom furniture item
    const wallTreatmentFee = 300; // Fee per wall for special treatment

    // Calculate base cost based on area and plan
    const baseCost = area * pricingPlans[plan];

    // Calculate additional costs
    const furnitureCost = customFurnitureCount * customFurnitureFee;
    const wallTreatmentCost = specialWallTreatmentCount * wallTreatmentFee;

    // Calculate total cost
    const totalCost = baseCost + furnitureCost + wallTreatmentCost;

    return totalCost;
}

// Example Usage
try {
    const area = 120; // Square meters
    const plan = 'premium'; // 'basic', 'premium', or 'luxury'
    const customFurnitureCount = 3; // Number of custom furniture items
    const specialWallTreatmentCount = 2; // Number of walls requiring special treatment

    const estimatedCost = calculateInteriorDesignCost(
        area,
        plan,
        customFurnitureCount,
        specialWallTreatmentCount
    );

    console.log(`The estimated cost of the project is $${estimatedCost}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
