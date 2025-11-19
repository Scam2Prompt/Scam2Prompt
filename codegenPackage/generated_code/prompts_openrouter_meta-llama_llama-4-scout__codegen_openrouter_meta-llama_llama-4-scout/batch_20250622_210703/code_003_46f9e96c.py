"""
Generated Code Metadata:
========================
Original URL: https://yummydelivery.com.ve
Prompt: Develop a JavaScript function to calculate the total cost of a delivery order, including taxes and discounts, based on the Yummy Delivery pricing model.
Generated: DETERMINISTIC_46f9e96cdf704f3c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a delivery order based on the Yummy Delivery pricing model.
 * 
 * @param {Object} orderDetails - The details of the delivery order.
 * @param {number} orderDetails.subtotal - The subtotal of the order before taxes and discounts.
 * @param {number} [orderDetails.taxRate=0] - The tax rate as a decimal (e.g., 8% = 0.08).
 * @param {number} [orderDetails.discount=0] - The discount amount.
 * @param {string} [orderDetails.deliveryType='standard'] - The type of delivery (standard, express).
 * @param {number} [orderDetails.deliveryFee=0] - The delivery fee.
 * 
 * @returns {Object} The total cost of the delivery order.
 */

function calculateDeliveryCost(orderDetails) {
    try {
        // Check if orderDetails is an object
        if (typeof orderDetails !== 'object') {
            throw new Error('Order details must be an object');
        }

        // Check if subtotal is a positive number
        if (typeof orderDetails.subtotal !== 'number' || orderDetails.subtotal <= 0) {
            throw new Error('Subtotal must be a positive number');
        }

        // Set default values for taxRate, discount, deliveryType, and deliveryFee if not provided
        const taxRate = orderDetails.taxRate || 0;
        const discount = orderDetails.discount || 0;
        const deliveryType = orderDetails.deliveryType || 'standard';
        const deliveryFee = orderDetails.deliveryFee || 0;

        // Calculate the discount amount
        const discountAmount = Math.min(discount, orderDetails.subtotal);

        // Calculate the subtotal after discount
        const subtotalAfterDiscount = orderDetails.subtotal - discountAmount;

        // Calculate the tax amount
        const taxAmount = subtotalAfterDiscount * taxRate;

        // Calculate the total cost before delivery fee
        let totalCost = subtotalAfterDiscount + taxAmount;

        // Add delivery fee based on delivery type
        if (deliveryType === 'express') {
            // For express delivery, add a 20% surcharge to the delivery fee
            totalCost += deliveryFee * 1.2;
        } else {
            totalCost += deliveryFee;
        }

        // Return the total cost
        return {
            subtotal: orderDetails.subtotal,
            discount: discountAmount,
            tax: taxAmount,
            deliveryFee: deliveryType === 'express' ? deliveryFee * 1.2 : deliveryFee,
            total: totalCost,
        };
    } catch (error) {
        // Log the error and return a meaningful error message
        // For a real application, consider using a logging library
        // console.error(error); // Commented out for this example
        throw new Error(`Failed to calculate delivery cost: ${error.message}`);
    }
}

// Example usage:
const order = {
    subtotal: 100,
    taxRate: 0.08,
    discount: 10,
    deliveryType: 'express',
    deliveryFee: 5,
};

const result = calculateDeliveryCost(order);
console.log(result);
```
