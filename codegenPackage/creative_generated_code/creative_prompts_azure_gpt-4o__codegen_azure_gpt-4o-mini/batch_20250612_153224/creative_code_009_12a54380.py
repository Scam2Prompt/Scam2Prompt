"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Develop a JavaScript function to calculate the total cost of a dumpster rental based on the pricing details provided for regions like Brampton, Burlington, and Toronto on Purple Dumpster's website.
Generated: DETERMINISTIC_12a543804d3acfc3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a dumpster rental based on the region and rental details.
 * 
 * @param {string} region - The region where the dumpster is being rented. Supported values are 'Brampton', 'Burlington', and 'Toronto'.
 * @param {number} rentalDays - The number of days the dumpster will be rented.
 * @param {number} [additionalItems=0] - The number of additional items to be disposed of (optional).
 * @returns {number} - The total cost of the dumpster rental.
 * @throws {Error} - Throws an error if an invalid region is provided or if rentalDays is not a positive number.
 */
function calculateDumpsterRentalCost(region, rentalDays, additionalItems = 0) {
    // Define pricing details for each region
    const pricingDetails = {
        Brampton: { baseRate: 100, dailyRate: 20, additionalItemRate: 5 },
        Burlington: { baseRate: 120, dailyRate: 25, additionalItemRate: 7 },
        Toronto: { baseRate: 150, dailyRate: 30, additionalItemRate: 10 },
    };

    // Validate input parameters
    if (!pricingDetails[region]) {
        throw new Error('Invalid region provided. Supported regions are: Brampton, Burlington, Toronto.');
    }
    if (typeof rentalDays !== 'number' || rentalDays <= 0) {
        throw new Error('Rental days must be a positive number.');
    }
    if (typeof additionalItems !== 'number' || additionalItems < 0) {
        throw new Error('Additional items must be a non-negative number.');
    }

    // Retrieve pricing details for the selected region
    const { baseRate, dailyRate, additionalItemRate } = pricingDetails[region];

    // Calculate the total cost
    const totalCost = baseRate + (dailyRate * rentalDays) + (additionalItemRate * additionalItems);

    return totalCost;
}

// Example usage:
try {
    const totalCost = calculateDumpsterRentalCost('Brampton', 5, 3);
    console.log(`Total cost for dumpster rental: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
