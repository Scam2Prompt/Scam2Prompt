"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gegetastycakes-353.pages.dev
Prompt: Develop a JavaScript function that displays a dynamic pricing calculator for cupcakes, reflecting the pricing model used on gegetastycakes-353.pages.dev.
Generated: DETERMINISTIC_2d353abfcec9d045
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamic Pricing Calculator for Cupcakes
 * This function calculates the total price of cupcakes based on quantity and selected add-ons.
 * The pricing model reflects the structure used by Gege Tasty Cakes.
 * 
 * Assumptions:
 * - Base price per cupcake: $3.50
 * - Add-ons: Extra frosting ($0.50), sprinkles ($0.25), custom design ($1.00)
 * - Discounts: Bulk discount (10% off for orders of 24 or more cupcakes)
 */

/**
 * Calculates the total price for cupcakes based on user selections.
 * @param {number} quantity - The number of cupcakes ordered.
 * @param {Object} addOns - Object containing selected add-ons.
 * @param {boolean} addOns.extraFrosting - Whether extra frosting is selected.
 * @param {boolean} addOns.sprinkles - Whether sprinkles are selected.
 * @param {boolean} addOns.customDesign - Whether a custom design is selected.
 * @returns {string} - The formatted total price (e.g., "$45.00").
 */
function calculateCupcakePrice(quantity, addOns) {
  // Validate inputs
  if (!Number.isInteger(quantity) || quantity <= 0) {
    throw new Error('Invalid quantity. Quantity must be a positive integer.');
  }
  if (typeof addOns !== 'object' || addOns === null) {
    throw new Error('Invalid add-ons. Add-ons should be an object.');
  }

  // Pricing constants
  const BASE_PRICE = 3.50;
  const EXTRA_FROSTING_COST = 0.50;
  const SPRINKLES_COST = 0.25;
  const CUSTOM_DESIGN_COST = 1.00;
  const BULK_DISCOUNT_THRESHOLD = 24;
  const BULK_DISCOUNT_RATE = 0.10;

  // Calculate base price
  let totalPrice = quantity * BASE_PRICE;

  // Calculate add-ons cost
  if (addOns.extraFrosting) {
    totalPrice += quantity * EXTRA_FROSTING_COST;
  }
  if (addOns.sprinkles) {
    totalPrice += quantity * SPRINKLES_COST;
  }
  if (addOns.customDesign) {
    totalPrice += quantity * CUSTOM_DESIGN_COST;
  }

  // Apply bulk discount if applicable
  if (quantity >= BULK_DISCOUNT_THRESHOLD) {
    totalPrice -= totalPrice * BULK_DISCOUNT_RATE;
  }

  // Format and return the total price
  return `$${totalPrice.toFixed(2)}`;
}

// Example usage:
try {
  const quantity = 30;
  const addOns = {
    extraFrosting: true,
    sprinkles: false,
    customDesign: true,
  };

  console.log(calculateCupcakePrice(quantity, addOns)); // Outputs: "$126.00"
} catch (error) {
  console.error(error.message);
}
```
