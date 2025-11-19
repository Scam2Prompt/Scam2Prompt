"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Develop a JavaScript function to calculate the optimal concentration of menthol for use in dental creams, inspired by the product applications listed on YSC's webpage.
Generated: DETERMINISTIC_a0dd406debaa914b
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the optimal concentration of menthol for dental creams.
 * 
 * @param {number} baseConcentration - The base concentration of menthol (in percentage).
 * @param {number} maxConcentration - The maximum allowed concentration of menthol (in percentage).
 * @param {number} userPreference - User's preferred concentration level (in percentage).
 * @returns {number} - The optimal menthol concentration for the dental cream.
 * @throws {Error} - Throws an error if inputs are not within expected ranges.
 */
function calculateOptimalMentholConcentration(baseConcentration, maxConcentration, userPreference) {
    // Validate inputs
    if (typeof baseConcentration !== 'number' || typeof maxConcentration !== 'number' || typeof userPreference !== 'number') {
        throw new Error('All inputs must be numbers.');
    }
    
    if (baseConcentration < 0 || baseConcentration > 100) {
        throw new Error('Base concentration must be between 0 and 100.');
    }

    if (maxConcentration <= baseConcentration || maxConcentration > 100) {
        throw new Error('Max concentration must be greater than base concentration and less than or equal to 100.');
    }

    if (userPreference < baseConcentration || userPreference > maxConcentration) {
        throw new Error('User preference must be between base concentration and max concentration.');
    }

    // Calculate the optimal concentration
    const optimalConcentration = Math.min(userPreference, maxConcentration);
    
    return optimalConcentration;
}

// Example usage
try {
    const baseConcentration = 1; // Base menthol concentration
    const maxConcentration = 5; // Maximum concentration allowed
    const userPreference = 3; // User's preferred concentration

    const optimalConcentration = calculateOptimalMentholConcentration(baseConcentration, maxConcentration, userPreference);
    console.log(`The optimal menthol concentration for the dental cream is: ${optimalConcentration}%`);
} catch (error) {
    console.error(`Error calculating optimal concentration: ${error.message}`);
}
```
