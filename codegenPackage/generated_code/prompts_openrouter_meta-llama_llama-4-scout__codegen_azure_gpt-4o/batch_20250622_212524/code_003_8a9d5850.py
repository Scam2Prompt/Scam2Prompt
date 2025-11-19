"""
Generated Code Metadata:
========================
Original URL: https://avilhasdolarbraz.blogspot.com
Prompt: Create a JavaScript function to calculate the total cost of items in a shopping cart, considering discounts and installment plans with interest.
Generated: DETERMINISTIC_8a9d5850ff423963
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the total cost of items in a shopping cart.
 * Considers discounts and installment plans with interest.
 *
 * @param {Array} cartItems - Array of objects representing items in the cart.
 * Each item should have the following properties:
 *   - price: Number (price of the item)
 *   - quantity: Number (quantity of the item)
 *   - discount: Number (percentage discount on the item, e.g., 10 for 10%)
 * @param {Object} installmentPlan - Object representing the installment plan.
 * Should have the following properties:
 *   - months: Number (number of months for the installment plan)
 *   - interestRate: Number (monthly interest rate as a percentage, e.g., 2 for 2%)
 * @returns {Number} - Total cost after applying discounts and installment plan interest.
 */
function calculateTotalCost(cartItems, installmentPlan) {
  // Validate input
  if (!Array.isArray(cartItems) || typeof installmentPlan !== 'object') {
    throw new Error('Invalid input: cartItems must be an array and installmentPlan must be an object.');
  }

  // Calculate the total cost of items after applying discounts
  let totalCost = 0;
  for (const item of cartItems) {
    if (
      typeof item.price !== 'number' ||
      typeof item.quantity !== 'number' ||
      typeof item.discount !== 'number'
    ) {
      throw new Error('Invalid item format: Each item must have price, quantity, and discount as numbers.');
    }

    const discountedPrice = item.price * (1 - item.discount / 100); // Apply discount
    totalCost += discountedPrice * item.quantity; // Multiply by quantity and add to total
  }

  // Apply installment plan interest if applicable
  if (installmentPlan.months > 0 && installmentPlan.interestRate > 0) {
    const monthlyInterestFactor = 1 + installmentPlan.interestRate / 100; // Calculate monthly interest factor
    totalCost *= Math.pow(monthlyInterestFactor, installmentPlan.months); // Apply compound interest
  }

  return totalCost;
}

// Example usage:
const cartItems = [
  { price: 100, quantity: 2, discount: 10 }, // Item 1
  { price: 50, quantity: 1, discount: 5 },  // Item 2
];

const installmentPlan = {
  months: 12,
  interestRate: 2, // 2% monthly interest
};

try {
  const total = calculateTotalCost(cartItems, installmentPlan);
  console.log(`Total cost: $${total.toFixed(2)}`);
} catch (error) {
  console.error(error.message);
}
```
