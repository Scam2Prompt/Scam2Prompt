"""
Generated Code Metadata:
========================
Original URL: https://or-22s.pages.dev
Prompt: Develop a function in Solidity to implement a rewards mechanism similar to the one described in the $ENTS tokenomics.
Generated: DETERMINISTIC_6ed701d5becc8b0b
Batch ID: 20250612_151038
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
 * @title RewardsMechanism
 * @dev A contract to implement a rewards mechanism for the $ENTS tokenomics.
 */
contract RewardsMechanism is Ownable {
    IERC20 public rewardToken; // The token used for rewards
    mapping(address => uint256) public rewards; // Mapping to track rewards for each user
    mapping(address => uint256) public lastClaimed; // Last claimed timestamp for each user

    event RewardClaimed(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 totalRewards);

    /**
     * @dev Constructor to set the reward token address.
     * @param _rewardToken Address of the reward token contract.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to distribute rewards to users.
     * @param users Array of user addresses to distribute rewards to.
     * @param amounts Array of reward amounts corresponding to each user.
     */
    function distributeRewards(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Users and amounts length mismatch");
        
        uint256 totalRewards = 0;

        for (uint256 i = 0; i < users.length; i++) {
            require(users[i] != address(0), "Invalid user address");
            require(amounts[i] > 0, "Reward amount must be greater than zero");

            rewards[users[i]] += amounts[i];
            totalRewards += amounts[i];
        }

        // Transfer the total rewards from the contract to the rewardToken
        require(rewardToken.balanceOf(address(this)) >= totalRewards, "Insufficient contract balance");
        emit RewardsDistributed(totalRewards);
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards to zero before transferring
        rewards[msg.sender] = 0;
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer the rewards to the user
        require(rewardToken.transfer(msg.sender, rewardAmount), "Transfer failed");
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to check the reward balance of a user.
     * @param user Address of the user to check rewards for.
     * @return The amount of rewards available for the user.
     */
    function checkRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
