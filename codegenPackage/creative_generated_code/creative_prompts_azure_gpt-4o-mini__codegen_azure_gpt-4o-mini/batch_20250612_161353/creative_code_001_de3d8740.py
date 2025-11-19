"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: Write a JavaScript function to calculate potential earnings based on the lock duration and amount of HMZ tokens staked.
Generated: DETERMINISTIC_de3d8740bfcb21f0
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential earnings based on lock duration and amount of HMZ tokens staked.
 * 
 * @param {number} amountStaked - The amount of HMZ tokens staked.
 * @param {number} lockDuration - The duration for which tokens are locked, in days.
 * @param {number} dailyEarningRate - The daily earning rate as a percentage (e.g., 0.05 for 5%).
 * @returns {number} The total potential earnings after the lock duration.
 * @throws {Error} Throws an error if the inputs are not valid numbers or if they are less than or equal to zero.
 */
function calculatePotentialEarnings(amountStaked, lockDuration, dailyEarningRate) {
    // Input validation
    if (typeof amountStaked !== 'number' || amountStaked <= 0) {
        throw new Error('Amount staked must be a positive number.');
    }
    if (typeof lockDuration !== 'number' || lockDuration <= 0) {
        throw new Error('Lock duration must be a positive number.');
    }
    if (typeof dailyEarningRate !== 'number' || dailyEarningRate < 0) {
        throw new Error('Daily earning rate must be a non-negative number.');
    }

    // Calculate total earnings
    const totalEarnings = amountStaked * (dailyEarningRate / 100) * lockDuration;

    return totalEarnings;
}

// Example usage (uncomment to use):
// try {
//     const earnings = calculatePotentialEarnings(1000, 30, 5);
//     console.log(`Potential Earnings: ${earnings} HMZ`);
// } catch (error) {
//     console.error(error.message);
// }
```
