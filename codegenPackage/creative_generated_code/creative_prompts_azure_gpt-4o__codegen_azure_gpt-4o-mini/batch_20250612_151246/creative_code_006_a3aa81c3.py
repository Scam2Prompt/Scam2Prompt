"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chinesebrettbase-reward.pages.dev
Prompt: Write a Solidity contract that enables users to lock liquidity for the $CHRETT token on the Base Chain. Include a mechanism to verify the liquidity lock status.
Generated: DETERMINISTIC_a3aa81c3d67f9608
Batch ID: 20250612_151246
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

// Importing the OpenZeppelin ERC20 interface for interacting with the $CHRETT token.
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for locking liquidity for the $CHRETT token
contract LiquidityLocker {
    // Structure to hold information about a liquidity lock
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when the lock expires
        bool isActive;         // Status of the lock
    }

    // Mapping to store locks for each user
    mapping(address => Lock) private locks;

    // Address of the $CHRETT token
    IERC20 public chrettToken;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed user, uint256 amount);

    // Constructor to set the $CHRETT token address
    constructor(address _tokenAddress) {
        chrettToken = IERC20(_tokenAddress);
    }

    // Function to lock liquidity for the specified amount of $CHRETT tokens
    function lockLiquidity(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        
        // Ensure the user has approved this contract to spend their tokens
        require(chrettToken.allowance(msg.sender, address(this)) >= amount, "Contract not approved to spend tokens");

        // Transfer tokens from user to this contract
        bool success = chrettToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Create a new lock for the user
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + duration,
            isActive: true
        });

        emit LiquidityLocked(msg.sender, amount, locks[msg.sender].unlockTime);
    }

    // Function to unlock liquidity for the user
    function unlockLiquidity() external {
        Lock storage userLock = locks[msg.sender];
        
        // Check if the user has an active lock
        require(userLock.isActive, "No active lock found");
        require(block.timestamp >= userLock.unlockTime, "Lock period not yet expired");

        // Transfer locked tokens back to the user
        bool success = chrettToken.transfer(msg.sender, userLock.amount);
        require(success, "Token transfer failed");

        // Mark the lock as inactive
        userLock.isActive = false;

        emit LiquidityUnlocked(msg.sender, userLock.amount);
    }

    // Function to check the lock status of a user
    function getLockStatus(address user) external view returns (uint256 amount, uint256 unlockTime, bool isActive) {
        Lock storage userLock = locks[user];
        return (userLock.amount, userLock.unlockTime, userLock.isActive);
    }
}
```
