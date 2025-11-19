"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Generate a smart contract that enables Farcaster channels to issue programmatic rewards for followers who engage with specific content, using Moxie Reward functionality.
Generated: DETERMINISTIC_d6be56909411643a
Batch ID: 20250612_150715
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for Farcaster channels to issue programmatic rewards
contract FarcasterReward is Ownable {
    // Event emitted when rewards are issued
    event RewardsIssued(address indexed follower, uint256 amount);

    // Mapping to track rewards for each follower
    mapping(address => uint256) public rewards;

    // The ERC20 token used for rewards
    IERC20 public rewardToken;

    // Constructor to initialize the contract with the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Function to issue rewards to followers
    // Only callable by the contract owner
    function issueRewards(address[] calldata followers, uint256[] calldata amounts) external onlyOwner {
        require(followers.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < followers.length; i++) {
            require(followers[i] != address(0), "Invalid follower address");
            require(amounts[i] > 0, "Reward amount must be greater than zero");

            // Update the rewards mapping
            rewards[followers[i]] += amounts[i];

            // Transfer the reward tokens to the follower
            require(rewardToken.transfer(followers[i], amounts[i]), "Token transfer failed");

            // Emit an event for the issued reward
            emit RewardsIssued(followers[i], amounts[i]);
        }
    }

    // Function to check the reward balance of a follower
    function checkRewardBalance(address follower) external view returns (uint256) {
        return rewards[follower];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner
        require(rewardToken.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
