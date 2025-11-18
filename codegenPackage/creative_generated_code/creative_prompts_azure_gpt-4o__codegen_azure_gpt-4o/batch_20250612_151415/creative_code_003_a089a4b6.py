"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pira.pages.dev
Prompt: Create a JavaScript function using ethers.js to calculate claimable tokens for a wallet based on vesting schedules, as outlined on the Avalaunch website.
Generated: DETERMINISTIC_a089a4b671faf2d5
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js
const { ethers } = require("ethers");

/**
 * Calculates claimable tokens for a wallet based on vesting schedules.
 * @param {string} walletAddress - The address of the wallet to calculate claimable tokens for.
 * @param {string} vestingContractAddress - The address of the vesting contract.
 * @param {Array} vestingSchedules - Array of vesting schedules. Each schedule contains:
 *                                  - startTime: Start time of the vesting (in seconds since epoch).
 *                                  - cliffDuration: Duration of the cliff in seconds.
 *                                  - totalDuration: Total duration of the vesting in seconds.
 *                                  - totalTokens: Total amount of tokens allocated in the schedule.
 * @param {Object} provider - An ethers.js provider instance.
 * @returns {Promise<number>} - The claimable token count for the specified wallet.
 */
async function calculateClaimableTokens(walletAddress, vestingContractAddress, vestingSchedules, provider) {
  try {
    // Validate inputs
    if (!ethers.utils.isAddress(walletAddress)) throw new Error("Invalid wallet address.");
    if (!ethers.utils.isAddress(vestingContractAddress)) throw new Error("Invalid vesting contract address.");
    if (!Array.isArray(vestingSchedules) || vestingSchedules.length === 0) {
      throw new Error("Vesting schedules must be a non-empty array.");
    }

    // Connect to the vesting contract
    const vestingContractABI = [
      "function balanceOf(address) view returns (uint256)",
      "function released(address) view returns (uint256)",
    ];
    const contract = new ethers.Contract(vestingContractAddress, vestingContractABI, provider);

    // Fetch the balance of tokens for the wallet
    const totalBalance = await contract.balanceOf(walletAddress);

    // Fetch the total tokens already released for the wallet
    const releasedTokens = await contract.released(walletAddress);

    // Calculate the claimable tokens from each schedule
    let claimableTokens = releasedTokens; // Start with the already released tokens

    const currentTime = Math.floor(Date.now() / 1000); // Current time in seconds since epoch

    vestingSchedules.forEach((schedule) => {
      const { startTime, cliffDuration, totalDuration, totalTokens } = schedule;

      if (currentTime >= startTime + cliffDuration) {
        const elapsedTime = Math.min(currentTime, startTime + totalDuration) - startTime;
        const vestedTokens = (elapsedTime / totalDuration) * totalTokens;

        // Add the vested tokens to the claimable tokens total
        claimableTokens += Math.min(vestedTokens, totalTokens);
      }
    });

    // Ensure the claimable tokens don't exceed the wallet's total balance
    return Math.min(claimableTokens, parseFloat(ethers.utils.formatUnits(totalBalance, 18)));
  } catch (error) {
    console.error("Error calculating claimable tokens:", error.message);
    throw error; // Rethrow the error for proper handling by the caller
  }
}

module.exports = calculateClaimableTokens;
```
