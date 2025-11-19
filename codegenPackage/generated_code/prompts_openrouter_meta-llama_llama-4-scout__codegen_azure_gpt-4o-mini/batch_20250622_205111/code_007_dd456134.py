"""
Generated Code Metadata:
========================
Original URL: https://token-pushdstore.pages.dev
Prompt: Write a smart contract code to implement a rewards program that incentivizes users to participate in the growth of a decentralized marketplace like Pushd.
Generated: DETERMINISTIC_dd456134a1acef24
Batch ID: 20250622_205111
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
 * @title RewardsProgram
 * @dev A smart contract to implement a rewards program for a decentralized marketplace.
 */
contract RewardsProgram is Ownable {
    // Token used for rewards
    IERC20 public rewardToken;

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to distribute rewards to a user.
     * @param user Address of the user to receive rewards.
     * @param amount Amount of rewards to distribute.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        // Update user rewards
        userRewards[user] += amount;

        // Emit event for rewards distribution
        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimRewards() external {
        uint256 amount = userRewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset user rewards before transferring to prevent re-entrancy
        userRewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");

        // Emit event for rewards claim
        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to check the reward balance of a user.
     * @param user Address of the user.
     * @return The amount of rewards the user has.
     */
    function checkRewards(address user) external view returns (uint256) {
        return userRewards[user];
    }

    /**
     * @dev Function to withdraw tokens from the contract in case of emergency.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(rewardToken.transfer(owner(), amount), "Transfer failed");
    }
}
```
