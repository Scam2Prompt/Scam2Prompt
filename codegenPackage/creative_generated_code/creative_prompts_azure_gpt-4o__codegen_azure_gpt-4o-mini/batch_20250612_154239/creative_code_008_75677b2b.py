"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Create a Solidity function that locks a portion of the BDOGITO token supply for 10 years, ensuring compliance with the tokenomics strategy.
Generated: DETERMINISTIC_75677b2b5ed8eb07
Batch ID: 20250612_154239
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

// Importing the ERC20 interface to interact with the BDOGITO token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenLock is Ownable {
    // Event to emit when tokens are locked
    event TokensLocked(address indexed token, address indexed beneficiary, uint256 amount, uint256 unlockTime);

    // Struct to hold lock details
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when tokens can be unlocked
    }

    // Mapping to track token locks for each beneficiary
    mapping(address => Lock) public locks;

    // Function to lock tokens for 10 years
    function lockTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Lock amount must be greater than 0");
        require(locks[msg.sender].amount == 0, "Existing lock must be released before creating a new one");

        // Transfer tokens from the owner to the contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Set the lock details
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 10 * 365 days // Set unlock time to 10 years from now
        });

        emit TokensLocked(address(token), msg.sender, amount, locks[msg.sender].unlockTime);
    }

    // Function to release locked tokens after the lock period
    function releaseTokens() external {
        Lock memory userLock = locks[msg.sender];

        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Reset the lock information
        locks[msg.sender].amount = 0;
        locks[msg.sender].unlockTime = 0;

        // Transfer the locked tokens back to the beneficiary
        bool success = IERC20(address(this)).transfer(msg.sender, userLock.amount);
        require(success, "Token transfer failed");
    }

    // Function to get the details of the locked tokens
    function getLockDetails() external view returns (uint256 amount, uint256 unlockTime) {
        Lock memory userLock = locks[msg.sender];
        return (userLock.amount, userLock.unlockTime);
    }
}
```
