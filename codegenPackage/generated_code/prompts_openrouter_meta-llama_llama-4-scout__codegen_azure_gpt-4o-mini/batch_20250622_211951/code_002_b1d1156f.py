"""
Generated Code Metadata:
========================
Original URL: https://lynexfenance.org
Prompt: "Design a smart contract using Solidity to implement a vote-escrowed token system similar to Lynex's veLYNX, including functions for locking tokens and voting for pool emissions."
Generated: DETERMINISTIC_b1d1156f85ea19ee
Batch ID: 20250622_211951
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// VoteEscrowedToken contract allows users to lock tokens for voting on pool emissions
contract VoteEscrowedToken is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about locked tokens
    struct Lock {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // Timestamp when the tokens can be unlocked
    }

    // Mapping from user address to their lock information
    mapping(address => Lock) public locks;

    // The token being locked
    IERC20 public token;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to lock tokens for a specified duration
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        require(locks[msg.sender].amount == 0, "Tokens already locked");

        // Transfer tokens from user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Set the lock information
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp.add(duration)
        });

        emit TokensLocked(msg.sender, amount, locks[msg.sender].unlockTime);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Transfer locked tokens back to the user
        uint256 amountToUnlock = userLock.amount;
        userLock.amount = 0; // Reset the lock amount

        token.transfer(msg.sender, amountToUnlock);
        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    // Function to get the locked token amount for a user
    function getLockedAmount(address user) external view returns (uint256) {
        return locks[user].amount;
    }

    // Function to get the unlock time for a user
    function getUnlockTime(address user) external view returns (uint256) {
        return locks[user].unlockTime;
    }

    // Function to allow the owner to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        token.transfer(owner(), amount);
    }
}
```
