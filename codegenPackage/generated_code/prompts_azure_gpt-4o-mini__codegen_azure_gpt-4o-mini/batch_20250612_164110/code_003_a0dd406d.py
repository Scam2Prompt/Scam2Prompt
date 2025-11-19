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
 * Calculates the optimal concentration of menthol for use in dental creams.
 * The optimal concentration is determined based on a predefined range and 
 * user-defined parameters that influence the effectiveness and safety of menthol.
 *
 * @param {number} minConcentration - The minimum concentration of menthol (in %).
 * @param {number} maxConcentration - The maximum concentration of menthol (in %).
 * @param {number} userPreference - A user-defined preference value (0 to 1) 
 *                                  that influences the final concentration.
 * @returns {number} - The optimal concentration of menthol (in %).
 * @throws {Error} - Throws an error if input values are out of range or invalid.
 */
function calculateOptimalMentholConcentration(minConcentration, maxConcentration, userPreference) {
    // Validate input parameters
    if (typeof minConcentration !== 'number' || typeof maxConcentration !== 'number' || typeof userPreference !== 'number') {
        throw new Error('All parameters must be numbers.');
    }
    if (minConcentration < 0 || maxConcentration > 100 || minConcentration >= maxConcentration) {
        throw new Error('Concentration values must be between 0 and 100, and min must be less than max.');
    }
    if (userPreference < 0 || userPreference > 1) {
        throw new Error('User preference must be between 0 and 1.');
    }

    // Calculate the range of concentrations
    const concentrationRange = maxConcentration - minConcentration;

    // Calculate the optimal concentration based on user preference
    const optimalConcentration = minConcentration + (concentrationRange * userPreference);

    // Return the optimal concentration rounded to two decimal places
    return parseFloat(optimalConcentration.toFixed(2));
}

// Example usage
try {
    const optimalConcentration = calculateOptimalMentholConcentration(0.5, 2.0, 0.75);
    console.log(`Optimal Menthol Concentration: ${optimalConcentration}%`);
} catch (error) {
    console.error(`Error calculating optimal concentration: ${error.message}`);
}
```
