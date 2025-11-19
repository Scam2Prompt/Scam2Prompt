"""
Generated Code Metadata:
========================
Original URL: https://pushdtoken.pages.dev
Prompt: Develop a Solidity contract for locking liquidity in a blockchain-based marketplace like Pushd, ensuring liquidity is locked for 20 years to prevent rug pulls.
Generated: DETERMINISTIC_3fc959534b06c02b
Batch ID: 20250612_150226
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title LiquidityLocker
 * @author [Your Name]
 * @notice A contract for locking liquidity in a blockchain-based marketplace.
 */
contract LiquidityLocker {
    using SafeMath for uint256;

    // Mapping of liquidity pools to their lock status
    mapping(address => LockInfo) public lockedPools;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed pool, uint256 amount, uint256 lockDuration);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed pool);

    // Struct to store lock information
    struct LockInfo {
        uint256 amount;
        uint256 lockUntil;
        bool isLocked;
    }

    /**
     * @notice Locks liquidity for a specified pool.
     * @param _pool The address of the liquidity pool.
     * @param _amount The amount of liquidity to lock.
     */
    function lockLiquidity(address _pool, uint256 _amount) public {
        require(_amount > 0, "Liquidity amount must be greater than zero.");
        require(!lockedPools[_pool].isLocked, "Liquidity is already locked for this pool.");

        // Transfer liquidity to the contract
        IERC20 token = IERC20(_pool);
        require(token.transferFrom(msg.sender, address(this), _amount), "Failed to transfer liquidity.");

        // Calculate lock until timestamp (20 years from now)
        uint256 lockUntil = block.timestamp.add(20 * 365 * 24 * 60 * 60);

        // Update lock information
        lockedPools[_pool] = LockInfo(_amount, lockUntil, true);

        emit LiquidityLocked(_pool, _amount, lockUntil);
    }

    /**
     * @notice Unlocks liquidity for a specified pool.
     * @param _pool The address of the liquidity pool.
     */
    function unlockLiquidity(address _pool) public {
        require(lockedPools[_pool].isLocked, "Liquidity is not locked for this pool.");
        require(msg.sender == _pool, "Only the pool owner can unlock liquidity.");
        require(block.timestamp >= lockedPools[_pool].lockUntil, "Liquidity is still locked.");

        // Transfer locked liquidity back to the pool owner
        IERC20 token = IERC20(_pool);
        require(token.transfer(msg.sender, lockedPools[_pool].amount), "Failed to transfer liquidity.");

        // Update lock information
        lockedPools[_pool].isLocked = false;

        emit LiquidityUnlocked(_pool);
    }

    /**
     * @notice Checks if liquidity is locked for a specified pool.
     * @param _pool The address of the liquidity pool.
     * @return bool True if liquidity is locked, false otherwise.
     */
    function isLiquidityLocked(address _pool) public view returns (bool) {
        return lockedPools[_pool].isLocked;
    }

    /**
     * @notice Gets the lock information for a specified pool.
     * @param _pool The address of the liquidity pool.
     * @return LockInfo The lock information for the specified pool.
     */
    function getLockInfo(address _pool) public view returns (LockInfo memory) {
        return lockedPools[_pool];
    }
}
```
