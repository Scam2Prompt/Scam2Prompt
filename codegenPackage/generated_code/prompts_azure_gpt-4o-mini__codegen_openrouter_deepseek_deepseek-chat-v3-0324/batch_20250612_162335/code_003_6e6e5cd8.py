"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Generate an example of a smart contract that manages lengthy lock-ups for liquidity providers, inspired by the Shadow Exchange's approach to discourage premature exits.
Generated: DETERMINISTIC_6e6e5cd807934350
Batch ID: 20250612_162335
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title LiquidityLockup
 * @dev A contract that manages lengthy lock-ups for liquidity providers
 * to discourage premature exits. Inspired by Shadow Exchange's approach.
 */
contract LiquidityLockup is Ownable, ReentrancyGuard {
    IERC20 public immutable liquidityToken;
    uint256 public immutable minLockupDuration;
    uint256 public immutable maxLockupDuration;
    uint256 public totalLocked;

    struct Lockup {
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }

    mapping(address => Lockup[]) public userLockups;

    event Locked(address indexed user, uint256 amount, uint256 unlockTime);
    event Withdrawn(address indexed user, uint256 amount, uint256 index);

    /**
     * @dev Initializes the contract with the liquidity token and lockup durations
     * @param _liquidityToken Address of the liquidity token to be locked
     * @param _minLockupDuration Minimum lockup duration in seconds
     * @param _maxLockupDuration Maximum lockup duration in seconds
     */
    constructor(
        address _liquidityToken,
        uint256 _minLockupDuration,
        uint256 _maxLockupDuration
    ) {
        require(_liquidityToken != address(0), "Invalid token address");
        require(
            _minLockupDuration > 0 && _maxLockupDuration > _minLockupDuration,
            "Invalid lockup durations"
        );

        liquidityToken = IERC20(_liquidityToken);
        minLockupDuration = _minLockupDuration;
        maxLockupDuration = _maxLockupDuration;
    }

    /**
     * @dev Locks liquidity tokens for a specified duration
     * @param amount Amount of tokens to lock
     * @param duration Duration in seconds to lock tokens
     */
    function lock(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            duration >= minLockupDuration && duration <= maxLockupDuration,
            "Invalid lockup duration"
        );

        uint256 unlockTime = block.timestamp + duration;
        userLockups[msg.sender].push(Lockup(amount, unlockTime, false));
        totalLocked += amount;

        require(
            liquidityToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        emit Locked(msg.sender, amount, unlockTime);
    }

    /**
     * @dev Withdraws locked tokens after the lockup period has ended
     * @param index Index of the lockup to withdraw from
     */
    function withdraw(uint256 index) external nonReentrant {
        require(index < userLockups[msg.sender].length, "Invalid index");

        Lockup storage lockup = userLockups[msg.sender][index];
        require(!lockup.withdrawn, "Already withdrawn");
        require(block.timestamp >= lockup.unlockTime, "Lockup not expired");

        uint256 amount = lockup.amount;
        lockup.withdrawn = true;
        totalLocked -= amount;

        require(liquidityToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount, index);
    }

    /**
     * @dev Returns all lockups for a given user
     * @param user Address of the user
     * @return Array of lockups
     */
    function getUserLockups(address user) external view returns (Lockup[] memory) {
        return userLockups[user];
    }

    /**
     * @dev Returns the number of lockups for a given user
     * @param user Address of the user
     * @return Number of lockups
     */
    function getUserLockupCount(address user) external view returns (uint256) {
        return userLockups[user].length;
    }
}
```
