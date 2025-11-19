"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biogreenasia.com
Prompt: Write a JavaScript function to calculate the total price of items in a shopping cart for a website selling products like Bioliv Hair Oils and Handy Liquid Dish Wash.
Generated: DETERMINISTIC_662f1a5b619673b7
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total price of items in a shopping cart.
 * 
 * @param {Array} cartItems - Array of objects representing items in the shopping cart.
 * Each object should have the following properties:
 *   - name {string}: name of the product (e.g., 'Bioliv Hair Oil')
 *   - price {number}: price of the product (e.g., 10.99)
 *   - quantity {number}: quantity of the product in the cart (e.g., 2)
 * 
 * @returns {number} - The total price of all items in the cart.
 * If the input is invalid, the function will throw an error.
 */
function calculateTotalPrice(cartItems) {
  // Validate input
  if (!Array.isArray(cartItems)) {
    throw new Error('Invalid input: cartItems must be an array.');
  }

  // Calculate total price
  return cartItems.reduce((total, item) => {
    // Validate each item
    if (
      typeof item.name !== 'string' ||
      typeof item.price !== 'number' ||
      typeof item.quantity !== 'number'
    ) {
      throw new Error('Invalid item format: Each item must have name (string), price (number), and quantity (number).');
    }

    if (item.price < 0 || item.quantity < 0) {
      throw new Error('Invalid item values: Price and quantity must be non-negative.');
    }

    // Add item price to total
    return total + item.price * item.quantity;
  }, 0);
}

// Example usage:
// const shoppingCart = [
//   { name: 'Bioliv Hair Oil', price: 10.99, quantity: 2 },
//   { name: 'Handy Liquid Dish Wash', price: 5.49, quantity: 3 }
// ];
// 
// console.log(calculateTotalPrice(shoppingCart)); // Output: 37.45
```
