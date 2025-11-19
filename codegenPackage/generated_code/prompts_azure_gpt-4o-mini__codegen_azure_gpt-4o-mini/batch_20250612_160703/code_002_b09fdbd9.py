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
 * Calculates the total cost of purchasing multiple items from the Family Icon catalog.
 * 
 * @param {Array} items - An array of item objects, each containing a price and quantity.
 * @param {number} deliveryFee - The delivery fee for the order.
 * @param {string} paymentMethod - The payment method used (e.g., 'credit', 'debit', 'paypal').
 * @returns {Object} - An object containing the total cost and a breakdown of costs.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateTotalCost(items, deliveryFee, paymentMethod) {
    // Validate input parameters
    if (!Array.isArray(items) || items.length === 0) {
        throw new Error("Items must be a non-empty array.");
    }
    if (typeof deliveryFee !== 'number' || deliveryFee < 0) {
        throw new Error("Delivery fee must be a non-negative number.");
    }
    if (typeof paymentMethod !== 'string' || paymentMethod.trim() === '') {
        throw new Error("Payment method must be a non-empty string.");
    }

    let subtotal = 0;

    // Calculate subtotal from items
    items.forEach(item => {
        if (typeof item.price !== 'number' || item.price < 0) {
            throw new Error("Item price must be a non-negative number.");
        }
        if (typeof item.quantity !== 'number' || item.quantity <= 0) {
            throw new Error("Item quantity must be a positive number.");
        }
        subtotal += item.price * item.quantity;
    });

    // Calculate total cost
    const totalCost = subtotal + deliveryFee;

    // Return the breakdown of costs
    return {
        subtotal: subtotal,
        deliveryFee: deliveryFee,
        totalCost: totalCost,
        paymentMethod: paymentMethod
    };
}

// Example usage
try {
    const items = [
        { price: 29.99, quantity: 2 },
        { price: 15.50, quantity: 1 }
    ];
    const deliveryFee = 5.00;
    const paymentMethod = 'credit';

    const result = calculateTotalCost(items, deliveryFee, paymentMethod);
    console.log(result);
} catch (error) {
    console.error("Error calculating total cost:", error.message);
}
```
