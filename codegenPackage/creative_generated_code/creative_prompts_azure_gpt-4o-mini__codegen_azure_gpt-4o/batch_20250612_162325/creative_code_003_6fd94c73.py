"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a JavaScript function that manages the logistics of storing and transporting cosmetic products, based on the logistics solutions provided by Fabricare.
Generated: DETERMINISTIC_6fd94c7362952433
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to manage logistics for storing and transporting cosmetic products.
 * This function is designed to integrate logistics solutions provided by Fabricare.
 *
 * @param {Array<Object>} products - Array of cosmetic product objects. Each object should contain:
 *                                   - id {string}: Unique identifier for the product.
 *                                   - name {string}: Name of the product.
 *                                   - quantity {number}: Quantity of the product.
 *                                   - temperatureSensitive {boolean}: Whether the product requires temperature control.
 * @param {Object} fabricareLogistics - Logistics solutions provided by Fabricare. Should contain:
 *                                      - storageCapacity {number}: Total storage capacity in units.
 *                                      - transportCapacity {number}: Transport capacity per trip in units.
 *                                      - temperatureControlledTransport {boolean}: Availability of temperature-controlled transport.
 * @returns {Object} - Summary of logistics management including:
 *                     - storageStatus {string}: Success or failure of storage operation.
 *                     - transportStatus {string}: Success or failure of transport operation.
 *                     - details {Array<Object>}: Detailed status for each product.
 */
function manageCosmeticsLogistics(products, fabricareLogistics) {
    if (!Array.isArray(products) || typeof fabricareLogistics !== 'object') {
        throw new Error('Invalid input: products must be an array and fabricareLogistics must be an object.');
    }

    const storageCapacity = fabricareLogistics.storageCapacity;
    const transportCapacity = fabricareLogistics.transportCapacity;
    const temperatureControlledTransport = fabricareLogistics.temperatureControlledTransport;

    let totalStored = 0;
    let totalTransported = 0;
    const details = [];

    for (const product of products) {
        try {
            // Validate product properties
            if (
                typeof product.id !== 'string' ||
                typeof product.name !== 'string' ||
                typeof product.quantity !== 'number' ||
                typeof product.temperatureSensitive !== 'boolean'
            ) {
                throw new Error(`Invalid product properties: ${JSON.stringify(product)}`);
            }

            // Check storage capacity
            if (totalStored + product.quantity > storageCapacity) {
                details.push({
                    productId: product.id,
                    status: 'Failed',
                    reason: 'Insufficient storage capacity',
                });
                continue;
            }

            // Check transport capability
            if (
                product.temperatureSensitive &&
                !temperatureControlledTransport
            ) {
                details.push({
                    productId: product.id,
                    status: 'Failed',
                    reason: 'Temperature-controlled transport not available',
                });
                continue;
            }

            if (totalTransported + product.quantity > transportCapacity) {
                details.push({
                    productId: product.id,
                    status: 'Failed',
                    reason: 'Insufficient transport capacity for this trip',
                });
                continue;
            }

            // Update storage and transport totals
            totalStored += product.quantity;
            totalTransported += product.quantity;

            details.push({
                productId: product.id,
                status: 'Success',
                reason: 'Product stored and transport scheduled successfully',
            });
        } catch (error) {
            details.push({
                productId: product.id || 'Unknown',
                status: 'Error',
                reason: error.message,
            });
        }
    }

    const storageStatus =
        totalStored <= storageCapacity ? 'Success' : 'Failed';
    const transportStatus =
        totalTransported <= transportCapacity ? 'Success' : 'Failed';

    return {
        storageStatus,
        transportStatus,
        details,
    };
}

// Example usage:
const products = [
    { id: '1', name: 'Lipstick', quantity: 50, temperatureSensitive: false },
    { id: '2', name: 'Foundation', quantity: 70, temperatureSensitive: true },
    { id: '3', name: 'Perfume', quantity: 30, temperatureSensitive: false },
];

const fabricareLogistics = {
    storageCapacity: 200,
    transportCapacity: 100,
    temperatureControlledTransport: true,
};

console.log(manageCosmeticsLogistics(products, fabricareLogistics));
```
