"""
Generated Code Metadata:
========================
Original URL: https://familyicon.ru
Prompt: Create a JavaScript function that calculates the total cost of purchasing multiple items from the Family Icon catalog, including options for delivery and payment.
Generated: DETERMINISTIC_b09fdbd99725621c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of purchasing items from the Family Icon catalog.
 * Includes options for delivery and payment.
 *
 * @param {Array} items - Array of objects representing items to purchase. Each object should have:
 *                        - name {string}: Name of the item
 *                        - price {number}: Price of the item
 *                        - quantity {number}: Quantity of the item
 * @param {string} deliveryOption - Delivery option. Can be "standard", "express", or "pickup".
 *                                   - "standard": $5 delivery fee
 *                                   - "express": $10 delivery fee
 *                                   - "pickup": No delivery fee
 * @param {string} paymentMethod - Payment method. Can be "credit_card", "paypal", or "cash".
 *                                 - "credit_card": 2% processing fee
 *                                 - "paypal": 3% processing fee
 *                                 - "cash": No processing fee
 * @returns {number} - The total cost including delivery and payment fees.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateTotalCost(items, deliveryOption, paymentMethod) {
  // Validate input
  if (!Array.isArray(items) || items.length === 0) {
    throw new Error("Invalid items array. Must be a non-empty array.");
  }

  if (!["standard", "express", "pickup"].includes(deliveryOption)) {
    throw new Error("Invalid delivery option. Must be 'standard', 'express', or 'pickup'.");
  }

  if (!["credit_card", "paypal", "cash"].includes(paymentMethod)) {
    throw new Error("Invalid payment method. Must be 'credit_card', 'paypal', or 'cash'.");
  }

  // Calculate the total cost of items
  let itemTotal = 0;
  items.forEach((item) => {
    if (
      typeof item.name !== "string" ||
      typeof item.price !== "number" ||
      typeof item.quantity !== "number" ||
      item.price < 0 ||
      item.quantity < 0
    ) {
      throw new Error("Invalid item object. Each item must have a valid name, price, and quantity.");
    }
    itemTotal += item.price * item.quantity;
  });

  // Calculate delivery fee
  let deliveryFee = 0;
  switch (deliveryOption) {
    case "standard":
      deliveryFee = 5;
      break;
    case "express":
      deliveryFee = 10;
      break;
    case "pickup":
      deliveryFee = 0;
      break;
  }

  // Calculate payment processing fee
  let paymentFee = 0;
  switch (paymentMethod) {
    case "credit_card":
      paymentFee = itemTotal * 0.02; // 2% fee
      break;
    case "paypal":
      paymentFee = itemTotal * 0.03; // 3% fee
      break;
    case "cash":
      paymentFee = 0;
      break;
  }

  // Calculate the final total cost
  const totalCost = itemTotal + deliveryFee + paymentFee;

  return totalCost;
}

// Example usage:
try {
  const items = [
    { name: "Item A", price: 20, quantity: 2 },
    { name: "Item B", price: 15, quantity: 1 },
  ];
  const deliveryOption = "standard";
  const paymentMethod = "credit_card";

  const totalCost = calculateTotalCost(items, deliveryOption, paymentMethod);
  console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
