"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovate-appsolution.live
Prompt: Write a code snippet to facilitate token migration and claiming rewards in a Dapp environment.
Generated: DETERMINISTIC_ebed1b320f4fbfa1
Batch ID: 20250612_162408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenMigration
 * @dev Contract for migrating tokens and claiming rewards in a decentralized application (DApp).
 */
contract TokenMigration is ReentrancyGuard, Ownable {
    // Address of the old token contract
    IERC20 public oldToken;

    // Address of the new token contract
    IERC20 public newToken;

    // Mapping to track claimed rewards
    mapping(address => bool) public hasClaimedRewards;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set old and new token addresses.
     * @param _oldToken Address of the old ERC20 token.
     * @param _newToken Address of the new ERC20 token.
     */
    constructor(IERC20 _oldToken, IERC20 _newToken) {
        oldToken = _oldToken;
        newToken = _newToken;
    }

    /**
     * @dev Migrate tokens from the old token contract to the new token contract.
     * @param amount The amount of old tokens to migrate.
     */
    function migrateTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient old token balance");

        // Transfer old tokens to this contract
        oldToken.transferFrom(msg.sender, address(this), amount);

        // Transfer equivalent new tokens to the user
        newToken.transfer(msg.sender, amount);

        emit TokensMigrated(msg.sender, amount);
    }

    /**
     * @dev Claim rewards for migrating tokens. Can only be claimed once per user.
     * @param rewardAmount The amount of rewards to claim.
     */
    function claimRewards(uint256 rewardAmount) external nonReentrant {
        require(!hasClaimedRewards[msg.sender], "Rewards already claimed");
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(newToken.balanceOf(address(this)) >= rewardAmount, "Insufficient rewards available");

        // Update the claim status
        hasClaimedRewards[msg.sender] = true;

        // Transfer rewards to the user
        newToken.transfer(msg.sender, rewardAmount);
        
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance for withdrawal");
        token.transfer(msg.sender, amount);
    }
}
```
