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

/**
 * @title LiquidityLockup
 * @dev A smart contract to manage lock-ups for liquidity providers, discouraging premature exits.
 */
contract LiquidityLockup {
    // Struct to represent a lock-up
    struct Lockup {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // Timestamp when tokens can be withdrawn
    }

    // Mapping of user addresses to their lock-ups
    mapping(address => Lockup) public lockups;

    // Token interface
    IERC20 public immutable token;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Invalid token address");
        token = _token;
    }

    /**
     * @dev Lock tokens for a specified duration.
     * @param _amount Amount of tokens to lock.
     * @param _lockDuration Duration (in seconds) for which tokens will be locked.
     */
    function lockTokens(uint256 _amount, uint256 _lockDuration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_lockDuration > 0, "Lock duration must be greater than zero");

        Lockup storage userLockup = lockups[msg.sender];

        // Ensure no active lock-up exists
        require(userLockup.amount == 0, "Existing lock-up must be withdrawn first");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + _lockDuration;

        // Transfer tokens to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Create a new lock-up
        userLockup.amount = _amount;
        userLockup.unlockTime = unlockTime;

        emit TokensLocked(msg.sender, _amount, unlockTime);
    }

    /**
     * @dev Withdraw tokens after the lock-up period has ended.
     */
    function withdrawTokens() external {
        Lockup storage userLockup = lockups[msg.sender];

        // Ensure tokens are locked
        require(userLockup.amount > 0, "No tokens locked");

        // Ensure lock-up period has ended
        require(block.timestamp >= userLockup.unlockTime, "Lock-up period not yet ended");

        uint256 amount = userLockup.amount;

        // Reset lock-up
        userLockup.amount = 0;
        userLockup.unlockTime = 0;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get details of a user's lock-up.
     * @param _user Address of the user.
     * @return amount Amount of tokens locked.
     * @return unlockTime Timestamp when tokens can be withdrawn.
     */
    function getLockupDetails(address _user) external view returns (uint256 amount, uint256 unlockTime) {
        Lockup memory userLockup = lockups[_user];
        return (userLockup.amount, userLockup.unlockTime);
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
