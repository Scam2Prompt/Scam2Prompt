"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Generate code in Solidity to implement a vote escrow model (ve) similar to Shadow Exchange, where users lock assets to gain non-transferable voting rights.
Generated: DETERMINISTIC_ca1250dd85d31af8
Batch ID: 20250612_155028
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
 * @title Vote Escrow (ve) Contract
 * @dev Implements a vote escrow model where users lock assets to gain non-transferable voting rights.
 */
contract VoteEscrow {
    // Structure to represent user lock details
    struct Lock {
        uint256 amount;         // Amount locked by the user
        uint256 unlockTime;     // Time when the lock expires
    }

    // Mapping to store user locks
    mapping(address => Lock) public locks;

    // ERC20 token used for locking
    IERC20 public immutable token;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address
     * @param _token Address of the ERC20 token contract
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Lock tokens for voting rights
     * @param _amount Amount of tokens to lock
     * @param _duration Duration (in seconds) for which tokens will be locked
     */
    function lockTokens(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + _duration;

        // Update lock details
        locks[msg.sender].amount += _amount;
        locks[msg.sender].unlockTime = unlockTime;

        // Transfer tokens to the contract
        bool success = token.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        emit TokensLocked(msg.sender, _amount, unlockTime);
    }

    /**
     * @dev Withdraw tokens after the lock period has expired
     */
    function withdrawTokens() external {
        Lock memory userLock = locks[msg.sender];
        require(userLock.amount > 0, "No locked tokens found");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Update user lock
        locks[msg.sender].amount = 0;
        locks[msg.sender].unlockTime = 0;

        // Transfer tokens back to the user
        bool success = token.transfer(msg.sender, userLock.amount);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, userLock.amount);
    }

    /**
     * @dev Function to check the voting power of a user
     * @return The amount of tokens locked by the user
     */
    function getVotingPower(address _user) external view returns (uint256) {
        return locks[_user].amount;
    }
}

/**
 * @dev Minimal ERC20 interface for token interaction
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
