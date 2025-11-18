"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Write a Solidity contract that includes a mechanism for locking tokens for a fixed period, ensuring they cannot be withdrawn before a specified time, as described in BTC20's staking process.
Generated: DETERMINISTIC_c061158465e0f781
Batch ID: 20250612_151333
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for locking tokens
contract TokenLocker is Ownable {
    // Struct to hold lock information
    struct Lock {
        uint256 amount;       // Amount of tokens locked
        uint256 unlockTime;   // Time when tokens can be unlocked
    }

    // Mapping to hold the locks for each user
    mapping(address => Lock) private locks;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    IERC20 public token; // The ERC20 token to lock

    // Constructor to set the token contract address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to lock tokens for a specified period
    function lockTokens(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockDuration > 0, "Lock duration must be greater than zero");

        // Transfer tokens from user to this contract
        token.transferFrom(msg.sender, address(this), amount);

        // Set the lock details
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + lockDuration
        });

        emit TokensLocked(msg.sender, amount, locks[msg.sender].unlockTime);
    }

    // Function to unlock tokens after the lock duration
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];
        
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Get the amount to unlock
        uint256 amountToUnlock = userLock.amount;

        // Reset the user's lock
        delete locks[msg.sender];

        // Transfer the unlocked tokens back to the user
        token.transfer(msg.sender, amountToUnlock);

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    // Function to check the lock details for a user
    function checkLockDetails(address user) external view returns (uint256 amount, uint256 unlockTime) {
        Lock storage userLock = locks[user];
        return (userLock.amount, userLock.unlockTime);
    }
}
```
