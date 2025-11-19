"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Write a JavaScript function that calculates the total cost of a christening outfit order, including free shipping for orders over $150.
Generated: DETERMINISTIC_326b2ca3f66f8366
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of a christening outfit order
 * with free shipping applied for orders over $150.
 *
 * @param {Array<Object>} items - Array of objects representing the items in the order. 
 * Each item should have `price` and `quantity` properties.
 * @param {number} shippingFee - Flat shipping fee applied for orders under $150.
 * @returns {number} - Total cost of the order including shipping (if applicable).
 */
function calculateTotalCost(items, shippingFee) {
  // Validate input
  if (!Array.isArray(items)) {
    throw new Error("Invalid input: 'items' must be an array.");
  }
  if (typeof shippingFee !== "number" || shippingFee < 0) {
    throw new Error("Invalid input: 'shippingFee' must be a non-negative number.");
  }

  // Calculate the subtotal (sum of item prices * quantities)
  let subtotal = items.reduce((total, item) => {
    if (typeof item.price !== "number" || typeof item.quantity !== "number") {
      throw new Error("Invalid item: Each item must have a 'price' and 'quantity' of type number.");
    }
    if (item.price < 0 || item.quantity < 0) {
      throw new Error("Invalid item: 'price' and 'quantity' cannot be negative.");
    }
    return total + item.price * item.quantity;
  }, 0);

  // Apply free shipping for orders above $150
  const totalCost = subtotal >= 150 ? subtotal : subtotal + shippingFee;

  return totalCost;
}

// Example usage:
try {
  const items = [
    { price: 50, quantity: 2 }, // 2 items at $50 each
    { price: 20, quantity: 3 }, // 3 items at $20 each
  ];
  const shippingFee = 15;

  const total = calculateTotalCost(items, shippingFee);
  console.log(`The total cost of the order is $${total.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
