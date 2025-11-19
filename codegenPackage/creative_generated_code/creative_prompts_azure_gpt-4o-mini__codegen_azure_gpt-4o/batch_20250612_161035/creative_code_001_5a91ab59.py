"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novavault.shop
Prompt: Write a function in JavaScript to calculate the estimated total for a shopping cart, including taxes and discounts, as seen on Novavault's checkout page.
Generated: DETERMINISTIC_5a91ab5902b224f0
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the estimated total for a shopping cart, including taxes and discounts.
 * 
 * @param {Array} items - Array of objects representing items in the cart. Each object has:
 *                        - price {number}: The price of the item.
 *                        - quantity {number}: The quantity of the item.
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.07 for 7% tax).
 * @param {number} discountRate - The discount rate as a decimal (e.g., 0.10 for 10% discount).
 * 
 * @returns {number} - The estimated total after applying taxes and discounts.
 */
function calculateEstimatedTotal(items, taxRate, discountRate) {
  // Input validation
  if (!Array.isArray(items)) {
    throw new Error("Invalid input: items must be an array.");
  }

  if (typeof taxRate !== 'number' || taxRate < 0 || taxRate > 1) {
    throw new Error("Invalid input: taxRate must be a number between 0 and 1.");
  }

  if (typeof discountRate !== 'number' || discountRate < 0 || discountRate > 1) {
    throw new Error("Invalid input: discountRate must be a number between 0 and 1.");
  }

  try {
    // Calculate the subtotal by summing the price * quantity for all items
    const subtotal = items.reduce((total, item) => {
      if (typeof item.price !== 'number' || item.price < 0) {
        throw new Error("Invalid item price detected.");
      }
      if (typeof item.quantity !== 'number' || item.quantity < 0) {
        throw new Error("Invalid item quantity detected.");
      }
      return total + item.price * item.quantity;
    }, 0);

    // Apply tax to the subtotal
    const taxAmount = subtotal * taxRate;

    // Apply discount to the subtotal
    const discountAmount = subtotal * discountRate;

    // Calculate the final total
    const estimatedTotal = subtotal + taxAmount - discountAmount;

    // Return the rounded total to 2 decimal places
    return parseFloat(estimatedTotal.toFixed(2));
  } catch (error) {
    console.error("Error calculating estimated total:", error.message);
    throw error; // Rethrow error for external handling
  }
}

// Example usage
try {
  const shoppingCart = [
    { price: 29.99, quantity: 2 },
    { price: 15.99, quantity: 1 },
    { price: 9.99, quantity: 3 }
  ];
  const taxRate = 0.07; // 7% tax
  const discountRate = 0.10; // 10% discount

  const total = calculateEstimatedTotal(shoppingCart, taxRate, discountRate);
  console.log("Estimated Total:", total);
} catch (error) {
  console.error("Failed to calculate the total:", error.message);
}
```
