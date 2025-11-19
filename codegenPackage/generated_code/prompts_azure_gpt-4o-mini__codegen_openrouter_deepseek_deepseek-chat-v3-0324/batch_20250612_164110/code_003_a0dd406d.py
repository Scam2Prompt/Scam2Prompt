"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: Develop a JavaScript function to calculate the optimal concentration of menthol for use in dental creams, inspired by the product applications listed on YSC's webpage.
Generated: DETERMINISTIC_a0dd406debaa914b
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the optimal concentration of menthol for dental creams based on given parameters.
 * Inspired by YSC's product applications.
 * 
 * @param {number} baseConcentration - The base concentration of menthol (percentage).
 * @param {Object} preferences - User preferences for sensory attributes.
 * @param {number} preferences.coolingEffect - Desired cooling effect intensity (1-10).
 * @param {number} preferences.mintiness - Desired mint flavor intensity (1-10).
 * @param {number} preferences.sensitivity - User sensitivity level (1-10, 10 being most sensitive).
 * @returns {number} Optimal menthol concentration (percentage).
 * @throws {Error} If invalid parameters are provided.
 */
function calculateOptimalMentholConcentration(baseConcentration, preferences) {
    // Validate input parameters
    if (typeof baseConcentration !== 'number' || baseConcentration < 0 || baseConcentration > 100) {
        throw new Error('Base concentration must be a number between 0 and 100');
    }

    if (!preferences || 
        typeof preferences.coolingEffect !== 'number' || 
        typeof preferences.mintiness !== 'number' || 
        typeof preferences.sensitivity !== 'number') {
        throw new Error('Preferences object must contain coolingEffect, mintiness, and sensitivity properties');
    }

    const { coolingEffect, mintiness, sensitivity } = preferences;

    if ([coolingEffect, mintiness, sensitivity].some(val => val < 1 || val > 10)) {
        throw new Error('Preference values must be between 1 and 10');
    }

    // Calculate adjustment factors
    const coolingFactor = coolingEffect / 5; // Normalize to ~0.2-2 range
    const mintinessFactor = mintiness / 10;  // Normalize to 0.1-1 range
    const sensitivityFactor = 1 - (sensitivity / 20); // More sensitive = lower concentration

    // Calculate optimal concentration with bounds checking
    let optimalConcentration = baseConcentration * coolingFactor * mintinessFactor * sensitivityFactor;

    // Ensure result is within safe and effective bounds (0.1% to 2.5% typical for dental creams)
    optimalConcentration = Math.max(0.1, Math.min(optimalConcentration, 2.5));

    // Round to 2 decimal places for precision
    return parseFloat(optimalConcentration.toFixed(2));
}

// Example usage:
// try {
//     const optimal = calculateOptimalMentholConcentration(1.5, {
//         coolingEffect: 7,
//         mintiness: 8,
//         sensitivity: 3
//     });
//     console.log(`Optimal menthol concentration: ${optimal}%`);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
