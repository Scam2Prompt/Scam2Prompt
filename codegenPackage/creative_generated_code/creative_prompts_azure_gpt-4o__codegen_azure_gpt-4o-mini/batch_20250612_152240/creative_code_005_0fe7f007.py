"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap-dogs.pages.dev
Prompt: Develop a smart contract for distributing $DOGS tokens as rewards to users based on specific criteria within the TON ecosystem.
Generated: DETERMINISTIC_0fe7f0073cbe6e12
Batch ID: 20250612_152240
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

// Import necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DogTokenDistributor
 * @notice This contract distributes $DOGS tokens as rewards to users based on specific criteria.
 */
contract DogTokenDistributor is Ownable {
    IERC20 public dogToken; // The $DOGS token contract
    mapping(address => uint256) public rewards; // Track rewards for each user
    uint256 public totalRewards; // Total rewards available for distribution

    event RewardDistributed(address indexed user, uint256 amount);
    event RewardsAdded(uint256 amount);

    /**
     * @dev Constructor to set the $DOGS token contract address.
     * @param _dogToken Address of the $DOGS token contract.
     */
    constructor(IERC20 _dogToken) {
        require(address(_dogToken) != address(0), "Invalid token address");
        dogToken = _dogToken;
    }

    /**
     * @dev Add rewards to the contract.
     * @param amount Amount of $DOGS tokens to add as rewards.
     */
    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(dogToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalRewards += amount;
        emit RewardsAdded(amount);
    }

    /**
     * @dev Distribute rewards to a user based on specific criteria.
     * @param user Address of the user to distribute rewards to.
     * @param amount Amount of rewards to distribute.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(totalRewards >= amount, "Insufficient total rewards");
        
        rewards[user] += amount; // Update user's rewards
        totalRewards -= amount; // Deduct from total rewards

        // Transfer the rewards to the user
        require(dogToken.transfer(user, amount), "Transfer failed");
        emit RewardDistributed(user, amount);
    }

    /**
     * @dev View the reward balance of a specific user.
     * @param user Address of the user.
     * @return The reward balance of the user.
     */
    function viewRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }

    /**
     * @dev Withdraw unused $DOGS tokens from the contract by the owner.
     * @param amount Amount of $DOGS tokens to withdraw.
     */
    function withdrawUnusedTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(dogToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        require(dogToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
