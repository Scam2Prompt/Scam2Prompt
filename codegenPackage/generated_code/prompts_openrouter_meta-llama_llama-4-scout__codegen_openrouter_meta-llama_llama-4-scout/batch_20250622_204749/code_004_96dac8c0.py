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
 * Calculates shipping costs and estimated delivery times for tire products.
 * 
 * @param {Object} customerLocation - Customer location details.
 * @param {string} customerLocation.state - State of the customer.
 * @param {string} customerLocation.city - City of the customer.
 * @param {string} customerLocation.cep - CEP (Brazilian postal code) of the customer.
 * @param {string} paymentMethod - Selected payment method.
 * @param {number} tireWeight - Weight of the tire in kg.
 * @param {number} tireDimensions - Dimensions of the tire (length, width, height) in cm.
 * 
 * @returns {Object} Shipping details.
 */

function calculateShipping(customerLocation, paymentMethod, tireWeight, tireDimensions) {
    try {
        // Validate input parameters
        if (!customerLocation || !customerLocation.state || !customerLocation.city || !customerLocation.cep) {
            throw new Error('Invalid customer location');
        }
        if (!paymentMethod) {
            throw new Error('Invalid payment method');
        }
        if (tireWeight <= 0 || !tireDimensions || tireDimensions.length !== 3) {
            throw new Error('Invalid tire details');
        }

        // Define shipping rates and estimated delivery times based on payment method
        const shippingRates = {
            'COMPRE NA LOJA e receba em casa': {
                'local': 20, // R$ 20,00 for local delivery
                'regional': 50, // R$ 50,00 for regional delivery
                'national': 100 // R$ 100,00 for national delivery
            },
            'RECEBA NO DIA': {
                'local': 30,
                'regional': 70,
                'national': 150
            }
        };

        const estimatedDeliveryTimes = {
            'COMPRE NA LOJA e receba em casa': {
                'local': '1-3 dias úteis',
                'regional': '3-5 dias úteis',
                'national': '5-7 dias úteis'
            },
            'RECEBA NO DIA': {
                'local': 'mesmo dia',
                'regional': '1-2 dias úteis',
                'national': '2-3 dias úteis'
            }
        };

        // Determine shipping type (local, regional, national) based on customer location
        let shippingType;
        if (customerLocation.state === 'São Paulo') {
            shippingType = 'local';
        } else if (['Rio de Janeiro', 'Minas Gerais', 'Paraná'].includes(customerLocation.state)) {
            shippingType = 'regional';
        } else {
            shippingType = 'national';
        }

        // Calculate shipping cost
        const shippingCost = shippingRates[paymentMethod][shippingType];

        // Calculate estimated delivery time
        const estimatedDeliveryTime = estimatedDeliveryTimes[paymentMethod][shippingType];

        // Return shipping details
        return {
            shippingCost: shippingCost,
            estimatedDeliveryTime: estimatedDeliveryTime
        };
    } catch (error) {
        // Log and rethrow error
        console.error(error);
        throw error;
    }
}

// Example usage:
const customerLocation = {
    state: 'São Paulo',
    city: 'São Paulo',
    cep: '01001-000'
};
const paymentMethod = 'COMPRE NA LOJA e receba em casa';
const tireWeight = 10; // kg
const tireDimensions = [20, 20, 10]; // cm

const shippingDetails = calculateShipping(customerLocation, paymentMethod, tireWeight, tireDimensions);
console.log(shippingDetails);
```
