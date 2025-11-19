"""
Generated Code Metadata:
========================
Original URL: https://starkenergie.com
Prompt: Write a JavaScript function to simulate the energy savings of switching to LED light bulbs from incandescent bulbs over a year.
Generated: DETERMINISTIC_a4bfdf82a39f5f42
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the energy and cost savings from switching to LED bulbs from incandescent bulbs.
 * @param {number} incandescentWatts - Power consumption of incandescent bulb in watts.
 * @param {number} ledWatts - Power consumption of LED bulb in watts.
 * @param {number} hoursPerDay - Average daily usage in hours.
 * @param {number} daysPerYear - Number of days used per year.
 * @param {number} costPerKwh - Electricity cost per kilowatt-hour in dollars.
 * @param {number} bulbCount - Number of bulbs being replaced.
 * @returns {Object} An object containing energy savings and cost savings details.
 * @throws {Error} If any input parameter is invalid (non-number, negative, etc.).
 */
function calculateLEDSavings(
    incandescentWatts,
    ledWatts,
    hoursPerDay,
    daysPerYear,
    costPerKwh,
    bulbCount
) {
    // Validate input parameters
    if (
        typeof incandescentWatts !== 'number' ||
        typeof ledWatts !== 'number' ||
        typeof hoursPerDay !== 'number' ||
        typeof daysPerYear !== 'number' ||
        typeof costPerKwh !== 'number' ||
        typeof bulbCount !== 'number' ||
        incandescentWatts <= 0 ||
        ledWatts <= 0 ||
        hoursPerDay <= 0 ||
        daysPerYear <= 0 ||
        costPerKwh <= 0 ||
        bulbCount <= 0
    ) {
        throw new Error('All parameters must be positive numbers');
    }

    // Calculate annual energy consumption for both bulb types
    const incandescentKwhPerYear = (incandescentWatts * hoursPerDay * daysPerYear * bulbCount) / 1000;
    const ledKwhPerYear = (ledWatts * hoursPerDay * daysPerYear * bulbCount) / 1000;

    // Calculate savings
    const energySavingsKwh = incandescentKwhPerYear - ledKwhPerYear;
    const costSavings = energySavingsKwh * costPerKwh;

    return {
        incandescentEnergy: incandescentKwhPerYear,
        ledEnergy: ledKwhPerYear,
        energySavings: energySavingsKwh,
        costSavings: costSavings,
        savingsPercentage: (energySavingsKwh / incandescentKwhPerYear) * 100
    };
}

// Example usage:
try {
    const results = calculateLEDSavings(60, 9, 5, 365, 0.12, 10);
    console.log(results);
} catch (error) {
    console.error('Error calculating LED savings:', error.message);
}
```
