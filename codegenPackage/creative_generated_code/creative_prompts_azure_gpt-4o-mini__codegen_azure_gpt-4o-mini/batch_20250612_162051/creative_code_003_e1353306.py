"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Develop a JavaScript function that calculates the cost of various home services like cleaning and insulation, based on the pricing model mentioned by شركة انجاز.
Generated: DETERMINISTIC_e13533062f03d97b
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
 * Calculates the total cost of home services based on the service type and quantity.
 * 
 * @param {string} serviceType - The type of service ('cleaning' or 'insulation').
 * @param {number} quantity - The quantity of the service required (e.g., hours for cleaning, square meters for insulation).
 * @returns {number} - The total cost of the services.
 * @throws {Error} - Throws an error if the service type is invalid or the quantity is negative.
 */
function calculateServiceCost(serviceType, quantity) {
    // Define pricing models for each service type
    const pricingModel = {
        cleaning: 25.00, // cost per hour for cleaning
        insulation: 15.00 // cost per square meter for insulation
    };

    // Validate the service type
    if (!pricingModel.hasOwnProperty(serviceType)) {
        throw new Error(`Invalid service type: ${serviceType}. Valid options are: ${Object.keys(pricingModel).join(', ')}`);
    }

    // Validate the quantity
    if (typeof quantity !== 'number' || quantity < 0) {
        throw new Error(`Invalid quantity: ${quantity}. Quantity must be a non-negative number.`);
    }

    // Calculate the total cost
    const cost = pricingModel[serviceType] * quantity;

    return parseFloat(cost.toFixed(2)); // Return cost rounded to two decimal places
}

// Example usage
try {
    const totalCleaningCost = calculateServiceCost('cleaning', 5); // 5 hours of cleaning
    console.log(`Total cleaning cost: $${totalCleaningCost}`);

    const totalInsulationCost = calculateServiceCost('insulation', 100); // 100 square meters of insulation
    console.log(`Total insulation cost: $${totalInsulationCost}`);
} catch (error) {
    console.error(error.message); // Handle any errors that might occur
}
```
