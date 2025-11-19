"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-in.web.app
Prompt: Create a Solidity function to lock $MPEPE tokens during presale stages, ensuring security and compliance with the roadmap milestones.
Generated: DETERMINISTIC_fd9cbf35eb4ac8f3
Batch ID: 20250612_154115
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for locking $MPEPE tokens during presale stages
contract TokenLocker is Ownable {
    // Struct to hold lock information
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when tokens can be unlocked
        bool isLocked;         // Status of the lock
    }

    // Mapping to track locked tokens for each address
    mapping(address => Lock) public lockedTokens;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed beneficiary, uint256 amount, uint256 unlockTime);
    
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed beneficiary, uint256 amount);

    // Reference to the $MPEPE token contract
    IERC20 public mpepeToken;

    // Constructor to initialize the token contract
    constructor(IERC20 _mpepeToken) {
        mpepeToken = _mpepeToken;
    }

    // Function to lock tokens
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        require(lockedTokens[msg.sender].isLocked == false, "Tokens already locked");

        // Transfer tokens from the sender to this contract
        require(mpepeToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Set lock details
        lockedTokens[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + duration,
            isLocked: true
        });

        emit TokensLocked(msg.sender, amount, lockedTokens[msg.sender].unlockTime);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        Lock storage userLock = lockedTokens[msg.sender];
        require(userLock.isLocked, "No tokens are locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Transfer locked tokens back to the user
        uint256 amountToUnlock = userLock.amount;
        userLock.isLocked = false; // Update lock status

        // Reset lock details
        userLock.amount = 0;
        userLock.unlockTime = 0;

        require(mpepeToken.transfer(msg.sender, amountToUnlock), "Token transfer failed");

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    // Function to check the lock status of an address
    function getLockStatus(address beneficiary) external view returns (uint256 amount, uint256 unlockTime, bool isLocked) {
        Lock storage userLock = lockedTokens[beneficiary];
        return (userLock.amount, userLock.unlockTime, userLock.isLocked);
    }
}
```
