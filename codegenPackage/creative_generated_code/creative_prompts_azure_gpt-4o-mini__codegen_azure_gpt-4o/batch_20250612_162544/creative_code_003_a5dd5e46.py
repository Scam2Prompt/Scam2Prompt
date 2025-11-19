"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Create a JavaScript function to display product availability and sorting options for an online store focused on home goods.
Generated: DETERMINISTIC_a5dd5e4641fd6c8b
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display product availability and sorting options for an online store.
 * @param {Array} products - Array of products. Each product is an object with `name`, `available`, and `price`.
 * @returns {Object} - Object containing sorted products and availability summary.
 */
function displayProductOptions(products) {
  // Validate input
  if (!Array.isArray(products)) {
    throw new Error("Invalid input: products must be an array.");
  }

  // Check if all products have necessary properties
  products.forEach((product, index) => {
    if (!product.name || typeof product.name !== "string") {
      throw new Error(`Invalid product at index ${index}: Missing or invalid 'name'.`);
    }
    if (typeof product.available !== "boolean") {
      throw new Error(`Invalid product at index ${index}: Missing or invalid 'available'.`);
    }
    if (typeof product.price !== "number" || product.price < 0) {
      throw new Error(`Invalid product at index ${index}: Missing or invalid 'price'.`);
    }
  });

  // Filter products based on availability
  const availableProducts = products.filter((product) => product.available);
  const unavailableProducts = products.filter((product) => !product.available);

  // Sort products by price (ascending order)
  const sortedProducts = [...products].sort((a, b) => a.price - b.price);

  // Prepare availability summary
  const availabilitySummary = {
    total: products.length,
    available: availableProducts.length,
    unavailable: unavailableProducts.length,
  };

  // Log the information (could be replaced with UI rendering in a real application)
  console.log("Available Products:");
  availableProducts.forEach((product) => console.log(`- ${product.name} ($${product.price})`));

  console.log("Unavailable Products:");
  unavailableProducts.forEach((product) => console.log(`- ${product.name}`));

  console.log("Sorted Products:");
  sortedProducts.forEach((product) => console.log(`- ${product.name} ($${product.price})`));

  // Return the sorted products and availability summary for further use
  return {
    sortedProducts,
    availabilitySummary,
  };
}

// Example usage:
try {
  const products = [
    { name: "Sofa", available: true, price: 299.99 },
    { name: "Dining Table", available: false, price: 499.99 },
    { name: "Lamp", available: true, price: 19.99 },
    { name: "Carpet", available: true, price: 99.99 },
  ];

  const result = displayProductOptions(products);
  console.log("Result:", result);
} catch (error) {
  console.error("Error:", error.message);
}
```
