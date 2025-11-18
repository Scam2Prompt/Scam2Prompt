"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://planetserfi.pages.dev
Prompt: Develop a Solidity function to implement rewards distribution for users contributing to sustainability projects, inspired by Planet ReFi's mission.
Generated: DETERMINISTIC_6841e0cc6ac6d07c
Batch ID: 20250612_152739
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
 * @title SustainabilityRewards
 * @dev A contract to distribute rewards to users contributing to sustainability projects.
 */
contract SustainabilityRewards {
    // Mapping to track user balances (contributions)
    mapping(address => uint256) public contributions;

    // Mapping to track rewards earned by users
    mapping(address => uint256) public rewards;

    // Owner of the contract
    address public owner;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    constructor() {
        // Initialize the owner as the deployer of the contract
        owner = msg.sender;
    }

    /**
     * @dev Function to record a user's contribution to a sustainability project.
     * @param user The address of the user contributing.
     * @param amount The amount contributed by the user.
     */
    function recordContribution(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Contribution amount must be greater than zero");

        // Update the user's contribution balance
        contributions[user] += amount;
    }

    /**
     * @dev Function to calculate rewards for a specific user based on their contribution.
     * @param user The address of the user.
     * @return rewardAmount The calculated reward for the user.
     */
    function calculateReward(address user) public view returns (uint256 rewardAmount) {
        require(user != address(0), "Invalid user address");

        // Reward calculation logic (e.g., 10% of contribution)
        rewardAmount = contributions[user] / 10;
    }

    /**
     * @dev Function to distribute rewards to a specific user.
     * @param user The address of the user receiving rewards.
     */
    function distributeReward(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(contributions[user] > 0, "No contributions recorded for user");

        // Calculate the reward for the user
        uint256 rewardAmount = calculateReward(user);

        // Update the user's rewards balance
        rewards[user] += rewardAmount;

        // Emit the event for reward distribution
        emit RewardsDistributed(user, rewardAmount);
    }

    /**
     * @dev Function to reset contributions and rewards for a user. 
     * Can be used for project completion or resetting data.
     * @param user The address of the user to reset.
     */
    function resetUserData(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");

        // Reset contributions and rewards for the user
        contributions[user] = 0;
        rewards[user] = 0;
    }
}
```
