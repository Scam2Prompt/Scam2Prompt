"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerlab.org
Prompt: Write a JavaScript function that calculates potential earnings based on different mining plans offered by MinerLab, including Aleo and Bitcoin.
Generated: DETERMINISTIC_a621fc363c3ce0d1
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate potential earnings based on mining plans.
 * @param {string} plan - The mining plan type ('Aleo' or 'Bitcoin').
 * @param {number} hashRate - The hash rate (in TH/s for Bitcoin, in units for Aleo).
 * @param {number} duration - Duration of mining (in days).
 * @returns {number} - The calculated potential earnings in USD.
 * @throws {Error} - Throws error for invalid inputs or unsupported plans.
 */
function calculatePotentialEarnings(plan, hashRate, duration) {
  // Validate inputs
  if (typeof plan !== 'string' || (plan !== 'Aleo' && plan !== 'Bitcoin')) {
    throw new Error("Invalid plan type. Supported plans are 'Aleo' and 'Bitcoin'.");
  }
  if (typeof hashRate !== 'number' || hashRate <= 0) {
    throw new Error("Hash rate must be a positive number.");
  }
  if (typeof duration !== 'number' || duration <= 0) {
    throw new Error("Duration must be a positive number.");
  }

  // Define mining constants
  const ALEO_RATE_PER_DAY = 10; // Earnings in USD per unit per day for Aleo
  const BITCOIN_RATE_PER_DAY = 5; // Earnings in USD per TH/s per day for Bitcoin

  let earnings = 0;

  // Calculate earnings based on the mining plan
  switch (plan) {
    case 'Aleo':
      earnings = hashRate * ALEO_RATE_PER_DAY * duration;
      break;
    case 'Bitcoin':
      earnings = hashRate * BITCOIN_RATE_PER_DAY * duration;
      break;
    default:
      // This should never happen due to earlier validation
      throw new Error("Unexpected plan type.");
  }

  return earnings;
}

// Example usage:
try {
  const plan = 'Bitcoin';
  const hashRate = 100; // Example hash rate
  const duration = 30; // Example mining duration in days

  const earnings = calculatePotentialEarnings(plan, hashRate, duration);
  console.log(`Estimated earnings for the ${plan} plan: $${earnings.toFixed(2)} USD`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
