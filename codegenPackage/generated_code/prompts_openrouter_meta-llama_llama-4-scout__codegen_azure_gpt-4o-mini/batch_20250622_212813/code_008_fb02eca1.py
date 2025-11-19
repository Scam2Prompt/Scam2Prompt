"""
Generated Code Metadata:
========================
Original URL: https://stailoud.io
Prompt: "Outline a smart contract for distributing SOL rewards based on Loud's weekly SOL distribution mechanics."
Generated: DETERMINISTIC_fb02eca1ed619bfe
Batch ID: 20250622_212813
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title SOLRewardDistributor
 * @dev A smart contract for distributing SOL rewards based on Loud's weekly distribution mechanics.
 */
contract SOLRewardDistributor is Ownable {
    IERC20 public solToken; // The ERC20 token representing SOL
    uint256 public totalRewards; // Total rewards available for distribution
    uint256 public lastDistributionTime; // Last time rewards were distributed
    uint256 public distributionInterval; // Time interval for distribution (in seconds)

    mapping(address => uint256) public userRewards; // Mapping of user addresses to their rewards
    mapping(address => uint256) public lastClaimed; // Mapping of user addresses to their last claimed time

    event RewardsDistributed(uint256 totalRewards);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the SOL token address and distribution interval.
     * @param _solToken Address of the SOL token contract.
     * @param _distributionInterval Time interval for distribution in seconds.
     */
    constructor(address _solToken, uint256 _distributionInterval) {
        require(_solToken != address(0), "Invalid token address");
        require(_distributionInterval > 0, "Invalid distribution interval");

        solToken = IERC20(_solToken);
        distributionInterval = _distributionInterval;
        lastDistributionTime = block.timestamp;
    }

    /**
     * @dev Function to distribute rewards to users.
     * @param _totalRewards Total amount of rewards to distribute.
     */
    function distributeRewards(uint256 _totalRewards) external onlyOwner {
        require(block.timestamp >= lastDistributionTime + distributionInterval, "Distribution not allowed yet");
        require(_totalRewards > 0, "Total rewards must be greater than zero");
        require(solToken.balanceOf(address(this)) >= _totalRewards, "Insufficient contract balance");

        totalRewards += _totalRewards;
        lastDistributionTime = block.timestamp;

        emit RewardsDistributed(_totalRewards);
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimRewards() external {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        userRewards[msg.sender] = 0; // Reset user rewards before transfer to prevent re-entrancy
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer the rewards to the user
        require(solToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to update user rewards based on some logic (to be defined).
     * @param user Address of the user to update rewards for.
     * @param amount Amount of rewards to add.
     */
    function updateUserRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        userRewards[user] += amount;
    }

    /**
     * @dev Function to withdraw any ERC20 tokens from the contract (for emergency purposes).
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
