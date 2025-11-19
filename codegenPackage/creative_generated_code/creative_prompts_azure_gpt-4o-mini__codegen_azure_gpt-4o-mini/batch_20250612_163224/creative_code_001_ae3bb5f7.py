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
 * Calculates the potential earnings from staking USDT on the ALAI Network.
 * 
 * @param {number} principal - The amount of USDT to stake.
 * @param {number} duration - The duration in days for which the USDT is staked.
 * @returns {number} - The potential earnings from staking.
 * @throws {Error} - Throws an error if the principal or duration is invalid.
 */
function calculateStakingEarnings(principal, duration) {
    // Validate the input parameters
    if (typeof principal !== 'number' || principal <= 0) {
        throw new Error('Principal must be a positive number.');
    }
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Duration must be a positive number.');
    }

    // Define tiered APY rates based on staking duration
    const apyRates = [
        { maxDays: 30, rate: 0.05 }, // 5% APY for up to 30 days
        { maxDays: 90, rate: 0.07 }, // 7% APY for up to 90 days
        { maxDays: 180, rate: 0.1 }, // 10% APY for up to 180 days
        { maxDays: Infinity, rate: 0.12 } // 12% APY for more than 180 days
    ];

    // Determine the appropriate APY rate based on the duration
    let apy = 0;
    for (const tier of apyRates) {
        if (duration <= tier.maxDays) {
            apy = tier.rate;
            break;
        }
    }

    // Calculate potential earnings
    const earnings = principal * apy * (duration / 365);
    return parseFloat(earnings.toFixed(2)); // Return earnings rounded to two decimal places
}

// Example usage:
try {
    const stakeAmount = 1000; // Amount in USDT
    const stakeDuration = 60;  // Duration in days
    const earnings = calculateStakingEarnings(stakeAmount, stakeDuration);
    console.log(`Potential earnings from staking $${stakeAmount} USDT for ${stakeDuration} days: $${earnings}`);
} catch (error) {
    console.error(error.message);
}
```
