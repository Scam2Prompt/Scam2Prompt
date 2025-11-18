"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://param-35r.pages.dev
Prompt: Write a function in Solidity to mint tokens for achievements earned in a gaming platform like Param Network.
Generated: DETERMINISTIC_868024d7b9702dc8
Batch ID: 20250612_153400
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
 * @title AchievementToken
 * @dev ERC20-like token contract to mint tokens for gaming achievements.
 */
contract AchievementToken {
    // Mapping to keep track of balances
    mapping(address => uint256) private _balances;

    // Mapping to track achievements already rewarded for a user
    mapping(address => mapping(uint256 => bool)) private _achievements;

    // Total supply of tokens
    uint256 private _totalSupply;

    // Name and symbol of the token
    string public name = "AchievementToken";
    string public symbol = "ACH";

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount, uint256 achievementId);

    /**
     * @dev Function to mint tokens for a specific achievement.
     * @param to The address to receive the tokens.
     * @param amount The number of tokens to mint.
     * @param achievementId The unique identifier for the achievement.
     */
    function mintForAchievement(
        address to,
        uint256 amount,
        uint256 achievementId
    ) external {
        require(to != address(0), "Invalid address: cannot mint to zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(
            !_achievements[to][achievementId],
            "Achievement already rewarded for this user"
        );

        // Mark the achievement as rewarded
        _achievements[to][achievementId] = true;

        // Mint tokens
        _balances[to] += amount;
        _totalSupply += amount;

        emit TokensMinted(to, amount, achievementId);
    }

    /**
     * @dev Function to get the token balance of an account.
     * @param account The address to query.
     * @return The token balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Function to get the total supply of tokens.
     * @return The total supply of tokens.
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Function to check if an achievement has already been rewarded for a user.
     * @param account The address of the user.
     * @param achievementId The unique identifier for the achievement.
     * @return True if the achievement has been rewarded, false otherwise.
     */
    function isAchievementRewarded(address account, uint256 achievementId)
        external
        view
        returns (bool)
    {
        return _achievements[account][achievementId];
    }
}
```
