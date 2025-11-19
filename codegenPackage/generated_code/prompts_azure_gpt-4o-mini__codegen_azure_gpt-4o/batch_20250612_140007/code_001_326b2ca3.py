"""
Generated Code Metadata:
========================
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Write a JavaScript function that calculates the total cost of a christening outfit order, including free shipping for orders over $150.
Generated: DETERMINISTIC_326b2ca3f66f8366
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the total cost of a christening outfit order.
 * Includes free shipping for orders over $150.
 * 
 * @param {Array} items - Array of objects representing items in the order. Each object should have `price` and `quantity` properties.
 * @param {number} shippingCost - Flat shipping cost for orders under $150.
 * @returns {number} - The total cost of the order, including shipping if applicable.
 */
function calculateTotalCost(items, shippingCost) {
  // Validate input
  if (!Array.isArray(items)) {
    throw new Error("Invalid input: 'items' must be an array.");
  }
  if (typeof shippingCost !== 'number' || shippingCost < 0) {
    throw new Error("Invalid input: 'shippingCost' must be a non-negative number.");
  }

  // Calculate the subtotal by summing up the cost of each item
  let subtotal = items.reduce((total, item) => {
    if (typeof item.price !== 'number' || item.price < 0 || typeof item.quantity !== 'number' || item.quantity < 0) {
      throw new Error("Invalid item: Each item must have a non-negative 'price' and 'quantity'.");
    }
    return total + item.price * item.quantity;
  }, 0);

  // Determine if shipping is free
  const totalCost = subtotal >= 150 ? subtotal : subtotal + shippingCost;

  return totalCost;
}

// Example usage:
try {
  const items = [
    { price: 50, quantity: 2 }, // $100
    { price: 30, quantity: 1 }  // $30
  ];
  const shippingCost = 20; // Flat shipping cost

  const total = calculateTotalCost(items, shippingCost);
  console.log(`Total cost of the order: $${total}`); // Output: Total cost of the order: $130
} catch (error) {
  console.error(error.message);
}
```
