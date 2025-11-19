"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Write a JavaScript function to dynamically update the price of "Karma Çalışma Tezgahları" based on selected features like drawer count and material type.
Generated: DETERMINISTIC_51b4ad362999ee01
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Updates the price of "Karma Çalışma Tezgahları" based on selected features.
 * 
 * @param {number} basePrice - The base price of the product.
 * @param {number} drawerCount - The number of drawers selected.
 * @param {string} materialType - The type of material selected (e.g., 'wood', 'metal').
 * @returns {number} - The updated price after applying feature-based adjustments.
 * @throws {Error} - Throws an error if invalid parameters are provided.
 */
function updatePrice(basePrice, drawerCount, materialType) {
    // Validate input parameters
    if (typeof basePrice !== 'number' || basePrice < 0) {
        throw new Error('Invalid base price. It must be a non-negative number.');
    }
    if (typeof drawerCount !== 'number' || drawerCount < 0) {
        throw new Error('Invalid drawer count. It must be a non-negative number.');
    }
    if (typeof materialType !== 'string' || !['wood', 'metal'].includes(materialType)) {
        throw new Error('Invalid material type. It must be either "wood" or "metal".');
    }

    // Define price adjustments based on features
    const drawerPrice = 50; // Price per drawer
    const materialPriceFactor = {
        'wood': 1.2, // 20% increase for wood
        'metal': 1.0  // No increase for metal
    };

    // Calculate the total price
    const totalPrice = basePrice 
        + (drawerCount * drawerPrice) 
        * materialPriceFactor[materialType];

    return parseFloat(totalPrice.toFixed(2)); // Return price rounded to 2 decimal places
}

// Example usage
try {
    const basePrice = 200; // Base price of the product
    const drawerCount = 3; // Number of drawers selected
    const materialType = 'wood'; // Material type selected

    const updatedPrice = updatePrice(basePrice, drawerCount, materialType);
    console.log(`The updated price is: $${updatedPrice}`);
} catch (error) {
    console.error(error.message);
}
```
