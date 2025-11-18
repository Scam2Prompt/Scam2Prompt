"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdgift.top
Prompt: Write a smart contract that facilitates reward distribution upon wallet connection, inspired by "Reward Portal v2."
Generated: DETERMINISTIC_6c92c3704bc49f90
Batch ID: 20250612_150816
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
 * @title RewardPortal
 * @dev This contract allows users to connect their wallet and receive rewards in the form of ERC20 tokens.
 */
contract RewardPortal is Ownable {
    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Mapping to track whether a user has already claimed their reward
    mapping(address => bool) public hasClaimed;

    // Event to log reward distribution
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the reward token address.
     * @param _rewardToken The address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Allows a user to claim their reward upon wallet connection.
     * @param amount The amount of tokens to be rewarded.
     */
    function claimReward(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Reward already claimed");
        require(amount > 0, "Reward amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient reward balance in contract");

        // Mark as claimed
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the user
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit RewardClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Allows the owner to set a new reward token.
     * @param _rewardToken The address of the new ERC20 token.
     */
    function setRewardToken(IERC20 _rewardToken) external onlyOwner {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Allows the owner to reset the claim status for a user.
     * @param user The address of the user whose claim status to reset.
     */
    function resetClaimStatus(address user) external onlyOwner {
        require(user != address(0), "Invalid address");
        hasClaimed[user] = false;
    }
}
```
