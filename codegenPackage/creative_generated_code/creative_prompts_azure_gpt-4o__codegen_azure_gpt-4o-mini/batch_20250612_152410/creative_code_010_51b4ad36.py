"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Write a JavaScript function to dynamically update the price of "Karma Çalışma Tezgahları" based on selected features like drawer count and material type.
Generated: DETERMINISTIC_51b4ad362999ee01
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Updates the price of "Karma Çalışma Tezgahları" based on selected features
 * such as drawer count and material type.
 * 
 * @param {number} drawerCount - The number of drawers selected.
 * @param {string} materialType - The type of material selected (e.g., "wood", "metal").
 * @returns {number} The updated price of the workbench.
 */
function updateWorkbenchPrice(drawerCount, materialType) {
    // Base price of the workbench
    const basePrice = 200; // in dollars

    // Price adjustments based on the material type
    const materialPrices = {
        wood: 50,  // additional cost for wood material
        metal: 100, // additional cost for metal material
        plastic: 0 // no additional cost for plastic material
    };

    // Validate the material type
    if (!materialPrices.hasOwnProperty(materialType)) {
        throw new Error(`Invalid material type: ${materialType}. Valid types are: ${Object.keys(materialPrices).join(", ")}`);
    }

    // Calculate the additional cost based on the selected features
    const materialCost = materialPrices[materialType];
    const drawerCost = drawerCount * 20; // each drawer adds $20

    // Calculate the total price
    const totalPrice = basePrice + materialCost + drawerCost;

    // Ensure the total price is not negative
    if (totalPrice < 0) {
        throw new Error("Calculated price is negative. Please check the input values.");
    }

    // Return the updated price
    return totalPrice;
}

// Example usage:
try {
    const price = updateWorkbenchPrice(3, 'wood');
    console.log(`The updated price is: $${price}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
