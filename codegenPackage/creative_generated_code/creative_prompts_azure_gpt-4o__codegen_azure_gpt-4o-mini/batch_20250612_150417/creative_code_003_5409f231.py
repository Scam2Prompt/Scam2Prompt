"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lynexfenance.org
Prompt: Create a Solidity smart contract that locks LYNX tokens for up to 2 years and calculates veLYNX based on the lock duration.
Generated: DETERMINISTIC_5409f2314c24f2d0
Batch ID: 20250612_150417
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

// Importing the ERC20 interface for the LYNX token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LYNXLock {
    using SafeMath for uint256;

    // State variables
    IERC20 public lynxToken; // LYNX token contract address
    uint256 public constant MAX_LOCK_DURATION = 730 days; // Maximum lock duration (2 years)

    struct Lock {
        uint256 amount;        // Amount of LYNX tokens locked
        uint256 unlockTime;    // Timestamp when the tokens can be unlocked
        uint256 lockDuration;   // Duration of the lock in seconds
    }

    mapping(address => Lock) public locks; // Mapping of user addresses to their locks

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 duration);
    event TokensUnlocked(address indexed user, uint256 amount);
    
    // Constructor to set the LYNX token address
    constructor(address _lynxTokenAddress) {
        require(_lynxTokenAddress != address(0), "Invalid token address");
        lynxToken = IERC20(_lynxTokenAddress);
    }

    // Function to lock tokens
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0 && duration <= MAX_LOCK_DURATION, "Invalid lock duration");

        // Transfer tokens from the user to the contract
        lynxToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's lock information
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp.add(duration),
            lockDuration: duration
        });

        // Emit event
        emit TokensLocked(msg.sender, amount, duration);
    }

    // Function to unlock tokens after the lock duration
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];

        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");
        require(userLock.amount > 0, "No tokens to unlock");

        uint256 amountToUnlock = userLock.amount;

        // Reset user lock info
        delete locks[msg.sender];

        // Transfer unlocked tokens back to user
        lynxToken.transfer(msg.sender, amountToUnlock);

        // Emit event
        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    // Function to calculate veLYNX based on lock duration
    function calculateVeLYNX(address user) external view returns (uint256) {
        Lock memory userLock = locks[user];
        
        // If there's no lock, return 0
        if (userLock.amount == 0) {
            return 0;
        }

        // Calculate veLYNX based on lock duration proportional to maximum lock duration
        // veLYNX = amount * (lock duration / max lock duration)
        uint256 veLYNX = userLock.amount.mul(userLock.lockDuration).div(MAX_LOCK_DURATION);
        return veLYNX;
    }
}
```
