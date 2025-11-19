"""
Generated Code Metadata:
========================
Original URL: https://bulldogito.pages.dev
Prompt: Create a Solidity function that locks a portion of the BDOGITO token supply for 10 years, ensuring compliance with the tokenomics strategy.
Generated: DETERMINISTIC_75677b2b5ed8eb07
Batch ID: 20250612_154239
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

// Contract to manage the locking of BDOGITO tokens
contract TokenLock is Ownable {
    // The token being locked
    IERC20 public bdogitoToken;

    // Structure to hold lock information
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when tokens can be unlocked
    }

    // Mapping to track locks for each address
    mapping(address => Lock) public locks;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed beneficiary, uint256 amount, uint256 unlockTime);

    // Constructor to set the token address
    constructor(IERC20 _bdogitoToken) {
        bdogitoToken = _bdogitoToken;
    }

    // Function to lock tokens for 10 years
    function lockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(bdogitoToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(bdogitoToken.allowance(msg.sender, address(this)) >= amount, "Token allowance not set");

        // Calculate unlock time (10 years from now)
        uint256 unlockTime = block.timestamp + 10 * 365 days;

        // Transfer tokens from the sender to this contract
        bool success = bdogitoToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the lock information
        locks[msg.sender] = Lock(amount, unlockTime);

        // Emit the event for logging
        emit TokensLocked(msg.sender, amount, unlockTime);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];

        // Ensure there are tokens locked for the user
        require(userLock.amount > 0, "No tokens locked for this address");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Transfer the locked tokens back to the user
        bool success = bdogitoToken.transfer(msg.sender, userLock.amount);
        require(success, "Token transfer failed");

        // Reset the lock information
        delete locks[msg.sender];
    }

    // Function to check the lock status of an address
    function getLockInfo(address beneficiary) external view returns (uint256 amount, uint256 unlockTime) {
        Lock storage userLock = locks[beneficiary];
        return (userLock.amount, userLock.unlockTime);
    }
}
```
