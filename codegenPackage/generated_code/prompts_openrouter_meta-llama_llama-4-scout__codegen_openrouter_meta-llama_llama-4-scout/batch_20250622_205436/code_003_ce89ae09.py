"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Create a JavaScript function to calculate the cost of a custom window order, taking into account factors like material (aluminium, PVC, or bois), size, and type (e.g., fenêtre aluminium, porte de garage)."
Generated: DETERMINISTIC_ce89ae09660292eb
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of a custom window order.
 * 
 * @param {string} material - The material of the window (aluminium, PVC, or bois).
 * @param {number} width - The width of the window in meters.
 * @param {number} height - The height of the window in meters.
 * @param {string} type - The type of the window (e.g., fenêtre aluminium, porte de garage).
 * @returns {number} The total cost of the window.
 */
function calculateWindowCost(material, width, height, type) {
    // Define material prices per square meter
    const materialPrices = {
        aluminium: 150,
        PVC: 120,
        bois: 200
    };

    // Define type prices (base prices for standard sizes)
    const typePrices = {
        'fenêtre aluminium': 500,
        'porte de garage': 800
    };

    // Check if material is valid
    if (!(material in materialPrices)) {
        throw new Error(`Invalid material: ${material}. Supported materials: ${Object.keys(materialPrices).join(', ')}`);
    }

    // Check if type is valid
    if (!(type in typePrices)) {
        throw new Error(`Invalid type: ${type}. Supported types: ${Object.keys(typePrices).join(', ')}`);
    }

    // Calculate area
    const area = width * height;

    // Calculate material cost
    const materialCost = area * materialPrices[material];

    // Calculate type cost (base price + area-based price)
    const typeCost = typePrices[type] + (area * 50); // 50€/m² additional cost for type

    // Calculate total cost
    const totalCost = materialCost + typeCost;

    return totalCost;
}

// Example usage:
try {
    const cost = calculateWindowCost('aluminium', 1.5, 2, 'fenêtre aluminium');
    console.log(`The total cost is: ${cost}€`);
} catch (error) {
    console.error(error.message);
}
```
