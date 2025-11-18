"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lynexfl.org
Prompt: Generate code to lock LYNX tokens for up to 2 years and receive vote-escrowed LYNX (veLYNX). Include functionality to calculate the amount of veLYNX based on the lock duration.
Generated: DETERMINISTIC_b35018234142c7fc
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

// Interface for the LYNX token contract
interface ILynx {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Interface for the veLYNX contract
interface IVeLynx {
    function mint(address to, uint256 amount) external;
}

// Contract to lock LYNX tokens and receive veLYNX
contract LynxLocker {
    // LYNX token contract
    ILynx public lynxToken;
    // veLYNX contract
    IVeLynx public veLynxToken;

    // Lock structure to hold lock information
    struct Lock {
        uint256 amount;       // Amount of LYNX locked
        uint256 unlockTime;   // Time when the lock can be released
    }

    // Mapping of user addresses to their locks
    mapping(address => Lock) public locks;

    // Events for logging actions
    event Locked(address indexed user, uint256 amount, uint256 unlockTime);
    event Unlocked(address indexed user, uint256 amount);
    event VeLynxMinted(address indexed user, uint256 veAmount);

    // Constructor to set token contracts
    constructor(address _lynxToken, address _veLynxToken) {
        lynxToken = ILynx(_lynxToken);
        veLynxToken = IVeLynx(_veLynxToken);
    }

    // Function to lock LYNX tokens
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0 && duration <= 730 days, "Duration must be between 1 day and 2 years");

        // Ensure the user has enough LYNX to lock
        require(lynxToken.balanceOf(msg.sender) >= amount, "Insufficient LYNX balance");

        // Transfer LYNX tokens from user to contract
        require(lynxToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Set the lock for the user
        locks[msg.sender] = Lock(amount, block.timestamp + duration);

        // Emit lock event
        emit Locked(msg.sender, amount, locks[msg.sender].unlockTime);

        // Mint veLYNX based on the locked amount and duration
        uint256 veAmount = calculateVeLynx(amount, duration);
        veLynxToken.mint(msg.sender, veAmount);

        // Emit veLYNX mint event
        emit VeLynxMinted(msg.sender, veAmount);
    }

    // Function to unlock LYNX tokens after the lock period
    function unlockTokens() external {
        Lock memory userLock = locks[msg.sender];
        
        require(block.timestamp >= userLock.unlockTime, "Lock period not yet over");
        require(userLock.amount > 0, "No tokens to unlock");

        uint256 amountToUnlock = userLock.amount;

        // Reset the user's lock
        delete locks[msg.sender];

        // Transfer LYNX tokens back to the user
        require(lynxToken.transferFrom(address(this), msg.sender, amountToUnlock), "Transfer failed");

        // Emit unlock event
        emit Unlocked(msg.sender, amountToUnlock);
    }

    // Function to calculate veLYNX based on lock duration
    function calculateVeLynx(uint256 amount, uint256 duration) internal pure returns (uint256) {
        // The formula: veLYNX = amount * (duration / maxDuration)
        // where maxDuration is 730 days (2 years)
        // Assuming that veLYNX is proportional to the lock amount and duration
        return amount * duration / 730 days;
    }
}
```
