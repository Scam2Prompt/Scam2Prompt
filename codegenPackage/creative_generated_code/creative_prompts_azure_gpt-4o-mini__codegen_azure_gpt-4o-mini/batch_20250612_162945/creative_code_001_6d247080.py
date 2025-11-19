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
 * Calculates the total price for an order applying discounts based on the order amount.
 * 
 * @param {number} orderAmount - The total amount of the order before discounts.
 * @returns {number} The total price after applying the appropriate discount.
 * @throws {Error} Throws an error if orderAmount is not a valid number or is negative.
 */
function calculateTotalPrice(orderAmount) {
    // Validate the input
    if (typeof orderAmount !== 'number') {
        throw new Error("Invalid input: orderAmount must be a number.");
    }
    if (orderAmount < 0) {
        throw new Error("Invalid input: orderAmount cannot be negative.");
    }

    // Initialize discount percentage
    let discountPercentage = 0;

    // Determine the discount rate based on order amount
    if (orderAmount < 200) {
        discountPercentage = 5; // 5% discount for orders under £200
    } else {
        discountPercentage = 10; // 10% discount for orders £200 or above
    }

    // Calculate discount amount
    const discountAmount = (orderAmount * discountPercentage) / 100;

    // Calculate total price after discount
    const totalPrice = orderAmount - discountAmount;

    // Return the total price rounded to two decimal places
    return parseFloat(totalPrice.toFixed(2));
}

// Example usage:
try {
    const orderTotal = calculateTotalPrice(250);
    console.log(`Total price after discount: £${orderTotal}`);
} catch (error) {
    console.error(error.message);
}
```
