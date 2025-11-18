"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainetfclaim.pages.dev
Prompt: Write a Solidity function to calculate and distribute staking rewards for BTCETF tokens based on the total staked amount and individual user contributions.
Generated: DETERMINISTIC_e46aa4321184f9e0
Batch ID: 20250612_151141
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

contract BTCETFStaking {
    // Structure to hold user's staking information
    struct UserStake {
        uint256 amount;      // Amount of tokens staked by the user
        uint256 rewardDebt;  // Reward debt to manage rewards
    }

    // Total amount of staked tokens
    uint256 public totalStaked;

    // Mapping of user addresses to their stake information
    mapping(address => UserStake) public userStakes;

    // Total rewards distributed
    uint256 public totalRewards;

    // Reward per token staked (in wei)
    uint256 public rewardPerToken;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Modifier to check if the user has staked tokens
    modifier hasStaked(address user) {
        require(userStakes[user].amount > 0, "No staked tokens.");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");

        UserStake storage userStake = userStakes[msg.sender];

        // Update the total staked amount
        totalStaked += amount;

        // Update user's stake information
        userStake.amount += amount;
        userStake.rewardDebt = userStake.amount * rewardPerToken;

        // Assuming transferFrom is properly implemented for the token
        // token.transferFrom(msg.sender, address(this), amount);
    }

    // Function to distribute rewards to all users
    function distributeRewards(uint256 rewards) external {
        require(rewards > 0, "Rewards must be greater than zero.");

        // Update total rewards and reward per token
        totalRewards += rewards;
        rewardPerToken += rewards / totalStaked;

        // Iterate through all stakers to distribute rewards
        for (address user : getAllStakers()) {
            _distributeReward(user);
        }
    }

    // Internal function to distribute rewards for a specific user
    function _distributeReward(address user) internal hasStaked(user) {
        UserStake storage userStake = userStakes[user];

        // Calculate pending rewards for the user
        uint256 pendingReward = (userStake.amount * rewardPerToken) - userStake.rewardDebt;

        // Update user's reward debt
        userStake.rewardDebt = userStake.amount * rewardPerToken;

        // Transfer the rewards to the user
        if (pendingReward > 0) {
            // Assuming transfer is properly implemented for the token
            // token.transfer(user, pendingReward);
            emit RewardsDistributed(user, pendingReward);
        }
    }

    // Function to retrieve a list of all stakers (mock implementation)
    function getAllStakers() internal view returns (address[] memory) {
        // In a production contract, you would maintain an array of staker addresses
        // Here we would return a mock array for demonstration purposes
        address[] memory stakers = new address[](0); // Placeholder
        return stakers;
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external hasStaked(msg.sender) {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= amount, "Withdraw amount exceeds staked amount.");

        // Update the total staked amount and user's stake information
        totalStaked -= amount;
        userStake.amount -= amount;

        // Transfer the staked tokens back to the user
        // Assuming transfer is properly implemented for the token
        // token.transfer(msg.sender, amount);
    }
}
```
