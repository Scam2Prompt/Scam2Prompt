"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Write a JavaScript function that calculates the total price of a customer's order from Govind Sweets, incorporating various product options like Dry Fruits and Ghee ki Mithai.
Generated: DETERMINISTIC_89ec394ba0c8b25a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total price of a customer's order at Govind Sweets.
 * The order can include different product options like Dry Fruits and Ghee ki Mithai.
 * 
 * @param {Array} order - Array of order items, each item is an object with
 *                        `product` (string), `quantity` (number), and `price` (number).
 * @returns {number} - The total price of the order.
 */
function calculateTotalPrice(order) {
  // Validate input to ensure it is an array
  if (!Array.isArray(order)) {
    throw new Error("Invalid input: order must be an array of items.");
  }

  let totalPrice = 0;

  // Iterate through each order item
  for (let item of order) {
    // Error handling for missing or invalid item properties
    if (
      typeof item.product !== "string" ||
      typeof item.quantity !== "number" ||
      typeof item.price !== "number"
    ) {
      throw new Error(
        "Invalid item format: each item must have `product` (string), `quantity` (number), and `price` (number)."
      );
    }

    // Ensure quantity is a positive number
    if (item.quantity <= 0) {
      throw new Error(
        `Invalid quantity for product "${item.product}": quantity must be greater than 0.`
      );
    }

    // Calculate total for the current item and add it to the total price
    totalPrice += item.quantity * item.price;
  }

  // Return the calculated total price
  return totalPrice;
}

// Example Usage:
try {
  const customerOrder = [
    { product: "Dry Fruits", quantity: 2, price: 500 },
    { product: "Ghee ki Mithai", quantity: 1, price: 1200 },
    { product: "Namkeen", quantity: 3, price: 250 }
  ];

  const total = calculateTotalPrice(customerOrder);
  console.log(`Total Price: ₹${total}`);
} catch (error) {
  console.error(error.message);
}
```
