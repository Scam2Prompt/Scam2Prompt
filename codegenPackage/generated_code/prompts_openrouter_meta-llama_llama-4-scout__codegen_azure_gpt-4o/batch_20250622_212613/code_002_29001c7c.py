"""
Generated Code Metadata:
========================
Original URL: https://cmkjdwoihjif.com
Prompt: "Generate a smart contract code for vote-escrow governance on HyperEVM similar to KittenSwap's implementation."
Generated: DETERMINISTIC_29001c7cb23ab71b
Batch ID: 20250622_212613
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
 * @title Vote Escrow Governance Contract
 * @dev This contract allows users to lock tokens for governance voting power.
 * Inspired by KittenSwap's implementation.
 */
contract VoteEscrowGovernance {
    // Token used for locking
    IERC20 public immutable token;

    // Struct to store lock information
    struct Lock {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // Timestamp when tokens can be unlocked
    }

    // Mapping of user address to their lock information
    mapping(address => Lock) public locks;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token Address of the ERC20 token used for locking.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Invalid token address");
        token = _token;
    }

    /**
     * @dev Lock tokens for governance voting power.
     * @param _amount Amount of tokens to lock.
     * @param _duration Duration (in seconds) for which tokens will be locked.
     */
    function lockTokens(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + _duration;

        // Transfer tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update lock information
        locks[msg.sender] = Lock({
            amount: locks[msg.sender].amount + _amount,
            unlockTime: unlockTime
        });

        emit TokensLocked(msg.sender, _amount, unlockTime);
    }

    /**
     * @dev Unlock tokens after the lock period has expired.
     */
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        uint256 amountToUnlock = userLock.amount;

        // Reset lock information
        userLock.amount = 0;
        userLock.unlockTime = 0;

        // Transfer tokens back to user
        require(token.transfer(msg.sender, amountToUnlock), "Token transfer failed");

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    /**
     * @dev Get the voting power of a user based on their locked tokens.
     * @param _user Address of the user.
     * @return Voting power (amount of locked tokens).
     */
    function getVotingPower(address _user) external view returns (uint256) {
        return locks[_user].amount;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
