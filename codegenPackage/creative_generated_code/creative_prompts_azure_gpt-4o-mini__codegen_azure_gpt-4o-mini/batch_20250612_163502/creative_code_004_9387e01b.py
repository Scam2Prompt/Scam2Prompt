"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tapswapaii.pages.dev
Prompt: Provide a sample code for a smart contract that manages rewards distribution similar to TapSwap's offering.
Generated: DETERMINISTIC_9387e01b82169d7d
Batch ID: 20250612_163502
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
 * @title RewardsDistribution
 * @dev A smart contract to manage the distribution of rewards to users.
 */
contract RewardsDistribution is Ownable {
    // The ERC20 token to be used for rewards
    IERC20 public rewardToken;

    // Mapping to track the last claimed reward for each user
    mapping(address => uint256) public lastClaimed;

    // Total rewards available for distribution
    uint256 public totalRewards;

    event RewardsDistributed(address indexed user, uint256 amount);
    event RewardsAdded(uint256 amount);

    /**
     * @dev Constructor to initialize the contract with a reward token.
     * @param _rewardToken Address of the ERC20 reward token.
     */
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to add rewards to the contract.
     * @param amount The amount of rewards to add.
     * Emits a RewardsAdded event.
     */
    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        
        totalRewards += amount;
        emit RewardsAdded(amount);
    }

    /**
     * @dev Function to distribute rewards to a user.
     * @param user The address of the user to reward.
     * @param amount The amount of rewards to distribute.
     * Emits a RewardsDistributed event.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= totalRewards, "Insufficient rewards available");
        require(rewardToken.balanceOf(address(this)) >= amount, "Contract does not have enough tokens");
        
        lastClaimed[user] = block.timestamp;
        totalRewards -= amount;

        require(rewardToken.transfer(user, amount), "Token transfer failed");
        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Function to check the balance of rewards available in the contract.
     * @return The current balance of rewards.
     */
    function availableRewards() external view returns (uint256) {
        return rewardToken.balanceOf(address(this));
    }
}
```
