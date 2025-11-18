"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-pushdstore.pages.dev
Prompt: Write a Solidity contract to lock team tokens for 700 days and liquidity for 20 years, ensuring security and preventing rug pulls as outlined in Pushd's roadmap.
Generated: DETERMINISTIC_822d4137d7954aab
Batch ID: 20250612_150228
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

contract TokenLock {
    // Variables to store token amounts and lock durations
    uint256 public teamTokensLocked;
    uint256 public liquidityTokensLocked;

    // Lock duration constants
    uint256 public constant TEAM_LOCK_DURATION = 700 days;
    uint256 public constant LIQUIDITY_LOCK_DURATION = 20 * 365 days; // 20 years

    // Variable to store the unlocking times
    uint256 public teamUnlockTime;
    uint256 public liquidityUnlockTime;

    // Event to notify when tokens are locked
    event TokensLocked(address indexed locker, uint256 teamAmount, uint256 liquidityAmount, uint256 teamUnlockTime, uint256 liquidityUnlockTime);

    // Modifier to check if the tokens are unlocked
    modifier onlyWhenLocked() {
        require(block.timestamp < teamUnlockTime, "Team tokens are unlocked");
        require(block.timestamp < liquidityUnlockTime, "Liquidity tokens are unlocked");
        _;
    }

    // Constructor to initialize the contract with token amounts
    constructor(uint256 _teamTokens, uint256 _liquidityTokens) {
        require(_teamTokens > 0, "Team tokens must be greater than zero");
        require(_liquidityTokens > 0, "Liquidity tokens must be greater than zero");

        teamTokensLocked = _teamTokens;
        liquidityTokensLocked = _liquidityTokens;

        // Set the unlock times
        teamUnlockTime = block.timestamp + TEAM_LOCK_DURATION;
        liquidityUnlockTime = block.timestamp + LIQUIDITY_LOCK_DURATION;

        emit TokensLocked(msg.sender, teamTokensLocked, liquidityTokensLocked, teamUnlockTime, liquidityUnlockTime);
    }

    // Function to withdraw team tokens after the lock period
    function withdrawTeamTokens() external onlyWhenLocked {
        require(block.timestamp >= teamUnlockTime, "Team tokens are still locked");
        uint256 amount = teamTokensLocked;
        teamTokensLocked = 0; // Prevent re-entrancy

        // Transfer tokens to the owner (assuming the contract has the tokens)
        // Implement your token transfer logic here

        // Example: IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw liquidity tokens after the lock period
    function withdrawLiquidityTokens() external onlyWhenLocked {
        require(block.timestamp >= liquidityUnlockTime, "Liquidity tokens are still locked");
        uint256 amount = liquidityTokensLocked;
        liquidityTokensLocked = 0; // Prevent re-entrancy

        // Transfer tokens to the owner (assuming the contract has the tokens)
        // Implement your token transfer logic here

        // Example: IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to check the status of token locks
    function getLockStatus() external view returns (uint256, uint256, uint256, uint256) {
        return (teamTokensLocked, liquidityTokensLocked, teamUnlockTime, liquidityUnlockTime);
    }
}
```
