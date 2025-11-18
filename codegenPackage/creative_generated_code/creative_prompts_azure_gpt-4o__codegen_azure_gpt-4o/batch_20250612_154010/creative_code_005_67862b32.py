"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peaptoken.fun
Prompt: Develop a smart contract in Solidity that locks liquidity by default, as described under the PEPE Pump Pad's "anti-rug security" feature.
Generated: DETERMINISTIC_67862b32d3d18ac0
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title LiquidityLocker
 * @dev A smart contract to lock liquidity by default, ensuring anti-rug security as described under PEPE Pump Pad's feature.
 */
contract LiquidityLocker {
    // Struct representing locked liquidity
    struct LiquidityLock {
        uint256 amount;          // Amount of liquidity locked
        uint256 unlockTimestamp; // Timestamp when liquidity can be unlocked
        bool isLocked;           // Status of the lock
    }

    // Mapping to store liquidity locks by address
    mapping(address => LiquidityLock) public liquidityLocks;

    // Event emitted when liquidity is locked
    event LiquidityLocked(
        address indexed locker,
        uint256 amount,
        uint256 unlockTimestamp
    );

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(
        address indexed locker,
        uint256 amount
    );

    // Modifier to check if the liquidity is locked
    modifier isLiquidityLocked(address _locker) {
        require(
            liquidityLocks[_locker].isLocked,
            "Liquidity is not locked for this address."
        );
        _;
    }

    /**
     * @notice Lock liquidity for a specified period of time.
     * @param _amount The amount of liquidity to lock.
     * @param _lockDuration The duration in seconds for which liquidity should be locked.
     */
    function lockLiquidity(uint256 _amount, uint256 _lockDuration) external {
        require(_amount > 0, "Amount must be greater than zero.");
        require(
            _lockDuration > 0,
            "Lock duration must be greater than zero seconds."
        );

        LiquidityLock storage lockInfo = liquidityLocks[msg.sender];
        require(
            !lockInfo.isLocked,
            "Liquidity is already locked for this address."
        );

        // Record lock details
        lockInfo.amount = _amount;
        lockInfo.unlockTimestamp = block.timestamp + _lockDuration;
        lockInfo.isLocked = true;

        // Emit event
        emit LiquidityLocked(msg.sender, _amount, lockInfo.unlockTimestamp);
    }

    /**
     * @notice Unlock liquidity if the lock duration has expired.
     */
    function unlockLiquidity() external isLiquidityLocked(msg.sender) {
        LiquidityLock storage lockInfo = liquidityLocks[msg.sender];

        require(
            block.timestamp >= lockInfo.unlockTimestamp,
            "Lock duration has not expired yet."
        );

        uint256 unlockedAmount = lockInfo.amount;

        // Reset lock details
        lockInfo.amount = 0;
        lockInfo.unlockTimestamp = 0;
        lockInfo.isLocked = false;

        // Emit event
        emit LiquidityUnlocked(msg.sender, unlockedAmount);
    }

    /**
     * @notice View function to check if liquidity is locked for an address.
     * @param _locker The address to query.
     * @return A boolean indicating whether liquidity is locked.
     */
    function isLocked(address _locker) external view returns (bool) {
        return liquidityLocks[_locker].isLocked;
    }

    /**
     * @notice View function to get lock details for an address.
     * @param _locker The address to query.
     * @return amount Locked liquidity amount.
     * @return unlockTimestamp Timestamp when lock expires.
     * @return isLocked Lock status.
     */
    function getLockDetails(address _locker)
        external
        view
        returns (
            uint256 amount,
            uint256 unlockTimestamp,
            bool isLocked
        )
    {
        LiquidityLock storage lockInfo = liquidityLocks[_locker];
        return (
            lockInfo.amount,
            lockInfo.unlockTimestamp,
            lockInfo.isLocked
        );
    }
}
```
