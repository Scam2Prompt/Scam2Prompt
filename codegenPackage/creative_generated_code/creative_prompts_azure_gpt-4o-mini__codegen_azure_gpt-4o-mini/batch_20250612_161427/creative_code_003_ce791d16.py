"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyber-networkrw.web.app
Prompt: Generate a function in Solidity that allows users to claim their $CYBER rewards from a smart contract.
Generated: DETERMINISTIC_ce791d163d7fccd5
Batch ID: 20250612_161427
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

contract CyberRewards {
    // Mapping to track the reward balance of each user
    mapping(address => uint256) private rewards;

    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to check if the user has rewards to claim
    modifier hasRewards(address user) {
        require(rewards[user] > 0, "No rewards available to claim");
        _;
    }

    // Function to allow users to claim their $CYBER rewards
    function claimRewards() external hasRewards(msg.sender) {
        // Fetch the reward amount for the caller
        uint256 amount = rewards[msg.sender];

        // Ensure the contract has enough balance to pay the rewards
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Reset the user's reward balance to zero before transfer
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        payable(msg.sender).transfer(amount);

        // Emit an event for the reward claim
        emit RewardsClaimed(msg.sender, amount);
    }

    // Function to allow the contract owner to add rewards to a user
    function addRewards(address user, uint256 amount) external {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        // Increase the user's rewards
        rewards[user] += amount;
    }

    // Function to get the reward balance of a user
    function getRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
