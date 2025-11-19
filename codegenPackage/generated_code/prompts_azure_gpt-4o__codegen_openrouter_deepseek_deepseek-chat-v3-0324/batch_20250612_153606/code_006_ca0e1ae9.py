"""
Generated Code Metadata:
========================
Original URL: https://dappback.firebaseapp.com
Prompt: Create a smart contract example that could be deployed and utilized with DappBack for tracking user rewards.
Generated: DETERMINISTIC_ca0e1ae9e5949752
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DappBackRewards
 * @dev A smart contract for tracking and managing user rewards in the DappBack ecosystem
 */
contract DappBackRewards is Ownable, ReentrancyGuard {
    // Struct to store user reward information
    struct UserReward {
        uint256 totalEarned;
        uint256 totalClaimed;
        uint256 lastUpdated;
    }

    // Mapping of user addresses to their reward data
    mapping(address => UserReward) public userRewards;

    // Events
    event RewardEarned(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    /**
     * @dev Record earned rewards for a user
     * @param user Address of the user
     * @param amount Amount of rewards earned
     */
    function earnReward(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        UserReward storage reward = userRewards[user];
        reward.totalEarned += amount;
        reward.lastUpdated = block.timestamp;

        emit RewardEarned(user, amount);
    }

    /**
     * @dev Claim available rewards
     * @param amount Amount of rewards to claim
     */
    function claimReward(uint256 amount) external nonReentrant {
        address user = msg.sender;
        UserReward storage reward = userRewards[user];

        uint256 claimable = reward.totalEarned - reward.totalClaimed;
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= claimable, "Insufficient rewards");

        reward.totalClaimed += amount;
        reward.lastUpdated = block.timestamp;

        // In a real implementation, you would transfer tokens here
        // For example: rewardToken.transfer(user, amount);

        emit RewardClaimed(user, amount);
    }

    /**
     * @dev Get claimable rewards for a user
     * @param user Address of the user
     * @return Amount of claimable rewards
     */
    function getClaimableRewards(address user) external view returns (uint256) {
        UserReward storage reward = userRewards[user];
        return reward.totalEarned - reward.totalClaimed;
    }

    /**
     * @dev Emergency withdraw function for the contract owner
     * @notice This is a safety measure to recover any accidentally sent funds
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");

        emit EmergencyWithdraw(owner(), balance);
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}
}
```
