"""
Generated Code Metadata:
========================
Original URL: https://groovesup.pages.dev
Prompt: Write a smart contract in Solidity that enables artists to distribute $GROOVE token rewards to fans based on streaming activity, as described in the GrooveUP ecosystem.
Generated: DETERMINISTIC_3059e4787cbebdb9
Batch ID: 20250612_145923
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

// Importing the ERC20 interface for the $GROOVE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the GrooveUP ecosystem
contract GrooveUP is Ownable {
    // Event to log the distribution of rewards
    event RewardsDistributed(address indexed artist, address indexed fan, uint256 amount);

    // Mapping to track the streaming activity of fans
    mapping(address => uint256) public streamingActivity;

    // The address of the $GROOVE token contract
    IERC20 public grooveToken;

    // Constructor to set the $GROOVE token address
    constructor(address _grooveToken) {
        require(_grooveToken != address(0), "Invalid token address");
        grooveToken = IERC20(_grooveToken);
    }

    // Function to record streaming activity for a fan
    function recordStreamingActivity(address fan, uint256 activityAmount) external onlyOwner {
        require(fan != address(0), "Invalid fan address");
        require(activityAmount > 0, "Activity amount must be greater than zero");

        // Update the streaming activity for the fan
        streamingActivity[fan] += activityAmount;
    }

    // Function to distribute $GROOVE token rewards to fans based on their streaming activity
    function distributeRewards(address[] calldata fans) external onlyOwner {
        require(fans.length > 0, "No fans provided");

        uint256 totalReward = 0;

        // Calculate total rewards to distribute
        for (uint256 i = 0; i < fans.length; i++) {
            address fan = fans[i];
            uint256 rewardAmount = calculateReward(fan);
            require(rewardAmount > 0, "No rewards for this fan");

            totalReward += rewardAmount;
            // Reset the streaming activity after distribution
            streamingActivity[fan] = 0;

            // Emit an event for the reward distribution
            emit RewardsDistributed(msg.sender, fan, rewardAmount);
        }

        // Transfer the total rewards from the contract to the fans
        require(grooveToken.balanceOf(address(this)) >= totalReward, "Insufficient contract balance");
        for (uint256 i = 0; i < fans.length; i++) {
            address fan = fans[i];
            uint256 rewardAmount = calculateReward(fan);
            grooveToken.transfer(fan, rewardAmount);
        }
    }

    // Function to calculate the reward for a fan based on their streaming activity
    function calculateReward(address fan) internal view returns (uint256) {
        // Example reward calculation: 1 GROOVE token per streaming activity unit
        return streamingActivity[fan];
    }

    // Function to withdraw any remaining $GROOVE tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(grooveToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        grooveToken.transfer(msg.sender, amount);
    }
}
```
