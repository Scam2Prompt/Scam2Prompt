"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tendaoio.web.app
Prompt: Write a Solidity smart contract to interact with Tensor's platform for managing rewards in $TNSR tokens.
Generated: DETERMINISTIC_c497e157abf0ce4c
Batch ID: 20250612_153713
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

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TensorRewards
 * @dev A smart contract to manage rewards in $TNSR tokens
 */
contract TensorRewards is Ownable {
    // ERC20 token contract interface
    IERC20 public tnsrToken;

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the TNSR token address
     * @param _tnsrTokenAddress The address of the $TNSR token contract
     */
    constructor(address _tnsrTokenAddress) {
        require(_tnsrTokenAddress != address(0), "Invalid token address");
        tnsrToken = IERC20(_tnsrTokenAddress);
    }

    /**
     * @dev Function to distribute rewards to a user
     * @param user The address of the user to receive rewards
     * @param amount The amount of rewards to distribute
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        // Increase the user's reward balance
        rewards[user] += amount;

        // Emit rewards distribution event
        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Function for users to claim their rewards
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset user's rewards to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        require(tnsrToken.transfer(msg.sender, rewardAmount), "Token transfer failed");

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to retrieve the reward balance of a user
     * @param user The address of the user
     * @return The amount of rewards the user has
     */
    function getRewardsBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
