"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tapswaporg.pages.dev
Prompt: Create a smart contract that mimics TapSwap's reward mechanism, allowing users to claim $10,000 worth of rewards after completing verification steps.
Generated: DETERMINISTIC_48fe260148dd3327
Batch ID: 20250612_150342
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
 * @title TapSwapReward
 * @dev A smart contract for managing TapSwap-like reward claims.
 */
contract TapSwapReward is Ownable {
    IERC20 public rewardToken; // The ERC20 token to be used as rewards
    uint256 public constant REWARD_AMOUNT = 10000 * 10 ** 18; // Reward amount in wei
    mapping(address => bool) public verifiedUsers; // Tracks users who completed verification
    mapping(address => bool) public claimedRewards; // Tracks users who have claimed rewards

    event UserVerified(address indexed user);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Sets the reward token contract address.
     * @param _rewardToken Address of the reward token contract.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Allows the owner to verify a user for rewards.
     * @param user The address of the user to verify.
     */
    function verifyUser(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(!verifiedUsers[user], "User already verified");

        verifiedUsers[user] = true;
        emit UserVerified(user);
    }

    /**
     * @dev Allows a verified user to claim their reward.
     */
    function claimReward() external {
        require(verifiedUsers[msg.sender], "User not verified");
        require(!claimedRewards[msg.sender], "Reward already claimed");

        claimedRewards[msg.sender] = true;
        
        // Transfer the reward amount to the user
        bool success = rewardToken.transfer(msg.sender, REWARD_AMOUNT);
        require(success, "Token transfer failed");

        emit RewardClaimed(msg.sender, REWARD_AMOUNT);
    }

    /**
     * @dev Allows the owner to withdraw any tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 balance = rewardToken.balanceOf(address(this));
        require(amount <= balance, "Insufficient balance");

        bool success = rewardToken.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }
}
```
