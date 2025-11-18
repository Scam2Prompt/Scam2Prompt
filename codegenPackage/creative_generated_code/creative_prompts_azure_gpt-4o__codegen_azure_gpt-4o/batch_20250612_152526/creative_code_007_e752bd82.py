"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-finance-en.web.app
Prompt: Develop a smart contract in Solidity that supports Retik Finance's tiered rewards system (Silver, Gold, Diamond) for cashback benefits based on card usage.
Generated: DETERMINISTIC_e752bd820637b6e6
Batch ID: 20250612_152526
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
 * @title RetikRewards
 * @dev Smart contract implementing a tiered rewards system for Retik Finance.
 * Tiers: Silver, Gold, Diamond - with cashback benefits based on card usage.
 */
contract RetikRewards {
    // Struct to define user information and tier
    struct User {
        uint256 totalSpent;   // Total amount spent by the user
        uint256 cashbackEarned; // Total cashback earned by the user
        Tier userTier;        // Current reward tier of the user
    }

    // Enum to define reward tiers
    enum Tier {
        Silver, // Tier 1
        Gold,   // Tier 2
        Diamond // Tier 3
    }

    // Mapping to store user data
    mapping(address => User) private users;

    // Cashback percentages for each tier (in basis points, e.g., 500 = 5%)
    uint256 private constant SILVER_CASHBACK = 200; // 2%
    uint256 private constant GOLD_CASHBACK = 500;   // 5%
    uint256 private constant DIAMOND_CASHBACK = 1000; // 10%

    // Tier thresholds (in wei) for upgrading tiers
    uint256 private constant SILVER_THRESHOLD = 0;       // Default tier
    uint256 private constant GOLD_THRESHOLD = 1000 ether; // Gold tier threshold
    uint256 private constant DIAMOND_THRESHOLD = 5000 ether; // Diamond tier threshold

    // Event declarations
    event CashbackAwarded(address indexed user, uint256 amount, Tier tier);
    event TierUpgraded(address indexed user, Tier newTier);

    /**
     * @notice Records a user's spending and awards cashback based on their tier.
     * @param userAddress The address of the user.
     * @param amountSpent The amount spent by the user in wei.
     */
    function recordSpending(address userAddress, uint256 amountSpent) external {
        require(amountSpent > 0, "Amount spent must be greater than 0");

        User storage user = users[userAddress];

        // Update total spent by the user
        user.totalSpent += amountSpent;

        // Determine cashback percentage based on the user's tier
        uint256 cashbackPercentage = getCashbackPercentage(user.userTier);

        // Calculate cashback earned
        uint256 cashback = (amountSpent * cashbackPercentage) / 10000;

        // Update user's cashback earned
        user.cashbackEarned += cashback;

        emit CashbackAwarded(userAddress, cashback, user.userTier);

        // Check for tier upgrade based on updated spending
        upgradeTier(userAddress);
    }

    /**
     * @notice Gets the cashback percentage for a given tier.
     * @param tier The reward tier.
     * @return The cashback percentage in basis points.
     */
    function getCashbackPercentage(Tier tier) private pure returns (uint256) {
        if (tier == Tier.Silver) return SILVER_CASHBACK;
        if (tier == Tier.Gold) return GOLD_CASHBACK;
        if (tier == Tier.Diamond) return DIAMOND_CASHBACK;
        return 0;
    }

    /**
     * @notice Upgrades the user's tier based on their total spending.
     * @param userAddress The address of the user.
     */
    function upgradeTier(address userAddress) private {
        User storage user = users[userAddress];

        // Determine new tier based on total amount spent
        Tier newTier;
        if (user.totalSpent >= DIAMOND_THRESHOLD) {
            newTier = Tier.Diamond;
        } else if (user.totalSpent >= GOLD_THRESHOLD) {
            newTier = Tier.Gold;
        } else {
            newTier = Tier.Silver;
        }

        // Upgrade tier if necessary
        if (newTier != user.userTier) {
            user.userTier = newTier;
            emit TierUpgraded(userAddress, newTier);
        }
    }

    /**
     * @notice Gets the details of a user's rewards.
     * @param userAddress The address of the user.
     * @return totalSpent The total amount spent by the user.
     * @return cashbackEarned The total cashback earned by the user.
     * @return userTier The current reward tier of the user.
     */
    function getUserDetails(address userAddress)
        external
        view
        returns (
            uint256 totalSpent,
            uint256 cashbackEarned,
            Tier userTier
        )
    {
        User memory user = users[userAddress];
        return (user.totalSpent, user.cashbackEarned, user.userTier);
    }
}
```
