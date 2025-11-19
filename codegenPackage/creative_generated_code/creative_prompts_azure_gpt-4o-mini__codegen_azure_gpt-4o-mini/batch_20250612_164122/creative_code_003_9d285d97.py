"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Create a JavaScript function that calculates rush charges for environmental testing based on A & B Labs' pricing structure.
Generated: DETERMINISTIC_9d285d97c6d52c3a
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates rush charges for environmental testing based on A & B Labs' pricing structure.
 * 
 * @param {number} baseCharge - The base charge for the environmental test.
 * @param {number} rushMultiplier - The multiplier for rush charges. (e.g., 1.5 for 50% more)
 * @param {boolean} isRush - Indicates if the rush charge should be applied.
 * @returns {number} Total charge after applying rush fee if applicable.
 * @throws {Error} Throws an error if baseCharge or rushMultiplier is not a positive number.
 */
function calculateRushCharges(baseCharge, rushMultiplier, isRush) {
    // Validate input parameters
    if (typeof baseCharge !== 'number' || baseCharge < 0) {
        throw new Error('Base charge must be a positive number.');
    }
    if (typeof rushMultiplier !== 'number' || rushMultiplier <= 0) {
        throw new Error('Rush multiplier must be a positive number.');
    }
    if (typeof isRush !== 'boolean') {
        throw new Error('isRush must be a boolean value.');
    }

    // Calculate total charges
    let totalCharge = baseCharge;

    // Apply rush charge if specified
    if (isRush) {
        totalCharge *= rushMultiplier;
    }

    return totalCharge;
}

// Example usage
try {
    const baseCharge = 200; // The base cost of the test
    const rushMultiplier = 1.5; // 50% additional for rush service
    const isRush = true; // Indicating rush service is requested

    const total = calculateRushCharges(baseCharge, rushMultiplier, isRush);
    console.log(`Total charge: $${total.toFixed(2)}`);
} catch (error) {
    console.error('Error calculating charges:', error.message);
}
```
