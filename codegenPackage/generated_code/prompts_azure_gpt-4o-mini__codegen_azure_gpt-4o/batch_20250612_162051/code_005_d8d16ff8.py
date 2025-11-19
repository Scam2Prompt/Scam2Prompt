"""
Generated Code Metadata:
========================
Original URL: https://vaperiyadh2.com
Prompt: Write a JavaScript function to filter and display only the disposable vape products from the Vape Riyadh 2 inventory.
Generated: DETERMINISTIC_d8d16ff8377e2d2e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and displays disposable vape products from the Vape Riyadh 2 inventory.
 * 
 * @param {Array} inventory - Array of vape product objects.
 * Each product object should have the following structure:
 * {
 *   id: Number,
 *   name: String,
 *   type: String, // e.g., "disposable", "rechargeable", etc.
 *   price: Number
 * }
 * 
 * @returns {Array} - Array of disposable vape products.
 */
function filterDisposableVapes(inventory) {
  // Validate input
  if (!Array.isArray(inventory)) {
    throw new Error("Invalid inventory data. Expected an array of products.");
  }

  // Filter disposable vape products
  const disposableVapes = inventory.filter(product => {
    // Ensure product has the required structure and type is "disposable"
    return product && product.type === "disposable";
  });

  // Log disposable vapes to the console
  console.log("Disposable Vape Products:", disposableVapes);

  // Return the filtered array
  return disposableVapes;
}

// Example usage:
// Sample inventory data
const vapeInventory = [
  { id: 1, name: "Vape A", type: "disposable", price: 25 },
  { id: 2, name: "Vape B", type: "rechargeable", price: 40 },
  { id: 3, name: "Vape C", type: "disposable", price: 30 },
  { id: 4, name: "Vape D", type: "pod system", price: 50 }
];

// Call the function with the sample inventory
try {
  const disposableVapes = filterDisposableVapes(vapeInventory);
  // Further processing or display logic can be added here
} catch (error) {
  console.error("Error filtering disposable vapes:", error.message);
}
```
