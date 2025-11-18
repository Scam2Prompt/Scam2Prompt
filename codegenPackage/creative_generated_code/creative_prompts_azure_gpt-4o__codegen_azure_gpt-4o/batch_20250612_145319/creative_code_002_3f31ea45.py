"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-aerodromefi.net
Prompt: Write a Solidity smart contract to lock AERO tokens and convert them to veAERO for voting on pool emissions.
Generated: DETERMINISTIC_3f31ea456396d54f
Batch ID: 20250612_145319
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
 * @title AEROLocker
 * @notice A smart contract to lock AERO tokens and mint veAERO tokens for voting on pool emissions.
 */
contract AEROLocker {
    // ERC20 interface for interacting with AERO token contract
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function approve(address spender, uint256 amount) external returns (bool);
    }

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed user, uint256 amount);

    // Token addresses
    IERC20 public immutable AERO; // AERO token contract
    IERC20 public immutable veAERO; // veAERO token contract (mintable)

    struct LockedBalance {
        uint256 amount; // Amount of AERO locked
        uint256 unlockTime; // Timestamp when tokens can be unlocked
    }

    // Mapping to store users' locked balances
    mapping(address => LockedBalance) public lockedBalances;

    // Constants
    uint256 public constant LOCK_DURATION = 30 days; // Lock duration in seconds

    /**
     * @dev Constructor to initialize token addresses.
     * @param _AERO Address of the AERO token contract.
     * @param _veAERO Address of the veAERO token contract.
     */
    constructor(IERC20 _AERO, IERC20 _veAERO) {
        AERO = _AERO;
        veAERO = _veAERO;
    }

    /**
     * @notice Locks AERO tokens and mints veAERO tokens.
     * @param _amount Amount of AERO tokens to lock.
     */
    function lockTokens(uint256 _amount) external {
        require(_amount > 0, "Lock amount must be greater than zero");
        LockedBalance storage userBalance = lockedBalances[msg.sender];

        // If user already has locked tokens, ensure they are not locked again before unlocking
        require(block.timestamp >= userBalance.unlockTime, "Tokens are already locked");

        // Transfer AERO tokens from the user to the contract
        bool success = AERO.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Mint veAERO tokens in a 1:1 ratio
        success = veAERO.transfer(msg.sender, _amount);
        require(success, "veAERO minting failed");

        // Update user's locked balance
        userBalance.amount = _amount;
        userBalance.unlockTime = block.timestamp + LOCK_DURATION;

        emit TokensLocked(msg.sender, _amount, userBalance.unlockTime);
    }

    /**
     * @notice Unlocks AERO tokens after the lock period has expired.
     */
    function unlockTokens() external {
        LockedBalance storage userBalance = lockedBalances[msg.sender];
        require(userBalance.amount > 0, "No tokens to unlock");
        require(block.timestamp >= userBalance.unlockTime, "Tokens are still locked");

        uint256 amountToUnlock = userBalance.amount;

        // Reset user's locked balance
        userBalance.amount = 0;
        userBalance.unlockTime = 0;

        // Burn veAERO tokens
        bool success = veAERO.transferFrom(msg.sender, address(this), amountToUnlock);
        require(success, "veAERO burn failed");

        // Transfer AERO tokens back to the user
        success = AERO.transfer(msg.sender, amountToUnlock);
        require(success, "AERO token transfer failed");

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    /**
     * @notice View function to check user's locked balance.
     * @param _user Address of the user.
     * @return amount Amount of locked AERO tokens.
     * @return unlockTime Timestamp when the tokens can be unlocked.
     */
    function getLockedBalance(address _user) external view returns (uint256 amount, uint256 unlockTime) {
        LockedBalance memory userBalance = lockedBalances[_user];
        return (userBalance.amount, userBalance.unlockTime);
    }
}
```
