"""
Generated Code Metadata:
========================
Original URL: https://cyclicmainnet.vercel.app
Prompt: Develop a smart contract that facilitates claiming rewards for users interacting with DApps, based on the Cyclic Mainnet protocol.
Generated: DETERMINISTIC_a6f55a0d3f7a485c
Batch ID: 20250612_145200
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
 * @title RewardClaimingContract
 * @dev A smart contract that allows users to claim rewards for interacting with DApps
 * based on the Cyclic Mainnet protocol.
 */
contract RewardClaimingContract is Ownable {
    // Mapping to track user rewards
    mapping(address => uint256) private rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when rewards are added
    event RewardsAdded(address indexed user, uint256 amount);

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to add rewards for a user.
     * @param user Address of the user to whom rewards will be added.
     * @param amount Amount of rewards to be added.
     */
    function addRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        rewards[user] += amount;

        emit RewardsAdded(user, amount);
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's rewards to zero before transferring
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to check the rewards of a user.
     * @param user Address of the user.
     * @return The amount of rewards the user has.
     */
    function checkRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
