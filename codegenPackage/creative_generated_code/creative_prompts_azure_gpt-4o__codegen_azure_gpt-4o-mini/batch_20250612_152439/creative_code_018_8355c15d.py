"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Write a Solidity contract to implement a community collar ranking system for $AI holders based on the amount and duration of locked tokens.
Generated: DETERMINISTIC_8355c15d6f2aa9e3
Batch ID: 20250612_152439
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

// Import OpenZeppelin's SafeERC20 and Ownable contracts for security and ownership management
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A contract to manage the community collar ranking system for $AI holders
contract CollarRankingSystem is Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a user's lock information
    struct LockInfo {
        uint256 amount;            // Amount of tokens locked
        uint256 unlockTime;        // Time when the tokens can be unlocked
        uint256 duration;          // Duration that tokens are locked for
    }

    // Mapping from user address to their lock information
    mapping(address => LockInfo) public lockInfo;

    // The ERC20 token to be used for locking
    IERC20 public aiToken;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 duration);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _aiToken) {
        aiToken = _aiToken;
    }

    // Function to lock tokens for a specified duration
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer tokens from user to this contract
        aiToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update the user's lock information
        lockInfo[msg.sender] = LockInfo({
            amount: amount,
            unlockTime: block.timestamp + duration,
            duration: duration
        });

        emit TokensLocked(msg.sender, amount, duration);
    }

    // Function to unlock previously locked tokens
    function unlockTokens() external {
        LockInfo storage userLock = lockInfo[msg.sender];

        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Get the amount of tokens to unlock
        uint256 amountToUnlock = userLock.amount;

        // Reset user's lock information
        userLock.amount = 0;
        userLock.unlockTime = 0;
        userLock.duration = 0;

        // Transfer the unlocked tokens back to the user
        aiToken.safeTransfer(msg.sender, amountToUnlock);

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    // Function to check the locked status of the user
    function getLockStatus(address user) external view returns (uint256 amount, uint256 unlockTime, uint256 duration) {
        LockInfo storage userLock = lockInfo[user];
        return (userLock.amount, userLock.unlockTime, userLock.duration);
    }

    // Function to withdraw tokens in case of emergency. Only the owner can call this.
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(aiToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer specified amount of tokens to the owner
        aiToken.safeTransfer(msg.sender, amount);
    }
}
```
