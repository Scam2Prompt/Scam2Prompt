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
 * Calculate the cost of a deep cleaning service based on home size and additional services.
 * 
 * @param {number} homeSize - The size of the home in square feet.
 * @param {boolean} fridgeCleaning - Whether fridge cleaning is selected (optional, default: false).
 * @param {boolean} ovenCleaning - Whether oven cleaning is selected (optional, default: false).
 * @returns {number} - The total cost of the cleaning service.
 * @throws {Error} - If the home size is invalid or not provided.
 */
function calculateCleaningCost(homeSize, fridgeCleaning = false, ovenCleaning = false) {
    // Validate home size input
    if (typeof homeSize !== 'number' || homeSize <= 0) {
        throw new Error("Invalid home size. Please provide a positive number for the size of the home.");
    }

    // Base cost per square foot
    const costPerSquareFoot = 0.10; // Example: $0.10 per square foot
    const baseCleaningCost = homeSize * costPerSquareFoot;

    // Additional service costs
    const fridgeCleaningCost = 25; // Example: $25 for fridge cleaning
    const ovenCleaningCost = 30; // Example: $30 for oven cleaning

    // Calculate total cost
    let totalCost = baseCleaningCost;
    if (fridgeCleaning) {
        totalCost += fridgeCleaningCost;
    }
    if (ovenCleaning) {
        totalCost += ovenCleaningCost;
    }

    // Return the final cost rounded to two decimal places
    return parseFloat(totalCost.toFixed(2));
}

// Example usage
try {
    const homeSize = 1200; // Example home size in square feet
    const fridgeCleaning = true; // Include fridge cleaning service
    const ovenCleaning = false; // Exclude oven cleaning service

    const totalCost = calculateCleaningCost(homeSize, fridgeCleaning, ovenCleaning);
    console.log(`The total cleaning cost is $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```
