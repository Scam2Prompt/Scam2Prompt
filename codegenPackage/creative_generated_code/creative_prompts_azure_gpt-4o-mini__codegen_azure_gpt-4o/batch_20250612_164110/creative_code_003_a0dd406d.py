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
 * Calculate the optimal concentration of menthol for use in dental creams.
 * The formula is inspired by product applications from YSC's webpage.
 *
 * The function considers general parameters such as:
 * - Minimum and maximum permissible menthol concentrations.
 * - User preferences (if provided).
 * - Safety margins.
 * 
 * @param {number} baseConcentration - Recommended base concentration (percentage).
 * @param {number} userPreference - User preferred concentration (percentage). Optional.
 * @returns {string} - Optimal concentration percentage or an error message.
 */
function calculateOptimalMentholConcentration(baseConcentration, userPreference = null) {
  try {
    // Define constants for permissible concentration range (in percentage)
    const MIN_CONCENTRATION = 1;   // Minimum safe concentration
    const MAX_CONCENTRATION = 5;   // Maximum safe concentration

    // Validate the base concentration
    if (typeof baseConcentration !== 'number' || baseConcentration < MIN_CONCENTRATION || baseConcentration > MAX_CONCENTRATION) {
      throw new Error(
        `Base concentration must be a number between ${MIN_CONCENTRATION} and ${MAX_CONCENTRATION}.`
      );
    }

    // If user preference is provided, validate it
    if (userPreference !== null) {
      if (typeof userPreference !== 'number' || userPreference < MIN_CONCENTRATION || userPreference > MAX_CONCENTRATION) {
        throw new Error(
          `User preference must be a number between ${MIN_CONCENTRATION} and ${MAX_CONCENTRATION}.`
        );
      }
    }

    // Calculate the optimal concentration
    let optimalConcentration;

    if (userPreference !== null) {
      // Use average of base and user preference, ensuring it stays within safe bounds
      optimalConcentration = Math.min(
        Math.max(
          (baseConcentration + userPreference) / 2, 
          MIN_CONCENTRATION
        ), 
        MAX_CONCENTRATION
      );
    } else {
      // If no user preference is provided, default to the base concentration
      optimalConcentration = baseConcentration;
    }

    // Return the formatted result
    return `The optimal concentration of menthol for dental cream is ${optimalConcentration.toFixed(2)}%.`;

  } catch (error) {
    // Handle errors gracefully by returning a meaningful message
    return `Error calculating optimal concentration: ${error.message}`;
  }
}

// Example usage:
console.log(calculateOptimalMentholConcentration(3)); // Without user preference
console.log(calculateOptimalMentholConcentration(3, 4)); // With user preference
console.log(calculateOptimalMentholConcentration(6)); // Invalid input
```
