"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberclstage.web.app
Prompt: Write a code snippet for claiming rewards from an ERC-20 smart contract that resembles the claiming process described on CyberConnect.
Generated: DETERMINISTIC_f1b4e23c03b19cde
Batch ID: 20250612_161420
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

/**
 * @title RewardsClaimer
 * @dev A contract for claiming rewards from an ERC-20 token contract.
 */
contract RewardsClaimer {
    // Address of the ERC-20 token contract
    IERC20 public rewardToken;

    // Mapping to track claimed rewards for each user
    mapping(address => uint256) public claimedRewards;

    // Event to notify successful reward claim
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the reward token address.
     * @param _rewardToken Address of the ERC-20 token contract used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Function to claim rewards for the sender.
     * @param _amount The amount of rewards to claim.
     */
    function claimRewards(uint256 _amount) external {
        require(_amount > 0, "Reward amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient reward balance");

        // Update claimed rewards state
        claimedRewards[msg.sender] += _amount;

        // Transfer rewards to the sender
        bool success = rewardToken.transfer(msg.sender, _amount);
        require(success, "Reward transfer failed");

        // Emit event for successful claim
        emit RewardClaimed(msg.sender, _amount);
    }

    /**
     * @dev Function to check the reward balance of the contract.
     * @return The reward token balance held by the contract.
     */
    function getRewardBalance() external view returns (uint256) {
        return rewardToken.balanceOf(address(this));
    }
}

/**
 * @dev Interface for ERC-20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
