"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrare.tech
Prompt: Write a Solidity contract that implements a reward distribution system for early adopters, similar to the token distribution model described for LOOKS tokens on LooksRare.
Generated: DETERMINISTIC_73be225ef7fd8c75
Batch ID: 20250612_145121
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RewardDistribution
 * @dev A contract for distributing rewards to early adopters of a token.
 * The contract owner can set up a reward distribution schedule and users can claim rewards.
 */
contract RewardDistribution is Ownable {
    // The token used for reward distribution
    IERC20 public rewardToken;

    // Struct to hold reward information for each user
    struct RewardInfo {
        uint256 totalReward; // Total reward assigned to the user
        uint256 claimedAmount; // Amount claimed by the user
        uint256 lastClaimed;  // Timestamp of last claim
    }

    // Mapping to store reward information per user
    mapping(address => RewardInfo) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the reward token
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Function to distribute rewards to a user.
     * @param user The address of the user to distribute rewards to.
     * @param amount The amount of rewards to distribute.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        rewards[user].totalReward += amount;

        // Transfer tokens from the contract to the user
        require(rewardToken.transfer(user, amount), "Transfer failed");

        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Function for a user to claim their rewards.
     */
    function claimRewards() external {
        RewardInfo storage userReward = rewards[msg.sender];

        uint256 claimableAmount = userReward.totalReward - userReward.claimedAmount;
        require(claimableAmount > 0, "No rewards available to claim");

        userReward.claimedAmount += claimableAmount;
        userReward.lastClaimed = block.timestamp;

        // Transfer the claimable rewards to the user
        require(rewardToken.transfer(msg.sender, claimableAmount), "Transfer failed");
    }

    /**
     * @dev Function to check how many rewards a user has available to claim.
     * @param user The address of the user.
     * @return availableRewards The amount of rewards available for claiming.
     */
    function availableRewards(address user) external view returns (uint256) {
        RewardInfo storage userReward = rewards[user];
        return userReward.totalReward - userReward.claimedAmount;
    }

    /**
     * @dev Function to withdraw tokens accidentally sent to this contract.
     * @param token The address of the token to withdraw.
     * @param to The address to send the withdrawn tokens to.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, address to, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(to, amount);
    }
}
```
