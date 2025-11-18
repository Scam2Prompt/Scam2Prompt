"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.gtempus.com
Prompt: Create a JavaScript function to calculate insurance premiums based on user inputs such as age, coverage type, and duration, tailored to Grupo de Seguros Tempus's offerings.
Generated: DETERMINISTIC_941fedb5e39d5d7a
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate insurance premiums based on user inputs.
 * Grupo de Seguros Tempus offers the following coverage types:
 * - "basic": Base coverage
 * - "standard": Standard coverage
 * - "premium": Premium coverage
 *
 * @param {number} age - The age of the insured person (must be >= 18).
 * @param {string} coverageType - The type of coverage ("basic", "standard", "premium").
 * @param {number} duration - Duration in years (1-30 years).
 * @returns {number} - The calculated premium amount in USD.
 * @throws {Error} - Throws error for invalid inputs.
 */
function calculateInsurancePremium(age, coverageType, duration) {
  // Validate inputs
  if (typeof age !== 'number' || age < 18) {
    throw new Error('Invalid age. Age must be a number and at least 18.');
  }
  if (!['basic', 'standard', 'premium'].includes(coverageType)) {
    throw new Error('Invalid coverage type. Must be "basic", "standard", or "premium".');
  }
  if (typeof duration !== 'number' || duration < 1 || duration > 30) {
    throw new Error('Invalid duration. Duration must be a number between 1 and 30 years.');
  }

  // Base premium rate per year per age group (in USD)
  const baseRates = {
    basic: 50,
    standard: 100,
    premium: 150,
  };

  // Age adjustment multiplier
  const ageMultiplier = age >= 18 && age <= 25 ? 1.2 :
                        age >= 26 && age <= 40 ? 1.5 :
                        age >= 41 && age <= 60 ? 1.8 :
                        2.5; // Age > 60

  // Calculate total premium
  const baseRate = baseRates[coverageType];
  const totalPremium = baseRate * ageMultiplier * duration;

  // Round to two decimal places and return
  return parseFloat(totalPremium.toFixed(2));
}

// Example usage (uncomment to run):
// try {
//   const premium = calculateInsurancePremium(30, 'standard', 10);
//   console.log(`The premium amount is $${premium}`);
// } catch (error) {
//   console.error(`Error: ${error.message}`);
// }
```
