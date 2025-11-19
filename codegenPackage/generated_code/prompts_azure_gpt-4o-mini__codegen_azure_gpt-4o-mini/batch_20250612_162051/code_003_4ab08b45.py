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
 * Function to update the price of the Evening Desert Safari based on selected options.
 * @param {boolean} isVIP - Indicates if the VIP service is selected.
 * @param {Array<string>} additionalActivities - Array of additional activities selected.
 * @returns {number} - The updated total price for the safari.
 */
function updateSafariPrice(isVIP, additionalActivities) {
    // Base price for the Evening Desert Safari
    const basePrice = 100; // Base price in currency units
    let totalPrice = basePrice;

    // Price adjustment for VIP service
    const vipServicePrice = 50; // Additional cost for VIP service
    if (isVIP) {
        totalPrice += vipServicePrice;
    }

    // Price adjustments for additional activities
    const activityPrices = {
        camelRide: 30,
        sandboarding: 20,
        quadBiking: 40,
        dinner: 25
    };

    // Validate and calculate the price for each selected activity
    additionalActivities.forEach(activity => {
        if (activityPrices.hasOwnProperty(activity)) {
            totalPrice += activityPrices[activity];
        } else {
            console.warn(`Activity "${activity}" is not recognized.`);
        }
    });

    // Return the final calculated price
    return totalPrice;
}

// Example usage
try {
    const isVIP = true; // Example: User selected VIP service
    const selectedActivities = ['camelRide', 'dinner']; // Example: User selected activities
    const finalPrice = updateSafariPrice(isVIP, selectedActivities);
    console.log(`The total price for the Evening Desert Safari is: $${finalPrice}`);
} catch (error) {
    console.error('An error occurred while updating the safari price:', error);
}
```
