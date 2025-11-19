"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Write a JavaScript function that calculates the total cost of a shopping cart on the Art Pel website, including discounts for first-time purchases and payment via PIX.
Generated: DETERMINISTIC_1b15676b9af08ab5
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a shopping cart including discounts for first-time purchases
 * and PIX payment method.
 * 
 * @param {Array} cartItems - Array of items in the shopping cart
 * @param {boolean} isFirstTimePurchase - Flag indicating if it's a first-time purchase
 * @param {string} paymentMethod - Payment method used ('PIX', 'CREDIT_CARD', etc.)
 * @returns {Object} An object containing the subtotal, discounts, and total amount
 * @throws {Error} If cartItems is not an array or is empty
 */
function calculateCartTotal(cartItems, isFirstTimePurchase, paymentMethod) {
    // Validate input
    if (!Array.isArray(cartItems) || cartItems.length === 0) {
        throw new Error('Invalid cart items: must be a non-empty array');
    }

    // Calculate subtotal
    const subtotal = cartItems.reduce((sum, item) => {
        if (typeof item.price !== 'number' || item.price < 0) {
            throw new Error(`Invalid price for item: ${JSON.stringify(item)}`);
        }
        if (typeof item.quantity !== 'number' || item.quantity <= 0) {
            throw new Error(`Invalid quantity for item: ${JSON.stringify(item)}`);
        }
        return sum + (item.price * item.quantity);
    }, 0);

    // Apply discounts
    let discounts = 0;
    const discountDetails = [];

    // First-time purchase discount (10%)
    if (isFirstTimePurchase) {
        const firstTimeDiscount = subtotal * 0.1;
        discounts += firstTimeDiscount;
        discountDetails.push({
            type: 'FIRST_TIME_PURCHASE',
            amount: firstTimeDiscount
        });
    }

    // PIX payment discount (5%)
    if (paymentMethod === 'PIX') {
        const pixDiscount = subtotal * 0.05;
        discounts += pixDiscount;
        discountDetails.push({
            type: 'PIX_PAYMENT',
            amount: pixDiscount
        });
    }

    // Calculate final total
    const total = subtotal - discounts;

    return {
        subtotal: parseFloat(subtotal.toFixed(2)),
        discounts: parseFloat(discounts.toFixed(2)),
        discountDetails,
        total: parseFloat(total.toFixed(2))
    };
}
```
