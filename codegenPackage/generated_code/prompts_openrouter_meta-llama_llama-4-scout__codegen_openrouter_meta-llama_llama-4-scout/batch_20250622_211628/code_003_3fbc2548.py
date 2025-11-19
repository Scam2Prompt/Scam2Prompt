"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Develop a JavaScript function to calculate the cost of a basketball camp based on the number of campers, similar to L-Zero's camp pricing at Courtside Fitness, and provide a discount for early registration.
Generated: DETERMINISTIC_3fbc25482df103a9
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of a basketball camp based on the number of campers.
 * Provides a discount for early registration.
 */

/**
 * @typedef {Object} CampPricing
 * @property {number} baseCost - The base cost per camper.
 * @property {number} earlyRegistrationDiscount - The discount percentage for early registration.
 * @property {Date} earlyRegistrationDeadline - The deadline for early registration.
 */

/**
 * @typedef {Object} CampDetails
 * @property {number} numCampers - The number of campers.
 * @property {Date} registrationDate - The date of registration.
 */

/**
 * Calculates the cost of a basketball camp.
 * 
 * @param {CampPricing} campPricing - The pricing details for the camp.
 * @param {CampDetails} campDetails - The details of the camp registration.
 * @returns {number} The total cost of the camp.
 */
function calculateCampCost(campPricing, campDetails) {
    // Check if the input parameters are valid
    if (!campPricing || !campDetails) {
        throw new Error('Invalid input parameters');
    }

    // Calculate the base cost
    const baseCost = campPricing.baseCost * campDetails.numCampers;

    // Check if the registration is early
    let discount = 0;
    if (campDetails.registrationDate <= campPricing.earlyRegistrationDeadline) {
        // Apply early registration discount
        discount = baseCost * (campPricing.earlyRegistrationDiscount / 100);
    }

    // Calculate the total cost
    const totalCost = baseCost - discount;

    return totalCost;
}

// Example usage:
const campPricing = {
    baseCost: 100,
    earlyRegistrationDiscount: 10,
    earlyRegistrationDeadline: new Date('2024-09-15')
};

const campDetails = {
    numCampers: 5,
    registrationDate: new Date('2024-09-01')
};

try {
    const totalCost = calculateCampCost(campPricing, campDetails);
    console.log(`The total cost of the camp is: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
