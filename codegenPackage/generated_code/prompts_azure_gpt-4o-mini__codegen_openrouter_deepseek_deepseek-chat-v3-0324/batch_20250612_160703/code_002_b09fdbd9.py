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
 * Calculates the total cost of purchasing items from the Family Icon catalog.
 * @param {Array} items - Array of items with price and quantity
 * @param {Object} deliveryOptions - Delivery options object
 * @param {Object} paymentOptions - Payment options object
 * @returns {Object} - Result containing subtotal, delivery cost, payment fee, and total
 */
function calculateTotalCost(items, deliveryOptions, paymentOptions) {
    // Validate input parameters
    if (!Array.isArray(items) || !deliveryOptions || !paymentOptions) {
        throw new Error('Invalid input parameters');
    }

    // Calculate subtotal
    let subtotal = 0;
    try {
        subtotal = items.reduce((sum, item) => {
            if (!item.price || !item.quantity || 
                typeof item.price !== 'number' || 
                typeof item.quantity !== 'number' ||
                item.price < 0 || item.quantity < 0) {
                throw new Error('Invalid item data');
            }
            return sum + (item.price * item.quantity);
        }, 0);
    } catch (error) {
        throw new Error(`Error calculating subtotal: ${error.message}`);
    }

    // Calculate delivery cost
    let deliveryCost = 0;
    try {
        if (!deliveryOptions.method || !deliveryOptions.cost || 
            typeof deliveryOptions.cost !== 'number' || 
            deliveryOptions.cost < 0) {
            throw new Error('Invalid delivery options');
        }
        deliveryCost = deliveryOptions.cost;
    } catch (error) {
        throw new Error(`Error calculating delivery cost: ${error.message}`);
    }

    // Calculate payment fee
    let paymentFee = 0;
    try {
        if (!paymentOptions.method || !paymentOptions.feePercentage || 
            typeof paymentOptions.feePercentage !== 'number' || 
            paymentOptions.feePercentage < 0) {
            throw new Error('Invalid payment options');
        }
        paymentFee = subtotal * (paymentOptions.feePercentage / 100);
    } catch (error) {
        throw new Error(`Error calculating payment fee: ${error.message}`);
    }

    // Calculate total
    const total = subtotal + deliveryCost + paymentFee;

    return {
        subtotal: parseFloat(subtotal.toFixed(2)),
        deliveryCost: parseFloat(deliveryCost.toFixed(2)),
        paymentFee: parseFloat(paymentFee.toFixed(2)),
        total: parseFloat(total.toFixed(2)),
        currency: 'USD' // Default currency
    };
}

// Example usage:
/*
const items = [
    { price: 10.99, quantity: 2 },
    { price: 5.50, quantity: 3 }
];

const deliveryOptions = {
    method: 'standard',
    cost: 5.99
};

const paymentOptions = {
    method: 'credit_card',
    feePercentage: 2.5
};

try {
    const result = calculateTotalCost(items, deliveryOptions, paymentOptions);
    console.log(result);
} catch (error) {
    console.error('Error:', error.message);
}
*/
```
