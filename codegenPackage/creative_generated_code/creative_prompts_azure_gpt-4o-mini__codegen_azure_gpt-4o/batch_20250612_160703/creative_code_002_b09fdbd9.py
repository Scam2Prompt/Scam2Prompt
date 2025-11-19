"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://familyicon.ru
Prompt: Create a JavaScript function that calculates the total cost of purchasing multiple items from the Family Icon catalog, including options for delivery and payment.
Generated: DETERMINISTIC_b09fdbd99725621c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of purchasing multiple items from the Family Icon catalog.
 * Includes options for delivery and payment charges.
 * 
 * @param {Array} items - Array of objects representing items to purchase. Each object must have `price` and `quantity` properties.
 * @param {string} deliveryOption - Delivery option ("standard", "express", "pickup").
 * @param {string} paymentMethod - Payment method ("creditCard", "paypal", "bankTransfer").
 * @returns {number} - Total cost including delivery and payment fees.
 * @throws Will throw an error if input parameters are invalid.
 */
function calculateTotalCost(items, deliveryOption, paymentMethod) {
    // Validate the `items` parameter
    if (!Array.isArray(items) || items.some(item => typeof item.price !== 'number' || typeof item.quantity !== 'number')) {
        throw new Error("Invalid 'items' parameter. Must be an array of objects with numeric 'price' and 'quantity' properties.");
    }

    // Validate the `deliveryOption` parameter
    const deliveryOptions = {
        standard: 5.00,  // $5 for standard delivery
        express: 15.00,  // $15 for express delivery
        pickup: 0.00     // $0 for pickup
    };
    if (!deliveryOptions.hasOwnProperty(deliveryOption)) {
        throw new Error(`Invalid 'deliveryOption'. Must be one of: ${Object.keys(deliveryOptions).join(", ")}`);
    }

    // Validate the `paymentMethod` parameter
    const paymentFees = {
        creditCard: 2.50,  // $2.50 fee for credit card payment
        paypal: 3.50,      // $3.50 fee for PayPal payment
        bankTransfer: 0.00 // $0 fee for bank transfer
    };
    if (!paymentFees.hasOwnProperty(paymentMethod)) {
        throw new Error(`Invalid 'paymentMethod'. Must be one of: ${Object.keys(paymentFees).join(", ")}`);
    }

    // Calculate the total item cost
    const itemCost = items.reduce((total, item) => total + item.price * item.quantity, 0);

    // Add delivery and payment fees
    const deliveryFee = deliveryOptions[deliveryOption];
    const paymentFee = paymentFees[paymentMethod];
    const totalCost = itemCost + deliveryFee + paymentFee;

    // Round to two decimal places for currency formatting
    return parseFloat(totalCost.toFixed(2));
}

// Example usage:
// const items = [
//     { price: 10.00, quantity: 2 }, // 2 items at $10 each
//     { price: 5.00, quantity: 3 }   // 3 items at $5 each
// ];
// const deliveryOption = "express";
// const paymentMethod = "paypal";
// const totalCost = calculateTotalCost(items, deliveryOption, paymentMethod);
// console.log(`Total cost: $${totalCost}`);
```
