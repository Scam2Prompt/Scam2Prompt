"""
Generated Code Metadata:
========================
Original URL: https://bananagunn.io
Prompt: Describe how to set up a reward forfeiture system in a smart contract for users who sell or transfer more than 300 $BANANA tokens.
Generated: DETERMINISTIC_44ab2cc059536a9d
Batch ID: 20250612_160628
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
 * @title RewardForfeiture
 * @dev A smart contract to manage reward forfeiture for users who sell or transfer more than 300 $BANANA tokens.
 */
contract RewardForfeiture {
    // Address of the $BANANA token contract
    address public bananaToken;

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Mapping to track forfeited rewards
    mapping(address => bool) public forfeited;

    // Event emitted when rewards are forfeited
    event RewardsForfeited(address indexed user, uint256 amount);

    // Event emitted when rewards are added
    event RewardsAdded(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the $BANANA token address.
     * @param _bananaToken Address of the $BANANA token contract.
     */
    constructor(address _bananaToken) {
        require(_bananaToken != address(0), "Invalid token address");
        bananaToken = _bananaToken;
    }

    /**
     * @dev Modifier to check if the user has forfeited their rewards.
     * @param user Address of the user.
     */
    modifier notForfeited(address user) {
        require(!forfeited[user], "User has forfeited rewards");
        _;
    }

    /**
     * @dev Function to add rewards for a user.
     * @param user Address of the user.
     * @param amount Amount of rewards to add.
     */
    function addRewards(address user, uint256 amount) external notForfeited(user) {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        rewards[user] += amount;
        emit RewardsAdded(user, amount);
    }

    /**
     * @dev Function to forfeit rewards if a user sells or transfers more than 300 $BANANA tokens.
     * This function should be called by the $BANANA token contract during transfers.
     * @param user Address of the user.
     * @param transferAmount Amount of $BANANA tokens being transferred.
     */
    function checkForfeiture(address user, uint256 transferAmount) external {
        require(msg.sender == bananaToken, "Only the $BANANA token contract can call this function");
        require(user != address(0), "Invalid user address");

        if (transferAmount > 300 * (10 ** 18)) { // Assuming $BANANA has 18 decimals
            forfeited[user] = true;
            uint256 forfeitedAmount = rewards[user];
            rewards[user] = 0;

            emit RewardsForfeited(user, forfeitedAmount);
        }
    }

    /**
     * @dev Function to get the reward balance of a user.
     * @param user Address of the user.
     * @return The reward balance of the user.
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
