"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-aerodromefinance.net
Prompt: Create a smart contract that allows users to lock AERO tokens and convert them to veAERO for voting on liquidity pools in Aerodrome Finance.
Generated: DETERMINISTIC_21844b5369a8b330
Batch ID: 20250612_155429
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

// Importing the ERC20 interface for interacting with AERO tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract AeroLock is Ownable {
    using SafeMath for uint256;

    // AERO token interface
    IERC20 public aeroToken;

    // Struct to represent a locked position
    struct Lock {
        uint256 amount;   // Amount of AERO locked
        uint256 unlockTime; // Time when the lock can be released
    }

    // Mapping from user address to their lock
    mapping(address => Lock) public locks;

    // Event emitted when tokens are locked
    event Locked(address indexed user, uint256 amount, uint256 unlockTime);
    
    // Event emitted when tokens are unlocked
    event Unlocked(address indexed user, uint256 amount);

    // Constructor to set the AERO token address
    constructor(address _aeroToken) {
        require(_aeroToken != address(0), "Invalid token address");
        aeroToken = IERC20(_aeroToken);
    }

    /// @notice Lock AERO tokens for a specified duration
    /// @param amount The amount of AERO tokens to lock
    /// @param duration The duration in seconds for which the tokens should be locked
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Transfer AERO tokens from the user to the contract
        require(aeroToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's lock information
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp.add(duration)
        });

        emit Locked(msg.sender, amount, locks[msg.sender].unlockTime);
    }

    /// @notice Unlock previously locked AERO tokens
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];

        // Check if the lock is valid and the unlock time has passed
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Transfer locked tokens back to the user
        uint256 amountToUnlock = userLock.amount;
        userLock.amount = 0; // Reset the user's lock

        require(aeroToken.transfer(msg.sender, amountToUnlock), "Transfer failed");

        emit Unlocked(msg.sender, amountToUnlock);
    }

    /// @notice Get the lock information of a user
    /// @param user The address of the user
    /// @return amount The amount of AERO tokens locked
    /// @return unlockTime The time when the tokens can be unlocked
    function getLockInfo(address user) external view returns (uint256 amount, uint256 unlockTime) {
        Lock storage userLock = locks[user];
        return (userLock.amount, userLock.unlockTime);
    }
}
```
