"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewardclaimdapp.pages.dev
Prompt: Write a Solidity smart contract function to calculate claimable rewards based on the last epoch APY, similar to the reward structure described on Redacted's dApp.
Generated: DETERMINISTIC_120fabc12719b83c
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title RewardCalculator
 * @dev Smart contract to calculate claimable rewards based on APY from the last epoch.
 */
contract RewardCalculator {
    // State variables
    uint256 public lastEpochAPY; // Annual Percentage Yield for the last epoch (e.g., in basis points, 5000 = 50.00%)
    uint256 public constant BASIS_POINTS_DIVISOR = 10000; // Divides APY to calculate percentage
    uint256 public constant SECONDS_IN_YEAR = 31536000; // Number of seconds in a year

    mapping(address => uint256) public userStakedBalance; // Tracks staked balances for each user
    mapping(address => uint256) public lastClaimTimestamp; // Tracks last claim timestamp per user

    /**
     * @dev Updates the APY for the last epoch. Callable only by the contract owner.
     * @param _apy The last epoch APY in basis points (e.g., 5000 = 50.00%).
     */
    function updateLastEpochAPY(uint256 _apy) external {
        // NOTE: Add access control here for owner-only functionality
        lastEpochAPY = _apy;
    }

    /**
     * @dev Updates the user’s staked balance. Simulates staking. Callable by anyone.
     * @param _amount The amount the user has staked.
     */
    function updateStakedBalance(address _user, uint256 _amount) external {
        userStakedBalance[_user] = _amount;
        lastClaimTimestamp[_user] = block.timestamp; // Reset last claim timestamp
    }

    /**
     * @dev Calculates claimable rewards for a user based on their staked balance and elapsed time.
     * @param _user The address of the user.
     * @return claimableRewards The amount of claimable rewards for the user.
     */
    function calculateClaimableRewards(address _user) public view returns (uint256 claimableRewards) {
        // Ensure the user has a staked balance
        uint256 stakedBalance = userStakedBalance[_user];
        require(stakedBalance > 0, "No staked balance found for user");

        // Time elapsed since last claim
        uint256 timeElapsed = block.timestamp - lastClaimTimestamp[_user];

        // Calculate rewards based on APY, staked balance, and time elapsed
        claimableRewards = (stakedBalance * lastEpochAPY * timeElapsed) / (BASIS_POINTS_DIVISOR * SECONDS_IN_YEAR);
    }

    /**
     * @dev Allows the user to claim their rewards. Updates the last claim timestamp.
     */
    function claimRewards() external {
        uint256 rewards = calculateClaimableRewards(msg.sender);

        // Ensure rewards are greater than 0
        require(rewards > 0, "No rewards available to claim");

        // Update last claim timestamp
        lastClaimTimestamp[msg.sender] = block.timestamp;

        // Transfer rewards (placeholder logic; actual implementation depends on reward token)
        // NOTE: Add token transfer logic here
    }
}
```
