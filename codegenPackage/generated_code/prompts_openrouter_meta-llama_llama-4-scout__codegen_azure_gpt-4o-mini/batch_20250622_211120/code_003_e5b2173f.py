"""
Generated Code Metadata:
========================
Original URL: https://penpie.io
Prompt: Develop a smart contract to lock PNP and get vlPNP at a 1:1 ratio, with a 60-day cooldown period for unlocking vlPNP.
Generated: DETERMINISTIC_e5b2173f5273d3d3
Batch ID: 20250622_211120
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

// Importing the ERC20 interface for PNP token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for locking PNP tokens and minting vlPNP
contract PNPVault is Ownable {
    // State variables
    IERC20 public pnpToken; // PNP token contract
    mapping(address => uint256) public lockedPNP; // Amount of locked PNP per user
    mapping(address => uint256) public lockTime; // Lock time for each user
    uint256 public constant COOLDOWN_PERIOD = 60 days; // Cooldown period for unlocking vlPNP

    // Event declarations
    event Locked(address indexed user, uint256 amount);
    event Unlocked(address indexed user, uint256 amount);

    // Constructor to set the PNP token address
    constructor(address _pnpToken) {
        require(_pnpToken != address(0), "Invalid PNP token address");
        pnpToken = IERC20(_pnpToken);
    }

    // Function to lock PNP tokens and mint vlPNP
    function lock(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(pnpToken.balanceOf(msg.sender) >= amount, "Insufficient PNP balance");
        require(pnpToken.allowance(msg.sender, address(this)) >= amount, "Allowance not set");

        // Transfer PNP tokens to the contract
        pnpToken.transferFrom(msg.sender, address(this), amount);

        // Update locked amount and lock time
        lockedPNP[msg.sender] += amount;
        lockTime[msg.sender] = block.timestamp;

        emit Locked(msg.sender, amount);
    }

    // Function to unlock vlPNP after the cooldown period
    function unlock() external {
        require(lockedPNP[msg.sender] > 0, "No locked PNP to unlock");
        require(block.timestamp >= lockTime[msg.sender] + COOLDOWN_PERIOD, "Cooldown period not yet over");

        uint256 amountToUnlock = lockedPNP[msg.sender];

        // Reset the locked amount and lock time
        lockedPNP[msg.sender] = 0;
        lockTime[msg.sender] = 0;

        // Transfer PNP tokens back to the user
        pnpToken.transfer(msg.sender, amountToUnlock);

        emit Unlocked(msg.sender, amountToUnlock);
    }

    // Function to check the locked PNP amount for a user
    function getLockedAmount(address user) external view returns (uint256) {
        return lockedPNP[user];
    }

    // Function to check the remaining cooldown time for a user
    function getRemainingCooldown(address user) external view returns (uint256) {
        if (block.timestamp >= lockTime[user] + COOLDOWN_PERIOD) {
            return 0;
        }
        return (lockTime[user] + COOLDOWN_PERIOD) - block.timestamp;
    }
}
```
