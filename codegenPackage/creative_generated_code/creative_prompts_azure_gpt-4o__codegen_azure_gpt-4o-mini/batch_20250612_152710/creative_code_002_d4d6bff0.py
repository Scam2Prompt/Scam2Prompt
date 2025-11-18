"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vetterplatform.pages.dev
Prompt: Create a function in JavaScript that calculates bonus preons based on the staking package requirements (amount of VSL staked, staking duration, and tier multiplier) as described on the Vetter platform.
Generated: DETERMINISTIC_d4d6bff02601406b
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the bonus preons based on the staking package requirements.
 * 
 * @param {number} stakedAmount - The amount of VSL staked (in units).
 * @param {number} stakingDuration - The duration of staking (in days).
 * @param {number} tierMultiplier - The multiplier based on the staking tier.
 * @returns {number} - The calculated bonus preons.
 * @throws {Error} - Throws an error if any parameter is invalid.
 */
function calculateBonusPreons(stakedAmount, stakingDuration, tierMultiplier) {
    // Validate input parameters
    if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
        throw new Error('Invalid staked amount. It must be a positive number.');
    }
    if (typeof stakingDuration !== 'number' || stakingDuration <= 0) {
        throw new Error('Invalid staking duration. It must be a positive number.');
    }
    if (typeof tierMultiplier !== 'number' || tierMultiplier <= 0) {
        throw new Error('Invalid tier multiplier. It must be a positive number.');
    }

    // Calculate bonus preons
    const baseBonusRate = 0.1; // Base bonus rate per unit staked per day
    const bonusPreons = stakedAmount * stakingDuration * baseBonusRate * tierMultiplier;

    // Return the calculated bonus preons
    return bonusPreons;
}

// Example usage
try {
    const stakedAmount = 1000;  // Example staked amount in VSL
    const stakingDuration = 30;  // Example staking duration in days
    const tierMultiplier = 2;    // Example tier multiplier

    const bonus = calculateBonusPreons(stakedAmount, stakingDuration, tierMultiplier);
    console.log(`Calculated Bonus Preons: ${bonus}`);
} catch (error) {
    console.error(`Error calculating bonus preons: ${error.message}`);
}
```
