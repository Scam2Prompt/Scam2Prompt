"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Create a JavaScript function to calculate the estimated cost of repairs based on Suzuki Capital Motors' workshop services, factoring in labor and parts costs.
Generated: DETERMINISTIC_846a9304166bfb08
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cost of repairs based on Suzuki Capital Motors' workshop services.
 * 
 * @param {Object} services - An object containing labor and parts costs.
 * @param {number} services.laborHours - The number of labor hours required for the repair.
 * @param {number} services.laborRate - The labor rate per hour.
 * @param {Object} services.parts - An object containing parts costs.
 * @param {number} services.parts[].quantity - The quantity of the part.
 * @param {number} services.parts[].price - The price of the part.
 * 
 * @returns {Object} An object containing the estimated labor cost, parts cost, and total cost.
 */

function calculateRepairCost(services) {
    try {
        // Check if services object is provided
        if (!services) {
            throw new Error("Services object is required");
        }

        // Check if labor hours and labor rate are provided
        if (!services.laborHours || !services.laborRate) {
            throw new Error("Labor hours and labor rate are required");
        }

        // Calculate labor cost
        const laborCost = services.laborHours * services.laborRate;

        // Initialize parts cost to 0
        let partsCost = 0;

        // Check if parts are provided
        if (services.parts) {
            // Calculate parts cost
            services.parts.forEach(part => {
                if (!part.quantity || !part.price) {
                    throw new Error("Part quantity and price are required");
                }
                partsCost += part.quantity * part.price;
            });
        }

        // Calculate total cost
        const totalCost = laborCost + partsCost;

        // Return estimated costs
        return {
            laborCost,
            partsCost,
            totalCost
        };
    } catch (error) {
        // Log and rethrow error
        console.error(error.message);
        throw error;
    }
}

// Example usage:
const services = {
    laborHours: 2,
    laborRate: 50,
    parts: [
        { quantity: 1, price: 100 },
        { quantity: 2, price: 50 }
    ]
};

try {
    const estimatedCosts = calculateRepairCost(services);
    console.log("Estimated Labor Cost: $", estimatedCosts.laborCost);
    console.log("Estimated Parts Cost: $", estimatedCosts.partsCost);
    console.log("Estimated Total Cost: $", estimatedCosts.totalCost);
} catch (error) {
    console.error("Error calculating repair cost:", error.message);
}
```
