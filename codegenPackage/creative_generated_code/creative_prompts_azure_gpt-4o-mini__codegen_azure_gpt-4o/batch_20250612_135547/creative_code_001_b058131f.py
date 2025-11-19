"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woopytee.com
Prompt: Write a JavaScript function to calculate the discount on a cart total based on the WoopyTee "Buy More Save More" promotion.
Generated: DETERMINISTIC_b058131f01ee27e6
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the discount on a cart total based on the "Buy More Save More" promotion.
 * 
 * Promotion rules:
 * - $0 - $50: No discount
 * - $51 - $100: 5% discount
 * - $101 - $200: 10% discount
 * - Above $200: 15% discount
 * 
 * @param {number} cartTotal - The total amount of the cart before the discount.
 * @returns {object} - An object containing the discount percentage, 
 *                     the discount amount, and the final total after applying the discount.
 * @throws {Error} - If the cartTotal is not a valid positive number.
 */
function calculateDiscount(cartTotal) {
  // Input validation: Ensure cartTotal is a valid positive number
  if (typeof cartTotal !== 'number' || cartTotal < 0) {
    throw new Error('Invalid cart total. Please provide a positive number.');
  }

  // Define discount rules
  let discountPercentage = 0;

  if (cartTotal > 200) {
    discountPercentage = 15;
  } else if (cartTotal > 100) {
    discountPercentage = 10;
  } else if (cartTotal > 50) {
    discountPercentage = 5;
  }

  // Calculate discount amount and final total
  const discountAmount = (cartTotal * discountPercentage) / 100;
  const finalTotal = cartTotal - discountAmount;

  // Return the results in a structured object
  return {
    discountPercentage: discountPercentage,
    discountAmount: parseFloat(discountAmount.toFixed(2)), // Round to 2 decimal places for currency
    finalTotal: parseFloat(finalTotal.toFixed(2)), // Round to 2 decimal places for currency
  };
}

// Example usage:
try {
  const cartTotal = 120; // Replace with actual cart total
  const discountDetails = calculateDiscount(cartTotal);
  console.log('Discount Details:', discountDetails);
} catch (error) {
  console.error('Error:', error.message);
}
```
