"""
Generated Code Metadata:
========================
Original URL: https://doge2014sale.pages.dev
Prompt: Write a Solidity function for calculating staking rewards for Doge2014 tokens based on the staking allocation percentage (25%) and the user's staked amount. Include logic for secure reward distribution.
Generated: DETERMINISTIC_7bf14d0c23dd27d6
Batch ID: 20250612_152240
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

contract Doge2014Staking {
    // State variable to hold the total staked amount
    uint256 public totalStaked;

    // Mapping to hold the staked amount for each user
    mapping(address => uint256) public stakedAmounts;

    // Staking reward percentage (25%)
    uint256 public constant REWARD_PERCENTAGE = 25;

    // Event to log staking rewards distribution
    event RewardsDistributed(address indexed user, uint256 reward);

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update the user's staked amount and total staked amount
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        // Transfer tokens from the user to the contract (assuming ERC20 token)
        // Replace `token` with the actual token contract instance
        // token.transferFrom(msg.sender, address(this), amount);
    }

    // Function to calculate staking rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        require(stakedAmounts[user] > 0, "User has no staked amount");

        // Calculate the user's reward based on their staked amount
        uint256 userStakedAmount = stakedAmounts[user];
        uint256 reward = (userStakedAmount * REWARD_PERCENTAGE) / 100;

        return reward;
    }

    // Function to distribute rewards to users
    function distributeRewards() external {
        // Iterate through all users (this could be optimized with a better data structure)
        // For demonstration, we assume a fixed list of users
        address[] memory users = getUsers(); // Placeholder for user retrieval logic

        for (uint256 i = 0; i < users.length; i++) {
            address user = users[i];
            uint256 reward = calculateRewards(user);

            // Ensure the contract has enough balance to pay the rewards
            require(address(this).balance >= reward, "Insufficient contract balance for rewards");

            // Transfer the reward to the user
            payable(user).transfer(reward);

            // Emit an event for the reward distribution
            emit RewardsDistributed(user, reward);
        }
    }

    // Placeholder function to retrieve users (to be implemented)
    function getUsers() internal view returns (address[] memory) {
        // Logic to retrieve the list of users who have staked tokens
        // This could be a dynamic array or a more efficient data structure
        return new address[](0); // Placeholder return
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
