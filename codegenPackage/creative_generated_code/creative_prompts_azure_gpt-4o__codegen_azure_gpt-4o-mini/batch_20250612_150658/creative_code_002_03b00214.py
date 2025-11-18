"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdart.top
Prompt: Generate a smart contract that facilitates reward distribution when a wallet is connected, as described in the REWARD Portal v2.
Generated: DETERMINISTIC_03b00214ac853558
Batch ID: 20250612_150658
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
 * @title RewardDistribution
 * @dev A smart contract for distributing rewards to connected wallets.
 */
contract RewardDistribution is Ownable {
    // The ERC20 token used for rewards
    IERC20 public rewardToken;

    // Mapping to track rewards per user
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the reward token.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Function to distribute rewards to a user.
     * Can only be called by the contract owner.
     * @param user Address of the user to whom rewards will be distributed.
     * @param amount Amount of rewards to distribute.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update the user's rewards balance
        rewards[user] += amount;

        // Transfer the reward tokens to the user
        require(rewardToken.transfer(user, amount), "Token transfer failed");

        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Function to claim rewards by the user.
     */
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's rewards before transferring to prevent reentrancy attacks
        rewards[msg.sender] = 0;

        // Transfer the reward tokens to the user
        require(rewardToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Function to withdraw tokens accidentally sent to the contract.
     * Can only be called by the contract owner.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        require(token.transfer(owner(), amount), "Token transfer failed");
    }
}
```
