"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a JavaScript function to calculate shipping costs and estimated delivery times for tire products based on the customer's location and selected payment method (e.g., COMPRE NA LOJA e receba em casa).
Generated: DETERMINISTIC_96dac8c0ce05812b
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates shipping costs and estimated delivery times for tire products
 * @param {Object} options - Shipping calculation options
 * @param {string} options.customerLocation - Customer's location (e.g., "SP", "RJ")
 * @param {string} options.paymentMethod - Selected payment method (e.g., "COMPRE_NA_LOJA")
 * @param {number} options.tireQuantity - Number of tires being ordered
 * @param {string} options.tireSize - Size of the tires (e.g., "205/55R16")
 * @returns {Object} - Shipping information including cost and delivery time
 */
function calculateTireShipping(options) {
    // Validate input parameters
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid options parameter');
    }

    const { customerLocation, paymentMethod, tireQuantity, tireSize } = options;

    if (!customerLocation || typeof customerLocation !== 'string') {
        throw new Error('Invalid customerLocation');
    }

    if (!paymentMethod || typeof paymentMethod !== 'string') {
        throw new Error('Invalid paymentMethod');
    }

    if (!tireQuantity || typeof tireQuantity !== 'number' || tireQuantity <= 0) {
        throw new Error('Invalid tireQuantity');
    }

    if (!tireSize || typeof tireSize !== 'string') {
        throw new Error('Invalid tireSize');
    }

    // Base shipping rates by region (in BRL)
    const regionRates = {
        'SP': { baseCost: 50, perTire: 10 },
        'RJ': { baseCost: 70, perTire: 15 },
        'MG': { baseCost: 80, perTire: 20 },
        'default': { baseCost: 100, perTire: 25 }
    };

    // Delivery times by region (in business days)
    const deliveryTimes = {
        'SP': { minDays: 1, maxDays: 3 },
        'RJ': { minDays: 2, maxDays: 4 },
        'MG': { minDays: 3, maxDays: 5 },
        'default': { minDays: 5, maxDays: 10 }
    };

    // Special cases for "COMPRE NA LOJA" payment method
    const storePickupDiscounts = {
        'COMPRE_NA_LOJA': { discount: 0.5, extraDays: 0 },
        'default': { discount: 0, extraDays: 0 }
    };

    // Get region rates and delivery times
    const region = regionRates[customerLocation] || regionRates.default;
    const delivery = deliveryTimes[customerLocation] || deliveryTimes.default;
    const pickupDiscount = storePickupDiscounts[paymentMethod] || storePickupDiscounts.default;

    // Calculate base shipping cost
    let shippingCost = region.baseCost + (region.perTire * tireQuantity);

    // Apply discounts for special payment methods
    shippingCost = shippingCost * (1 - pickupDiscount.discount);

    // Calculate delivery time range
    const minDeliveryDays = delivery.minDays + pickupDiscount.extraDays;
    const maxDeliveryDays = delivery.maxDays + pickupDiscount.extraDays;

    // Additional charge for large tires (R18 and above)
    const sizeMatch = tireSize.match(/R(\d+)/);
    if (sizeMatch && sizeMatch[1]) {
        const rimSize = parseInt(sizeMatch[1]);
        if (rimSize >= 18) {
            shippingCost += 30 * tireQuantity;
        }
    }

    return {
        shippingCost: Math.round(shippingCost * 100) / 100,
        estimatedDelivery: `${minDeliveryDays}-${maxDeliveryDays} business days`,
        paymentMethod,
        customerLocation,
        tireQuantity,
        tireSize
    };
}

// Example usage:
// try {
//     const shippingInfo = calculateTireShipping({
//         customerLocation: 'SP',
//         paymentMethod: 'COMPRE_NA_LOJA',
//         tireQuantity: 4,
//         tireSize: '205/55R16'
//     });
//     console.log(shippingInfo);
// } catch (error) {
//     console.error('Error calculating shipping:', error.message);
// }
```
