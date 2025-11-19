"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-alainetwork.pages.dev
Prompt: Write a JavaScript function that calculates the potential earnings from staking $USDT on the ALAI Network based on the tiered APY rates provided.
Generated: DETERMINISTIC_ae3bb5f72101c1bc
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate potential earnings from staking $USDT on the ALAI Network.
 * The calculation is based on tiered APY rates.
 *
 * @param {number} principal - The amount of $USDT being staked.
 * @param {number} days - The number of days the $USDT will be staked.
 * @returns {number} - The potential earnings in $USDT (rounded to 2 decimal places).
 *
 * Tiered APY Rates:
 * - <= $1000: 5% APY
 * - > $1000 and <= $5000: 7% APY
 * - > $5000: 10% APY
 */

function calculateStakingEarnings(principal, days) {
  // Validate input parameters
  if (typeof principal !== 'number' || principal <= 0) {
    throw new Error('Invalid principal amount. It must be a positive number.');
  }
  if (typeof days !== 'number' || days <= 0) {
    throw new Error('Invalid staking duration. It must be a positive number.');
  }

  // APY Rates based on tiers
  const apyRates = {
    tier1: 0.05, // 5% APY for <= $1000
    tier2: 0.07, // 7% APY for > $1000 and <= $5000
    tier3: 0.10, // 10% APY for > $5000
  };

  let apy;

  // Determine the appropriate APY rate based on the principal
  if (principal <= 1000) {
    apy = apyRates.tier1;
  } else if (principal > 1000 && principal <= 5000) {
    apy = apyRates.tier2;
  } else {
    apy = apyRates.tier3;
  }

  // Calculate the earnings
  const annualEarnings = principal * apy; // Annual earnings based on APY
  const dailyEarnings = annualEarnings / 365; // Divide by 365 to get daily earnings
  const totalEarnings = dailyEarnings * days; // Multiply by number of staking days

  // Return the total earnings rounded to 2 decimal places
  return parseFloat(totalEarnings.toFixed(2));
}

// Example usage:
try {
  const principal = 2000; // Amount being staked ($USDT)
  const days = 30; // Staking duration in days
  const earnings = calculateStakingEarnings(principal, days);
  console.log(`Potential earnings: $${earnings}`);
} catch (error) {
  console.error(error.message);
}
```
