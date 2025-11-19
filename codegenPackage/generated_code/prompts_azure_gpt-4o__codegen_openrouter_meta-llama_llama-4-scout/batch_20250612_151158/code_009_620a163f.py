"""
Generated Code Metadata:
========================
Original URL: https://flashstakeio.pages.dev
Prompt: Create a Solidity contract that integrates with Flashstake to allow users to lock tokens, specify lock duration, and claim upfront yield, while ensuring no liquidation risk.
Generated: DETERMINISTIC_620a163f0cc5c629
Batch ID: 20250612_151158
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Flashstake Integration Contract
 * @author [Your Name]
 * @notice This contract integrates with Flashstake to allow users to lock tokens, 
 *         specify lock duration, and claim upfront yield, while ensuring no liquidation risk.
 */
contract FlashstakeIntegration {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user lock information
    mapping(address => LockInfo) public userLocks;

    // Flashstake contract address
    address public flashstakeAddress;

    // Token contract address
    address public tokenAddress;

    // Max lock duration in seconds
    uint256 public maxLockDuration;

    /**
     * @dev Constructor
     * @param _flashstakeAddress Flashstake contract address
     * @param _tokenAddress Token contract address
     * @param _maxLockDuration Max lock duration in seconds
     */
    constructor(address _flashstakeAddress, address _tokenAddress, uint256 _maxLockDuration) {
        flashstakeAddress = _flashstakeAddress;
        tokenAddress = _tokenAddress;
        maxLockDuration = _maxLockDuration;
    }

    /**
     * @dev Lock tokens and claim upfront yield
     * @param _amount Amount of tokens to lock
     * @param _lockDuration Lock duration in seconds
     */
    function lockTokens(uint256 _amount, uint256 _lockDuration) external {
        require(_lockDuration <= maxLockDuration, "Lock duration exceeds maximum");
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens to contract
        IERC20(tokenAddress).safeTransferFrom(msg.sender, address(this), _amount);

        // Calculate upfront yield
        uint256 upfrontYield = calculateUpfrontYield(_amount, _lockDuration);

        // Update user lock information
        userLocks[msg.sender] = LockInfo(_amount, _lockDuration, block.timestamp);

        // Claim upfront yield
        IERC20(tokenAddress).safeTransfer(msg.sender, upfrontYield);

        // Notify Flashstake of lock
        IFlashstake(flashstakeAddress).notifyLock(msg.sender, _amount, _lockDuration);
    }

    /**
     * @dev Claim locked tokens after lock duration
     */
    function claimTokens() external {
        LockInfo memory lockInfo = userLocks[msg.sender];
        require(lockInfo.amount > 0, "No locked tokens");
        require(block.timestamp >= lockInfo.lockEnd, "Lock duration not expired");

        // Transfer locked tokens back to user
        IERC20(tokenAddress).safeTransfer(msg.sender, lockInfo.amount);

        // Reset user lock information
        userLocks[msg.sender] = LockInfo(0, 0, 0);
    }

    /**
     * @dev Calculate upfront yield
     * @param _amount Amount of tokens locked
     * @param _lockDuration Lock duration in seconds
     * @return Upfront yield
     */
    function calculateUpfrontYield(uint256 _amount, uint256 _lockDuration) internal view returns (uint256) {
        // Implement yield calculation logic here
        // For demonstration purposes, assume 10% APY
        uint256 apy = 10000; // 10%
        uint256 upfrontYield = _amount.mul(apy).mul(_lockDuration).div(365 days).div(100);
        return upfrontYield;
    }

    /**
     * @dev Struct for user lock information
     */
    struct LockInfo {
        uint256 amount;
        uint256 lockDuration;
        uint256 lockEnd;
    }
}

interface IFlashstake {
    function notifyLock(address user, uint256 amount, uint256 lockDuration) external;
}
```
