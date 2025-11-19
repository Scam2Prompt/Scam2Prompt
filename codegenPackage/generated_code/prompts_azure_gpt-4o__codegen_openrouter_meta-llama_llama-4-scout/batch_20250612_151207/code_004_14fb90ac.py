"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ai-liveclaim.pages.dev
Prompt: Write a Solidity function to calculate staking rewards for $WAI tokens based on the annual percentage yield (APY) of 114%.
Generated: DETERMINISTIC_14fb90ac2c600616
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title StakingRewardsCalculator
 * @author [Your Name]
 * @notice Calculates staking rewards for $WAI tokens based on the annual percentage yield (APY).
 */
contract StakingRewardsCalculator {
    /**
     * @dev Annual percentage yield (APY) for $WAI tokens in basis points (114%).
     */
    uint256 public constant ANNUAL_APY_BASIS_POINTS = 11400;

    /**
     * @dev Calculates the staking rewards for $WAI tokens based on the APY.
     * @param principal The initial amount of $WAI tokens staked.
     * @param timeElapsed The time elapsed in seconds.
     * @return The total rewards earned.
     */
    function calculateStakingRewards(uint256 principal, uint256 timeElapsed) public pure returns (uint256) {
        // Convert APY from basis points to a decimal
        uint256 apyDecimal = ANNUAL_APY_BASIS_POINTS / 10000;

        // Calculate the total seconds in a year
        uint256 secondsInAYear = 365 days * 24 hours * 60 minutes * 60 seconds;

        // Calculate the fraction of the year that has elapsed
        uint256 fractionOfYearElapsed = timeElapsed / secondsInAYear;

        // Calculate the reward
        uint256 reward = (principal * apyDecimal * fractionOfYearElapsed) / 100;

        return reward;
    }

    /**
     * @dev Calculates the total amount of $WAI tokens after staking, including rewards.
     * @param principal The initial amount of $WAI tokens staked.
     * @param timeElapsed The time elapsed in seconds.
     * @return The total amount of $WAI tokens after staking.
     */
    function calculateTotalStakedAmount(uint256 principal, uint256 timeElapsed) public pure returns (uint256) {
        uint256 rewards = calculateStakingRewards(principal, timeElapsed);
        return principal + rewards;
    }
}
```
