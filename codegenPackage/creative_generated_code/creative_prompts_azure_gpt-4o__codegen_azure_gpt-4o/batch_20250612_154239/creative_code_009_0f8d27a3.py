"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Write a Solidity function for Bulldogito Coin that distributes loyalty rewards to token holders based on their wallet balance and holding duration.
Generated: DETERMINISTIC_0f8d27a371186072
Batch ID: 20250612_154239
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
 * @title BulldogitoCoin Loyalty Rewards
 * @dev A smart contract function for distributing loyalty rewards to token holders
 *      based on their wallet balance and holding duration.
 */
contract BulldogitoCoin {
    // Mapping to store token balances of holders
    mapping(address => uint256) public balances;

    // Mapping to store the timestamp of when tokens were last received by holders
    mapping(address => uint256) public holdingStartTime;

    // Event to log reward distribution
    event RewardDistributed(address indexed holder, uint256 rewardAmount);

    // Modifier to ensure only non-zero balances are eligible for rewards
    modifier onlyTokenHolders(address holder) {
        require(balances[holder] > 0, "Holder must have a non-zero balance to receive rewards");
        _;
    }

    /**
     * @dev Function to distribute rewards to token holders based on their balance and holding duration.
     * @param holder Address of the token holder to distribute rewards.
     * @param rewardPool Total reward pool available for distribution (provided by the caller).
     */
    function distributeRewards(address holder, uint256 rewardPool) external onlyTokenHolders(holder) {
        // Ensure reward pool is a non-zero value
        require(rewardPool > 0, "Reward pool must be greater than zero");

        // Calculate holding duration in days
        uint256 holdingDuration = (block.timestamp - holdingStartTime[holder]) / 1 days;

        // Calculate reward based on balance and holding duration
        uint256 rewardAmount = (balances[holder] * holdingDuration) / 1000;

        // Ensure reward amount does not exceed the available reward pool
        require(rewardAmount <= rewardPool, "Reward amount exceeds available reward pool");

        // Transfer the reward (implementation depends on the actual reward mechanism)
        // For simplicity, we assume a direct transfer to the holder
        // Example: rewardToken.transfer(holder, rewardAmount);

        // Emit an event for the reward distribution
        emit RewardDistributed(holder, rewardAmount);

        // Update the holding start time to reset reward eligibility
        holdingStartTime[holder] = block.timestamp;
    }

    /**
     * @dev Example function to update holder's balance and holding start time.
     * @param holder Address of the token holder.
     * @param amount Amount of tokens to update balance with.
     */
    function updateBalance(address holder, uint256 amount) external {
        // Update balance
        balances[holder] += amount;

        // Update holding start time only if the holder is new
        if (holdingStartTime[holder] == 0) {
            holdingStartTime[holder] = block.timestamp;
        }
    }
}
```
