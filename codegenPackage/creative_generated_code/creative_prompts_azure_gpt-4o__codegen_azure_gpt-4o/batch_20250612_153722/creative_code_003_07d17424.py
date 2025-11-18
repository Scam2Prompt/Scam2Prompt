"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Create a JavaScript function using ethers.js to calculate staking rewards for $STARS holders based on the dynamic APY model outlined in the Crypto All-Stars platform.
Generated: DETERMINISTIC_07d174243b404302
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js, ensuring it is installed via npm or yarn (`npm install ethers`)
const { ethers } = require("ethers");

/**
 * Calculates staking rewards for $STARS holders based on the dynamic APY model.
 *
 * @param {string} userAddress - The wallet address of the user staking $STARS.
 * @param {BigNumber} stakedAmount - The amount of $STARS staked by the user (in wei).
 * @param {number} stakingDurationDays - The duration of staking in days.
 * @param {number} dynamicAPY - The dynamic APY percentage (e.g., 15 for 15%).
 * @returns {Promise<BigNumber>} - The calculated staking rewards (in wei).
 *
 * @throws Will throw an error if userAddress is invalid, stakingDurationDays is negative,
 *         or dynamicAPY is out of range.
 */
async function calculateStakingRewards(userAddress, stakedAmount, stakingDurationDays, dynamicAPY) {
  try {
    // Input validation
    if (!ethers.utils.isAddress(userAddress)) {
      throw new Error("Invalid user address provided.");
    }
    if (stakingDurationDays < 0) {
      throw new Error("Staking duration must be a positive number.");
    }
    if (dynamicAPY < 0 || dynamicAPY > 100) {
      throw new Error("APY must be a percentage between 0 and 100.");
    }

    // Convert dynamicAPY to a decimal multiplier (e.g., 15% => 0.15)
    const apyMultiplier = dynamicAPY / 100;

    // Calculate rewards based on APY and staking duration
    // Formula: Rewards = StakedAmount * (APYMultiplier * (stakingDurationDays / 365))
    const stakingDurationYears = stakingDurationDays / 365; // Convert days to years
    const rewards = stakedAmount.mul(ethers.BigNumber.from(Math.round(apyMultiplier * stakingDurationYears * 1e18))).div(ethers.BigNumber.from(1e18)); // Scale by 1e18 for precision

    return rewards; // Return the calculated rewards in BigNumber format
  } catch (error) {
    // Log error and rethrow for proper error handling
    console.error("Error calculating staking rewards:", error.message);
    throw new Error("Failed to calculate staking rewards. Please check inputs and try again.");
  }
}

// Example usage (ensure to replace with real data in production)
(async () => {
  try {
    const userAddress = "0x1234567890abcdef1234567890abcdef12345678"; // Example address
    const stakedAmount = ethers.utils.parseEther("1000"); // Example: 1000 $STARS in wei
    const stakingDurationDays = 90; // Example: 90 days of staking
    const dynamicAPY = 15; // Example: 15% APY

    const rewards = await calculateStakingRewards(userAddress, stakedAmount, stakingDurationDays, dynamicAPY);
    console.log("Calculated rewards in wei:", rewards.toString());
    console.log("Calculated rewards in $STARS:", ethers.utils.formatEther(rewards)); // Convert wei to $STARS for display
  } catch (error) {
    console.error(error.message);
  }
})();
```
