"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Explain how to integrate vote escrow models in a DeFi project to enhance user participation and governance, based on the mechanisms used by Shadow Exchange.
Generated: DETERMINISTIC_a68c3511ec215dd2
Batch ID: 20250612_162335
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// VoteEscrow contract to manage vote escrow mechanisms
contract VoteEscrow is Ownable {
    // Struct to hold user information
    struct UserInfo {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // Time when tokens can be unlocked
    }

    // Mapping to store user information
    mapping(address => UserInfo) public userInfo;

    // ERC20 token used for voting
    IERC20 public votingToken;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the voting token
    constructor(IERC20 _votingToken) {
        votingToken = _votingToken;
    }

    // Function to lock tokens for voting
    function lockTokens(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        // Transfer tokens from user to contract
        votingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user information
        userInfo[msg.sender].amount += _amount;
        userInfo[msg.sender].unlockTime = block.timestamp + _duration;

        emit TokensLocked(msg.sender, _amount, userInfo[msg.sender].unlockTime);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        UserInfo storage user = userInfo[msg.sender];
        require(block.timestamp >= user.unlockTime, "Tokens are still locked");
        require(user.amount > 0, "No tokens to unlock");

        // Transfer tokens back to the user
        uint256 amountToUnlock = user.amount;
        user.amount = 0; // Reset user's amount
        votingToken.transfer(msg.sender, amountToUnlock);

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    // Function to check the locked amount of tokens for a user
    function getLockedAmount(address _user) external view returns (uint256) {
        return userInfo[_user].amount;
    }

    // Function to check the unlock time for a user
    function getUnlockTime(address _user) external view returns (uint256) {
        return userInfo[_user].unlockTime;
    }
}
```

This Solidity code implements a basic vote escrow model for a DeFi project, allowing users to lock tokens for governance participation. It includes functions for locking and unlocking tokens, along with proper error handling and event emissions for tracking state changes.
