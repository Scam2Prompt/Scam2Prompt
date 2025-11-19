"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: Develop a JavaScript function that dynamically updates the price of the Evening Desert Safari based on selected options like VIP service and additional activities.
Generated: DETERMINISTIC_4ab08b4542c1968c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total price of the Evening Desert Safari based on selected options.
 * 
 * @param {Object} options - Selected options for the Evening Desert Safari.
 * @param {Boolean} options.vipService - Whether VIP service is selected.
 * @param {Array<String>} options.additionalActivities - List of additional activities selected.
 * @param {Number} [options.paxCount=1] - Number of passengers.
 * 
 * @returns {Number} The total price of the Evening Desert Safari.
 */
function calculateEveningDesertSafariPrice(options) {
    // Base price for the Evening Desert Safari
    const basePrice = 50.0;

    // VIP service price
    const vipServicePrice = 20.0;

    // Prices for additional activities
    const additionalActivitiesPrices = {
        'camelRide': 10.0,
        'duneBashing': 15.0,
        'desertCamping': 25.0,
    };

    // Validate input options
    if (!options || typeof options !== 'object') {
        throw new Error('Invalid options provided');
    }

    // Calculate base price with VIP service if selected
    let totalPrice = basePrice;
    if (options.vipService && options.vipService === true) {
        totalPrice += vipServicePrice;
    }

    // Calculate price for additional activities
    if (options.additionalActivities && Array.isArray(options.additionalActivities)) {
        options.additionalActivities.forEach(activity => {
            if (additionalActivitiesPrices[activity]) {
                totalPrice += additionalActivitiesPrices[activity];
            } else {
                console.warn(`Unknown additional activity: ${activity}`);
            }
        });
    }

    // Apply pax count if provided
    if (options.paxCount && typeof options.paxCount === 'number' && options.paxCount > 0) {
        totalPrice *= options.paxCount;
    }

    return totalPrice;
}

// Example usage:
try {
    const options = {
        vipService: true,
        additionalActivities: ['camelRide', 'duneBashing'],
        paxCount: 2,
    };
    const totalPrice = calculateEveningDesertSafariPrice(options);
    console.log(`Total price: $${totalPrice.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
