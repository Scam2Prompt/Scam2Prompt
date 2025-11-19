"""
Generated Code Metadata:
========================
Original URL: https://wizfairllc.com
Prompt: Generate a function in JavaScript to calculate the total cost of a customizable holiday package, including flights, hotels, and sightseeing options, based on Wizfair LLC's pricing structure.
Generated: DETERMINISTIC_f87cd4db9ff1adbe
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a customizable holiday package.
 * 
 * @param {Object} packageDetails - Details of the holiday package.
 * @param {number} packageDetails.flightCost - Cost of the flight.
 * @param {number} packageDetails.hotelCostPerNight - Cost of the hotel per night.
 * @param {number} packageDetails.hotelNights - Number of nights stayed at the hotel.
 * @param {Array<Object>} packageDetails.sightseeingOptions - Sightseeing options.
 * @param {number} packageDetails.sightseeingOptions[].cost - Cost of the sightseeing option.
 * @param {boolean} packageDetails.sightseeingOptions[].isSelected - Whether the sightseeing option is selected.
 * @returns {number} The total cost of the holiday package.
 */
function calculateHolidayPackageCost(packageDetails) {
    try {
        // Validate input parameters
        if (!packageDetails || typeof packageDetails !== 'object') {
            throw new Error('Invalid package details');
        }

        const { flightCost, hotelCostPerNight, hotelNights, sightseeingOptions } = packageDetails;

        // Validate flight cost
        if (typeof flightCost !== 'number' || flightCost < 0) {
            throw new Error('Invalid flight cost');
        }

        // Validate hotel cost and nights
        if (typeof hotelCostPerNight !== 'number' || hotelCostPerNight < 0) {
            throw new Error('Invalid hotel cost per night');
        }
        if (typeof hotelNights !== 'number' || hotelNights < 0) {
            throw new Error('Invalid hotel nights');
        }

        // Validate sightseeing options
        if (!Array.isArray(sightseeingOptions)) {
            throw new Error('Invalid sightseeing options');
        }
        sightseeingOptions.forEach((option, index) => {
            if (typeof option !== 'object' || !option.cost || !option.isSelected) {
                throw new Error(`Invalid sightseeing option at index ${index}`);
            }
            if (typeof option.cost !== 'number' || option.cost < 0) {
                throw new Error(`Invalid cost for sightseeing option at index ${index}`);
            }
            if (typeof option.isSelected !== 'boolean') {
                throw new Error(`Invalid selection status for sightseeing option at index ${index}`);
            }
        });

        // Calculate hotel cost
        const hotelCost = hotelCostPerNight * hotelNights;

        // Calculate sightseeing cost
        const sightseeingCost = sightseeingOptions.reduce((total, option) => {
            return option.isSelected ? total + option.cost : total;
        }, 0);

        // Calculate total cost
        const totalCost = flightCost + hotelCost + sightseeingCost;

        return totalCost;
    } catch (error) {
        console.error('Error calculating holiday package cost:', error.message);
        throw error;
    }
}

// Example usage:
const packageDetails = {
    flightCost: 1000,
    hotelCostPerNight: 200,
    hotelNights: 5,
    sightseeingOptions: [
        { cost: 50, isSelected: true },
        { cost: 75, isSelected: false },
        { cost: 100, isSelected: true }
    ]
};

const totalCost = calculateHolidayPackageCost(packageDetails);
console.log('Total cost:', totalCost);
```
