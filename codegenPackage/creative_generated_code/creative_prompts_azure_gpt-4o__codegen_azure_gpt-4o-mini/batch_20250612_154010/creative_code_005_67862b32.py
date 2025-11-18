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
pragma solidity ^0.8.0;

// Importing ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
// Importing Ownable contract for ownership management
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for liquidity locking
contract LiquidityLock is Ownable {
    // Struct to hold information about each liquidity lock
    struct Lock {
        uint256 amount;       // Amount of liquidity locked
        uint256 unlockTime;   // Timestamp when liquidity can be unlocked
        bool isActive;        // Status of the lock
    }

    // Mapping to store locks by token address
    mapping(address => Lock) public locks;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);
    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed token, uint256 amount);

    /**
     * @dev Locks liquidity for a specified token.
     * @param _token The address of the token to lock.
     * @param _amount The amount of liquidity to lock.
     * @param _duration The duration (in seconds) for which to lock the liquidity.
     */
    function lockLiquidity(address _token, uint256 _amount, uint256 _duration) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");
        require(locks[_token].isActive == false, "Liquidity already locked for this token");

        // Transfer tokens to this contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Set the lock details
        locks[_token] = Lock({
            amount: _amount,
            unlockTime: block.timestamp + _duration,
            isActive: true
        });

        emit LiquidityLocked(_token, _amount, locks[_token].unlockTime);
    }

    /**
     * @dev Unlocks the liquidity for the specified token.
     * Only callable after the unlock time has passed.
     * @param _token The address of the token to unlock.
     */
    function unlockLiquidity(address _token) external onlyOwner {
        require(locks[_token].isActive, "No active lock for this token");
        require(block.timestamp >= locks[_token].unlockTime, "Unlock time has not yet passed");

        // Get the amount to unlock
        uint256 amountToUnlock = locks[_token].amount;

        // Reset lock details
        locks[_token].isActive = false;
        locks[_token].amount = 0;
        locks[_token].unlockTime = 0;

        // Transfer the locked tokens back to the owner
        IERC20(_token).transfer(msg.sender, amountToUnlock);

        emit LiquidityUnlocked(_token, amountToUnlock);
    }

    /**
     * @dev Returns the lock details for a specified token.
     * @param _token The address of the token to query.
     * @return amount The amount locked.
     * @return unlockTime The unlock timestamp.
     * @return isActive The status of the lock.
     */
    function getLockDetails(address _token) external view returns (uint256 amount, uint256 unlockTime, bool isActive) {
        Lock memory lock = locks[_token];
        return (lock.amount, lock.unlockTime, lock.isActive);
    }
}
```
