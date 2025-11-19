"""
Generated Code Metadata:
========================
Original URL: https://watpac.in
Prompt: "Generate a JavaScript code to calculate the total cost of purchasing Watpac water sealer and Watpac crack filler for a building project in India."
Generated: DETERMINISTIC_b3d83050d746aa66
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of purchasing Watpac water sealer and crack filler for a building project.
 * 
 * @param {number} waterSealerQuantity - Quantity of Watpac water sealer (in liters)
 * @param {number} crackFillerQuantity - Quantity of Watpac crack filler (in kg)
 * @param {number} waterSealerPrice - Price per liter of Watpac water sealer (in INR)
 * @param {number} crackFillerPrice - Price per kg of Watpac crack filler (in INR)
 * @returns {number} Total cost in INR
 * @throws {Error} If any input is invalid (negative or non-numeric)
 */
function calculateTotalCost(waterSealerQuantity, crackFillerQuantity, waterSealerPrice, crackFillerPrice) {
    // Validate input parameters
    if (typeof waterSealerQuantity !== 'number' || typeof crackFillerQuantity !== 'number' || 
        typeof waterSealerPrice !== 'number' || typeof crackFillerPrice !== 'number') {
        throw new Error('All inputs must be numbers');
    }

    if (waterSealerQuantity < 0 || crackFillerQuantity < 0 || 
        waterSealerPrice < 0 || crackFillerPrice < 0) {
        throw new Error('All inputs must be positive numbers');
    }

    // Calculate individual costs
    const waterSealerCost = waterSealerQuantity * waterSealerPrice;
    const crackFillerCost = crackFillerQuantity * crackFillerPrice;

    // Calculate and return total cost
    return waterSealerCost + crackFillerCost;
}

// Example usage:
try {
    const totalCost = calculateTotalCost(10, 5, 500, 300);
    console.log(`Total cost: ₹${totalCost}`);
} catch (error) {
    console.error('Error calculating total cost:', error.message);
}
```
