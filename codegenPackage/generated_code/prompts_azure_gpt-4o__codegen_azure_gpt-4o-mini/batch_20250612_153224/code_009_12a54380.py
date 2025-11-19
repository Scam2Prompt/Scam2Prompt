"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Develop a JavaScript function to calculate the total cost of a dumpster rental based on the pricing details provided for regions like Brampton, Burlington, and Toronto on Purple Dumpster's website.
Generated: DETERMINISTIC_12a543804d3acfc3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a dumpster rental based on the region and rental details.
 * 
 * @param {string} region - The region for the dumpster rental (e.g., 'Brampton', 'Burlington', 'Toronto').
 * @param {number} days - The number of days for the rental.
 * @param {number} size - The size of the dumpster in cubic yards.
 * @returns {number} - The total cost of the dumpster rental.
 * @throws {Error} - Throws an error if the region is invalid or if the input values are not positive numbers.
 */
function calculateDumpsterRentalCost(region, days, size) {
    // Pricing details for each region
    const pricing = {
        Brampton: { baseRate: 300, dailyRate: 20 },
        Burlington: { baseRate: 350, dailyRate: 25 },
        Toronto: { baseRate: 400, dailyRate: 30 }
    };

    // Validate input parameters
    if (!pricing[region]) {
        throw new Error(`Invalid region: ${region}. Please choose from Brampton, Burlington, or Toronto.`);
    }
    if (typeof days !== 'number' || days <= 0) {
        throw new Error('Invalid number of days. It must be a positive number.');
    }
    if (typeof size !== 'number' || size <= 0) {
        throw new Error('Invalid dumpster size. It must be a positive number.');
    }

    // Calculate total cost
    const { baseRate, dailyRate } = pricing[region];
    const totalCost = baseRate + (dailyRate * days);

    return totalCost;
}

// Example usage
try {
    const totalCost = calculateDumpsterRentalCost('Brampton', 5, 10);
    console.log(`Total cost for the dumpster rental: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
