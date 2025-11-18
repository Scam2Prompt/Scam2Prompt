"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Develop a function in JavaScript that calculates insurance premiums for KEK Insurance Brokers, factoring in policy types like motor insurance and life assurance as described on their website.
Generated: DETERMINISTIC_af114da8bd379a36
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the insurance premium based on policy type and other factors.
 * @param {string} policyType - Type of insurance policy ('motor' or 'life').
 * @param {number} basePremium - The base premium amount in USD.
 * @param {Object} factors - Additional factors affecting premium calculation.
 * @param {number} factors.age - Age of the insured person (applies to 'life' policy).
 * @param {number} factors.vehicleValue - Value of the vehicle in USD (applies to 'motor' policy).
 * @param {boolean} factors.hasAccidents - Whether the individual has prior accidents (applies to 'motor' policy).
 * @returns {number} - The calculated insurance premium.
 * @throws {Error} Throws an error if policyType is invalid or required factors are missing.
 */
function calculateInsurancePremium(policyType, basePremium, factors) {
  // Validate inputs
  if (typeof policyType !== 'string' || typeof basePremium !== 'number' || typeof factors !== 'object') {
    throw new Error('Invalid input parameters.');
  }

  if (basePremium <= 0) {
    throw new Error('Base premium must be greater than zero.');
  }

  let finalPremium = basePremium;

  switch (policyType.toLowerCase()) {
    case 'motor':
      // Ensure required factors for motor insurance are provided
      if (typeof factors.vehicleValue !== 'number' || typeof factors.hasAccidents !== 'boolean') {
        throw new Error('Missing or invalid factors for motor insurance.');
      }

      // Add percentage based on vehicle value
      finalPremium += factors.vehicleValue * 0.02; // 2% of vehicle value

      // Increase premium for prior accidents
      if (factors.hasAccidents) {
        finalPremium *= 1.25; // 25% increase for accidents
      }
      break;

    case 'life':
      // Ensure required factors for life assurance are provided
      if (typeof factors.age !== 'number' || factors.age <= 0) {
        throw new Error('Missing or invalid age for life assurance.');
      }

      // Risk factor based on age
      if (factors.age < 25) {
        finalPremium *= 1.1; // 10% increase for age under 25
      } else if (factors.age > 50) {
        finalPremium *= 1.4; // 40% increase for age over 50
      }
      break;

    default:
      throw new Error('Invalid policy type. Accepted values are "motor" and "life".');
  }

  // Return the calculated premium rounded to two decimal places
  return parseFloat(finalPremium.toFixed(2));
}

// Example usage:
try {
  const premium = calculateInsurancePremium('motor', 500, {
    vehicleValue: 20000,
    hasAccidents: true,
  });
  console.log('Calculated Premium:', premium); // Output: Calculated Premium: 1250
} catch (error) {
  console.error('Error:', error.message);
}
```
