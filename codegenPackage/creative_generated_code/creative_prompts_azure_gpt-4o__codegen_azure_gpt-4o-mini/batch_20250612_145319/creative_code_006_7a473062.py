"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposals-aerodromefi.net
Prompt: Create a smart contract that rewards veAERO voters with protocol incentives and fees based on their voting activity.
Generated: DETERMINISTIC_7a4730620f83f0d8
Batch ID: 20250612_145319
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title VotingReward
 * @dev A smart contract that rewards veAERO voters with protocol incentives and fees
 */
contract VotingReward is Ownable {
    // State variables
    IERC20 public rewardToken; // Token used for rewarding voters
    mapping(address => uint256) public voterRewards; // Mapping from voter address to their accumulated rewards
    mapping(address => bool) public hasVoted; // Track if an address has voted
    uint256 public totalRewards; // Total amount of rewards available for distribution

    // Events
    event RewardsClaimed(address indexed voter, uint256 amount);
    event NewVote(address indexed voter);

    /**
     * @dev Constructor to initialize the contract with the reward token address
     * @param _rewardToken The address of the ERC20 reward token
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Function to update total rewards available for distribution
     * @param amount The amount of new rewards to add
     */
    function updateRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        totalRewards += amount;
        rewardToken.transferFrom(msg.sender, address(this), amount);
    }

    /**
     * @dev Function to record a vote and reward the voter
     */
    function vote() external {
        require(!hasVoted[msg.sender], "You have already voted");
        require(totalRewards > 0, "No rewards available");

        // Mark that the voter has voted
        hasVoted[msg.sender] = true;

        // Calculate rewards (arbitrary logic for this example)
        uint256 rewardAmount = totalRewards / 100; // Reward 1% of total rewards
        require(rewardAmount > 0, "No rewards to distribute");

        // Update the voter's reward balance
        voterRewards[msg.sender] += rewardAmount;
        totalRewards -= rewardAmount; // Decrease the total rewards

        emit NewVote(msg.sender);
    }

    /**
     * @dev Function for voters to claim their rewards
     */
    function claimRewards() external {
        uint256 rewardAmount = voterRewards[msg.sender];
        require(rewardAmount > 0, "No rewards available to claim");

        // Reset the voter's reward balance to prevent re-entrancy attacks
        voterRewards[msg.sender] = 0;

        // Transfer rewards to the voter
        rewardToken.transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to withdraw tokens in case of emergency (onlyOwner)
     * @param tokenAddress The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
