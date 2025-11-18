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
 * Function to dynamically calculate and update the price of "Karma Çalışma Tezgahları"
 * based on selected features such as drawer count and material type.
 * 
 * @param {number} basePrice - The base price of the product.
 * @param {number} drawerCount - The number of drawers selected.
 * @param {string} materialType - The type of material selected (e.g., "wood", "metal", "glass").
 * @returns {number} - The updated price based on selected features.
 */
function calculateUpdatedPrice(basePrice, drawerCount, materialType) {
  // Validate inputs
  if (typeof basePrice !== "number" || basePrice < 0) {
    throw new Error("Invalid base price. Base price must be a non-negative number.");
  }
  if (typeof drawerCount !== "number" || drawerCount < 0) {
    throw new Error("Invalid drawer count. Drawer count must be a non-negative number.");
  }
  if (typeof materialType !== "string" || !materialType.trim()) {
    throw new Error("Invalid material type. Material type must be a non-empty string.");
  }

  // Additional costs based on drawer count
  const drawerCostPerUnit = 75; // Price per drawer
  const drawerCost = drawerCount * drawerCostPerUnit;

  // Additional costs based on material type
  const materialCostMap = {
    wood: 200,
    metal: 300,
    glass: 400
  };
  const materialCost = materialCostMap[materialType.toLowerCase()] || 0;

  // Check if material type is valid
  if (materialCost === 0) {
    throw new Error("Invalid material type selected. Valid types are: wood, metal, glass.");
  }

  // Calculate the final price
  const finalPrice = basePrice + drawerCost + materialCost;

  // Return the calculated price
  return finalPrice;
}

// Example usage
try {
  const basePrice = 1000; // Base price of the item
  const drawerCount = 4; // Number of drawers selected
  const materialType = "wood"; // Selected material type

  const updatedPrice = calculateUpdatedPrice(basePrice, drawerCount, materialType);
  console.log(`Updated Price: ${updatedPrice}`);
} catch (error) {
  console.error(error.message);
}
```
