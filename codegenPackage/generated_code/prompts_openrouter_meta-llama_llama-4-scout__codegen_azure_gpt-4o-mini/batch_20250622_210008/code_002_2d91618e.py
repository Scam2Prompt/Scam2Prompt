"""
Generated Code Metadata:
========================
Original URL: https://radiant-capital.pages.dev
Prompt: Generate a smart contract code in Solidity to implement a RDNT locker, allowing users to lock $RDNT liquidity and receive revenue from interest and flash loan fees.
Generated: DETERMINISTIC_2d91618e2be8fc95
Batch ID: 20250622_210008
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// RDNTLocker contract allows users to lock RDNT liquidity and earn revenue
contract RDNTLocker is Ownable, ReentrancyGuard {
    // Struct to hold user lock information
    struct Lock {
        uint256 amount; // Amount of RDNT locked
        uint256 unlockTime; // Time when the lock can be released
    }

    // Mapping to store user locks
    mapping(address => Lock) public locks;

    // The RDNT token contract
    IERC20 public rdntToken;

    // Events for logging
    event Locked(address indexed user, uint256 amount, uint256 unlockTime);
    event Unlocked(address indexed user, uint256 amount);

    // Constructor to set the RDNT token address
    constructor(address _rdntToken) {
        require(_rdntToken != address(0), "Invalid token address");
        rdntToken = IERC20(_rdntToken);
    }

    // Function to lock RDNT tokens
    function lock(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Transfer RDNT tokens from user to the contract
        require(rdntToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Set the lock details
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + duration
        });

        emit Locked(msg.sender, amount, locks[msg.sender].unlockTime);
    }

    // Function to unlock RDNT tokens
    function unlock() external nonReentrant {
        Lock memory userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Lock period not yet over");

        // Reset the user's lock
        uint256 amountToUnlock = userLock.amount;
        delete locks[msg.sender];

        // Transfer RDNT tokens back to the user
        require(rdntToken.transfer(msg.sender, amountToUnlock), "Transfer failed");

        emit Unlocked(msg.sender, amountToUnlock);
    }

    // Function to check the locked amount of a user
    function getLockedAmount(address user) external view returns (uint256) {
        return locks[user].amount;
    }

    // Function to check the unlock time of a user
    function getUnlockTime(address user) external view returns (uint256) {
        return locks[user].unlockTime;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(rdntToken), "Cannot withdraw RDNT tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
