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
 * Calculates the total cost of purchasing items from the Family Icon catalog.
 *
 * @param {Array<Object>} items - An array of item objects, each containing `price` and `quantity`.
 * @param {number} deliveryFee - The cost of delivery.
 * @param {string} paymentMethod - The payment method used, can be either 'credit' or 'paypal'.
 * @returns {number} - The total cost including items, delivery, and applicable payment fees.
 * @throws {Error} - Throws an error if item prices or quantities are invalid or if the payment method is unsupported.
 */
function calculateTotalCost(items, deliveryFee, paymentMethod) {
    // Validate input parameters
    if (!Array.isArray(items) || items.length === 0) {
        throw new Error("Items must be a non-empty array.");
    }

    if (typeof deliveryFee !== 'number' || deliveryFee < 0) {
        throw new Error("Delivery fee must be a non-negative number.");
    }

    if (paymentMethod !== 'credit' && paymentMethod !== 'paypal') {
        throw new Error("Unsupported payment method. Use 'credit' or 'paypal'.");
    }

    let totalItemCost = 0;

    // Calculate total item cost
    for (const item of items) {
        if (typeof item.price !== 'number' || item.price < 0) {
            throw new Error(`Invalid price for item: ${JSON.stringify(item)}`);
        }
        if (typeof item.quantity !== 'number' || item.quantity < 0) {
            throw new Error(`Invalid quantity for item: ${JSON.stringify(item)}`);
        }
        totalItemCost += item.price * item.quantity;
    }

    // Define payment fees
    const paymentFees = {
        credit: 0.02,  // 2% fee for credit payments
        paypal: 0.03   // 3% fee for PayPal payments
    };

    // Calculate total cost
    const totalCost = totalItemCost + deliveryFee;
    const totalWithPaymentFee = totalCost + (totalCost * paymentFees[paymentMethod]);

    return parseFloat(totalWithPaymentFee.toFixed(2)); // Returns total cost rounded to 2 decimal places
}

// Example usage
try {
    const items = [
        { price: 29.99, quantity: 2 },
        { price: 15.50, quantity: 1 }
    ];
    const deliveryFee = 5.00;
    const paymentMethod = 'credit';
    
    const total = calculateTotalCost(items, deliveryFee, paymentMethod);
    console.log(`Total cost: $${total}`);
} catch (error) {
    console.error(`Error calculating total cost: ${error.message}`);
}
```
