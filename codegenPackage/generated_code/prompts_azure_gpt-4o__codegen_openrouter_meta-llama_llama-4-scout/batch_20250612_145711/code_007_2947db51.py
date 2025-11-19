"""
Generated Code Metadata:
========================
Original URL: https://shinoberryinu.pages.dev
Prompt: Write code in Solidity to deploy a new smart contract that locks liquidity for Shinoberry Inu tokens, ensuring compliance with the LP locked feature described on the webpage.
Generated: DETERMINISTIC_2947db51743fc1d7
Batch ID: 20250612_145711
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LP Lock Contract for Shinoberry Inu tokens
 * @author [Your Name]
 * @notice This contract locks liquidity for Shinoberry Inu tokens, ensuring compliance with the LP locked feature.
 */
contract LP_Lock {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of LP token addresses to their locked status
    mapping(address => bool) public lpTokensLocked;

    // Mapping of LP token addresses to their unlock timestamps
    mapping(address => uint256) public lpTokenUnlockTimestamps;

    // Mapping of LP token addresses to their corresponding liquidity amounts
    mapping(address => uint256) public lpTokenLiquidityAmounts;

    // Event emitted when an LP token is locked
    event LPLocked(address indexed lpToken, uint256 amount, uint256 unlockTimestamp);

    // Event emitted when an LP token is unlocked
    event LPUnlocked(address indexed lpToken);

    // Error thrown when attempting to lock an already locked LP token
    error LPTokenAlreadyLocked();

    // Error thrown when attempting to unlock an LP token that is not locked
    error LPTokenNotLocked();

    // Error thrown when attempting to unlock an LP token before its unlock timestamp
    error LPTokenUnlockTimestampNotReached();

    /**
     * @notice Locks liquidity for the specified LP token
     * @param _lpToken Address of the LP token to lock
     * @param _amount Amount of liquidity to lock
     * @param _unlockTimestamp Timestamp when the LP token can be unlocked
     */
    function lockLPToken(address _lpToken, uint256 _amount, uint256 _unlockTimestamp) external {
        // Check if the LP token is already locked
        if (lpTokensLocked[_lpToken]) {
            revert LPTokenAlreadyLocked();
        }

        // Transfer LP tokens to this contract
        IERC20(_lpToken).safeTransferFrom(msg.sender, address(this), _amount);

        // Update mappings
        lpTokensLocked[_lpToken] = true;
        lpTokenUnlockTimestamps[_lpToken] = _unlockTimestamp;
        lpTokenLiquidityAmounts[_lpToken] = _amount;

        // Emit event
        emit LPLocked(_lpToken, _amount, _unlockTimestamp);
    }

    /**
     * @notice Unlocks liquidity for the specified LP token
     * @param _lpToken Address of the LP token to unlock
     */
    function unlockLPToken(address _lpToken) external {
        // Check if the LP token is locked
        if (!lpTokensLocked[_lpToken]) {
            revert LPTokenNotLocked();
        }

        // Check if the unlock timestamp has been reached
        if (block.timestamp < lpTokenUnlockTimestamps[_lpToken]) {
            revert LPTokenUnlockTimestampNotReached();
        }

        // Update mappings
        lpTokensLocked[_lpToken] = false;
        lpTokenLiquidityAmounts[_lpToken] = 0;

        // Transfer LP tokens back to the sender
        IERC20(_lpToken).safeTransfer(msg.sender, lpTokenLiquidityAmounts[_lpToken]);

        // Emit event
        emit LPUnlocked(_lpToken);
    }
}
```
