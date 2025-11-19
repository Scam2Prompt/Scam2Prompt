"""
Generated Code Metadata:
========================
Original URL: https://beltsmania.com
Prompt: Develop a JavaScript function to handle payment processing and shipping calculations for an online store selling replica wrestling belts.
Generated: DETERMINISTIC_722d7677f1b4b72f
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Payment and Shipping Handler for Online Wrestling Belts Store
 * 
 * This module handles payment processing and shipping calculations for an online store
 * selling replica wrestling belts. It includes functions for calculating shipping costs,
 * applying discounts, processing payments, and handling errors.
 */

/**
 * Shipping rates based on weight and destination
 */
const SHIPPING_RATES = {
    domestic: {
        standard: { base: 5.99, perPound: 1.50 },
        express: { base: 12.99, perPound: 2.50 }
    },
    international: {
        standard: { base: 15.99, perPound: 5.00 },
        express: { base: 29.99, perPound: 8.00 }
    }
};

/**
 * Discount codes and their values
 */
const DISCOUNT_CODES = {
    'BELT10': 0.10,  // 10% off
    'CHAMP20': 0.20, // 20% off
    'WRESTLE30': 0.30 // 30% off
};

/**
 * Calculates shipping cost based on weight, destination, and shipping method
 * @param {number} weight - Weight in pounds
 * @param {string} destination - 'domestic' or 'international'
 * @param {string} method - 'standard' or 'express'
 * @returns {number} Calculated shipping cost
 * @throws {Error} If invalid parameters are provided
 */
function calculateShipping(weight, destination, method) {
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error('Invalid weight: must be a positive number');
    }

    if (!['domestic', 'international'].includes(destination)) {
        throw new Error('Invalid destination: must be "domestic" or "international"');
    }

    if (!['standard', 'express'].includes(method)) {
        throw new Error('Invalid method: must be "standard" or "express"');
    }

    const rate = SHIPPING_RATES[destination][method];
    return rate.base + (rate.perPound * weight);
}

/**
 * Applies discount code to order total
 * @param {number} subtotal - Order subtotal before discounts
 * @param {string} discountCode - Discount code to apply
 * @returns {number} Discounted total
 * @throws {Error} If invalid discount code is provided
 */
function applyDiscount(subtotal, discountCode) {
    if (typeof subtotal !== 'number' || subtotal <= 0) {
        throw new Error('Invalid subtotal: must be a positive number');
    }

    if (!discountCode) {
        return subtotal;
    }

    const discount = DISCOUNT_CODES[discountCode];
    if (!discount) {
        throw new Error('Invalid discount code');
    }

    return subtotal * (1 - discount);
}

/**
 * Processes payment using a payment gateway
 * @param {Object} paymentDetails - Payment details object
 * @param {number} amount - Amount to charge
 * @returns {Promise<Object>} Payment result
 * @throws {Error} If payment fails
 */
async function processPayment(paymentDetails, amount) {
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Invalid amount: must be a positive number');
    }

    if (!paymentDetails || !paymentDetails.cardNumber || !paymentDetails.expiry || !paymentDetails.cvv) {
        throw new Error('Invalid payment details: missing required fields');
    }

    // In a real implementation, this would call an actual payment gateway API
    // This is a mock implementation for demonstration purposes
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // Simulate random failures for demonstration
            if (Math.random() < 0.05) {
                reject(new Error('Payment processing failed: network error'));
            } else if (paymentDetails.cardNumber === '4111111111111111') {
                reject(new Error('Payment processing failed: insufficient funds'));
            } else {
                resolve({
                    success: true,
                    transactionId: `txn_${Math.random().toString(36).substr(2, 9)}`,
                    amount: amount
                });
            }
        }, 1000);
    });
}

/**
 * Processes an order with payment and shipping calculations
 * @param {Object} order - Order details
 * @param {Array} order.items - Array of items in order
 * @param {string} order.shippingMethod - 'standard' or 'express'
 * @param {string} order.destination - 'domestic' or 'international'
 * @param {string} [order.discountCode] - Optional discount code
 * @param {Object} paymentDetails - Payment details
 * @returns {Promise<Object>} Order processing result
 */
async function processOrder(order, paymentDetails) {
    try {
        // Validate order
        if (!order || !order.items || !order.shippingMethod || !order.destination) {
            throw new Error('Invalid order: missing required fields');
        }

        // Calculate subtotal
        const subtotal = order.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);

        // Calculate total weight
        const totalWeight = order.items.reduce((sum, item) => sum + (item.weight * item.quantity), 0);

        // Apply discount if available
        const discountedTotal = applyDiscount(subtotal, order.discountCode);

        // Calculate shipping
        const shippingCost = calculateShipping(totalWeight, order.destination, order.shippingMethod);

        // Calculate final total
        const total = discountedTotal + shippingCost;

        // Process payment
        const paymentResult = await processPayment(paymentDetails, total);

        return {
            success: true,
            orderDetails: {
                subtotal: subtotal,
                discountApplied: order.discountCode ? DISCOUNT_CODES[order.discountCode] : 0,
                shippingCost: shippingCost,
                total: total,
                shippingMethod: order.shippingMethod,
                destination: order.destination
            },
            paymentResult: paymentResult
        };
    } catch (error) {
        return {
            success: false,
            error: error.message
        };
    }
}

// Export functions for module use
module.exports = {
    calculateShipping,
    applyDiscount,
    processPayment,
    processOrder
};
```
