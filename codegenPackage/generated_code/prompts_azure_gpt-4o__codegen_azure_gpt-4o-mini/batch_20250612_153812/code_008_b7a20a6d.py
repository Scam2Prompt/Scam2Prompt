"""
Generated Code Metadata:
========================
Original URL: https://kenduinu-an.web.app
Prompt: Write a Solidity contract to implement a reward distribution mechanism for Kendu Inu, ensuring fair allocation of staking rewards to token holders.
Generated: DETERMINISTIC_b7a20a6d4252a05c
Batch ID: 20250612_153812
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title KenduInuRewardDistribution
 * @dev A contract for distributing staking rewards to Kendu Inu token holders.
 */
contract KenduInuRewardDistribution is Ownable {
    IERC20 public kenduInuToken; // The Kendu Inu token contract
    uint256 public totalRewards; // Total rewards available for distribution
    mapping(address => uint256) public rewards; // Mapping of user addresses to their rewards
    mapping(address => uint256) public lastClaimed; // Last claimed timestamp for each user

    event RewardsDistributed(address indexed user, uint256 amount);
    event RewardsAdded(uint256 amount);

    /**
     * @dev Constructor to set the Kendu Inu token address.
     * @param _kenduInuToken Address of the Kendu Inu token contract.
     */
    constructor(address _kenduInuToken) {
        require(_kenduInuToken != address(0), "Invalid token address");
        kenduInuToken = IERC20(_kenduInuToken);
    }

    /**
     * @dev Function to add rewards to the contract.
     * @param amount Amount of rewards to add.
     */
    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        totalRewards += amount;
        kenduInuToken.transferFrom(msg.sender, address(this), amount);
        emit RewardsAdded(amount);
    }

    /**
     * @dev Function to claim rewards for the caller.
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update the last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer the rewards to the user
        rewards[msg.sender] = 0; // Reset rewards after claiming
        totalRewards -= reward; // Decrease total rewards
        kenduInuToken.transfer(msg.sender, reward);
        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Function to calculate the reward for a user.
     * @param user Address of the user.
     * @return The calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        // Simple reward calculation based on total rewards and last claimed time
        // This can be modified to implement a more complex reward mechanism
        uint256 timeElapsed = block.timestamp - lastClaimed[user];
        uint256 userReward = (totalRewards * timeElapsed) / 1 days; // Example calculation
        return userReward > rewards[user] ? userReward : rewards[user];
    }

    /**
     * @dev Function to view the pending rewards for a user.
     * @param user Address of the user.
     * @return The pending reward amount.
     */
    function pendingRewards(address user) external view returns (uint256) {
        return calculateReward(user);
    }

    /**
     * @dev Function to withdraw any ERC20 tokens accidentally sent to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != kenduInuToken, "Cannot withdraw Kendu Inu tokens");
        token.transfer(msg.sender, amount);
    }
}
```
