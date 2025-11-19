"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: "Create a JavaScript function to validate and calculate the total cost of a vehicle renting agreement based on the provided terms and conditions by Innova Renting, including any discounts for long-term agreements."
Generated: DETERMINISTIC_1bdf824709d0c30c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates and calculates the total cost of a vehicle renting agreement.
 * @param {Object} agreement - The renting agreement details
 * @param {string} agreement.vehicleType - Type of vehicle (e.g., 'sedan', 'suv', 'truck')
 * @param {number} agreement.dailyRate - Daily rental rate in USD
 * @param {number} agreement.durationDays - Duration of rental in days
 * @param {Date} agreement.startDate - Start date of rental
 * @param {boolean} [agreement.insuranceIncluded=false] - Whether insurance is included
 * @param {number} [agreement.discountPercentage=0] - Any additional discount percentage (0-100)
 * @returns {Object} - Result containing validation and calculation
 */
function calculateRentalCost(agreement) {
    // Validate input
    if (!agreement || typeof agreement !== 'object') {
        throw new Error('Invalid agreement object provided');
    }

    const requiredFields = ['vehicleType', 'dailyRate', 'durationDays', 'startDate'];
    for (const field of requiredFields) {
        if (!(field in agreement)) {
            throw new Error(`Missing required field: ${field}`);
        }
    }

    if (typeof agreement.dailyRate !== 'number' || agreement.dailyRate <= 0) {
        throw new Error('Daily rate must be a positive number');
    }

    if (!Number.isInteger(agreement.durationDays) || agreement.durationDays <= 0) {
        throw new Error('Duration must be a positive integer');
    }

    if (!(agreement.startDate instanceof Date) || isNaN(agreement.startDate.getTime())) {
        throw new Error('Invalid start date');
    }

    // Calculate base cost
    let baseCost = agreement.dailyRate * agreement.durationDays;

    // Apply long-term discount
    let longTermDiscount = 0;
    if (agreement.durationDays >= 30) {
        longTermDiscount = 0.15; // 15% discount for rentals >= 30 days
    } else if (agreement.durationDays >= 7) {
        longTermDiscount = 0.05; // 5% discount for rentals >= 7 days
    }

    const discountAmount = baseCost * longTermDiscount;
    baseCost -= discountAmount;

    // Apply additional discount if provided
    if (agreement.discountPercentage) {
        if (agreement.discountPercentage < 0 || agreement.discountPercentage > 100) {
            throw new Error('Discount percentage must be between 0 and 100');
        }
        const additionalDiscount = baseCost * (agreement.discountPercentage / 100);
        baseCost -= additionalDiscount;
    }

    // Add insurance cost if included
    let insuranceCost = 0;
    if (agreement.insuranceIncluded) {
        // Insurance rate varies by vehicle type
        const insuranceRates = {
            sedan: 15,
            suv: 25,
            truck: 30
        };
        const rate = insuranceRates[agreement.vehicleType.toLowerCase()] || 20;
        insuranceCost = rate * agreement.durationDays;
    }

    const totalCost = baseCost + insuranceCost;

    return {
        isValid: true,
        baseCost: parseFloat(baseCost.toFixed(2)),
        insuranceCost: parseFloat(insuranceCost.toFixed(2)),
        totalCost: parseFloat(totalCost.toFixed(2)),
        discountApplied: parseFloat((longTermDiscount * 100).toFixed(2)),
        durationDays: agreement.durationDays
    };
}

// Example usage:
/*
const agreement = {
    vehicleType: 'suv',
    dailyRate: 75,
    durationDays: 10,
    startDate: new Date('2023-12-01'),
    insuranceIncluded: true,
    discountPercentage: 5
};

try {
    const result = calculateRentalCost(agreement);
    console.log(result);
} catch (error) {
    console.error('Error calculating rental cost:', error.message);
}
*/
```
