"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate code for a staking platform that utilizes the $GGG token, including features for user protection and tier systems like ArbiPad.
Generated: DETERMINISTIC_c854d2468dab4c1d
Batch ID: 20250622_211123
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Staking contract for the $GGG token
contract StakingPlatform is Ownable, ReentrancyGuard {
    // Token to be staked
    IERC20 public gggToken;

    // Struct to hold user staking information
    struct UserStake {
        uint256 amount; // Amount staked
        uint256 tier;   // User tier
        uint256 timestamp; // Timestamp of the last stake
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserStake) public stakes;

    // Tier system based on staked amount
    uint256[] public tierThresholds = [100 * 10**18, 500 * 10**18, 1000 * 10**18]; // Example thresholds
    string[] public tierNames = ["Bronze", "Silver", "Gold"]; // Tier names

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event TierUpdated(address indexed user, uint256 newTier);

    // Constructor to set the GGG token address
    constructor(address _gggToken) {
        require(_gggToken != address(0), "Invalid token address");
        gggToken = IERC20(_gggToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(gggToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        gggToken.transferFrom(msg.sender, address(this), amount);

        // Update user stake information
        UserStake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        // Update user tier
        updateUserTier(msg.sender);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        UserStake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user stake information
        userStake.amount -= amount;

        // Transfer tokens back to user
        gggToken.transfer(msg.sender, amount);

        // Update user tier
        updateUserTier(msg.sender);

        emit Unstaked(msg.sender, amount);
    }

    // Function to update user tier based on staked amount
    function updateUserTier(address user) internal {
        UserStake storage userStake = stakes[user];
        uint256 newTier = 0;

        for (uint256 i = 0; i < tierThresholds.length; i++) {
            if (userStake.amount >= tierThresholds[i]) {
                newTier = i + 1; // Tier starts from 1
            }
        }

        if (newTier != userStake.tier) {
            userStake.tier = newTier;
            emit TierUpdated(user, newTier);
        }
    }

    // Function to get user stake information
    function getUserStake(address user) external view returns (uint256 amount, uint256 tier, uint256 timestamp) {
        UserStake storage userStake = stakes[user];
        return (userStake.amount, userStake.tier, userStake.timestamp);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(gggToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        gggToken.transfer(msg.sender, amount);
    }
}
```
