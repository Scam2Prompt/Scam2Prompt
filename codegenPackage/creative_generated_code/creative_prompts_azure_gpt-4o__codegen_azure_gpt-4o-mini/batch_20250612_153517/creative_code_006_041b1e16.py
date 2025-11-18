"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Create a Solidity function to implement tier-based reward boosts for a staking platform, where tiers provide percentage increases to APY rates, as described on Decubate.
Generated: DETERMINISTIC_041b1e16295b5227
Batch ID: 20250612_153517
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
 * @title TieredStaking
 * @dev A contract for a tier-based staking system that provides reward boosts based on user tiers.
 */
contract TieredStaking is Ownable {
    // Struct to represent a Stake
    struct Stake {
        uint256 amount; // Amount staked
        uint256 tier;   // User tier
        uint256 timestamp; // Time of staking
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // APY percentages for different tiers (in basis points; 10000 = 100%)
    mapping(uint256 => uint256) public tierAPY; 

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount, uint256 tier);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize tier APY values
    constructor() {
        // Assign example APY boosts for each tier
        tierAPY[1] = 500;   // 5% for tier 1
        tierAPY[2] = 1000;  // 10% for tier 2
        tierAPY[3] = 1500;  // 15% for tier 3
        // Add more tiers as needed
    }

    /**
     * @dev Allows a user to stake tokens and sets their tier.
     * @param amount The amount of tokens to stake.
     * @param tier The tier the user is staking at.
     */
    function stake(uint256 amount, uint256 tier) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(tier > 0 && tier <= 3, "Invalid tier specified"); // Validate tier range

        // Transfer tokens from user to the contract
        IERC20 token = IERC20(0xYourTokenAddressHere); // Replace with actual token address
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.tier = tier;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount, tier);
    }

    /**
     * @dev Allows a user to unstake their tokens.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found for user");

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0; 
        userStake.timestamp = 0;

        // Transfer tokens back to user
        IERC20 token = IERC20(0xYourTokenAddressHere); // Replace with actual token address
        require(token.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Returns the current APY rate for the user's tier.
     * @param user The address of the user to check.
     * @return The APY rate in basis points.
     */
    function getCurrentAPY(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        return tierAPY[userStake.tier];
    }

    /**
     * @dev Allows the owner to update the APY for a specific tier.
     * @param tier The tier to update.
     * @param newAPY The new APY value (in basis points).
     */
    function updateTierAPY(uint256 tier, uint256 newAPY) external onlyOwner {
        require(tier > 0 && tier <= 3, "Invalid tier specified");
        tierAPY[tier] = newAPY;
    }
}
```
