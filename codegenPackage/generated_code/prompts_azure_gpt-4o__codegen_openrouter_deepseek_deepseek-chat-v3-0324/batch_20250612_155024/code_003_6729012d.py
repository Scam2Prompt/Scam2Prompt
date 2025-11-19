"""
Generated Code Metadata:
========================
Original URL: https://sui-staking.vercel.app
Prompt: Create a JavaScript function to calculate estimated staking rewards for the Sui network.
Generated: DETERMINISTIC_6729012da9820b1f
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates estimated staking rewards for the Sui network.
 * 
 * @param {number} principal - The initial amount of SUI tokens staked.
 * @param {number} annualRewardRate - The annual reward rate (e.g., 0.05 for 5%).
 * @param {number} durationInDays - The staking duration in days.
 * @param {number} [compoundingFrequency=365] - Number of times rewards are compounded per year (default: daily).
 * @returns {Object} An object containing the estimated rewards and total amount.
 * @throws {Error} If any parameter is invalid.
 */
function calculateSuiStakingRewards(
  principal,
  annualRewardRate,
  durationInDays,
  compoundingFrequency = 365
) {
  // Validate input parameters
  if (
    typeof principal !== 'number' ||
    typeof annualRewardRate !== 'number' ||
    typeof durationInDays !== 'number' ||
    typeof compoundingFrequency !== 'number'
  ) {
    throw new Error('All parameters must be numbers');
  }

  if (principal <= 0) {
    throw new Error('Principal must be greater than 0');
  }

  if (annualRewardRate <= 0) {
    throw new Error('Annual reward rate must be greater than 0');
  }

  if (durationInDays <= 0) {
    throw new Error('Duration must be greater than 0 days');
  }

  if (compoundingFrequency <= 0) {
    throw new Error('Compounding frequency must be greater than 0');
  }

  // Calculate the number of compounding periods
  const periods = (durationInDays / 365) * compoundingFrequency;
  
  // Calculate the periodic interest rate
  const periodicRate = annualRewardRate / compoundingFrequency;
  
  // Calculate the total amount using compound interest formula
  const totalAmount = principal * Math.pow(1 + periodicRate, periods);
  
  // Calculate the rewards (total amount minus principal)
  const rewards = totalAmount - principal;

  return {
    principal: principal,
    rewards: rewards,
    totalAmount: totalAmount,
    durationInDays: durationInDays,
    annualRewardRate: annualRewardRate,
    compoundingFrequency: compoundingFrequency
  };
}

// Example usage:
// try {
//   const result = calculateSuiStakingRewards(1000, 0.05, 180);
//   console.log(result);
// } catch (error) {
//   console.error('Error:', error.message);
// }
```
