"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Create a JavaScript function to calculate the cost of printing services, such as business card printing, based on the quantity and type of material, like Detalj Reklam's pricing model."
Generated: DETERMINISTIC_bd2e5ca21aa9596c
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of printing services based on quantity and material type.
 * @param {number} quantity - The number of items to be printed.
 * @param {string} materialType - The type of material (e.g., "standard", "premium", "luxury").
 * @returns {number} - The total cost of printing services.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculatePrintingCost(quantity, materialType) {
  // Validate input
  if (!Number.isInteger(quantity) || quantity <= 0) {
    throw new Error("Invalid quantity. Quantity must be a positive integer.");
  }
  if (typeof materialType !== "string" || materialType.trim() === "") {
    throw new Error("Invalid material type. Material type must be a non-empty string.");
  }

  // Pricing model (example pricing based on Detalj Reklam's model)
  const pricing = {
    standard: 0.5, // $0.50 per item
    premium: 1.0,  // $1.00 per item
    luxury: 2.0    // $2.00 per item
  };

  // Check if the material type exists in the pricing model
  if (!pricing.hasOwnProperty(materialType.toLowerCase())) {
    throw new Error(`Invalid material type. Available options are: ${Object.keys(pricing).join(", ")}`);
  }

  // Calculate total cost
  const costPerItem = pricing[materialType.toLowerCase()];
  const totalCost = quantity * costPerItem;

  return totalCost;
}

// Example usage:
try {
  const quantity = 100; // Number of items
  const materialType = "premium"; // Material type
  const totalCost = calculatePrintingCost(quantity, materialType);
  console.log(`The total cost for printing ${quantity} items on ${materialType} material is $${totalCost.toFixed(2)}.`);
} catch (error) {
  console.error(error.message);
}
```
