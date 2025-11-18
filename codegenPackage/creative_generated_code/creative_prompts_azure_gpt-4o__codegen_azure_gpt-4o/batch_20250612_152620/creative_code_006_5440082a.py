"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.xyz
Prompt: Provide code to implement responsible gaming features, such as playtime limits and spending caps, for a decentralized gaming platform like BetSwirl.
Generated: DETERMINISTIC_5440082a84b460c7
Batch ID: 20250612_152620
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
 * @title ResponsibleGaming
 * @dev Implements responsible gaming features: playtime limits and spending caps for a decentralized gaming platform.
 */
contract ResponsibleGaming {
    // Struct to store player limits
    struct PlayerLimits {
        uint256 dailyPlaytimeLimit; // Daily playtime limit in seconds
        uint256 dailySpendingLimit; // Daily spending limit in wei
        uint256 playtimeToday; // Accumulated playtime today in seconds
        uint256 spendingToday; // Accumulated spending today in wei
        uint256 lastActivityTimestamp; // Last recorded activity timestamp
    }

    // Mapping of player addresses to their limits
    mapping(address => PlayerLimits) private playerLimits;

    // Event to notify limit updates
    event LimitsUpdated(
        address indexed player,
        uint256 dailyPlaytimeLimit,
        uint256 dailySpendingLimit
    );

    // Event to track spending
    event SpendingRecorded(address indexed player, uint256 amountSpent);

    // Modifier to restrict playtime
    modifier enforcePlaytimeLimit(address player) {
        PlayerLimits storage limits = playerLimits[player];
        uint256 currentTime = block.timestamp;
        uint256 elapsedTime = currentTime - limits.lastActivityTimestamp;

        // Update playtime only if the player was active recently
        if (limits.lastActivityTimestamp > 0) {
            limits.playtimeToday += elapsedTime;
        }

        // Reset playtime counter if it's a new day
        if (isNewDay(limits.lastActivityTimestamp)) {
            limits.playtimeToday = 0;
        }

        require(
            limits.playtimeToday <= limits.dailyPlaytimeLimit,
            "Playtime limit exceeded"
        );

        // Update last activity timestamp
        limits.lastActivityTimestamp = currentTime;

        _;
    }

    // Modifier to restrict spending
    modifier enforceSpendingLimit(address player, uint256 amount) {
        PlayerLimits storage limits = playerLimits[player];

        // Reset spending counter if it's a new day
        if (isNewDay(limits.lastActivityTimestamp)) {
            limits.spendingToday = 0;
        }

        require(
            limits.spendingToday + amount <= limits.dailySpendingLimit,
            "Spending limit exceeded"
        );

        // Update spending counter
        limits.spendingToday += amount;

        _;
    }

    /**
     * @dev Function to set daily playtime and spending limits for a player.
     * @param dailyPlaytimeLimit Daily playtime limit in seconds.
     * @param dailySpendingLimit Daily spending limit in wei.
     */
    function setLimits(
        uint256 dailyPlaytimeLimit,
        uint256 dailySpendingLimit
    ) external {
        require(dailyPlaytimeLimit > 0, "Playtime limit must be greater than 0");
        require(dailySpendingLimit > 0, "Spending limit must be greater than 0");

        playerLimits[msg.sender] = PlayerLimits({
            dailyPlaytimeLimit: dailyPlaytimeLimit,
            dailySpendingLimit: dailySpendingLimit,
            playtimeToday: 0,
            spendingToday: 0,
            lastActivityTimestamp: block.timestamp
        });

        emit LimitsUpdated(msg.sender, dailyPlaytimeLimit, dailySpendingLimit);
    }

    /**
     * @dev Function to record gameplay activity (playtime).
     * Enforces playtime limits.
     */
    function recordGameplay() external enforcePlaytimeLimit(msg.sender) {
        // Game logic can be implemented here
    }

    /**
     * @dev Function to record spending for a player.
     * Enforces spending limits.
     * @param amount Amount spent in wei.
     */
    function recordSpending(uint256 amount)
        external
        enforceSpendingLimit(msg.sender, amount)
    {
        require(amount > 0, "Amount must be greater than 0");

        emit SpendingRecorded(msg.sender, amount);
    }

    /**
     * @dev Helper function to check if a new day has started.
     * @param lastActivityTimestamp Last activity timestamp.
     * @return True if it's a new day, false otherwise.
     */
    function isNewDay(uint256 lastActivityTimestamp)
        internal
        view
        returns (bool)
    {
        return
            (block.timestamp / 1 days) >
            (lastActivityTimestamp / 1 days);
    }

    /**
     * @dev Function to view current limits and activity of a player.
     * @param player Address of the player.
     * @return PlayerLimits struct with current limits and activity.
     */
    function viewLimits(address player)
        external
        view
        returns (PlayerLimits memory)
    {
        return playerLimits[player];
    }
}
```
