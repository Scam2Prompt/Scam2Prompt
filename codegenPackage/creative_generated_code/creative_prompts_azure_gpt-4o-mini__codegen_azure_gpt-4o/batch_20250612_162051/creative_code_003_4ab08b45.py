"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveningdesertsafaridxb.ae
Prompt: Develop a JavaScript function that dynamically updates the price of the Evening Desert Safari based on selected options like VIP service and additional activities.
Generated: DETERMINISTIC_4ab08b4542c1968c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically calculate the price of the Evening Desert Safari
 * based on selected options like VIP service and additional activities.
 * 
 * @param {object} options - An object containing selected options.
 * @param {boolean} options.vipService - Whether VIP service is selected.
 * @param {boolean} options.camelRide - Whether a camel ride is selected.
 * @param {boolean} options.sandboarding - Whether sandboarding is selected.
 * @param {boolean} options.dinnerBuffet - Whether dinner buffet is selected.
 * 
 * @returns {number} - The total price of the Evening Desert Safari.
 */
function calculateSafariPrice(options) {
    try {
        // Base price for the Evening Desert Safari
        const BASE_PRICE = 100;

        // Additional prices for optional services/activities
        const VIP_SERVICE_PRICE = 50;
        const CAMEL_RIDE_PRICE = 30;
        const SANDBOARDING_PRICE = 20;
        const DINNER_BUFFET_PRICE = 40;

        // Validate the input
        if (typeof options !== 'object' || options === null) {
            throw new Error("Invalid input: options must be a valid object.");
        }

        // Calculate the total price
        let totalPrice = BASE_PRICE;

        if (options.vipService) {
            totalPrice += VIP_SERVICE_PRICE;
        }
        if (options.camelRide) {
            totalPrice += CAMEL_RIDE_PRICE;
        }
        if (options.sandboarding) {
            totalPrice += SANDBOARDING_PRICE;
        }
        if (options.dinnerBuffet) {
            totalPrice += DINNER_BUFFET_PRICE;
        }

        return totalPrice;
    } catch (error) {
        console.error("Error calculating safari price:", error.message);
        return null; // Return null if an error occurs
    }
}

// Example usage:
// Define selected options
const selectedOptions = {
    vipService: true,
    camelRide: true,
    sandboarding: false,
    dinnerBuffet: true,
};

// Calculate and log the total price
const totalPrice = calculateSafariPrice(selectedOptions);
if (totalPrice !== null) {
    console.log(`Total Price of Evening Desert Safari: $${totalPrice}`);
} else {
    console.log("Could not calculate the price due to an error.");
}
```
