"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ffuuu.pages.dev
Prompt: Write a smart contract that integrates OpenRunes reward distribution mechanics for team and Twitter-based incentives.
Generated: DETERMINISTIC_e66186e2a6146b1d
Batch ID: 20250612_153400
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
 * @title OpenRunesRewardDistribution
 * @dev A smart contract for distributing rewards based on team performance and Twitter-based incentives.
 */
contract OpenRunesRewardDistribution is Ownable {
    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Mapping to track rewards for each team
    mapping(address => uint256) public teamRewards;

    // Mapping to track rewards for Twitter users
    mapping(address => uint256) public twitterRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the reward token.
     * @param _rewardToken The address of the ERC20 token to be used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Distributes team rewards.
     * @param teamAddress The address of the team to reward.
     * @param amount The amount of tokens to distribute as reward.
     */
    function distributeTeamRewards(address teamAddress, uint256 amount) external onlyOwner {
        require(teamAddress != address(0), "Invalid team address");
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Update the team rewards mapping
        teamRewards[teamAddress] += amount;

        // Transfer tokens to the team
        require(rewardToken.transfer(teamAddress, amount), "Token transfer failed");
        
        emit RewardsDistributed(teamAddress, amount);
    }

    /**
     * @dev Distributes Twitter-based incentives.
     * @param twitterUser The address of the Twitter user to reward.
     * @param amount The amount of tokens to distribute as incentive.
     */
    function distributeTwitterIncentives(address twitterUser, uint256 amount) external onlyOwner {
        require(twitterUser != address(0), "Invalid Twitter user address");
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Update the Twitter rewards mapping
        twitterRewards[twitterUser] += amount;

        // Transfer tokens to the Twitter user
        require(rewardToken.transfer(twitterUser, amount), "Token transfer failed");
        
        emit RewardsDistributed(twitterUser, amount);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        require(rewardToken.transfer(owner(), amount), "Token transfer failed");
    }

    /**
     * @dev Returns the total reward balance of the contract.
     * @return The total balance of the reward token in the contract.
     */
    function totalRewardBalance() external view returns (uint256) {
        return rewardToken.balanceOf(address(this));
    }
}
```
