"""
Generated Code Metadata:
========================
Original URL: https://ethevista.app
Prompt: Create a Solidity function that enforces a mandatory 5-day liquidity lock for new token launches, aligning with Ethervista's safeguards for user trust.
Generated: DETERMINISTIC_d10c60364114e77a
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TokenLaunchManager
 * @author [Your Name]
 * @notice Manages token launches with a mandatory 5-day liquidity lock.
 */
contract TokenLaunchManager is ReentrancyGuard {
    // Mapping of token addresses to their launch timestamps
    mapping(address => uint256) public tokenLaunches;

    /**
     * @notice Event emitted when a new token launch is scheduled
     * @param token Address of the token
     * @param launchTimestamp Timestamp of the token launch
     */
    event TokenLaunchScheduled(address indexed token, uint256 launchTimestamp);

    /**
     * @notice Event emitted when liquidity is unlocked for a token
     * @param token Address of the token
     */
    event LiquidityUnlocked(address indexed token);

    /**
     * @notice Schedules a new token launch with a 5-day liquidity lock
     * @param token Address of the token to launch
     */
    function scheduleTokenLaunch(address token) external nonReentrant {
        // Check if token is a valid ERC20
        require(ERC20(token).totalSupply() > 0, "Invalid token");

        // Check if token launch has already been scheduled
        require(tokenLaunches[token] == 0, "Token launch already scheduled");

        // Calculate the liquidity unlock timestamp (5 days from now)
        uint256 launchTimestamp = block.timestamp;
        uint256 liquidityUnlockTimestamp = launchTimestamp + 5 days;

        // Store the launch timestamp
        tokenLaunches[token] = liquidityUnlockTimestamp;

        // Emit event
        emit TokenLaunchScheduled(token, launchTimestamp);
    }

    /**
     * @notice Checks if liquidity is unlocked for a token
     * @param token Address of the token to check
     * @return True if liquidity is unlocked, false otherwise
     */
    function isLiquidityUnlocked(address token) public view returns (bool) {
        // Check if token launch has been scheduled
        uint256 liquidityUnlockTimestamp = tokenLaunches[token];
        require(liquidityUnlockTimestamp > 0, "Token launch not scheduled");

        // Check if liquidity unlock timestamp has passed
        return block.timestamp >= liquidityUnlockTimestamp;
    }

    /**
     * @notice Unlocks liquidity for a token
     * @param token Address of the token to unlock liquidity for
     */
    function unlockLiquidity(address token) external nonReentrant {
        // Check if token launch has been scheduled
        uint256 liquidityUnlockTimestamp = tokenLaunches[token];
        require(liquidityUnlockTimestamp > 0, "Token launch not scheduled");

        // Check if liquidity unlock timestamp has passed
        require(block.timestamp >= liquidityUnlockTimestamp, "Liquidity lock not expired");

        // Update token launch mapping
        tokenLaunches[token] = 0;

        // Emit event
        emit LiquidityUnlocked(token);
    }
}
```
