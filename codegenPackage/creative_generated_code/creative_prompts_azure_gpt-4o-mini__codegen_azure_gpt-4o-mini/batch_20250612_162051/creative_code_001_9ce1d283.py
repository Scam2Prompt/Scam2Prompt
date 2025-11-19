"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Write a JavaScript function that calculates the cost of a deep cleaning service based on the size of the home and additional services like fridge and oven cleaning, as described on the Maria HouseKeepers website.
Generated: DETERMINISTIC_9ce1d2831af12b2a
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
 * Calculates the cost of a deep cleaning service based on home size and additional services.
 * 
 * @param {number} size - The size of the home in square feet.
 * @param {boolean} fridgeCleaning - Indicates if fridge cleaning is required.
 * @param {boolean} ovenCleaning - Indicates if oven cleaning is required.
 * @returns {number} - The total cost of the cleaning service.
 * @throws {Error} - Throws an error if size is not a positive number.
 */
function calculateDeepCleaningCost(size, fridgeCleaning = false, ovenCleaning = false) {
    // Base cost per square foot for deep cleaning
    const baseCostPerSquareFoot = 0.25; // Example cost
    // Additional costs for extra services
    const fridgeCleaningCost = 50; // Example cost for fridge cleaning
    const ovenCleaningCost = 50; // Example cost for oven cleaning

    // Validate the input size
    if (typeof size !== 'number' || size <= 0) {
        throw new Error('The size must be a positive number.');
    }

    // Calculate the base cost based on the size of the home
    let totalCost = size * baseCostPerSquareFoot;

    // Add costs for additional services if requested
    if (fridgeCleaning) {
        totalCost += fridgeCleaningCost;
    }
    if (ovenCleaning) {
        totalCost += ovenCleaningCost;
    }

    return totalCost;
}

// Example usage:
try {
    const cost = calculateDeepCleaningCost(1500, true, false);
    console.log(`The total cost for the cleaning service is $${cost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating cleaning cost: ${error.message}`);
}
```
