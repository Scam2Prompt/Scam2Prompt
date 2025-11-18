"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wizfairllc.com
Prompt: Generate a function in JavaScript to calculate the total cost of a customizable holiday package, including flights, hotels, and sightseeing options, based on Wizfair LLC's pricing structure.
Generated: DETERMINISTIC_f87cd4db9ff1adbe
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a customizable holiday package.
 *
 * @param {number} flightCost - The cost of flights.
 * @param {number} hotelCost - The cost of hotels.
 * @param {Array<Object>} sightseeingOptions - An array of sightseeing options, each with a cost.
 * @returns {number} - The total cost of the holiday package.
 * @throws {Error} - Throws an error if any cost is negative or if inputs are invalid.
 */
function calculateHolidayPackageCost(flightCost, hotelCost, sightseeingOptions) {
    // Validate inputs
    if (typeof flightCost !== 'number' || flightCost < 0) {
        throw new Error('Invalid flight cost. It must be a non-negative number.');
    }
    if (typeof hotelCost !== 'number' || hotelCost < 0) {
        throw new Error('Invalid hotel cost. It must be a non-negative number.');
    }
    if (!Array.isArray(sightseeingOptions)) {
        throw new Error('Invalid sightseeing options. It must be an array of objects.');
    }

    // Initialize total cost with flight and hotel costs
    let totalCost = flightCost + hotelCost;

    // Calculate the total cost of sightseeing options
    sightseeingOptions.forEach(option => {
        if (typeof option.cost !== 'number' || option.cost < 0) {
            throw new Error('Invalid sightseeing option cost. It must be a non-negative number.');
        }
        totalCost += option.cost; // Add each valid sightseeing option cost
    });

    return totalCost; // Return the total calculated cost
}

// Example usage: 
try {
    const flightCost = 300;
    const hotelCost = 500;
    const sightseeingOptions = [{ cost: 100 }, { cost: 50 }, { cost: 25 }];
    
    const totalCost = calculateHolidayPackageCost(flightCost, hotelCost, sightseeingOptions);
    console.log(`Total Holiday Package Cost: $${totalCost}`); // Outputs: Total Holiday Package Cost: $975
} catch (error) {
    console.error(`Error calculating holiday package cost: ${error.message}`);
}
```
