"""
Generated Code Metadata:
========================
Original URL: https://bonkrewards-6st.pages.dev
Prompt: Generate a smart contract code in Solidity to implement a similar rewards system with dynamic multipliers based on lock duration.
Generated: DETERMINISTIC_94d1071e8b6f8e1b
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title RewardsSystem
 * @dev A smart contract to implement a rewards system with dynamic multipliers based on lock duration.
 */
contract RewardsSystem {
    // Struct to store user stake information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lockDuration; // Lock duration in seconds
        uint256 startTime; // Timestamp when the stake was created
    }

    // Mapping to store stakes for each user
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 lockDuration);

    // Event emitted when a user withdraws their stake and rewards
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Token multiplier based on lock duration (in seconds)
    // Example: 30 days = 1.2x, 90 days = 1.5x, 180 days = 2x
    mapping(uint256 => uint256) public multipliers;

    // Constructor to initialize multipliers
    constructor() {
        multipliers[30 days] = 120; // 1.2x multiplier (120%)
        multipliers[90 days] = 150; // 1.5x multiplier (150%)
        multipliers[180 days] = 200; // 2x multiplier (200%)
    }

    /**
     * @dev Stake tokens with a specified lock duration.
     * @param amount The amount of tokens to stake.
     * @param lockDuration The lock duration in seconds.
     */
    function stake(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(multipliers[lockDuration] > 0, "Invalid lock duration");

        // Ensure the user does not already have an active stake
        require(stakes[msg.sender].amount == 0, "Active stake exists");

        // Record the stake details
        stakes[msg.sender] = Stake({
            amount: amount,
            lockDuration: lockDuration,
            startTime: block.timestamp
        });

        emit Staked(msg.sender, amount, lockDuration);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards.
     */
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");

        // Ensure the lock duration has passed
        require(
            block.timestamp >= userStake.startTime + userStake.lockDuration,
            "Lock duration not yet completed"
        );

        // Calculate rewards based on the multiplier
        uint256 multiplier = multipliers[userStake.lockDuration];
        uint256 reward = (userStake.amount * multiplier) / 100;

        // Clear the user's stake
        delete stakes[msg.sender];

        emit Withdrawn(msg.sender, userStake.amount, reward);

        // Transfer the staked amount and rewards to the user
        // Note: Replace the following line with actual token transfer logic
        // Example: ERC20(tokenAddress).transfer(msg.sender, userStake.amount + reward);
    }

    /**
     * @dev Get the details of a user's stake.
     * @param user The address of the user.
     * @return amount The amount of tokens staked.
     * @return lockDuration The lock duration in seconds.
     * @return startTime The timestamp when the stake was created.
     */
    function getStake(address user)
        external
        view
        returns (
            uint256 amount,
            uint256 lockDuration,
            uint256 startTime
        )
    {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.lockDuration, userStake.startTime);
    }
}
```
