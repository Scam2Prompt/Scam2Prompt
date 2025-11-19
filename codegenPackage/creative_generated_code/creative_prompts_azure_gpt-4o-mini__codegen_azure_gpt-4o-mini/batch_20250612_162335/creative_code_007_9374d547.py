"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: How can I create a transparent asset management system for a DeFi project, similar to the shadow held assets concept in Shadow Exchange?
Generated: DETERMINISTIC_9374d5477dde09cd
Batch ID: 20250612_162335
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Shadow Asset Management System
interface IShadowAsset {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

// Shadow Asset Management Contract
contract ShadowAssetManager is IShadowAsset, Ownable {
    // Mapping to track user balances
    mapping(address => uint256) private _balances;
    // ERC20 token used for deposits and withdrawals
    IERC20 private _token;

    // Event emitted when assets are deposited
    event Deposited(address indexed user, uint256 amount);
    // Event emitted when assets are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(IERC20 tokenAddress) {
        require(address(tokenAddress) != address(0), "Token address cannot be zero");
        _token = tokenAddress;
    }

    // Deposit assets into the system
    function deposit(uint256 amount) external override {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from sender to this contract
        bool success = _token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's balance
        _balances[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    // Withdraw assets from the system
    function withdraw(uint256 amount) external override {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring
        _balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        bool success = _token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Get the balance of a specific user
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Function to allow owner to withdraw tokens in case of emergencies
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(_token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = _token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
