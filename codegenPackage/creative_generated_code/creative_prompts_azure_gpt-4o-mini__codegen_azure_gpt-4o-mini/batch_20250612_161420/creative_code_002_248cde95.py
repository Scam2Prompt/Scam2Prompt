"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vlaunch-dapp.web.app
Prompt: Generate a JavaScript function that calculates the VPAD rewards based on different lockup durations mentioned on the VLaunch website.
Generated: DETERMINISTIC_248cde95290986f3
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates VPAD rewards based on different lockup durations.
 * 
 * @param {number} lockupDuration - The duration in days for the lockup.
 * @returns {number} - The calculated VPAD rewards.
 * @throws {Error} - Throws an error if the lockup duration is invalid.
 */
function calculateVPADRewards(lockupDuration) {
    // Define reward multipliers based on lockup duration
    const rewardMultipliers = {
        '30': 1.1,  // 30 days lockup gives a 10% bonus
        '60': 1.25, // 60 days lockup gives a 25% bonus
        '90': 1.5   // 90 days lockup gives a 50% bonus
    };

    // Check if the input is a valid number
    if (typeof lockupDuration !== 'number' || lockupDuration <= 0) {
        throw new Error('Invalid lockup duration. It must be a positive number.');
    }

    // Determine the reward multiplier based on the lockup duration
    let multiplier;
    if (lockupDuration in rewardMultipliers) {
        multiplier = rewardMultipliers[lockupDuration];
    } else {
        // No multiplier for durations not in the defined range
        multiplier = 1; // No bonus for undefined durations
    }

    // Base reward value - this should be set according to your system
    const baseReward = 100; // Example base reward

    // Calculate the total rewards based on the multiplier
    const totalRewards = baseReward * multiplier;

    return totalRewards;
}

// Example usage with error handling
try {
    const rewards = calculateVPADRewards(60);
    console.log(`Total VPAD rewards for a 60 days lockup: ${rewards}`);
} catch (error) {
    console.error(error.message);
}
```
