"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homemerce.com
Prompt: Write a function in JavaScript that calculates the total price for an order including a 5% discount for orders under £200 and a 10% discount for orders above £200, as mentioned on Homemerce.
Generated: DETERMINISTIC_6d247080bebf1dc0
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price for an order, including applicable discounts.
 * 
 * Discount Rules:
 * - 5% discount for orders under £200.
 * - 10% discount for orders above £200.
 * 
 * @param {number} orderAmount - The total price of the order before discount.
 * @returns {number} - The total price after applying the discount.
 * @throws {Error} - If the provided orderAmount is not a valid positive number.
 */
function calculateTotalPrice(orderAmount) {
    // Validate input
    if (typeof orderAmount !== 'number' || orderAmount <= 0) {
        throw new Error("Invalid order amount. Please provide a positive number.");
    }

    let discountRate = 0;

    // Determine the discount rate based on the order amount
    if (orderAmount < 200) {
        discountRate = 0.05; // 5% discount
    } else {
        discountRate = 0.10; // 10% discount
    }

    // Calculate the final price after applying the discount
    const discount = orderAmount * discountRate;
    const finalPrice = orderAmount - discount;

    return parseFloat(finalPrice.toFixed(2)); // Ensure the result is rounded to two decimal places
}

// Example usage:
// console.log(calculateTotalPrice(150)); // Output: 142.50
// console.log(calculateTotalPrice(250)); // Output: 225.00
```
