"""
Generated Code Metadata:
========================
Original URL: https://burncat-buy.pages.dev
Prompt: Create a Solidity smart contract that locks liquidity and burns tokens forever, similar to the liquidity lock mechanism described for Burn Cat's $BCAT.
Generated: DETERMINISTIC_e797e09c5d5002a5
Batch ID: 20250612_150552
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LiquidityLocker
 * @author [Your Name]
 * @notice A smart contract that locks liquidity and burns tokens forever.
 */
contract LiquidityLocker {
    using SafeMath for uint256;

    // Mapping of token addresses to their locked status
    mapping(address => bool) public lockedTokens;

    // Mapping of token addresses to their locked liquidity amounts
    mapping(address => uint256) public lockedLiquidityAmounts;

    // Mapping of token addresses to their liquidity lock expiration timestamps
    mapping(address => uint256) public lockExpirations;

    // Event emitted when a token is locked
    event TokenLocked(address indexed token, uint256 amount);

    // Event emitted when a token's liquidity lock expires
    event LockExpired(address indexed token);

    // Error thrown when attempting to lock an already locked token
    error TokenAlreadyLocked(address token);

    // Error thrown when attempting to unlock a token that is not locked
    error TokenNotLocked(address token);

    // Error thrown when attempting to lock zero liquidity
    error ZeroLiquidity();

    /**
     * @notice Locks liquidity for a given token and burns tokens forever.
     * @param token The address of the token to lock.
     * @param amount The amount of liquidity to lock.
     * @param expiration The timestamp when the liquidity lock expires.
     */
    function lockLiquidity(address token, uint256 amount, uint256 expiration) external {
        // Check if the token is already locked
        if (lockedTokens[token]) {
            revert TokenAlreadyLocked(token);
        }

        // Check if the amount of liquidity to lock is zero
        if (amount == 0) {
            revert ZeroLiquidity();
        }

        // Transfer the liquidity to the contract
        ERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update the locked token status, locked liquidity amount, and lock expiration
        lockedTokens[token] = true;
        lockedLiquidityAmounts[token] = amount;
        lockExpirations[token] = expiration;

        // Emit the TokenLocked event
        emit TokenLocked(token, amount);
    }

    /**
     * @notice Unlocks liquidity for a given token if the lock has expired.
     * @param token The address of the token to unlock.
     */
    function unlockLiquidity(address token) external {
        // Check if the token is locked
        if (!lockedTokens[token]) {
            revert TokenNotLocked(token);
        }

        // Check if the lock has expired
        if (lockExpirations[token] > block.timestamp) {
            revert("Lock has not expired yet");
        }

        // Transfer the locked liquidity back to the sender
        ERC20(token).transfer(msg.sender, lockedLiquidityAmounts[token]);

        // Update the locked token status and locked liquidity amount
        lockedTokens[token] = false;
        lockedLiquidityAmounts[token] = 0;

        // Emit the LockExpired event
        emit LockExpired(token);
    }

    /**
     * @notice Burns tokens forever.
     * @param token The address of the token to burn.
     * @param amount The amount of tokens to burn.
     */
    function burnTokens(address token, uint256 amount) external {
        // Check if the token is locked
        if (!lockedTokens[token]) {
            revert TokenNotLocked(token);
        }

        // Burn the tokens
        ERC20Burnable(token).burn(amount);
    }

    // Prevents contract from being exploited by reentrancy attacks
    fallback() external payable {}
    receive() external payable {}
}
```
