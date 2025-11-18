"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Create a Solidity function to lock $MPEPE tokens during presale stages, ensuring security and compliance with the roadmap milestones.
Generated: DETERMINISTIC_fd9cbf35eb4ac8f3
Batch ID: 20250612_154115
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

// Interface for the ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Contract for locking $MPEPE tokens during presale stages
contract PresaleTokenLocker {
    // State variables
    address public owner;
    IERC20 public mpepeToken;
    uint256 public lockEndTime;
    bool public isLocked;

    // Events
    event TokensLocked(address indexed locker, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed unlocker, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier onlyWhenLocked() {
        require(isLocked, "Tokens are not locked");
        _;
    }

    modifier onlyWhenUnlocked() {
        require(!isLocked, "Tokens are still locked");
        require(block.timestamp >= lockEndTime, "Lock period is not over");
        _;
    }

    // Constructor to initialize contract
    constructor(address _tokenAddress) {
        owner = msg.sender;
        mpepeToken = IERC20(_tokenAddress);
        isLocked = false;
    }

    // Function to lock the specified amount of tokens
    function lockTokens(uint256 amount, uint256 duration) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(!isLocked, "Tokens are already locked");

        // Transfer tokens from owner to this contract
        require(mpepeToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Set the lock status and duration
        isLocked = true;
        lockEndTime = block.timestamp + duration;

        emit TokensLocked(msg.sender, amount, lockEndTime);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external onlyOwner onlyWhenUnlocked {
        uint256 balance = mpepeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to unlock");

        // Transfer tokens back to the owner
        require(mpepeToken.transferFrom(address(this), owner, balance), "Token transfer failed");

        isLocked = false;
        emit TokensUnlocked(msg.sender, balance);
    }

    // Function to check the contract's token balance
    function getLockedTokenBalance() external view returns (uint256) {
        return mpepeToken.balanceOf(address(this));
    }
}
```
