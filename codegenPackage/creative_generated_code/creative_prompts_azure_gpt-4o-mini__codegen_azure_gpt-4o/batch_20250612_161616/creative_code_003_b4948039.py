"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snackpointemmen.nl
Prompt: Develop a JavaScript function that simulates ordering from a snack bar, including options for soft serve ice cream and chicken buckets, as seen at Snackpoint Emmen.
Generated: DETERMINISTIC_b4948039ea92b674
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates ordering from a snack bar.
 * This function allows a user to order soft serve ice cream or chicken buckets
 * and calculates the total cost based on their selection.
 * 
 * @param {Object[]} items - Array of order items. Each item should contain a `type`
 *                           ('softServe' or 'chickenBucket') and a `quantity`.
 * @returns {Object} - An object containing the order details and total cost.
 */
function snackBarOrder(items) {
  // Menu with prices
  const menu = {
    softServe: 2.5,       // Price per soft serve ice cream
    chickenBucket: 10.0   // Price per chicken bucket
  };

  // Validate input
  if (!Array.isArray(items)) {
    throw new Error("Invalid input: 'items' must be an array.");
  }

  let totalCost = 0;
  const orderDetails = [];

  // Process each item in the order
  items.forEach((item, index) => {
    if (!item.type || !item.quantity) {
      throw new Error(`Invalid item format at index ${index}. Each item must have a 'type' and 'quantity'.`);
    }

    const { type, quantity } = item;

    // Validate item type
    if (!menu[type]) {
      throw new Error(`Invalid item type '${type}' at index ${index}. Allowed types are: ${Object.keys(menu).join(", ")}`);
    }

    // Validate quantity
    if (typeof quantity !== 'number' || quantity <= 0) {
      throw new Error(`Invalid quantity '${quantity}' for item type '${type}' at index ${index}. Quantity must be a positive number.`);
    }

    // Calculate cost for this item
    const itemCost = menu[type] * quantity;
    totalCost += itemCost;

    // Add item details to the order
    orderDetails.push({
      type,
      quantity,
      cost: itemCost
    });
  });

  // Return the final order details
  return {
    orderDetails,
    totalCost
  };
}

// Example usage:
try {
  const order = snackBarOrder([
    { type: 'softServe', quantity: 3 },
    { type: 'chickenBucket', quantity: 2 }
  ]);
  console.log("Order Summary:", order);
} catch (error) {
  console.error("Error:", error.message);
}
```
